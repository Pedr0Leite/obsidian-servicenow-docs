---
title: "Service Mapping: What to do with maps when the Datacenter for your Business Service Application changes"
aliases:
  - KB0725682
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725682
kb_number: KB0725682
last_modified: 2024-04-07
---

## Service Mapping: What to do with maps when the Datacenter for your Business Service Application changes

  

### Issue

# Description

* * *

In many cases the application that is mapped on a business service might failover or transfer to another Datacenter.

Meaning the endpoints you have configured are now directing to a new load balancer than before.

There are some steps that need to be taken to make sure you map reflects the current datacenter and not the old one that was transferred from. 

# Procedure

* * *

1) Make sure that an nslookup from MID servers will resolve to the correct IP address, pointing to the appropriate LB. 

2) If it is not then fix that issue first. 

3) You should run a regular discovery on the new AND old Load balancers that would be associated with the business service.

4) Run the DNS lookup scheduled job on demand to update the IP address on the entrypoints of the business service. 

Here is the job, you can click 'execute now' to run it:   
\[Instance\_name.serice-now.com\]/nav\_to.do?uri=sysauto\_script.do?sys\_id=f178ab457fb213001952baf8befa91d3 

If you cannot find it through that, the job is called: "Run DNS Lookup For All Entry Points And Manual Connection Endpoints"

5) After that is finished, you can run the business service map and it should also switchover to the correct LB. 

# Applicable Versions

* * *

All

# Additional Information

* * *

The entry point, should have correct IP address after running job. You can find the entrypoint info on this table: "cmdb\_ci\_endpoint". You will need to expose the IP Address field on the list view or add it to that form. You can always view XML to see the value for that IP Address as well.

Look at which LB service the map should go to. See that the entry point should have the same IP address as the LB service that is associated with that Business Service Application. 

If these two match and are for the correct LB, your map should also run accurately. The IP address associated with the LB service is updated when we run regular discovery on the LB itself. That is why step 3 above is important.
