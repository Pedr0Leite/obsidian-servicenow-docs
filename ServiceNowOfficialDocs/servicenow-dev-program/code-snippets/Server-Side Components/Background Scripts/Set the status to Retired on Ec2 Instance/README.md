---
title: "Set the status to Retired on Ec2 Instance"
aliases:
  - Set the status to Retired on Ec2 Instance
tags:
  - servicenow-dev-program
  - code-snippet
  - set-the-status-to-retired-on-ec2-instance
  - background-scripts
---

This background script is used to set the Install_status to Retired if the status is terminated for the Ec2 Instances(Ci's)
We are quering the table against the table cmdb_ci_ec2_instance
Then we have encoded query to search if there is any record with the status as terminated and install_status is not retired
We are sorting based on name and set the limit to 10K records
We are searching if there are any records, If yes, we will set the install_Status to Retired and we are disabling the workflows to false.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/ACL Audit Utility/README|ACL Audit Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Access Analysis Utility/README|Access Analysis Utility]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Bookmarks - ITIL Users/README|Add Bookmarks - ITIL Users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Comments/README|Add Comments]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add No Audit Attribute To Multiple Dictionary Entries/README|Add No Audit Attribute To Multiple Dictionary Entries]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Background Scripts/Add Standard Change Model/README|Add Standard Change Model]]
