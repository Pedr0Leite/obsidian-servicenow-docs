---
title: "Discovery does not update operational status of retired CIs when rediscovered"
aliases:
  - KB0755747
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755747
kb_number: KB0755747
last_modified: 2026-06-30
---

## Discovery does not update operational status of retired CIs when rediscovered

  

### Issue

There is no base system script or system property that enables Discovery to update and un-retire the operational\_status field for a configuration item (CI), making it Operational again when the CI is rediscovered.

### Symptoms

\- A CI with an Operational Status of Retired is rediscovered by Discovery.  
\- After rediscovery, the CI's Operational Status remains Retired and is not automatically changed to Operational.  
\- No base system mechanism updates the Operational Status field as part of the Discovery process.

### Release

All

### Cause

**Integration with Asset Management**

The Operational Status field and the Status/Hardware Status field on a CI are kept synchronized when either field is set to Retired:

\- When Operational Status changes from Retired to another value, the Status/Hardware Status field is set to Installed.  
\- When Status/Hardware Status changes from Retired to another value, the Operational Status field is automatically set to Non-Operational.

For example, if you update a CI's Operational Status from Retired to Operational — manually or through another process — the Status/Hardware Status field changes to Installed.

Because of this synchronization behavior, Discovery does not include logic to override the Retired status and restore a CI to Operational when it is rediscovered.

### Resolution

To automatically update the Operational Status of a retired CI when it is rediscovered, you must create a custom Business Rule on the CI (cmdb\_ci) table.

**Recommended approach**

Base the Business Rule on the Most recent discovery field. This field updates each time Discovery successfully passes the identification phase and positively matches the CI. This makes it a reliable indicator that the CI was visited.

Note: Do not base the rule on the Updated field. The Updated field only changes when a CI attribute or relationship is modified after Discovery runs. If the CI is retired, Discovery does not modify any attributes, so the Updated field does not change.

**Create the Business Rule**

1\. Navigate to System Definition > Business Rules.  
2\. Select New.  
3\. Enter the following values:  
   - Name: Enter a descriptive name, for example: Un-retire CI on rediscovery  
   - Table: Configuration Item \[cmdb\_ci\]  
   - When: before  
   - Update: selected  
4\. Under Conditions, set the following:  
   - Most recent discovery — changes — (leave value blank, to trigger on any update to this field)  
   - Operational Status — is — Retired  
5\. In the Advanced tab, enter the following script in the Script field:

(function executeRule(current, previous) {  
    // Only proceed if the CI is currently Retired  
    if (current.operational\_status == 6) { // 6 = Retired  
        current.operational\_status = 1; // 1 = Operational  
    }  
})(current, previous);

6\. Select Submit to save the Business Rule.

**Verify the operational\_status field values**

The integer values for the operational\_status field may vary depending on your instance configuration. To confirm the correct values:

1\. Navigate to any CI record.  
2\. Right-click the Operational Status field label and select Show Choice List.  
3\. Note the Value column for Retired and Operational.  
4\. Update the script above with the correct values if they differ from the example.

**Important**: Because the Operational Status and Status/Hardware Status fields are synchronized, updating Operational Status to Operational also sets Status/Hardware Status to Installed. Review whether this behavior is appropriate for your environment before activating the Business Rule.

### Related Links

[CMDB CI Lifecycle Management](https://docs.servicenow.com/csh?topicname=cmdb-ci-lifecycle-mgmt.html&version=latest "CMDB CI Lifecycle Management")
