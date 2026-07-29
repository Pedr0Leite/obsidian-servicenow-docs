---
title: "Cloud Management CMPv1 Azure VM Discovery Identifier"
aliases:
  - KB0687807
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687807
kb_number: KB0687807
last_modified: 2024-04-07
---

## Cloud Management CMPv1 Azure VM Discovery Identifier

  

### Issue

# Overview

In CMPv1, Discovered VMs are stored in the \[cmdb\_ci\_azure\_vm\] table, with the discovery process being enabled by the legacy plugin Microsoft Azure.

# Details

During Discovery, the Identification and Reconciliation Engine (IRE) is not used. Instead, the procedure checks on the \[normalizedobject\_db\_mapping\] table fields with the following search criteria:

-   Resource Type = VM
-   Target Table = Azure Virtual Machine Instance
-   "Used to correlate" = true

The out of box field used for identification is \[correlation\_id\], which is mapped from "Resource ID" from Azure.

# Additional Information

[Azure troubleshooting](https://docs.servicenow.com/csh?topicname=r_ITOMApplications.html&version=latest "Azure troubleshooting")

[Azure Functions discovery](https://docs.servicenow.com/csh?topicname=azure-function-discovery.html&version=latest "Azure Functions discovery")
