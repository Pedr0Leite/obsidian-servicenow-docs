---
title: "AIX Cluster is being displayed as single node"
aliases:
  - KB0635344
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635344
kb_number: KB0635344
last_modified: 2025-04-07
---

## AIX Cluster is being displayed as single node

  

### Issue

The reason there is no cluster information was that there was an identification rule on **u\_cmdb\_ci\_ibm\_cluster** with identification attribute cluster\_id.

On the discovered cluster this field was not populated.

To seethe identification rules:

1.  Navigate to **CI Identifiers**
2.  Look for records that **applies to** u\_cmdb\_ci\_ibm\_cluster
3.  Change the identification rule to rely on the **name** attribute
4.  Check to see if the information is shown correctly on the right pane

If **name** is not sufficiently unique for this kind of cluster, cluster\_id may be brought back, but then the probe/sensor must populate this field.

![](sys_attachment.do?sys_id=092cec2edb42b450e515c223059619db)
