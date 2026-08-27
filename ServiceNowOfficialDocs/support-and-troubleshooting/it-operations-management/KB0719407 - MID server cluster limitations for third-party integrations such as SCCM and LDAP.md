---
title: "MID server cluster limitations for third-party integrations such as SCCM and LDAP"
aliases:
  - KB0719407
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719407
kb_number: KB0719407
last_modified: 2026-06-30
---

## MID server cluster limitations for third-party integrations such as SCCM and LDAP

  

### Issue

MID servers that are part of a MID server cluster cannot be used to integrate with third-party solutions such as SCCM or LDAP. This failover and load-balancing setup can have significant performance implications and is not supported for this use case.

Note: This limitation also applies to the Service Graph Connector for SCCM (SG-SCCM).

### Symptoms

You are attempting to use a MID server cluster to integrate with a third-party solution such as SCCM or LDAP.

After a MID server in the cluster fails over, you notice a large amount of duplicate data in the system.

Data duplication occurs following failover for JDBC or SCCM integrations.

### Release

  All supported releases

### Cause

When a MID server in a cluster fails over, any in-progress jobs restart on another MID server in the cluster. For JDBC and SCCM integrations specifically, this causes the restarted job to reprocess data that was already handled, resulting in significant data duplication.

### Resolution

To integrate third-party solutions such as SCCM or LDAP with the ServiceNow platform, you should use a dedicated MID Server — one that is not part of a MID server cluster.

A dedicated MID Server handles only the integration workload it is assigned to, without the failover behavior that causes data duplication in clustered environments.

For guidance on setting up and configuring a dedicated MID Server, refer to the MID Server installation and configuration documentation on [docs.servicenow.com](https://docs.servicenow.com)

**Service Graph Connector for SCCM (SG-SCCM)**

The same limitation applies when using the Service Graph Connector for SCCM. You should assign a dedicated MID Server to the SG-SCCM integration rather than using a clustered MID Server.
