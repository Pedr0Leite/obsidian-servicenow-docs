---
title: "The Purpose of the Quarterly Patching Program and Its Quarterly Schedule "
aliases:
  - KB0551462
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551462
kb_number: KB0551462
last_modified: 2026-04-21
---

## The Purpose of the Quarterly Patching Program and Its Quarterly Schedule 

  

### Issue

### Overview

The ServiceNow Quarterly Patching Program (QPP) provides quarterly patches for customer instances throughout the year. Its primary goal is to ensure that each customer instance receives the latest updates related to security, performance, availability, and functionality fixes. Importantly, patching addresses known security vulnerabilities is crucial in any patch management strategy.

ServiceNow will patch customer instances to the required version in the first month of each quarter. In the second and third months, security patches will be applied, totalling one full patch and two security patches. If no security patch is needed in the second or third months, you will be notified.

However, around 10 days before the quarter, ServiceNow announces the minimum patch version for each release family and the patch schedule, allowing you to upgrade to a higher version or patch earlier. In the first month, all instances are upgraded to the minimum version.

During the second and third months, we will address vulnerabilities with scheduled security patches, creating Changes one week in advance for non-production and three weeks for production instances, while allowing for higher versions or earlier patching. Security patches include fixes for target versions; for example, if the target is Xanadu Patch 6, the security patch Xanadu Patch 6a will include its fixes. Typically, there are fewer than five fixes, but more may be added if necessary.

**Note**: Instances not on the minimum version will undergo a separate patching program for that month.

### Release

ALL

### Resolution

**Every quarter, an Update record is created for each company. ServiceNow uses the Company Version Update record for these purposes:**

-   ServiceNow sends notifications about the quarterly patching program midway through the final month of a quarter. You will be informed of the Patch Targets for the next quarter, and a CHG will be scheduled to patch your instances accordingly. If a security patch is needed, you will be notified, and a CHG will be created at least 10 days before your first scheduled patch.
-   ServiceNow tracks all of the customer's instances requiring patching. If an instance is not on the minimum patch version for the patching month, you will be notified and a CHG will be created at least 5 days prior to your scheduled patch.
-   ServiceNow provides the opportunity to communicate with the dedicated team regarding their patching program through their **Parent CHG** in advance by asking questions, requesting extensions, to managing the Patching Program. For example, you should expect to see a communication and have your patch scheduled for January by mid-December. The February security patch should be scheduled during the final week of January.

Remember: Update and maintain contacts listed in your company record to ensure that you receive important program-related notifications and that they are sent to the appropriate contacts. For more information on managing company contacts, see [KB0547262: Managing company contacts on Now Support](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547262 "KB0547262: Managing company contacts on Now Support").

### Related Links

**For more information about the Quarterly Patching Program, see the following:**

-   [ServiceNow Patching Program FAQs](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696901 "ServiceNow Patching Program FAQs")

**For information on how customers can reach out to the dedicated ServiceNow team about their Patching and Upgrade Program, refer to the following KB:**

-   [How to Post Comments on Patching and EOL Changes (CHG) to Request Support](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1644913 "KB1644913")
