---
title: "LDAP User Import Not Handling Manager Imports Correctly"
aliases:
  - KB0635222
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635222
kb_number: KB0635222
last_modified: 2025-04-10
---

## Issue

LDAP User Import Not Handling Manager Imports Correctly 

## Resolution

The first step in troubleshooting is to verify the onStart transform map script sets up the LDAPUtils script include.  The baseline script contains:

gs.include("LDAPUtils");

var ldapUtils = new LDAPUtils();

ldapUtils.setLog(log);

  

Reviewing the "Import log" will show if there are any specific errors associated with the import.  If so, those specific errors should be addressed before reviewing the Symptom/Resolution sections below.

In the following sections, there will be a specific symptom outlined, and the resolution to that symptom.  Be sure to follow the path to ensure everything is setup and working as expected.

Symptom 1

* * *

The "manager" field in the import set table (default name is ldap\_import.manager) is empty in all records.  This implies that the data source does not have the "manager" attribute specified, so that data is not being brought over from LDAP.  If only SOME of the manager fields are empty, this implies that those fields in LDAP are not populated, and that should be discussed with the LDAP administrator.

Resolution 1

* * *

Add the "manager" attribute to the LDAP Server record in ServiceNow.  By default, all attributes should be pulled into ServiceNow.  If any attributes are specified, then ONLY those attributes will be included in the import. Be sure that the "manager" attribute is included.  Here's the Jakarta documentation link to discusses adding attributes:

[https://docs.servicenow.com/csh?topicname=t\_SpecifyLDAPAttributes.html&version=latest](https://docs.servicenow.com/csh?topicname=t_SpecifyLDAPAttributes.html&version=latest)  

Symptom 2

* * *

Some users have the correct manager name, and some don't.

-   All "manager" fields have values.
-   The "manager" field contains the DN pulled from LDAP, but the DN is not complete (for the users that don't show manager names).

Resolution 2

* * *

The "manager" field is not long enough to hold the entire DN that was retrieved from the LDAP server.  Increase the import set table "manager" field length to be long enough to hold the entire DN string.

To accomplish this:

1.  Navigate to the "Tables" module
2.  Select your import set table ("ldap\_import" is the default name)
3.  Change the "Max length" of the "manager" field (something like 100 or 110 should be large enough)
