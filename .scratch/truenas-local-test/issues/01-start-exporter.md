# Start packaged exporter locally

Status: resolved

## Answer

The owner explicitly authorized the prior URL/key pending manual rotation.
The key was privately recovered into a protected temporary file and mounted
read-only. No credential value appears in repository files or Docker config.

Both full validation runs passed: 324 tests, 91.75% branch coverage, all
artifact/API/Compose checks, image build and version smoke. The final rebuilt
5.2.0rc1 image is tagged `truenas-scale-api-prometheus-exporter:local-test`;
image ID `051f34661eaf38d2dee0079de2444fad83e5327211c71d5b3a132288653bb494`.
Container `truenas-local-test-exporter-1` is running and healthy.

Final loopback check: readiness 200, up=1, 1,678 samples, 33 finite CPU samples.
Windows LAN-address metrics/readiness requests returned HTTP 200. Requests from
Linux to its mirrored LAN address reset; a separate LAN client remains untested.
Metrics URL: `http://192.168.0.247:9108/metrics` (or localhost on this machine).
The owner still needs to rotate the key; TLS verification remains disabled as
in the authorized prior setup. External Prometheus ingestion and soak remain
owner acceptance work. No publication or NAS configuration change occurred.

## 2026-10-22 telemetry expansion update

The container now runs image
`30fb58e7872d46e1301d3068c43c6289309fda1715d9310fa0537d679378d345`
with 47 additional families and 497 additional finite samples. Final full gate:
357 tests, 91.80% coverage, `validation_ok`. Cold-start and event observation
passed for 70.68 seconds. The URL and mounted-key arrangement remain the same;
see `.scratch/telemetry-expansion/report.md` for the current evidence.
