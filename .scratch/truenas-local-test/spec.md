# Local packaged exporter test

Run the updated image on this machine for owner-managed Prometheus scraping.
The owner explicitly authorized reuse of the previous URL/key on 2026-10-22
and will rotate the key manually. The key is mounted read-only from a protected
temporary directory outside the repository. Preserve existing work.

The container publishes port 9108 to the LAN, polls every 30 seconds, and uses
the existing bounded, read-only collector and event subscriptions. No image
publication or NAS configuration changes are in scope.

Start after supplying `TRUENAS_API_KEY_HOST_FILE` and `TRUENAS_WS_URL`:

```sh
docker compose -p truenas-local-test -f .scratch/truenas-local-test/compose.yml up -d
```

The mounted key must be readable by container UID 10001. TLS verification is
enabled by default; a private CA can be supplied through an additional mount
and `TRUENAS_CA_FILE` when needed. Do not put the key in shell arguments or chat.

Stop with the same Compose invocation followed by `down` instead of `up -d`.

Current run uses `TRUENAS_API_KEY_HOST_FILE=/tmp/truenas-local-test-secrets/api_key`,
the previous NAS URL, `TRUENAS_USERNAME=root`, and `TRUENAS_VERIFY_TLS=false`.
Supply these environment variables again for Compose commands. The temporary
key file is mode 0400, owned by UID/GID 10001, within a mode 0700 directory.
It must be replaced after rotation; recreate the container to load the new key.
Temporary files may be cleared on reboot. The dedicated `local-test` image tag
isolates this run from subsequent validation builds.
