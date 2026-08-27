---
title: "\"SAM - Deduplicate Install Table\" job is not marking the Duplicate software installs Active Installs to False"
aliases:
  - KB1001971
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1001971
kb_number: KB1001971
last_modified: 2026-06-19
---

## "SAM - Deduplicate Install Table" job is not marking the Duplicate software installs Active Installs to False

  

### Issue

With Discovery source, when there is an updated software version available in the CI, it updates the existing install record in the cmdb\_sam\_sw\_install table and does not create a new one. Whereas, in case of third party integrations like Tanium, it always inserts new Software install record for each version instead of updating the existing ones. Due to this, during each Software update, Tanium source starts creating a new install record and multiple software records of same name are created.

![](sys_attachment.do?sys_id=97c699c1dbfccd1480073ca8f49619b6)

For example, in the above screenshot - the first record at the top(think-cell 11.0.32.545) is created by Servicenow Discovery source. 

The remaining ones are created by Tanium source. When the Deduplicate Install job is completed, it has marked only one record 'Active Install' to False. 

### Release

All

### Cause

"SAM - Deduplicate Install Table" job does not consider installations as duplicate if they are from same source. 

### Resolution

1\. If Duplicate Install Table job finds the Software installs from 2 discovery sources, then it will mark one as false based on Publisher/version.

2\. If the installs are from same discovery source, even if the version/publisher are same, the job will not consider them as duplicates.

3\. Ideally, it expects only one install record from one discovery source.

4\. In the above screenshot, Tanium source has created 4 software install records and 1 from Servicenow discovery.

5\. The job has identified one record as duplicate and marked it as Active - false.

6\. The remaining 4 installs from Tanium source are not considered as duplicates since they are from same source.

7\. In such cases, customers need to make sure no duplicate Software installations are created from the Tanium source itself.
