---
title: "AD flow configured to use MID Server fails with the error \"Authentication failure with the local MID server service credential\""
aliases:
  - KB0811747
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0811747
kb_number: KB0811747
last_modified: 2024-04-08
---

## AD flow configured to use MID Server fails with the error "Authentication failure with the local MID server service credential"

  

### Issue

This is specific to the scenario where the Flow contains power shell scripts configured to run on 'All MID Servers' and uses a Connection alias with the Credentials configured for a 'specific' MID Server.

### Cause

The MID Server when executing the Power shell script does not have access to the credentials since the Credential record is configured for a specific MID Server, so the MID Server uses its service account.

Since the MID Server service account does not have the appropriate access on AD, the script execution fails with the following error:

Authentication failure with the local MID server service credential

### Resolution

Update the Credential record and set the "Applies to" field to 'All MID Server' and make sure no specific MID Server is selected.

OR

Update the MID Server capabilities so the specific MID Server which is configured in the Credentials record is picked for the flow.

See the following documentation for this:

[How an application selects a MID Server](https://docs.servicenow.com/csh?topicname=c_MIDServerSelector.html&version=latest#d1192113e340 "How an application selects a MID Server")
