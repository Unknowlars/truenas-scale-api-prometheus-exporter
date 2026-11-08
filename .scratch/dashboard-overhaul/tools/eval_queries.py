import json,re,sys,urllib.request,urllib.parse,collections
def exprs(f):
    out=[]
    def walk(o,title=None):
        if isinstance(o,dict):
            t=o.get("title",title)
            if isinstance(o.get("expr"),str): out.append((t,o["expr"]))
            for v in o.values(): walk(v,t)
        elif isinstance(o,list):
            for v in o: walk(v,title)
    walk(json.load(open(f))); return out
import os
PROM=os.environ.get("PROM","http://127.0.0.1:9090")
def q(e):
    u=PROM+"/api/v1/query?"+urllib.parse.urlencode({"query":e})
    try: r=json.load(urllib.request.urlopen(u,timeout=20)); return r["status"], len(r["data"]["result"]) if r["data"]["resultType"] in("vector","matrix") else 1, None
    except urllib.error.HTTPError as x: return "error",0,json.load(x).get("error","")[:100]
for f in sys.argv[1:]:
    res=collections.Counter(); empty=[]; errs=[]; seen=set()
    for t,e in exprs(f):
        e2=re.sub(r"\$\{?__rate_interval\}?","2m",e); e2=re.sub(r"\$\{?__range\}?","6h",e2); e2=re.sub(r"\$\{?(\w+)(:\w+)?\}?",".*",e2)
        if e2 in seen: continue
        seen.add(e2); st,n,err=q(e2)
        if st=="error": res["error"]+=1; errs.append((t,e,err))
        elif n==0: res["empty"]+=1; empty.append((t,e))
        else: res["data"]+=1
    print(f, dict(res))
    json.dump({"empty":empty,"errors":errs},open(os.environ.get("EVAL_DIR",".")+"/"+f.split("/")[-1]+".eval.json","w"),indent=1)
    for t,e,err in errs: print("ERROR",t,"::",err,"::",e[:160])
