---
aliases:
  - "Comparing various things"
tags:
  - cis-certification
  - cmdb
  - csdm
  - data-foundations
  - exam-prep
---

# Comparing various things

1. **CMDB Health Dashboard**

Purpose: Measure and monitor CMDB data quality

What it is

- A reporting and KPI layer
- Shows how healthy your CMDB is, not how to fix it
- Read-only insight

Focus areas (very exam-relevant):

- Completeness
- Correctness
- Compliance
- Relationship health
- Duplicate CIs
- Stale CIs

Who uses it

- CMDB managers
- Process owners
- Architects
- Auditors

Typical exam wording

“Where do you view CMDB health metrics?”

“Which tool provides visibility into CMDB data quality?”

✅ Correct answer: CMDB Health Dashboard

Key exam trap

- ❌ It does not remediate issues
- ❌ It does not manage CI classes
- ❌ It does not load or normalize data

👉 Think: “scoreboard”

1. **CMDB Workspace**

Purpose: Operational workspace for managing and improving CMDB data

What it is

- A persona-based UI
- Central place to act on CMDB issues
- Used for day-to-day CMDB operations

What you actually do here

- Review health issues
- Investigate problematic CIs
- Launch remediation tasks
- Coordinate data owners and CI analysts

Who uses it

- CI Analysts
- CMDB Analysts
- Configuration Managers

Typical exam wording

“Where do CI analysts work to resolve CMDB issues?”

“Which interface supports operational CMDB maintenance?”

✅ Correct answer: CMDB Workspace

Key exam trap

- ❌ It is not where data sources are configured
- ❌ It is not for class modeling
- ❌ It is not pure reporting

👉 Think: “command center”

1. **CMDB Data Manager**

Purpose: Control and govern incoming CMDB data

This is one of the MOST tested areas in CIS-DF

What it is

- The data ingestion and normalization authority
- Governs what data is allowed into the CMDB and how

Key capabilities

- Data sources
- Identification rules
- Reconciliation rules
- Data precedence
- Attribute-level trust

Who uses it

- CMDB architects
- Platform owners
- Integration teams

Typical exam wording

“Which component controls data precedence?”

“Where are reconciliation rules defined?”

“How do you prevent poor-quality data from overwriting trusted sources?”

✅ Correct answer: CMDB Data Manager

Key exam trap

- ❌ It does not visualize health
- ❌ It does not manage CI class structure
- ❌ It does not handle operational remediation

👉 Think: “gatekeeper”

1. **CI Class Manager**

Purpose: Design and maintain the CMDB data model

What it is

- The schema/modeling tool for the CMDB
- Controls structure, not data quality

What you do here

- Create CI classes
- Extend base classes
- Define attributes
- Define relationships
- Control inheritance

Who uses it

- CMDB architects
- Platform architects

Typical exam wording

“Where do you define CI attributes?”

“Which tool manages CMDB class hierarchy?”

“How do you extend the CMDB data model?”

✅ Correct answer: CI Class Manager

Key exam trap

- ❌ It does not load data
- ❌ It does not fix duplicates
- ❌ It does not measure health

👉 Think: “blueprint”

**🔥 Exam-Perfect Comparison Table**

| **Tool** | **Core Function** | **Exam Keyword** |
| --- | --- | --- |
| CMDB Health Dashboard | Measure CMDB quality | Visibility |
| CMDB Workspace | Operate & remediate CMDB | Execution |
| CMDB Data Manager | Govern incoming data | Control |
| CI Class Manager | Define CMDB structure | Modeling |

**🧠 How the exam**

**tries to trick you**

- If the question says “view”, “monitor”, “assess” → Health Dashboard
- If it says “fix”, “resolve”, “work on issues” → Workspace
- If it says “source priority”, “reconciliation”, “trusted data” → Data Manager
- If it says “attributes”, “classes”, “relationships” → Class Manager

---

Below is an expanded “exam-perfect comparison table” with the extra dimensions the exam loves to test, plus the mental shortcuts to kill trick questions fast.

**🧠 Expanded Exam-Perfect Comparison Table (High-Yield)**

| **Dimension the Exam Tests** | **CMDB Health Dashboard** | **CMDB Workspace** | **CMDB Data Manager** | **CI Class Manager** |
| --- | --- | --- | --- | --- |
| Primary intent | Measure | Act | Govern | Model |
| Persona focus | Manager / Owner | Analyst / Operator | Architect / Platform | Architect |
| Read vs Write | Read-only | Read + Fix | Control writes | Schema changes |
| Data lifecycle stage | After data exists | After issues detected | Before data is committed | Before data exists |
| Handles duplicates? | Detect only | Remediate | Prevent via rules | No |
| Handles reconciliation? | No | No | Yes | No |
| Handles normalization? | No | No | Yes | No |
| Controls data trust? | No | No | Yes | No |
| Controls CI attributes? | No | No | No | Yes |
| Controls relationships? | No | Investigate only | No | Yes |
| Operational vs design | Governance | Operational | Governance | Design |
| Exam trigger words | Health, KPIs, visibility | Resolve, manage, work | Source, precedence, trust | Class, attribute, relationship |

**🔥 High-Frequency “Trick Dimensions” the Exam Uses**

1. **“Where in the lifecycle?” (very sneaky)**

If you map tools to when they act, answers get obvious:

- Before data enters CMDB → CMDB Data Manager
- After data enters CMDB but before fixing → CMDB Health Dashboard
- Fixing data already in CMDB → CMDB Workspace
- Before any CI exists at all → CI Class Manager

👉 If the question mentions “prevent”, it’s almost never Workspace or Dashboard.

1. **“Visibility vs Control” (classic exam bait)**

The exam loves to pair these words:

- Visibility, insight, metrics, monitoring → Health Dashboard
- Control, governance, enforcement → Data Manager

If both appear, control always wins.

1. **“Who would realistically do this?”**

This saves you when two answers feel right.

Ask:

- Would a CI Analyst do this? → Workspace
- Would a CMDB Architect do this? → Data Manager or Class Manager
- Would a Process Owner review this? → Health Dashboard

The exam is very role-driven even when it doesn’t say so.

1. **Duplicates: Detect vs Fix vs Prevent**

This is a huge exam favorite.

| **Action** | **Tool** |
| --- | --- |
| Detect duplicate CIs | CMDB Health Dashboard |
| Resolve / merge duplicates | CMDB Workspace |
| Prevent duplicates from trusted sources | CMDB Data Manager |
| Define CI uniqueness model | CI Class Manager (indirectly) |

If the question says “prevent”, Workspace is wrong 100% of the time.

1. **Data vs Structure (subtle but deadly)**
- Data = records, values, freshness → Dashboard / Workspace / Data Manager
- Structure = tables, fields, inheritance → CI Class Manager

If the question mentions:

- Attribute existence → Class Manager
- Attribute correctness → Health / Workspace / Data Manager

Existence ≠ correctness. The exam loves that distinction.

**🚨 Ultra-Common Exam Traps (Avoid These)**

❌ “CMDB Workspace improves CMDB health”

✔️ Wrong — it remediates issues, it does not measure health

❌ “CMDB Health Dashboard fixes data quality”

✔️ Wrong — it only reports

❌ “CI Class Manager controls data sources”

✔️ Wrong — that’s Data Manager territory

❌ “Reconciliation rules are defined in Workspace”

✔️ Wrong — always Data Manager

**🧠 One-Line Memory Hack (Gold for Exam Day)**

Model → Govern → Measure → Fix

Class Manager → Data Manager → Health Dashboard → Workspace

If you keep that order in your head, 90% of trick questions collapse instantly.

---

IRE is the final boss of CIS-DF trick questions. Once you really place it correctly, a lot of “this feels like two answers” problems just… disappear.

Below is the clean, exam-ready add-on:

1. IRE added to the comparison table
2. The exact traps the exam sets around it
3. A couple of killer memory rules that save time under pressure

**🧠 Expanded Exam-Perfect Comparison Table (with IRE)**

| **Tool** | **Core Role** | **Acts On** | **When It Acts** | **Key Exam Verbs** |
| --- | --- | --- | --- | --- |
| CI Class Manager | Define structure | Schema | Before data exists | Define, model, extend |
| CMDB Data Manager | Govern data | Sources & rules | Before commit | Control, prioritize, trust |
| IRE (Identification & Reconciliation Engine) | Enforce rules | Incoming records | At commit time | Identify, reconcile, merge |
| CMDB Health Dashboard | Measure quality | Stored data | After commit | View, assess, monitor |
| CMDB Workspace | Fix issues | Stored data | After detection | Resolve, remediate |

👉 IRE is the execution engine between Data Manager rules and actual CMDB writes.

**🎯 What IRE Actually Does (Exam-Correct)**

IRE is NOT a UI and NOT a configuration hub IRE:

- Applies identification rules
- Applies reconciliation rules
- Decides:
    - Update existing CI
    - Create new CI
    - Ignore incoming data
- Runs every time data is inserted or updated

Configured elsewhere, executed here.

Data Manager = policy

IRE = enforcement

This distinction shows up constantly.

**🚨 High-Probability IRE Exam Traps (Memorize These)**

**🔥 Trap 1: “Where are reconciliation rules defined?”**

- ❌ IRE
- ❌ CMDB Workspace
- ❌ Health Dashboard
- ✅ CMDB Data Manager

📌 IRE executes rules — it never defines them

**🔥 Trap 2: “Which component prevents duplicate CIs?”**

This is wording-dependent:

| **Wording** | **Correct Answer** |
| --- | --- |
| Prevents duplicates via rules | CMDB Data Manager |
| Identifies whether a CI already exists | IRE |
| Detects duplicate records | Health Dashboard |
| Resolves duplicates | Workspace |

If the question says “identify existing CI”, that’s IRE, not Data Manager.

**🔥 Trap 3: “Controls data precedence”**

- ❌ IRE
- ❌ Workspace
- ❌ Health Dashboard
- ✅ CMDB Data Manager

But…

“Applies data precedence during insert/update”

✅ IRE

Control vs Apply is the key word difference.

**🔥 Trap 4: “Where does identification happen?”**

- ❌ Discovery
- ❌ Import Set
- ❌ Data Source
- ❌ Workspace
- ✅ IRE

Even Discovery results go through IRE before touching the CMDB.

**🔥 Trap 5: “IRE improves CMDB health”**

❌ Wrong

IRE can prevent bad data, but it does not:

- Measure health
- Report on health
- Fix existing bad data

That’s Dashboard + Workspace territory.

**🧠 Ultra-Clean Mental Model (Exam Gold)**

**The**

**CMDB Data Flow Stack**

CI Class Manager  →  CMDB Data Manager  →  IRE  →  CMDB

↓

Health Dashboard → Workspace

Or in words:

Model → Govern → Enforce → Measure → Fix

If you remember this order, you can answer almost any CMDB tooling question by elimination alone.

**🧪 IRE vs Data Manager (Most Confused Pair)**

| **Question Angle** | **Correct Answer** |
| --- | --- |
| Where rules are created | Data Manager |
| Where rules are enforced | IRE |
| Who decides trust level | Data Manager |
| Who applies trust at runtime | IRE |
| Who merges records | IRE |
| Who defines merge behavior | Data Manager |

If both appear as options, ask yourself:

“Is this about definition or execution?”

**🧨 One-Sentence Exam Killer Rule**

If the question mentions “incoming data” + “decides create vs update” → IRE

No exception. Ever.

## Related

- [[Study material]]
- [[Exam questions]]
- [[Certified Implementation Specialist in Data Founda – Tips]]
- [[Certified Implementation Specialist in Data Founda]]
- [[CMDB]]