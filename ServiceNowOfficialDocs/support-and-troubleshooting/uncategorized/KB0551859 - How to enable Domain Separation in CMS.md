---
title: "How to enable Domain Separation in CMS"
aliases:
  - KB0551859
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551859
kb_number: KB0551859
last_modified: 2025-01-03
---

## How to enable Domain Separation in CMS

  

### Issue

How to make CMS domain aware

  

# Description

* * *

This article addresses questions about whether CMS can be Domain Separated and how this can be achieved

# Solution

* * *

1. The CMS is only partially domain separated because the Content Page \[content\_page\] table extends Portal Pages \[sys\_portal\_page\] which is domain separated.  The CMS Site \[content\_site\] records and underlying Service Catalog tables, categories, items, etc., do not have the domain field and are not domain separated.  The global CMS Configuration Page \[content\_config\] cannot be domain separated.

In general, if a table is part of the base instance and that table does not have a sys\_domain field, it is strongly recommended that you leave it that way and consider the following alternatives to Domain Separation:

-   ACLs (Contextual Security)
-   Form views
-   Separate instances (ServiceNow Express may even be considered)
-   User Criteria introduced with Fuji (Entitlements prior to Fuji)
-   Filters, Dictionary Overrides, and Reference Qualifiers (condition-based processing such as before query business rules, workflows, and UI Policies)

 **Note:** While the CMS can be customized with Domain Separation, this is not an out-of-box feature and implementation is going to fall beyond the scope of Customer Support.

2. One option is to create a CMS site for each company within a MSP (Managed Service Provider) instance.  
  
While the out-of-box provided CMS site (Employee Self-Service) could be used as a baseline template and the Copy option utilized to create a new, duplicated site for each company, careful consideration needs to be made for the number of records this generates and the number of companies in the instance. This may not be a scalable option.  
  
Parameterization within the Company table can be utilized to drive underlying CMS functionality; however this involves a knowledge of scripting to implement (for example, Login Rules, UI Scripts, and UI Macros) which falls outside the scope of ServiceNow Customer Support.

# Applicable Versions

* * *

ALL

# Additional Information

* * *

1\. If you want to read more about domain separation please use this link:

[https://docs.servicenow.com/csh?topicname=domain-sep-landing-page.html&version=latest](https://docs.servicenow.com/csh?topicname=domain-sep-landing-page.html&version=latest)

2\. For general information and questions, please see the [ServiceNow Community](http://community.servicenow.com "ServiceNow Community") and the following existing links:

3\. The following ServiceNow Community posts are related to CMS and Domain Separation: 

[https://community.servicenow.com/thread/163872](https://community.servicenow.com/thread/163872)

[https://community.servicenow.com/thread/169005](https://community.servicenow.com/thread/169005)

[https://community.servicenow.com/community/support/blog/2014/08/20/copying-cms-sites-and-pages](https://community.servicenow.com/community/support/blog/2014/08/20/copying-cms-sites-and-pages)

4\. If you are considering implementing Domain Separation, we highly recommend contacting an experienced partner or [ServiceNow Professional Services](http://www.servicenow.com/services/best-practices.html "ServiceNow Professional Services"). 

<table class="noteTable" style="width: 1337px;" align="left"><tbody><tr><td style="width: 50; vertical-align: middle; text-align: center;"><img style="align: baseline;" title="Important" src="/important_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="vertical-align: middle; text-align: left;"><strong>Important</strong>: Customizations applied to CMS in an effort to domain separate are done at the customers own risk and fall outside the scope of ServiceNow Customer Support where focus is on break/fix issues in the base&nbsp;instance.</td></tr></tbody></table>
