---
title: "User Criteria is not working via REST API or Web Service call"
aliases:
  - KB0724965
tags:
  - servicenow
  - support-kb
  - user-criteria
  - rest-api
  - web-services
  - script-fencing
  - service-catalog
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724965
kb_number: KB0724965
last_modified: 2026-03-03
---

## User Criteria is not working via REST API or Web Service call

  

### Issue

User Criteria is not working when initiated via a REST API call or Web Service

Logs or error show "Security constraints prevent ordering of Item"

com.glide.script.fencing.MethodNotAllowedException: Function log is not allowed in scope sn\_sc. Use gs.debug() or gs.info() instead

### Release

Any

### Cause

The User Criteria Script maybe using a function or method that is not allowed to be called from web service

### Resolution

Check the script if it has gs.log and replace it with gs.debug

If there is none, check for errors by checking the 'System Log'

## Related

- [[KB0780775 - How to reference the current user in a User Criteria script using the user_id variable]] - User Criteria scripting patterns
- [[KB0550924 - Understanding User Criteria and ACLs in Knowledge v3]] - how User Criteria interacts with ACLs
- [[KB0689656 - How should I design my Knowledge Base user criteria]] - design guidance for User Criteria scripts
- [[c_TableAPI]] - REST Table API reference (relevant when scripts run in the sn_sc/web-service scope)

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Server Side/User Criteria/README|User Criteria]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0693393 - How to generate a token using sn_auth - oAuth API for Resource Owner Password Credentials grant type|How to generate a token using sn_auth - oAuth API  for Resource Owner Password Credentials grant type?]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0693900 - How to generate a token using sn_auth - oAuth API for Authorization grant type|How to generate a token using sn_auth - oAuth API  for Authorization grant type?]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0725643 - How to generate bearer token for oAuth 2.0 - Authorization Grant type|How to generate bearer token for oAuth 2.0 - Authorization Grant type]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0746144 - Users do not see ticket information after ordering a catalog item|Users do not see ticket information after ordering a catalog item]]
