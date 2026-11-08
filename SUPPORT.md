# Support Policy

TrueNAS SCALE 27.0 is the primary target, with 25.10 and 26.0 compatibility
profiles retained. See the [version evidence table](README.md#supported-truenas-versions)
for the limits of documented, mocked, and live verification. Other releases
use a conservative compatibility profile.

Bug reports should include the exporter version, TrueNAS version, relevant
configuration flags, affected metric names, and redacted logs. Do not attach
API keys, `.env` files, private hostnames, or full live API responses.

Generic method/event extraction, automatic method discovery, and filesystem
listing are advanced features with a larger cardinality or compatibility
surface. Collector mode is the default supported runtime mode.
