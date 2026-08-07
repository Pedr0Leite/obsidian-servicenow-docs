---
title: "Outbound RESTMessageV2 request via MID server fails for users with snc_read_only role"
aliases:
  - KB0754125
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754125
kb_number: KB0754125
last_modified: 2024-04-07
---

## Outbound RESTMessageV2 request via MID server fails for users with snc\_read\_only role

  

### Issue

# Symptoms

When an outbound REST request is executed using RESTMessageV2 via a MID server as a user with snc\_read\_only role, it fails with the below error:

Security restricted: access for table: ecc\_queue, user: abel.tuter, operation: create -- from class: ReadOnlyRoleAccessHandler
REST Msg Outbound - ECCRESTResponse : Error while evaluating the XPATH Expression against response: org.apache.axiom.om.OMException: com.ctc.wstx.exc.WstxEOFException: Unexpected EOF in prolog
 at \[row,col {unknown-source}\]: \[1,0\]: org.apache.axiom.om.impl.builder.StAXOMBuilder.next(StAXOMBuilder.java:297)
org.apache.axiom.om.impl.dom.DocumentImpl.getOMDocumentElement(DocumentImpl.java:446)
org.apache.axiom.om.impl.dom.DocumentImpl.getDocumentElement(DocumentImpl.java:458)
com.glide.rest.outbound.ecc.ECCRESTResponse.getNodeList(ECCRESTResponse.java:252)
com.glide.rest.outbound.ecc.ECCRESTResponse.extractHeaders(ECCRESTResponse.java:215)
com.glide.rest.outbound.ecc.ECCRESTResponse.processResponse(ECCRESTResponse.java:176)
com.glide.rest.outbound.ecc.ECCRESTResponse.fetchAndProcessEccResponse(ECCRESTResponse.java:246)
com.glide.rest.outbound.ecc.ECCRESTResponse.getBody(ECCRESTResponse.java:135)

# Release

Applicable to all releases

# Cause

Since the REST Message is via the MID server, a RESTProbe ecc\_queue record is supposed to be created for the MID server to process this request. However, the creation of this record fails because the user has the snc\_read\_only role and doesn't have the permission for the 'create' operation on the ecc\_queue table. 

# Resolution

To be able to let users with snc\_read\_only execute RESTMessageV2 requests via the MID server, you need to create the following property:

Name: glide.security.snc\_read\_only\_role.tables.exempt\_create

Type: string

Value:

sys\_user\_session, sysevent, syslog, syslog\_transaction, sys\_user\_preference, sys\_ui\_list, sys\_ui\_list\_element, sys\_db\_cache, user\_multifactor\_auth, ecc\_queue

This will allow the 'create' operation to be successful on the ecc\_queue table even though the user has the snc\_read\_only role. 

# Additional Information

[Read-Only properties](https://docs.servicenow.com/csh?topicname=c_ReadOnlyRole.html&version=latest#r_ReadOnlyRoleProperties)
