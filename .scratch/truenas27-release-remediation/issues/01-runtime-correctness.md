# 01 Runtime correctness

Status: resolved

Fix collector-mode event publication, late deadline/transport health, and
26/27 SMB1 parsing. Cover freshness, expiry, recovery, blocked polling,
reconnect/teardown, shutdown, early/late deadlines, no late transport calls,
and malformed/missing SMB data.

## Answer

Implemented throttled collector event publication and timer shutdown, scrape-local
deadline/transport failure health, transport pre-send deadline checks, and
versioned SMB1 parsing. Focused regressions and the original reproducer pass;
current and repeated historical live sessions pass. One historical live attempt
had a transient event-freshness failure before the successful repeat.
