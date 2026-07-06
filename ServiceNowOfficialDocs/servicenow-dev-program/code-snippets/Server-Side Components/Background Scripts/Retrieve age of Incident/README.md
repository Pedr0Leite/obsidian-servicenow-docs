---
title: "Retrieve age of Incident"
aliases:
  - Retrieve age of Incident
tags:
  - servicenow-dev-program
  - code-snippet
  - retrieve-age-of-incident
  - background-scripts
---

This script is designed to calculate the age of incidents in the ServiceNow by comparing the creation date of each incident with the current date. It retrieves all the records from the incident table and iterates through them. For each incident, it calculates the time difference between its creation date (sys_created_on) and the current date in milliseconds, then converts that value into days. This approach is useful for monitoring how long incidents have been open, helping teams prioritize older issues and ensuring timely resolution. Whether you're tracking overall service performance or looking for bottlenecks in your incident management processes, this script can provide valuable insights into the duration of open incidents, aiding in improving service delivery.

var grIncidentAge = new GlideRecord('incident'); //This line creates a new GlideRecord object for the incident table, allowing the script to query and manipulate incident records.
grIncidentAge.query(); //This line executes a query to retrieve all records from the incident table.
while (grIncidentAge.next()) { //The while loop iterates over each record returned by the query. The next() method moves to the next record in the result set.
var incCreated = new GlideDateTime(grIncidentAge.sys_created_on); //A new GlideDateTime object is created using the sys_created_on field of the current incident record. This field stores the date and time when the incident was created.
var nowDT = new GlideDateTime(); //Another GlideDateTime object is created that contains the current date and time.
var ageInMilliseconds = nowDT.getNumericValue() - incCreated.getNumericValue(); //The numeric values of the current and created dates are obtained, and the difference is calculated to find the age of the incident in milliseconds.
var ageInDays = Math.floor(ageInMilliseconds / (1000 * 60 * 60 * 24)); //The age in milliseconds is converted to days by dividing by the number of milliseconds in a day (1,000 milliseconds/second * 60 seconds/minute * 60 minutes/hour * 24 hours/day). The result is rounded down using Math.floor().

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
