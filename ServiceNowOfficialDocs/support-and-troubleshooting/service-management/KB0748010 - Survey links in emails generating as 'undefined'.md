---
title: "Survey links in emails generating as 'undefined'"
aliases:
  - KB0748010
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748010
kb_number: KB0748010
last_modified: 2026-06-08
---

## Survey links in emails generating as 'undefined'

  

### Issue

After upgrading to Madrid, Survey Links in the email are broken. 

Basically, the Survey links in the email are generated with no URL. Instead, you see 'undefined' where the URL should be. 

Steps to reproduce: 

1\. Resolve the incident

2\. Check email for Survey 

3\. Survey link will show ‘undefined’

![Survey link will be undefined](sys_attachment.do?sys_id=53e96b81db6f8d902dc24f7813961908)

### Release

Madrid

### Cause

Upon investigating we identified there were customizations made on AssessmentUtils  Script include which skipped the file during the upgrade.

\- The notification used for the surveys is Survey User Invite 

\- In the Message of this Notification the mail script has the code below: 

 Click here to take your survey: 

<mail\_script> 

var html = new AssessmentUtils().getInstanceLinkHTML(current); 

template.print(html); 

</mail\_script> 

\- This is referencing OOB Script Include and the method 'getInstanceLinkHTML(current);' 

 - After reviewing the script include ‘AssessmentUtils ‘ we determined it has been heavily customized 

\- On the current custom version of this file a huge chunk of code missing.

 From line 1119 beginning of the relevant code ( getInstanceLinkHTML : function(instanceGr) {) 

 To line 1391 is missing from the custom version of the script but exists in the OOB code. 

### Resolution

Revert to the OOB version of this file ‘AssessmentUtils ‘. After reverting Script Include ‘AssessmentUtils’ to the original version, the survey url issue is fixed.

1\. To do this navigate to the Script Include record below 

https://xxxxxx.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=ca4033c1d7110100fceaa6859e610326 

Review the 'Versions' related list on the Form. 

From the versions list, right click on the record 'System Upgrades: glide-madrid-12-18-2018\_\_patch1-hotfix2-03-14-2019\_03-20-2019\_1304.zip' 

From the pop up which is opened, select 'revert to this version'. 

2\. Alternatively, navigate to Module > Upgrade History, find the relevant skipped log record below 

Open this record, and at the bottom of the open page click the 'Resolve Conflicts' button. 

In the page that opens, scroll to the bottom of the page click the 'Revert to base system' button. 

### Related Links

Please note as per recommended after an upgrade, best practice suggests you review your skipped objects. These records should be reviewed, and you should revert any of the supplied scripts to an Out Of Box state and then reapply any customizations on top. 

This ensures that any changes made in the underlying code are current and up to date, and will work as expected on that version of the ServiceNow platform
