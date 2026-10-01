# Core instruction fragments

Small, always-loaded prompt text. Each file is the **single canonical home** of a rule listed in
Spec Part B.2. Role and skill fragments add to these; they never restate them.

Load order: `identity.md` → `safety.md` → `regulatory_discipline.md` → `decision_support.md` →
`sea_eye.md` → `formats/*` (loaded when the router selects that format).

Bundle version is set in `capt_crewvn/core/system/VERSION` and recorded on every audit event.
