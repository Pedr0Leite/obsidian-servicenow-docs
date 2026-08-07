---
title: "How to make 'Windows OS - Servers' Pattern return Bios Serial number instead of Baseboard Serial number"
aliases:
  - KB0749739
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0749739
kb_number: KB0749739
last_modified: 2025-07-07
---

## How to make 'Windows OS - Servers' Pattern return Bios Serial number instead of Baseboard Serial number

  

### Issue

# Symptoms

By default, OOB 'Windows OS - Servers' Pattern return Baseboard Serial number, but in some case, customer might wanted to use the Bios Serial number for the CI instead.

# Cause

From the 'Windows OS -Server' pattern, step '5. Insert serial number to cmdb\_ci\_win\_server':  
  
Value=$cmdb\_serial\_number\[1\].serial\_number \[we will get the 1st row (baseboard) in the cmdb\_serial\_number table\]

# Resolution

There are 2 options:

1) Changed the order/swap these 2 steps (3.10 and 3.12) in the pattern 

![](sys_attachment.do?sys_id=916c686edb42b450e515c2230596193c)

2) Edit the 'OSs - Pre Sensor' Pattern Pre/Post Script index:

FROM: for(var serialIndex = 0; serialIndex < serialList.length; serialIndex++){  
TO: for(var serialIndex = 1; serialIndex < serialList.length; serialIndex++){

https://<instancename>.service-now.com/$sn\_pattern\_designer.do?sys\_id=670e55a4db702200c06776231f961942&authoring\_mode=modify&editor\_mode=advanced&section\_item\_type=identification&section\_item\_name=discovery

\[Note: attached script [here](sys_attachment.do?sys_id=d16c686edb42b450e515c22305961941 "here")\]

# Additional Information

Serial Number Valid Field:

https://hi.service-now.com/kb\_view.do?sys\_kb\_id=198e4f97db583b4813b5fb2439961924&sysparm\_rank=7&sysparm\_tsqueryId=b77a23a7db2dbf084819fb24399619ba
