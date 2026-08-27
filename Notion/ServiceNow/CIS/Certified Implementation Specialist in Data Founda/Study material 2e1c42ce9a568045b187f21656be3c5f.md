---
aliases:
  - "Study material"
area: "CIS"
source: notion-export
tags:
  - cis-certification
  - cmdb
  - csdm
  - data-foundations
  - exam-prep
---

# Study material

The CMDB is not just a database — it's a dynamic ecosystem built on three pillars: 
𝗜𝗻𝗴𝗲𝘀𝘁, 𝗚𝗼𝘃𝗲𝗿𝗻, 𝗮𝗻𝗱 𝗜𝗻𝘀𝗶𝗴𝗵𝘁.

Here's the breakdown:

⸻

𝗜𝗻𝗴𝗲𝘀𝘁𝗶𝗼𝗻 𝗶𝘀 𝗺𝗼𝗿𝗲 𝘁𝗵𝗮𝗻 𝗷𝘂𝘀𝘁 "𝗗𝗶𝘀𝗰𝗼𝘃𝗲𝗿𝘆"

When I started studying for the CIS-DR, I assumed the CMDB was just 
populated by network scans. In reality, it's a multi-layered approach:

- 𝗛𝗼𝗿𝗶𝘇𝗼𝗻𝘁𝗮𝗹 𝗗𝗶𝘀𝗰𝗼𝘃𝗲𝗿𝘆 finds the infrastructure
- 𝗦𝗲𝗿𝘃𝗶𝗰𝗲 𝗠𝗮𝗽𝗽𝗶𝗻𝗴 provides a top-down view of how infrastructure supports business services
- 𝗔𝗴𝗲𝗻𝘁 𝗖𝗹𝗶𝗲𝗻𝘁 𝗖𝗼𝗹𝗹𝗲𝗰𝘁𝗼𝗿 (𝗔𝗖𝗖) gives real-time visibility into endpoints and software usage
- 𝗦𝗲𝗿𝘃𝗶𝗰𝗲 𝗚𝗿𝗮𝗽𝗵 𝗖𝗼𝗻𝗻𝗲𝗰𝘁𝗼𝗿𝘀 keep everything consistent across third-party tools like Azure or AWS

⸻

𝗚𝗼𝘃𝗲𝗿𝗻𝗮𝗻𝗰𝗲 𝗶𝘀 𝘄𝗵𝗲𝗿𝗲 𝗺𝗼𝘀𝘁 𝘁𝗲𝗮𝗺𝘀 𝗳𝗮𝗶𝗹

Populating data is only half the battle. Keeping it healthy is the real work.

Good governance means focusing on three metrics: 𝗖𝗼𝗺𝗽𝗹𝗲𝘁𝗲𝗻𝗲𝘀𝘀, 𝗖𝗼𝗺𝗽𝗹𝗶𝗮𝗻𝗰𝗲, 𝗮𝗻𝗱 𝗖𝗼𝗿𝗿𝗲𝗰𝘁𝗻𝗲𝘀𝘀.

Correctness is huge — this is where you use the 𝗗𝘂𝗽𝗹𝗶𝗰𝗮𝘁𝗲 𝗖𝗜  𝗥𝗲𝗺𝗲𝗱𝗶𝗮𝘁𝗼𝗿 and 𝗜𝗥𝗘 (𝗜𝗱𝗲𝗻𝘁𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗮𝗻𝗱  𝗥𝗲𝗰𝗼𝗻𝗰𝗶𝗹𝗶𝗮𝘁𝗶𝗼𝗻 𝗘𝗻𝗴𝗶𝗻𝗲) to ensure you don't end up with five different records for the same physical server.

The crucial step most people miss: automated tools can't find everything. 
You 𝘮𝘶𝘴𝘵 supplement discovered data with  𝗻𝗼𝗻-𝗱𝗶𝘀𝗰𝗼𝘃𝗲𝗿𝗮𝗯𝗹𝗲 𝗱𝗮𝘁𝗮 like "Owned by," "Support  group," and "Location." Without this, your Incident and Change management processes will still be stuck in manual mode.

⸻

𝗜𝗻𝘀𝗶𝗴𝗵𝘁 𝗶𝘀 𝘁𝗵𝗲 𝘂𝗹𝘁𝗶𝗺𝗮𝘁𝗲 𝗴𝗼𝗮𝗹

The reason we do all this isn't to have a pretty list of servers — it's to bridge "The Gap."

On one side: IT Operations managing technology silos (Servers, Storage, Networks).

On the other: Business Users consuming services (Email, Payroll, Inventory).

The CMDB provides the Insight to answer business-critical questions:

- Which IT components deliver this service?
- If this server goes down, which business services are affected?
- Will this change have a business impact?

⸻

By treating the CMDB as a 𝗰𝗲𝗻𝘁𝗿𝗮𝗹 𝘀𝘆𝘀𝘁𝗲𝗺 𝗼𝗳 𝗿𝗲𝗰𝗼𝗿𝗱  that drives outcomes, you stop just managing "boxes" and start empowering data-driven decisions for the entire business.

[Comparing various things](Study%20material/Comparing%20various%20things%202f3c42ce9a56809180a2c25e0ac60009.md)

## Related
- [[CIS]]
- [[How to access a Technical Challenge]]
- [[Architectural Principles]]

- [[Certified Implementation Specialist in Data Founda]]
- [[Comparing various things]]
- [[Exam questions]]
- [[Certified Implementation Specialist in Data Founda – Tips]]
- [[CMDB]]