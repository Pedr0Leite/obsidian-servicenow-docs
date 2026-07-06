---
title: "How to export bulk data from ServiceNow using REST API pagination"
aliases:
  - KB0727636
tags:
  - servicenow
  - support-kb
  - rest-api
  - table-api
  - pagination
  - bulk-export
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727636
kb_number: KB0727636
last_modified: 2026-02-10
---

## How to export bulk data from ServiceNow using REST API pagination

  

### Issue

Learn how to export bulk data from a ServiceNow instance using REST API pagination. When exporting large data sets with millions of records, export data in chunks to avoid performance implications and impact on other services running on the instance.

### Release

All supported releases

### Resolution

### How REST API pagination works

By default, ServiceNow returns a maximum of 10,000 records per REST API call. This limit is controlled by the sysparm\_limit parameter, which defaults to 10,000. You can specify a higher value in the URL to return more records, but increasing this value significantly can cause the transaction to time out.

For example: /api/now/table/incident?sysparm\_limit=40000

Note: The default quota rule for REST API transactions is set to 60 seconds per transaction. Increasing sysparm\_limit drastically can cause the transaction to time out and get canceled.

The preferred method for retrieving large amounts of records is pagination, which retrieves subsets of records in separate calls. For example, the first call retrieves records 1 through 10,000, the second call retrieves records 10,001 through 20,000, and so on.

### Pagination parameters

Use the following parameters to control pagination:

-   sysparm\_limit — Defines how many records to return in one call (10,000 by default).
-   sysparm\_offset — Defines the starting record position, excluding preceding records from the query.
-   sysparm\_query=ORDERBYsys\_created\_on — Sorts the results by created date and time.

### Pagination example

The following examples show how to structure paginated REST API calls.

**First call:**

/api/now/table/incident?sysparm\_limit=10000&sysparm\_offset=0&sysparm\_query=ORDERBYsys\_created\_on 

**Second call:**

/api/now/table/incident?sysparm\_limit=10000&sysparm\_offset=10000&sysparm\_query=ORDERBYsys\_created\_on 

**Third call:**

/api/now/table/incident?sysparm\_limit=10000&sysparm\_offset=20000&sysparm\_query=ORDERBYsys\_created\_on 

Continue this pattern in a loop until all records are retrieved.

### Example bulk download script

The following bash script uses cURL to bulk download data from an instance using REST API pagination. This example is provided as a general guideline and can be adapted to your requirements.

```
#!/bin/bash

## Example of how to use REST API pagination to bulk download data

## Settings
PAGESIZE=10000
PAGESTOFETCH=10
TABLE=tablename # e.g incident, question_answer, task
INSTANCENAME=myinstancename # e.g if instance is acme.service-now.com then put 'acme' here
USERNAME=myuser
PASSWORD=mypassword
OUTPUTFORMAT=json # either xml or json

## Program
echo "Starting at `date`"

i=0
pageoffset=0
while [[ $i -le $PAGESTOFETCH ]];
do

echo "Starting download  of $PAGESIZE records from table $TABLE at offset $pageoffset"
curl "https://$INSTANCENAME.service-now.com/api/now/table/$TABLE?sysparm_offset=$pageoffset&sysparm_limit=$PAGESIZE" \
--request GET \
--header "Accept:application/$OUTPUTFORMAT" \
--header "Content-Type:application/json" \
--data "{}" \
--user ${USERNAME}:${PASSWORD} \
--output question_answer$i.xml \
--silent

echo "Saved $PAGESIZE records to question_answer$i.xml"

((pageoffset+=$PAGESIZE))
((i++))

done

echo "Finished at `date`"

```

 

**Important**: ServiceNow Support does not provide assistance with custom scripting. This example can be accomplished in many ways, for example, using Python instead of a bash shell.

### Related Links

[How to bulk export attachments from a ServiceNow instance](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790002) — for exporting attachment binary data, which uses a different procedure than the REST API pagination method described in this article

[Default quota rules](https://www.servicenow.com/docs/r/platform-administration/platform-performance/c_DefaultQuotaRules.html "Default quota rules")

## Related

- [[KB0790002 - How to bulk export attachments from a ServiceNow instance]] - companion procedure for attachment binary data
- [[c_TableAPI]] - REST Table API reference
- [[c_AggregateAPI]] - REST Aggregate API reference

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0753132 - Users getting Unauthorized access error in Service Portal when REST API level ACLs are in place|Users getting \"Unauthorized access\" error in Service Portal when REST API level ACLs are in place ]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0686244 - When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window show|When you impersonate a user and then try to re-impersonate your own user account, the Impersonate User popup window shows an error Failed API level ACL Validation]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0693393 - How to generate a token using sn_auth - oAuth API for Resource Owner Password Credentials grant type|How to generate a token using sn_auth - oAuth API  for Resource Owner Password Credentials grant type?]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0693900 - How to generate a token using sn_auth - oAuth API for Authorization grant type|How to generate a token using sn_auth - oAuth API  for Authorization grant type?]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0725643 - How to generate bearer token for oAuth 2.0 - Authorization Grant type|How to generate bearer token for oAuth 2.0 - Authorization Grant type]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0724965 - User Criteria is not working via REST API or Web Service call|User Criteria is not working via REST API or Web Service call]]
