---
title: "Troubleshooting upgrade issues"
aliases:
  - KB0535172
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535172
kb_number: KB0535172
last_modified: 2025-06-30
---

## Troubleshooting upgrade issues

  

### Issue

This article guides you through the process of troubleshooting an upgrade that is not starting or finishing properly. It provides steps to help you eliminate common causes for your problem by verifying that the configuration of your networking is correct.

The latest upgrade documentation can be found here: [ServiceNow Upgrades](https://docs.servicenow.com/csh?version=latest&topicname=upgrade.html "ServiceNow Upgrades").

### Symptoms

Symptoms may include the following:

-   Upgrade did not start
-   Upgrade schedule did not work
-   Upgrade did not finish

### Resolution

Validate that each troubleshooting step below is true for your environment. Each step provides instructions or a link to an article to eliminate possible causes and take corrective action as necessary. The steps are ordered in the most appropriate sequence to isolate the issue and identify the proper resolution. 

1.  First, review the upgrade process. For more information, see [ServiceNow Upgrades](https://docs.servicenow.com/csh?version=latest&topicname=upgrade.html "ServiceNow Upgrades").
2.  If the upgrade does not start, follow the troubleshooting steps in [KB0743666: Upgrade did not start at the expected time](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743666 "KB0743666: Upgrade did not start at the expected time").
3.  Determine if the upgrade was successful using the Upgrade Log. For more information, see [Explore upgrade history log](https://www.servicenow.com/docs/csh?topicname=uc-explore-history-log.html&version=latest "Explore upgrade history log").
4.  Check the upgrade WAR properties. For more information, see [KB0535199: Instance Dashboard shows different upgrade version from stats.do](/kb?id=kb_article_view&sysparm_article=KB0535199 "KB0535199: Instance Dashboard shows different upgrade version from stats.do").

 **Note:** If your problem still exists after trying the steps in this article, [submit a case to our Support team](/kb?id=kb_article_view&sysparm_article=KB0640039) and note this Knowledge Base article ID (KB0535172) in the description.
