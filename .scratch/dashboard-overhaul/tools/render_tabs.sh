#!/usr/bin/env bash
# Re-import Mission Control (v2 API) and render every tab + the classic
# dashboard with every row expanded (imported as a scratch copy).
# Usage: tools/render_tabs.sh [out_dir] [from]   (default: ./shots, now-30m)
# Env: GRAFANA (default http://localhost:3000), THEME (dark|light, default dark),
#      TABS (space-separated tab indexes to render, default all), CLASSIC=0 to skip.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"; repo="$(cd "$here/../../.." && pwd)"
out="${1:-$here/shots}"; from="${2:-now-30m}"; g="${GRAFANA:-http://localhost:3000}"
theme="${THEME:-dark}"
mc="$repo/grafana-dashboard/truenas-mission-control.json"; mkdir -p "$out"
api="$g/apis/dashboard.grafana.app/v2beta1/namespaces/default/dashboards"
curl -s -X DELETE "$api/truenas-mission-control" >/dev/null || true
curl -sf -X POST -H 'Content-Type: application/json' --data-binary @"$mc" "$api" >/dev/null
python3 -c "import json,sys;print(json.dumps({'dashboard':json.load(open(sys.argv[1])),'overwrite':True}))" \
  "$repo/grafana-dashboard/operations-center-dashboard.json" \
  | curl -sf -X POST -H 'Content-Type: application/json' --data-binary @- "$g/api/dashboards/db" >/dev/null
# Tab slug = Grafana slugifyForUrl(title): lowercase, drop non-word chars (emoji), spaces -> '-'.
python3 - "$mc" <<'PY' > "$out/tabs.txt"
import json,re,sys
d=json.load(open(sys.argv[1]))
for i,t in enumerate(d["spec"]["layout"]["spec"]["tabs"]):
    print(i, re.sub(r" +","-",re.sub(r"[^\w ]+","",t["spec"]["title"].lower())))
PY
while read -r i slug; do
  if [[ -n "${TABS:-}" && " $TABS " != *" $i "* ]]; then continue; fi
  curl -sf -m 170 -o "$out/mc-$i$slug.png" \
    "$g/render/d/truenas-mission-control?orgId=1&from=$from&to=now&width=1600&height=${HEIGHT:-3600}&kiosk&timeout=150&theme=$theme&dtab=$slug" \
    && echo "rendered mc-$i$slug.png" || echo "FAILED mc-$i$slug.png"
done < "$out/tabs.txt"
[[ "${CLASSIC:-1}" == "0" ]] && exit 0
# Classic dashboard: one scratch copy per row, every row expanded (the
# renderer caps very tall pages, so each row is rendered on its own).
python3 - "$repo/grafana-dashboard/operations-center-dashboard.json" "$out" <<'PY'
import json,re,sys,copy
d=json.load(open(sys.argv[1])); out=sys.argv[2]
rows=[p for p in d["panels"] if p["type"]=="row"]
for i,r in enumerate(rows):
    inner=copy.deepcopy(r.get("panels",[])); y0=min(p["gridPos"]["y"] for p in inner)
    for p in inner: p["gridPos"]["y"]-=y0
    h=max(p["gridPos"]["y"]+p["gridPos"]["h"] for p in inner)
    dd=copy.deepcopy(d); dd["panels"]=inner; dd["uid"]=f"oc-row-{i:02d}"; dd["title"]=f"OC {r['title']}"; dd.pop("id",None)
    slug=re.sub(r"[^a-z0-9]+","-",r["title"].lower()).strip("-")
    json.dump({"dashboard":dd,"overwrite":True},open(f"{out}/classic-row-{i:02d}.json","w"))
    print(f"{i:02d} {slug} {h*31+120}")
PY
python3 - "$repo/grafana-dashboard/operations-center-dashboard.json" "$out" > "$out/classic-rows.txt" <<'PY'
import json,re,sys,copy
d=json.load(open(sys.argv[1]))
for i,r in enumerate([p for p in d["panels"] if p["type"]=="row"]):
    inner=r.get("panels",[]); y0=min(p["gridPos"]["y"] for p in inner)
    h=max(p["gridPos"]["y"]-y0+p["gridPos"]["h"] for p in inner)
    print(f"{i:02d}", re.sub(r"[^a-z0-9]+","-",r["title"].lower()).strip("-"), h*38+220)
PY
while read -r i slug h; do
  curl -sf -X POST -H 'Content-Type: application/json' --data-binary @"$out/classic-row-$i.json" "$g/api/dashboards/db" >/dev/null
  curl -sf -m 200 -o "$out/classic-$i-$slug.png" \
    "$g/render/d/oc-row-$i?orgId=1&from=$from&to=now&width=1600&height=$h&kiosk&timeout=180&theme=$theme" \
    && echo "rendered classic-$i-$slug.png" || echo "FAILED classic-$i-$slug.png"
done < "$out/classic-rows.txt"
