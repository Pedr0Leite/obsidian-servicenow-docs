---
title: "Server Discovery - No Mem or CPU data returned due to snc_payload_processed"
aliases:
  - KB0720663
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720663
kb_number: KB0720663
last_modified: 2024-04-07
---

## Server Discovery - No Mem or CPU data returned due to snc\_payload\_processed

  

### Issue

# Symptoms

* * *

After discovering a Windows Server there is no CPU or Memory on the CI record. The input on the ECC queue record shows "snc\_payload\_processed" 

# Release

* * *

All 

# Cause

* * *

The discovery job runs successfully however the WMI Probe for "Windows - CPU / Memory" is set to cache results

# Resolution

* * *

**It is highly suggested that you perform the following in your test environment first before changing this in production:**

You can turn off caching on this probe directly by going to the probe and unchecking "Cache results" here:

https://<instance-name>.service-now.com/discovery\_probes\_wmi.do?sys\_id=b141fd470a0a0ba5001d3c32c7d834fb

Additionally you can change the caching globally you can go to "Discovery Definition >> Properties" in your navigation filter. On this page if you search for "cache" you'll see where you can deselect the "Yes/No" checkbox. When checked this is set to yes.

https://<instance-name>.service-now.com/system\_properties\_ui.do?sysparm\_title=Discovery%20Properties&sysparm\_category=Discovery

This is the System Properties direct link:  
https://<instance-name.service-now.com/nav\_to.do?uri=sys\_properties.do?sys\_id=68b748eddf511100079367f53df2635e

# Additional Information

* * *

This is the System Properties direct link:  
https://<instance-name>.service-now.com/nav\_to.do?uri=sys\_properties.do?sys\_id=68b748eddf511100079367f53df2635e
