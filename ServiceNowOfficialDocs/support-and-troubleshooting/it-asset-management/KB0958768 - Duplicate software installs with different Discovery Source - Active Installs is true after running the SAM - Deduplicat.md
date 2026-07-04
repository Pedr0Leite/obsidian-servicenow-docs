---
title: "Duplicate software installs with different Discovery Source - Active Installs is true after running the \"SAM - Deduplicate Install Table\" job."
aliases:
  - KB0958768
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0958768
kb_number: KB0958768
last_modified: 2024-03-06
---

## Duplicate software installs with different Discovery Source - Active Installs is true after running the "SAM - Deduplicate Install Table" job.

  

### Issue

There are duplicate software installs \[cmdb\_sam\_sw\_install\] records with different Discovery Source. The expectation after running the "SAM - Deduplicate Install Table" job the Active Install of the records will have 1 true and 1 false but it didn't happen.

**Examples:**

<table style="border-collapse: collapse; width: 100%;" border="1"><tbody><tr><td style="width: 16.6667%; text-align: center;"><strong>Software Install</strong></td><td style="width: 4.16667%; text-align: center;"><strong>Deduplication processed</strong></td><td style="width: 4.16667%; text-align: center;"><strong>Active Install</strong></td><td style="width: 4.16667%; text-align: center;"><strong>Installed on</strong></td><td style="width: 4.16667%; text-align: center;"><strong>Discovery Source</strong></td><td style="width: 16.6667%; text-align: center;"><strong>Software Discovery Models</strong></td><td style="width: 16.6667%; text-align: center;"><strong>Normalizaton Status</strong></td><td style="width: 8.33335%; text-align: center;"><strong>Publisher</strong></td><td style="width: 4.16667%; text-align: center;"><strong>Product</strong></td><td style="width: 2.08333%; text-align: center;"><strong>Version</strong></td><td style="width: 2.08333%; text-align: center;"><strong>Edition</strong></td><td style="width: 16.6667%; text-align: center;"><strong>Language</strong></td></tr><tr><td style="width: 16.6667%;">Microsoft BizTalk Server 2006 Standard Edition</td><td style="width: 4.16667%; text-align: center;">true</td><td style="width: 4.16667%; text-align: center;">true</td><td style="width: 4.16667%; text-align: center;">CI1</td><td style="width: 4.16667%; text-align: center;">ServiceNow</td><td style="width: 16.6667%;">Microsoft BizTalk Server 2006 Standard Edition 3.5.1.1602.0</td><td style="width: 16.6667%; text-align: center;">Manually Normalized</td><td style="width: 8.33335%; text-align: center;">Microsoft</td><td style="width: 4.16667%; text-align: center;">BizTalk Server</td><td style="width: 2.08333%; text-align: center;"><span style="background-color: #ffff00;">2016</span></td><td style="width: 2.08333%; text-align: center;">Standard</td><td style="width: 16.6667%; text-align: center;">Anything</td></tr><tr><td style="width: 16.6667%;">Microsoft BizTalk Server 2006 Standard Edition</td><td style="width: 4.16667%; text-align: center;">true</td><td style="width: 4.16667%; text-align: center;">true</td><td style="width: 4.16667%; text-align: center;">CI1</td><td style="width: 4.16667%; text-align: center;">Tanium</td><td style="width: 16.6667%;">Microsoft BizTalk Server 2006 Standard Edition 3.5.1.1602.0</td><td style="width: 16.6667%; text-align: center;">Normalized</td><td style="width: 8.33335%; text-align: center;">Microsoft</td><td style="width: 4.16667%; text-align: center;">BizTalk Server</td><td style="width: 2.08333%; text-align: center;"><span style="background-color: #ffff00;">Other</span></td><td style="width: 2.08333%; text-align: center;">Standard</td><td style="width: 16.6667%; text-align: center;">Anything</td></tr></tbody></table>

### Release

All

### Cause

DeDuplicationEngine(script include) considers 2 software discovery models as similar if Publisher, Product, Version, Edition and Language should match.

For the above example, there are different in the "Version" field.

### Resolution

1.To make sure the above said field values match, update the "Version" value of one of the software discovery models.

a. One of the software discovery models is Manually Normalized, update the version to "Other" to match the other software discovery models version by Revert the normalization.

2\. Check the "Deduplication processed"(deduplicated) flag for the Software Installs if the value is "true".

a. If the "Deduplication processed"(deduplicated) are "true", these installs will not be processed in "SAM - Deduplicate Install Table" job.

b. For these to be processed again, update the 'deduplicated' flag of the affected software installs to 'false' by running the script in the "Scripts - Background".  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Script - Start\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
var instGr = new GlideRecord('cmdb\_sam\_sw\_install');  
instGr.addEncodedQuery('display\_nameSTARTSWITHMicrosoft BizTalk Server 2006 Standard Edition');  
instGr.setValue('deduplicated', false);  
instGr.setWorkflow(false);  
instGr.updateMultiple();  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*Script - End\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

3\. Triggered the "SAM - Deduplicate Install Table" job.

After job completion, check the Active Install value of the Software Installs. 1 should be marked as "false".
