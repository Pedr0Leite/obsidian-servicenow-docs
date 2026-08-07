---
title: "GlideRecord to Object"
aliases:
  - GlideRecord to Object
tags:
  - servicenow-dev-program
  - code-snippet
  - gliderecord-to-object
  - gliderecord
---

This script takes in a GlideRecord object and returns an object. Use the following background script to test the function.

function _grToObject(recordToPackage) {
  var packageToSend = {};
  for (var property in recordToPackage) {
      try {
          packageToSend[property] = recordToPackage[property].getDisplayValue();
      } catch (err) {}
  }
  return packageToSend;
}

var incSysID = ''; // Update w/ Incident sysId in target instance

var grInc = new GlideRecord('incident');
if(grInc.get(incSysID)){
    gs.info(JSON.stringify(_grToObject(grInc)));
} else {
    gs.info('Invalid Incident sysId');
}

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/ACL enforcement using GlideRecord/README|ACL enforcement using GlideRecord]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Add n number of users to n number of groups using server scripts/README|Add n number of users to n number of groups using server scripts]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Archiving Old Incident Records to Improve Performance/readme|Archiving Old Incident Records to Improve Performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/CheckDuplicate-Server/readme|CheckDuplicate-Server]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Choose Window for better performance/README|Choose Window for better performance]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideRecord/Compare_2_records/README|Compare_2_records]]
