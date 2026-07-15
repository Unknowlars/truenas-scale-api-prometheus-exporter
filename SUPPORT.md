# Support Policy

The latest released exporter version is supported against TrueNAS SCALE
25.10.2. Nearby TrueNAS releases may work but are not compatibility targets
until fixtures and read-only validation are added.

Bug reports should include the exporter version, TrueNAS version, relevant
configuration flags, affected metric names, and redacted logs. Do not attach
API keys, `.env` files, private hostnames, or full live API responses.

Generic method/event extraction, automatic method discovery, and filesystem
listing are advanced features with a larger cardinality or compatibility
surface. Collector mode is the default supported runtime mode.
