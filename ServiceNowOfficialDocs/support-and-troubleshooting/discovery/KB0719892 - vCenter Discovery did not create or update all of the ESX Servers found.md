---
title: "vCenter Discovery did not create or update all of the ESX Servers found"
aliases:
  - KB0719892
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719892
kb_number: KB0719892
last_modified: 2024-04-07
---

## Issue

# Overview

* * *

This workaround is only applicable on the vCenter Discovery that didn't create or update all the ESX Servers found.

Note: (This has been taken from the customer's updates). 

"There is currently an active vCenter bug that will pull the chassis serial number instead of the blade serial number. This explains why we are only getting a blade per chassis." 

# vCenter Discovery didn't create or update all of the ESX Servers found

* * *

vCenter Discovery didn't create or update all of the ESX Servers found.

The "Out-Of-The-Box" behavior, the ESX servers are being identified based on the combination of "Morid", "correlation\_id" and "serial\_number". However, some of your ESX servers are sharing the same serial number. This is preventing the records with the same serial number getting created or updated in the ESX server table which is the ideal of not creating duplicate serial\_number records but since this is cause by the vCenter bug, this workaround is recommended.

The "Out-Of-The-Box" script include "VCenterESXHostsSensor" handles the combination of "Morid", "correlation\_id" and "serial\_number" to create or update the ESX servers even though they share the same serial number .   
  
Link to the script include: "VCenterESXHostsSensor"   
https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=4c6fbb6f8f575200c2fe0b5437bdeeae 

# Symptoms

* * *

If the Discovery results expects 2 or more ESX Servers to be created or updated and the results is less than expected, need to check on the ECC Queue Input payload of the Discovery Status to check on how many ESX Servers are retrieved.

Then, verify each ESX Server's "serial\_number". If there are any similarities on the ESX Server's serial\_number, then only 1 of the ESX Server will be created or updated.

# Workaround

* * *

From the Script Include:"VCenterESXHostsSensor" 

https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_script\_include.do?sys\_id=4c6fbb6f8f575200c2fe0b5437bdeeae 

Find the following in the script:

index: \[ \['morid', 'correlation\_id'\], \['serial\_number'\] \],   
  

Then change to:

index: \[ \['morid', 'correlation\_id'\]\],

NOTE:

Since this is a vCenter bug, please don't forget to revert the changes to the "Out-Of-The-Box" version when the vCenter bug is fixed.
