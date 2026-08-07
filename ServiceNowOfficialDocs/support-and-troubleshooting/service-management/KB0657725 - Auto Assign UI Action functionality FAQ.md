---
title: "Auto Assign UI Action functionality FAQ"
aliases:
  - KB0657725
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657725
kb_number: KB0657725
last_modified: 2024-04-07
---

## Auto Assign UI Action functionality FAQ

  

### Issue

Auto Assign functionality FAQ

  
  

# Overview

* * *

This article lists some of the FAQs on the Auto Assign UI Action to explain some of the logic behind the functionality and depict the auto assignment workflow. 

For more information, see the product documentation topic [Auto assignment](https://docs.servicenow.com/csh?topicname=c_UseAutoAssignment.html&version=latest).

# Frequently Asked Questions

**Q: What are the various criteria that auto assignment can work on?**

-   Agent Skills
-   Agent Location
-   Agent Time zone
-   Consistent assignment
-   Schedules
-   Priority Assignment

**Q: What is consistent assignment?**

Tasks under the same request will be assigned to the same agent when possible.

**Q: What is Priority Assignment?**

For the configured priority tasks, the task is assigned to the next available agent without considering time zone and location. If no agent can be found in a two-week time span, the task is assigned to the manager of the assignment group.

**Q: Can an admin choose to configure both consistent assignment of tasks and assignment using agent or task schedules?**

No. If schedule is one of the chosen criteria, then consistent assignment cannot be chosen as well. Only one of the two criteria can be chosen. Use consistent assignment only if travel distance is not an important factor.

**Q: How does auto assignment pick an agent?**

Based on the configured criteria, agents are assigned a rating. Then the agent with the best rating is picked.

**Q: What if all agents have the same rating?**

If schedule is not a configured criteria, then the agent with the fewest tasks assigned gets a higher preference. If schedule is a configured criteria, then the agents are sorted based on distance (if applicable), start time, and then agent ID.

**Q: What happens when schedule is one of the configured criteria?**

Based on the window start and end of the task, every agent is checked to see if they can complete the work in that window. If a valid work block is found, the task the agent would be working on before this task and after this task is identified. Then the travel time between the tasks is calculated and used to assign a rating for the work block. For every agent, the best work block is identified. Then the best work block among all the agents is identified. The task is then assigned to that agent for that work block.

**Q: How is agent availability determined?**

The availability of agents is determined using the work schedule of the agent. Any time off and tasks assigned to an agent will be considered as times the agent is not available to work.

**Q: If the agent does not have a work schedule assigned, what work schedule is considered?**

If the agent does not have a work schedule, then the agent work schedule is determined using a system property. For FSM, the start time property is - work.management.default.start.time and the end time property is work.management.default.end.time. If these properties are not configured, then an 08:00 to 17:00 default is used. For other application, the property prefix would be different.

**Q: As an admin, I want both skills and location of agent to be considered but want the location to be given a higher priority over skills. How can this be achieved?**

You can use system properties to provide weights to various criteria. An admin can provide a higher weight for location (10) and a lower weight for skills. The weights need to be between 0 and 10. For Field Service, these weights are work.management.skills.weight and work.management.location.weight. For other applications, the property prefix would be different.

# Workflow

![](sys_attachment.do?sys_id=682cec2edb42b450e515c22305961981)

![](sys_attachment.do?sys_id=642cec2edb42b450e515c22305961987) ![](sys_attachment.do?sys_id=a42cec2edb42b450e515c2230596198c)![](sys_attachment.do?sys_id=ac2cec2edb42b450e515c2230596199d)
