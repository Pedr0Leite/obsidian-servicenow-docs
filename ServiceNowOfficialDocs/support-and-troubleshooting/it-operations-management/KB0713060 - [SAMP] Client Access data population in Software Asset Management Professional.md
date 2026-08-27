---
title: "[SAMP] Client Access data population in Software Asset Management Professional"
aliases:
  - KB0713060
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713060
kb_number: KB0713060
last_modified: 2024-04-07
---

## \[SAMP\] Client Access data population in Software Asset Management Professional

  

### Issue

# Client Access Data:

* * *

While using the SAMP-Oracle package, we may required to populate client access data such as Oracle named user and license calculation for reconciliation. If we goto the tables, we can see that there are two different tables with name samp\_client\_access and samp\_sw\_client\_access.

We may get confused between these two tables as the naming is same. The real table used for the client access data is _samp\_sw\_client\_access_. 

**Note**:

Currently, there is no option to auto populate the table samp\_sw\_client\_access (like by using the discovery). Until Madrid release, the expectation is that table samp\_sw\_client\_access should be populated manually.

# Whats there on Client Access form:

* * *

 ![](/sys_attachment.do?sys_id=6a8aec66db42b450e515c22305961987)

_**Name**_: You can give any name that describes what model and instance (if any) in short form.

_**Software Model:**_ Select the Model of client access data that you wanted to calculate.

_**Database Instance:**_ This is visible only when the selected Software model product is Oracle Database

_**Total device count:**_ Enter the number of Unique devices allowed to access the product.

_**Total user count:**_ Enter the number of Unique users allowed to access the product.

_**Note**_: In case of Oracle DB: it's the number of user that is using this oracle instance

# Automate the Client Access data population

* * *

Currently, we do not have any OOB soilution to auto populate the table samp\_sw\_client\_access (like by using the discovery). Either by some manual automated process like import sets or others.

-   By manual entry.
-   By using the scheduled import sets and transform maps. Please refer below for scheduled import sets and transform maps.

[Scheduled Import Sets](https://docs.servicenow.com/csh?topicname=t_ScheduleADataImport.html&version=latest "Scheduled Import Sets")

[Transform maps](https://docs.servicenow.com/csh?topicname=c_CreatingNewTransformMaps.html&version=latest "Transform maps")

# Release

* * *

All releases up-to Madrid.

# Environment

* * *

Any.

# Additional Information

* * *

[Import sets](https://docs.servicenow.com/csh?topicname=import-sets-landing-page.html&version=latest "Import sets")

[Client Access \[samp\_sw\_client\_access\]](https://docs.servicenow.com/csh?topicname=c_SoftwareAssetMgmt.html&version=latest "Client Access [samp_sw_client_access]")
