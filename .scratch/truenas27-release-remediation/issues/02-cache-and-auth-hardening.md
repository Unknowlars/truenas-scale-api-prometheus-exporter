# 02 Cache and authentication hardening

Status: resolved

Independently assess the gap-analysis cache freshness and authentication
diagnostic findings. Fix reproduced defects with focused regression coverage.

## Answer

Reproduced both findings. Heavy-query refresh/expiry now uses monotonic wall
time and refreshes immediately after long polling outages. Authentication
diagnostics expose only a validated response enum; `Config.api_key` is excluded
from repr. Focused regressions pass.
