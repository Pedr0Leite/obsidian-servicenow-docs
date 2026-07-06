---
title: "Unix Cluster - Oracle Cluster pattern failing at  step \"Reference and relation between cmdb_ci_cluster_vip to cmdb_ci_unix_cluster\"
aliases:
  - KB0746936
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746936
kb_number: KB0746936
last_modified: 2024-04-07
---

## Issue

01) Run discovery on Linux server which has a Red hat cluster on it.

02) During the discovery, it would fail at step 57. Reference and relation between cmdb\_ci\_cluster\_vip to cmdb\_ci\_unix\_cluster with empty results.

## Resolution

Based on these errors, the user "XXXXXX" may not have enough permissions to pull the cluster information.

01) The following commands are run for Oracle clusterware:

Commands  
\==========  
ps -ef | grep corosync | grep -v grep  
clustat -x  
ifconfig | grep 'inet addr:' |awk '{print $1, $2 }'  
hostname -s  
hostname -s  
  
02) We require sudo permission to run the below command.

Sudo permission to run: sudo /u01/app/12.1.0.2/grid/bin/ocrcheck | egrep -v 'error|return code'

## Additional Information

[https://docs.servicenow.com/csh?topicname=red-hat-cluster-discovery.html&version=latest](https://docs.servicenow.com/csh?topicname=red-hat-cluster-discovery.html&version=latest)
