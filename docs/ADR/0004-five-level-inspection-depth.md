# ADR 0004 — Five-level inspection depth for takeover

Date: 2026-10-01 · Status: Accepted

## Context

CLAUDE.md §16 names four takeover levels: SEEN, INSPECTED, TESTED, VERIFIED. The owner's
Knowledge Pack 04 §1 uses five: L1 SEEN, L2 INSPECTED, L3 DOCUMENT VERIFIED, L4 FUNCTION
TESTED, L5 PERFORMANCE VERIFIED. The 04A checklists (287 lines, 49 systems) set a target
level per line using the five-level codes SEEN / INSPECTED / DOC / TESTED / PERF.

## Decision

`InspectionDepth` carries the five pack levels plus `NOT_SEEN`:
`NOT_SEEN(0) SEEN(1) INSPECTED(2) DOC(3) TESTED(4) PERF(5)`.

- `VERIFIED` stays as an alias of `PERF`, and the string `"VERIFIED"` parses to `PERF`, so
  CLAUDE.md wording and existing data keep working.
- `DOC` and `PERF` need at least one evidence record.
- Only `TESTED` and `PERF` may be called operational. A document check (`DOC`) is not a test.
- Pack 04 §2 short codes map one-to-one onto `EvidenceStatus` (`PACK_STATUS_CODES`).
- Pack 04 §9 defect classes are `DefectClass` A–D.

## Consequences

- Stored values change from `"VERIFIED"` to `"PERF"`. No data was stored before this change.
- Open point for the owner: pack 09 Template 2 still prints four boxes
  (SEEN / INSPECTED / TESTED / VERIFIED). Reports rendered from the five-level model should
  either add DOC and PERF to the template or map PERF → VERIFIED and show DOC separately.
