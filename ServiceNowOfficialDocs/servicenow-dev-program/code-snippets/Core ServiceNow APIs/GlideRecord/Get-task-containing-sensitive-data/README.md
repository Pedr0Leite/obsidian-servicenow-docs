---
title: "Get-task-containing-sensitive-data"
aliases:
  - Get-task-containing-sensitive-data
tags:
  - servicenow-dev-program
  - code-snippet
  - get-task-containing-sensitive-data
  - gliderecord
---

This script is used to get all task records based on sensitive data entered into this task based records. To make it simple to add the criteria for GDPR or sentive data i 
have created a property and used it in this line : getProperty.addQuery('name', 'nn.criticalDataPhrases');

Example: 
Property name : criteria.gdpr
Value: BSN,Burgerservicenummer,voornaam,achternaam,geslacht,gender,Geboortedatum,Birth,adres,woonplaats,straatnaam,huisnummer,postcode,telefoonnummer,mobiel,hypotheeknummer,IBAN,Rekeningnummer,Rekeningnr,Rek. nr.,Verzekeringsnummer,verzekeringsnr,wachtwoord,gebruikersnaam,username,password,pwd

Output:
Task sys_ids which contains GDPR data.

Usage:
In scripted reports, in script includes,etc.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/ACL enforcement using GlideRecord/README|ACL enforcement using GlideRecord]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Add n number of users to n number of groups using server scripts/README|Add n number of users to n number of groups using server scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Archiving Old Incident Records to Improve Performance/readme|Archiving Old Incident Records to Improve Performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/CheckDuplicate-Server/readme|CheckDuplicate-Server]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Choose Window for better performance/README|Choose Window for better performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Compare_2_records/README|Compare_2_records]]
