# 03 Container and Prometheus lint

Status: resolved

Build and scan the exact supported runtime image, remediate fixed advisories
without suppressions, preserve hardening, and account for every inherited
Prometheus lint warning while making new warnings fail validation.

## Answer

Updated the release runtime to Python 3.14.8 / Debian 13.7 and removed pip from
the final stage. The exact final image has 164 scanner findings, none critical
or with a listed fix, versus 330/3 critical historically; application audit is
clean. All inherited Prometheus warnings are fingerprinted and new warning-name
changes fail validation while all 420 metric contracts remain unchanged.
