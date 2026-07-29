---
title: "Best Practice plugins for Change / Incident / Problem / Service Level Management"
aliases:
  - KB0661879
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0661879
kb_number: KB0661879
last_modified: 2024-09-27
---

## Best Practice plugins for Change / Incident / Problem / Service Level Management

  

### Issue

Overview

* * *

The following new best practice plugins were introduced in Jakarta. 

<table class="internalTable" style="width: 735.455px;" align=""><tbody><tr class="sphr"><td style="vertical-align: middle;"><strong>Plugin Name</strong></td><td style="vertical-align: middle;"><strong>Plugin ID</strong></td></tr><tr class="sp"><td style="vertical-align: middle;">Change Management Best Practice - Jakarta</td><td style="vertical-align: middle;">com.snc.best_practice.change.jakarta</td></tr><tr class="sp"><td style="vertical-align: middle;">Incident Management Best Practice - Jakarta</td><td style="vertical-align: middle;">com.snc.best_practice.incident.jakarta</td></tr><tr class="sp"><td style="vertical-align: middle;">Problem Management Best Practice - Jakarta</td><td style="vertical-align: middle;">com.snc.best_practice.problem.jakarta</td></tr><tr class="sp"><td style="vertical-align: middle;">Service Level Management Best Practice - Jakarta</td><td style="vertical-align: middle;">com.snc.best_practice.sla.jakarta</td></tr></tbody></table>

These plugins are activated by default for new Jakarta instances.

Upgrading to Jakarta and activating the plugins

* * *

When upgrading to Jakarta, these plugins are available for activation by requesting them through the [Now Support (HI)](https://hi.service-now.com/hisp?id=hisp_sc_item&sys_id=891f088e465667e234a3cb52ffa1d299 "Now Support (HI)"). Activating these plugins updates the forms and functionality of the applications. Before activating these plugins in an upgraded production Jakarta instance, they should be activated in a cloned, upgraded sub-production instance and validated. 

These plugins are not displayed in your plugin list, even after activation. To determine if one of these plugins has been activated, check for the following enhancements:

-   Incident Management
    -   Before - Incident form has one related list
        -   Task SLAs
    -   After – Incident form has four (or five) related list (3 or 4 new)
        -   Task SLAs
        -   Affected CIs
        -   Impacted Services
        -   Child Incidents
        -   Requests (hidden if empty)
-   Change Management
    -   Before – Change form has 7 related lists
        -   Affected CIs
        -   Impacted Services/CIs
        -   Approvers
        -   Change Tasks
        -   Problems
        -   Incidents Fixed By Change
        -   Incidents Caused By Change
    -   After – Change form has 8 related lists (1 new)
        -   Affected CIs
        -   Impacted Services/CIs (now references cmdb\_ci instead of cmdb\_ci\_service)
        -   Approvers
        -   Change Tasks
        -   Problems
        -   Incidents Fixed By Change
        -   Incidents Caused By Change
        -   Task SLAs
-   Problem Management     
    -   After – **Business Service** field added to Problem form
-   Service Level Management
    -   After – **Target** field added to the SLA Definition form

Additional Information

* * *

For details about the changes made by these plugins, see the "ITIL proven practices alignment" section in the release notes below: 

-   [Change Management Best Practice - Jakarta](https://docs.servicenow.com/csh?topicname=change-management-rn.html&version=latest "Change Management Best Practice - Jakarta")
-   [Incident Management Best Practice - Jakarta](https://docs.servicenow.com/csh?topicname=incident-management-rn.html&version=latest "Incident Management Best Practice - Jakarta")
-   [Problem Management Best Practice - Jakarta](https://docs.servicenow.com/csh?topicname=problem-management-rn.html&version=latest "Problem Management Best Practice - Jakarta")
-   [Service Level Management Best Practice - Jakarta](https://docs.servicenow.com/csh?topicname=new-features-changes.html&version=latest "Service Level Management Best Practice - Jakarta")
