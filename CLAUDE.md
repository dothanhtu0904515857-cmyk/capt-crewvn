# CAPT CREWVN — CLAUDE.md

## 1. PROJECT IDENTITY

Project name:

**Capt Crewvn — Maritime AI Platform**

Capt Crewvn is a professional maritime AI platform for shipboard and shore-side maritime professionals.

It originated from the Cargo Ship Captain professional methodology but is being expanded into a modular, role-aware and vessel-aware maritime AI ecosystem.

This repository must not become a generic chatbot wrapper.

---

## 2. PRIMARY OBJECTIVE

Build Capt Crewvn as a durable architecture in which the following can evolve independently:

- LLM provider/model
- system instructions
- specialist skills/modules
- retrieval system
- vessel data
- company/SMS data
- user accounts
- frontend
- backend
- tools/functions
- databases
- reports
- audit trail

Do not tightly couple Capt Crewvn to one LLM vendor.

---

## 3. PROFESSIONAL BEHAVIOR

All system design must preserve these Capt Crewvn principles:

1. Safety first.
2. Practical seamanship.
3. Verified facts over assumptions.
4. Role-aware answers.
5. Vessel-aware answers.
6. Company/SMS-aware answers.
7. Accurate maritime terminology.
8. Source transparency.
9. No invented regulations.
10. No invented vessel particulars.
11. No fabricated inspection/test results.
12. No fabricated records.
13. No concealment of deficiencies.
14. No unsafe bypassing of protections.
15. Professional decision support, not unauthorized replacement of responsible officers.

---

## 4. USER ROLES

The architecture must support at minimum:

### Deck

- Master
- Chief Officer
- Second Officer
- Third Officer
- Deck Officer
- Bosun
- Able Seafarer / AB
- Ordinary Seaman / OS
- Deck Cadet

### Engine

- Chief Engineer
- Second Engineer
- Third Engineer
- Fourth Engineer
- Engine Officer
- ETO
- Electrician
- Fitter / Welder
- Oiler / Motorman
- Wiper
- Engine Cadet

### Shore

- Ship Owner
- Ship Manager
- Marine Superintendent
- Technical Superintendent
- DPA
- CSO
- HSQE
- Operations
- Crewing
- Purchasing
- Training
- Claims / P&I support where appropriate

### Training

- Cadet
- Maritime student
- Promotion candidate
- Maritime English learner
- Maritime Chinese learner

Never assume two roles require identical information.

---

## 5. VESSEL CONTEXT MODEL

Never hard-code one vessel's data into general application logic.

Use a vessel entity.

Suggested core structure:

```yaml
vessel:
  vessel_id:
  current_name:
  former_names: []
  imo_number:
  call_sign:
  flag:
  class_society:
  vessel_type:
  built:
  shipyard:
  dwt:
  gt:
  nt:
  loa:
  breadth:
  depth:
  summer_draft:
  main_engine:
  auxiliary_engines: []
  machinery: []
  navigation_equipment: []
  safety_equipment: []
  cargo_systems: []
  ballast_system:
  bwms:
  owners:
  managers:
  sms_profile:
```

<!-- NOTE: the pasted copy of section 5 ended after `sms_profile:`. Any further vessel fields or text from the original section 5 are not yet included. -->

---

## 6. COMPANY CONTEXT

Company data must be separate from global Capt Crewvn knowledge.

Suggested structure:

```yaml
company:
  company_id:
  name:
  sms_version:
  fleet:
  procedures:
  forms:
  pms_system:
  reporting_rules:
  defect_policy:
  purchasing_policy:
  emergency_contacts:
```

One company's SMS shall never automatically apply to another company.

---

## 7. KNOWLEDGE HIERARCHY

Use source-aware retrieval.

For vessel-operational questions, consider:

1. Verified live/current vessel facts
2. Approved vessel documents
3. Company SMS/PMS
4. Maker manuals
5. Applicable statutory requirements
6. Flag
7. Class
8. Port / terminal rules
9. Capt Crewvn curated knowledge
10. General model knowledge

The exact precedence depends on the question.

Never allow lower-authority material to silently override statutory or approved requirements.

---

## 8. KNOWLEDGE METADATA

Every indexed document should support metadata such as:

```yaml
document:
  document_id:
  title:
  document_type:
  authority:
  company_id:
  vessel_id:
  vessel_type:
  department:
  role:
  module:
  language:
  revision:
  effective_date:
  source:
  status:
```

Recommended `authority` values:

- IMO
- FLAG
- CLASS
- PORT
- TERMINAL
- COMPANY_SMS
- MAKER
- VESSEL_APPROVED
- CAPT_CREWVN
- TRAINING_REFERENCE

---

## 9. ROLE ROUTER

Before specialist reasoning, determine:

- user role
- vessel
- department
- operation
- task type
- urgency
- whether immediate danger exists
- required specialist module
- relevant source authority

Suggested conceptual pipeline:

```text
USER
 ↓
IDENTITY / ROLE
 ↓
VESSEL CONTEXT
 ↓
SAFETY TRIAGE
 ↓
TASK CLASSIFICATION
 ↓
SPECIALIST ROUTER
 ↓
KNOWLEDGE RETRIEVAL
 ↓
TOOLS
 ↓
LLM REASONING
 ↓
SOURCE / SAFETY CHECK
 ↓
OUTPUT
```

---

## 10. SPECIALIST MODULES

Keep modules independently maintainable.

Initial module namespace:

```text
captain-adviser
ship-takeover
psc-readiness
engine-systems
pms
defect-management
deck-machinery
cargo-operations
hold-inspection
hatch-cover
ballast-bilge
bwms
fuel-management
gmdss
bridge-watchkeeping
navigation
shiphandling-voyage
cold-weather
ice-navigation
grounding-emergency
crew-leadership
maritime-training
shipping-industry
inventory-stores
documentation
```

Do not put all domain rules into one system prompt.

---

## 11. SAFETY RULES

Never design a workflow that encourages users to:

- bypass safety protections
- disable alarms/interlocks
- falsify logs
- backdate records
- conceal deficiencies
- manipulate bunker figures
- hide pollution
- conduct illegal discharge
- enter enclosed spaces without approved controls
- conduct dangerous machinery tests outside approved procedures
- impersonate inspectors or authorities
- falsify signatures
- fabricate inspection evidence

For hazardous operations prefer:

- current vessel procedure
- permit-to-work
- risk assessment
- responsible officer authorization
- maker instructions
- company SMS
- isolation / LOTO where applicable

---

## 12. REGULATORY DISCIPLINE

Never generate a regulation number merely because one seems plausible.

For exact/current regulatory claims:

- retrieve authoritative source if available;
- clearly distinguish source text from model explanation;
- expose uncertainty;
- state applicable date/version when important.

Relevant frameworks may include:

- SOLAS
- MARPOL
- STCW
- COLREG
- ISM Code
- ISPS Code
- MLC 2006
- IMSBC Code
- IMDG Code
- BWM Convention
- Load Line Convention
- Flag requirements
- Class rules
- Port regulations

---

## 13. SEA EYE

Capt Crewvn may teach practical “sea eye” observations such as:

- abnormal vessel movement
- unusual machinery sound
- abnormal vibration
- developing weather
- mooring-line loading
- abnormal trim/list
- cargo-operation anomalies

However:

Observation is not diagnosis.

Use:

```text
OBSERVED
→ SUSPECTED
→ TESTED
→ VERIFIED
```

Never jump directly from observation to confirmed defect without evidence.

---

## 14. INCIDENT ANALYSIS

Preferred structure:

```text
FACTS
KNOWN RISKS
POSSIBLE CAUSES
IMMEDIATE ACTIONS
CORRECTIVE ACTIONS
PREVENTIVE ACTIONS
```

Do not state a cause as confirmed unless evidence supports it.

---

## 15. EMERGENCY RESPONSE

Preferred structure:

```text
IMMEDIATE ACTIONS
→ STABILIZE
→ ASSESS DAMAGE
→ COMMUNICATION
→ POLLUTION PREVENTION
→ STABILITY / STRENGTH
→ RECOVERY
→ RECORDS / EVIDENCE
→ FOLLOW-UP
```

Immediate safety takes precedence over documentation.

---

## 16. TAKEOVER INSPECTION MODEL

For ship delivery/takeover work distinguish:

```text
SEEN
INSPECTED
TESTED
VERIFIED
```

Never represent untested machinery as verified operational.

Support evidence statuses:

- SATISFACTORY_AS_OBSERVED
- DEFECT_OBSERVED
- NOT_TESTED
- NOT_ACCESSIBLE
- NOT_VERIFIED
- FURTHER_VERIFICATION_REQUIRED

Where access is restricted, preserve the restriction as evidence instead of inventing a conclusion.

---

## 17. LANGUAGE STRATEGY

Default professional languages:

- Vietnamese
- Maritime English
- Simplified Chinese

Do not use generic machine translation for maritime terminology when an established maritime term exists.

Examples:

```text
Master = Thuyền trưởng = 船长
Chief Officer = Đại phó = 大副
Chief Engineer = Máy trưởng = 轮机长
Second Engineer = Máy hai = 大管轮
spare parts = phụ tùng = 备件
stores/materials = vật tư = 物料
Engine Department = Bộ phận máy = 轮机部
Deck Department = Bộ phận boong = 甲板部
```

Preserve commonly used abbreviations such as:

- PSC
- PMS
- SMS
- GMDSS
- ECDIS
- OWS
- BWMS
- ROB

---

## 18. REPORTING

Reports should distinguish:

- observation
- measured data
- documentation evidence
- operator statement
- assumption
- recommendation
- unresolved item

Never phrase an assumption as a verified fact.

---

## 19. TOOL ARCHITECTURE

Tools must be typed and auditable.

Potential tool families:

```text
get_vessel_context()
search_sms()
search_maker_manual()
search_regulation()
search_class_requirement()
search_pms()
get_equipment_history()
get_defect_history()
create_defect_report()
create_takeover_report()
create_checklist()
calculate_rob()
reconcile_inventory()
create_handover_report()
translate_maritime()
```

Sensitive write operations should require appropriate permission.

---

## 20. SECURITY

Never expose:

- API keys
- database credentials
- private connector tokens
- service account secrets

Frontend code must never contain privileged API secrets.

Use server-side secrets and environment variables.

Implement role-based authorization for vessel/company data.

---

## 21. AUDITABILITY

For important outputs preserve when possible:

- user
- role
- vessel
- timestamp
- sources retrieved
- tool calls
- version of instructions
- generated report
- subsequent edits/approval

Human approval must remain distinguishable from AI-generated text.

---

## 22. SOFTWARE QUALITY

Prefer:

- modular architecture
- typed interfaces
- schemas
- unit tests
- integration tests
- deterministic validation
- clear error handling
- migrations
- logging
- maintainable documentation

Avoid:

- giant single files
- giant universal prompts
- hidden magic constants
- vessel data in source code
- duplicated domain rules
- untyped tool payloads

---

## 23. CHANGE POLICY

Before a major architectural change:

1. inspect existing architecture;
2. identify impacted modules;
3. preserve backward compatibility when practical;
4. explain migration;
5. update tests;
6. update documentation.

Do not rewrite stable portions of the system unnecessarily.

---

## 24. PRODUCT BOUNDARY

Capt Crewvn provides decision support.

It does not claim to be:

- the Master
- the Chief Engineer
- Flag State
- Classification Society
- surveyor
- competent authority
- doctor
- licensed legal counsel

The responsible human professional remains responsible for operational decisions.

---

## 25. COMMUNITY / CREWVN ECOSYSTEM

Capt Crewvn may support the wider Crewvn ecosystem including:

- professional community
- training
- recruitment
- career support
- seafarer development

Do not inject promotional content into unrelated technical answers.

Community references should be relevant, useful and non-intrusive.

---

## 26. FINAL ENGINEERING PRINCIPLE

When choosing between:

- a clever solution
- and a transparent, maintainable, verifiable solution

choose the transparent solution.

When choosing between:

- a plausible maritime answer
- and admitting missing vessel/source data

admit the missing data.

Capt Crewvn's credibility depends on professional accuracy.
