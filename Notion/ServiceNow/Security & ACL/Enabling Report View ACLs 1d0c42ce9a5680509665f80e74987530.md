---
aliases:
  - "Enabling Report View ACLs"
tags:
  - acl
  - report-view-acl
  - security
  - upgrade
  - domain-separation
---

# Enabling Report View ACLs

### **Report View ACLs?**

ServiceNow has introduced Report View ACLs (RVA) as an additional layer of control on tables. Report View ACLs limit which users can view sensitive data when reports are created.

All newly provisioned ServiceNow instances will have the Report View ACLs installed and enabled by default for all plugins and applications. Pre-Rome instances that have upgraded to current versions will have the Report View ACLs installed but remain disabled for the applications previously installed. Plugins and applications activated after the upgrade will install and enable the Report View ACLs specific to the application.

Prior to enabling RVAs, instance users could view an aggregated report shared to them while not having permissions to view the underlying table data. After RVAs are enabled, the same user is unable to view the report unless they have been granted the role(s) for the blocking RVA. For example, a user could have an aggregated report (e.g., pie chart) report shared with them that displays summarized sensitive financial data. The user does not have access to view the table level data due to table level read ACLs, however they can view the summary data. Report view ACLs (RVAs) control whether the user will be able to display the results of the aggregated report.

### **Known Issues**

As part of the effort to enable Report View Access controls (RVAs), many of the Access Control Lists (ACLs) were enabled and intentionally flagged to prevent changes to out-of-the-box (OOB) RVAs during an upgrade process. As a result, these RVAs are seen as 'skipped' during an upgrade. No changes or modifications have been made to these components, even though the upgrade log reports these RVAs as skipped due to customization. This problem has been **fixed in: San Diego Patch 10 Hot Fix 1, Tokyo Patch 7, Utah Patch 1, Vancouver**.

Some RVAs may become disabled during upgrades to family releases, patch updates, or store application updates. To ensure any disabled out-of-the-box RVAs are properly enabled, it is recommended to use the ACL Assessments for Reports application to complete enablement of ACLs post family release upgrades:

1. 
    1. Prior to an upgrade (patch, family, or store app) and after enabling RVA's on your instance, navigate to the **sys_security_acl** table, ensure the Updated Name field is in the list layout. Filter for **Operation is report_view** and **Active is false.** Export this list of ACLs to a file and save for post upgrade.
    2. Perform the upgrade
    3. To re-enable the Enable ACLs button on the app, we must remove appropriate entries from the **report_view_acl_activation_log** table.
        - When using Version 1 of the ACL Assessment for Reports app, the security admin should delete the record from table where '**Is Generate Report=false**'
        - When using Version 2 of the ACL Assessment for Reports app, the security admin should delete the record from the table where '**Activity=Enable ACLs'** *AND* '**Is last created=true'**
    - 
    - 
    1. Use the Enable ACLs button in the app to re-enable all OOB RVAs
    2. Using the list of ACLs we exported from step 1, open the **sys_security_acl records** table. Using the filter, search for the **Update Name** field **is one of** <your list of ACLs exported from step 1>.
        1. For each that is identified take appropriate action to deactivate RVAs to restore it to pre-upgrade state
        2. If no matches are identified, no further action is required
    3. 
    4. 

[Report_view ACLs activated on upgrades and plugin installation](https://support.servicenow.com/kb_view.do?sysparm_article=KB0997156)

[Core Company table report view ACL Utah issue](https://support.servicenow.com/kb_view.do?sysparm_article=KB1421879)

For administrators looking to **upgrade to Utah**: [Utah Report View ACL Dashboard](https://docs.servicenow.com/bundle/utah-now-intelligence/page/use/reporting/concept/report-view-acl-dashboard.html)

### **Enabling Report View ACLs**

Report View ACLs are enabled when the active field is set to true.

**Caution!** Enabling Report View ACLs will prevent some users from viewing some reports unless they have been granted the appropriate role defined for the specific Report View ACL. ServiceNow Admins must evaluate which users should retain report access and grant the appropriate Report View ACL role(s) before enabling the Report View ACLs.

ServiceNow recommends becoming familiar with these concepts before enabling RVAs:

- [Access Control Lists](https://docs.servicenow.com/bundle/rome-platform-administration/page/administer/contextual-security/concept/access-control-rules.html)
- [Groups](https://docs.servicenow.com/bundle/rome-platform-administration/page/administer/users-and-groups/concept/c_Groups.html)
- [Report View Access Controls](https://docs.servicenow.com/bundle/rome-now-intelligence/page/use/reporting/concept/report-view-access-control.html)
- [Roles](https://docs.servicenow.com/bundle/rome-platform-administration/page/administer/roles/concept/c_Roles.html)
- [Sharing Reports](https://docs.servicenow.com/bundle/rome-now-intelligence/page/use/reporting/task/t_ShareASetting.html)

The 5 steps below will guide you through the entire process. **Run the assessment on a non-production instance first!** Select the instance which has a recent clone from production to get a good understanding of the app before you take action in your production instance. Be aware that the assessment results may vary depending on what data is available on the instance it is being run on; run the assessment scan on production or a clone with full data set to get the most accurate scan results.

### **1. Install the ACL Assessment for Reports application**

ServiceNow has provided the **ACL Assessment for Reports** application to scan your instance and product an inventory of reports and users that will be affected when the Report View ACLs are enabled.

Install the [**ACL Assessment for Reports**](https://store.servicenow.com/sn_appstore_store.do#!/store/application/840a9f1ac35260100687e0dd9740ddae) application from the ServiceNow store.

**NOTE**: Upon choosing "Get" from the store, an email will be sent containing additional instructions on how to activate it on the desired instance.

If you are need help with locating or installing the ACL Assessment for Reports app through the ServiceNow Store, please contact Support for assistance.

**NOTE**: if your instance is self-hosted and does not have internet access to the ServiceNow store, review the instructions in:

[How On-Prem customers can request a Store App](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745101)

[How to generate and upload a certificate for on-prem store app + common issues resolutions on errors](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1080332)

Security Admin Role is required to view the "ACL Assessment for Reports" after installation is complete.

Video overview of installing the "ACL Assessment for Reports" and reviewing the affected reports scan; steps 1 and 2 below.

[[view full screen](https://players.brightcove.net/6274575390001/nUx4EKfUz_default/index.html?videoId=6299416073001)]

### **2. Run an assessment scan**

The assessment scan results provide a "what if" view into which reports, and users will be impacted when the Report View ACLs are enabled. Proactively assigning the Report View ACL role(s) to affected users will allow a seamless transition for those users who should keep access to the data within the report. Understanding what data is contained in the report should be considered when deciding whether to grant continued access to a user.

Navigate to Reports > ACL Assessment for Reports > Report ACL Dashboard

Using the ACL Assessment for Reports application, run your first scan. The scan may take many hours to complete, so plan accordingly.

**Note:** For customers running on an Oracle instances please review [KB1080280](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1080280) "ACL Assessment for Reports application provides incomplete scans for instances leveraging Oracle DB"

**TIP:** Run the assessment on a non-production instance first! Select an instance that has a recent clone from production to get comfortable with the application before you act in your production instance.

### **3. Evaluate the results of the scan**

Use the Assessment Scan Results to identify which reports will require action and determine who within your organization can provide context to ensure users retain appropriate access.

**TIP:**

Drill into more details of each report by clicking the

[](https://support.servicenow.com/sys_attachment.do?sys_id=2e28cd9147fdb19030fba325126d43e7)

and opening the record.

### **4. Ensure affected users retain appropriate report access**

### **Two remediation options to ensure affected users retain appropriate report access.**

### **Both options require manual intervention by the instance Security Administrator.**

**Option 1:** Change the sharing permission of reports by reducing the audience with whom a report is shared.

**Option 2**: Assign the appropriate Report View ACL role for the report to a group. Assign the affected users to the group.

### **Option 2 step-by-step:**

1. 
    1. Open an affected report listed in the scan results.
    2. Review the list of affected users. The users in this list will be unable to view this report when the report view RVAs are enabled.
        1. From the assessment scan results, drill into more details of each report by clicking the and opening the record. Click the link to view affected users. Scroll to the bottom of the page to view a list of users that are missing the required roles and will lose access after the report_view ACLs are enabled. Any role(s) added to a user(s) may also grant them the necessary access for other affected reports. The list of affected users will only update once the full assessment scan is rerun.
            
            [](https://support.servicenow.com/sys_attachment.do?sys_id=2e28cd9147fdb19030fba325126d43e7)
            
        2. The default list view only displays the first 5 users affected. See below "Increase the number of Affected Users displayed" to change this setting.
        3. Evaluating reports and users may require additional knowledge expertise within the organization. For example, evaluation of HR reports may require working with the HR admin to ensure the appropriate users maintain access to the HR reports in question.
    3. 
        
        [](https://support.servicenow.com/sys_attachment.do?sys_id=2e28cd9147fdb19030fba325126d43e7)
        
    
    [](https://support.servicenow.com/sys_attachment.do?sys_id=2e28cd9147fdb19030fba325126d43e7)
    
    1. 
    2. 
    3. To ensure users can access the report after the Report View ACLs enabled, the user must have one of the roles listed in the "Blocked by table ACL roles" found at the top of the affected users drill-down page.
        - You can create a new role, associate it with the ACL listed.
        - The users listed in the affected users list will lose access to the affected report when the Report View ACLs are enabled, this is due to the lack of required permission granted by the Report View ACL role. To prevent loss of access, grant the role via group to the user(s) desired prior to enabling the Report View ACLs.
    - 
    - 
    1. In **version 2 of the Report View ACL Assessments** application a feature has been introduced that enables assigning affected users to groups.
        1. Click the Show Affected Users button
        2. Select the user(s) by checking the box next to their name in the affected users list that need to be added to a group
        3. In the 'actions on selected rows…' drop down, select 'Assign to Groups
        4. Select the appropriate group from the Group drop down and Submit.
            1. Each one of the groups listed in the Group drop down has at least one of the required roles that grant access to the selected users
            2. Please keep in mind that adding a user to a group will give them all the roles assigned to that group
            3. Submitting the form, selected users will be added to the selected group and will no longer be blocked
                1. Please note reports based on DB View where users are blocked by 2 or more ACLs on 1 or more base tables will require all roles be identified from the base tables.
        5. If **no group is available** that has the blocking roles (when at step 4d), the Group drop down will populate the entire list of groups and present a Role drop down list
            1. Using the Role drop down a list of blocking role(s)is presented
            2. Select the Group you wish and assign the blocking Role
            3. By submitting the form, the selected role will be added to the selected group and the selected users will be added to the group.**Note:** It is recommended to create a new group and assign to it one of the required roles (outside of this application) and then select the group via this form to grant access to the selected blocked users.
    2. 
    3. 
    4. 
    5. 
        1. 
        2. 
        3. 
            1. 
    6. 
    7. 
    8. 
        1. 
    9. 
    10. 
        1. 
        2. 
        3. 
    11. 
    12. 
    13. 
    14. Once users have been provided with the role, the report will continue to display after the report view ACLs are enabled.**REPEAT steps 1-4 for all affected reports.**
    15. When all affected reports have been remediated, re-run the Assessment Scan with the dot-walk configuration (system property = sn_report_acl.com.par_report_acl_assessment.collect_dotwalk). A dot-walk affected report scan may show newly discovered reports that were not initially identified.**TIPS:**
- 
    - 
        - Triaging reports based on tables, users, or groups can expedite steps 1-4. By identifying a common role spanning multiple tables it is possible to grant access for many users. For a complete view of all affected reports, click the left nav link "**Affected Reports List**".
        - ServiceNow admins can create new roles or use the default roles
        - Create a New Group as necessary to assign the required role
        - Re-running the Assessment scan after remediation steps are complete provides an updated list of affected reports and users. Re-running the scan replaces the previous scan results and requires the same time to complete the scan. **Licensing considerations** – When assigning roles to groups for users, take subscription licensing into consideration. Applications that are entitled to use the "fulfiller" roles (e.g., ITSM and CSM) have a different subscription basis than a report viewer or "Requestor" role. Using a "non-Fulfiller" group to assign the report view access control roles grants access to reports without impacting subscription. Using groups that have been identified as fulfillers will impact subscriptions if added users were not previously subscribed as fulfillers. Reach out to your Sales Representative or Account Manager for specific contractual details regarding role types, subscriptions, and licensing.
    - 
    - 
    - 
    - 
- **Do not proceed to step 5 until you have remediated all impacted reports.**

### **5. Enabling Report View ACLs**

After you use the ACL Assessment for Reports application to review the inventory of affected reports and implement steps to remediate, you can now enable the report view ACLs. Click the **Enable ACL's button** in the app to enable all the report view ACLs. Enabling Report View ACLS is now complete!

- All Report View ACLs active value has been set 'true'.
- All affected users identified in assessment scan that were not granted the required role(s) will not be able to view the listed reports.
- The ACL Assessment for Reports application can continue to be used to identify affected users and reports.

### **Enabling Report View ACLs is now Complete!**

- All Report View ACLs 'active' field has been set 'true'.
- All affected users identified in assessment scan that were not granted the required role(s) will **not** be able to view the listed reports.
- The ACL Assessment for Reports application can continue to be used to identify affected users and reports.

### **Application Configuration, Options, Guidelines**

**Run the assessment on a non-production instance first!** Select the instance which has a recent clone from production to get a good understanding of the app before you take action in your production instance. Be aware that the assessment results may vary depending on what data is available on the instance it is being run on; run the assessment scan on production or a clone with full data set to get the most accurate scan results.

**Security admin (elevated role) is required to take actionConfigure the assessment scan for your instance:**

| **Configuration Option** | **Details** |
| --- | --- |
| Limiting your scan | By default, the scan collects information about reports that have been accessed (1 or more time by any user) within the last year (365 days). You can increase or decrease this number by adjusting the sn_report_acl.process_reports_executed_within_X_days_ago system property. |
| Expanding your scan | By default, the assessment scan uses the report_executions table to build an inventory of affected reports.This limits the assessment scan to only reports that have been accessed at least once.To expand the scan to include all reports, change the sn_report_acl.run_scan_based_on_report_execution_only system property. |
| Increase the number of Affected Users displayed | By default, when you view details about an affected report, the Affected Users related list loads five users. You can increase this value to show more users. Adjust the system property sn_report_acl.com.par_report_acl_assessment.max_affected_users to identify more impacted users. |
- **Give it time:** Some scans may take many hours to complete, so plan accordingly. Expanding your scan parameters will lengthen the time to complete.
- **View it live:** Although the scan may not be complete, you can begin to look at the results in real time.
- **Performance:** The scan, no matter how long it runs, should not impact instance performance

### **Published Reports and Report View access controls (public reports)**

ServiceNow recommends becoming familiar with these concepts before enabling RVAs:

- [Published Reports](https://docs.servicenow.com/bundle/sandiego-now-intelligence/page/use/reporting/task/t_PublishAReport.html)

Enabling RVAs may impact access to published reports by external, unauthenticated users.

Instance admins who have a requirement to publish reports to external, unauthenticated users will need to use a report view ACL specific to the table or field that is to be published. Apply the public role to the necessary report view ACL. When using the public role, take into consideration:

- Validating that all currently published reports are published appropriately
- Confirming that the "report_publisher" role is assigned in alignment with the principle of least privilege and only granted to users with a requirement to publish reports
- Ensuring all reports are shared with the appropriate audience
- Validating report data within each published report does not contain customer-determined sensitive information

### **Domain Separation**

if your instance uses domain separation, you can configure your assessment scan to search across all domains.

Please refer to [KB1005116 - Enabling Report View Access Controls for Domain Separated Instances](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1005116) for additional considerations for domain-separated instances.

### **Review the data**

Filter and sort your completed assessment scan report for your instance:

- Navigate to Reports > ACL Assessment for Reports > Affected Reports List to view the entire assessment scan report.
- A common way to view a completed scan is to identify the impacted tables that have the most report views.
    - Group by Table, Sort by Count – in this method you can quickly identify which table has the highest count of accessed reports and which groups that control access.

### **Ensure affected users retain appropriate report access by enabling report view ACLs through two common scenarios**

1. Change the sharing permission of reports by expanding or reducing the audience a report is shared with.
2. Assign the role for the report view ACL to a group. Assign the affected users to the group.

### **Double Check subscriptions (licensing)**

Use [Subscription Management](https://docs.servicenow.com/bundle/utah-platform-administration/page/administer/subscription-management/concept/subscription-mgt-admin-guide.html) to confirm if a [role has a subscription requirement](https://docs.servicenow.com/bundle/utah-platform-administration/page/administer/subscription-management/task/view-roles-for-subscription-plugin.html) before applying it to a group.

- Reach out to your Sales Representative or Account Manager for specific contractual details regarding role types, subscriptions, and licensing.

### **Manual action required**

Each instance security admin must take manual action to add the appropriate roles prior to activating report view ACLs.

### **Hide reports or users**

Specific reports or users can be hidden from your scan results using the ignore feature. All subsequent re-scans will obey the ignore.

- To remove the ignore from a user, use the Reports > ACL Assessment for Reports > Ignored Reports and Users List menu
- To remove the ignore from a report, use the Reports > ACL Assessment for Reports > Ignored Reports and Users List menu

### **Targeting a scan to a single table**

- Changing the value in the sn_report_acl.add_encoded_query_for_sys_report_table system property, you can choose a table to restrict the assessment scan.
- The subsequent scan will limit the results to only the table identified in the system property.

### **FAQs**

### **How to know who has access to these reports?**

- View the report_execution table to see a list of report access by users of the instance. If you see users in this table, confirm they should have access to these reports.

### **What does the assessment scan look for, exactly?**

- The assessment scan identifies reports that will have an impact to a user's ability to see the report data after the report view ACL is enabled.

### **ServiceNow recommends identifying "Applicable groups" for impacted reports. What does that mean?**

- When determining which role & group grants access to a report view the instance admin must take into consideration the intended use for the group, whether it requires subscriptions, and if it is fit for purpose for those assigned to the group.

### **How often should I re-run my scan?**

- Gathering fresh assessment data is always recommended. How frequently you refresh the data depends on many factors, including how long your scan takes to complete, and how you plan to implement the report view ACLs, and if changes have been made to ACLs.

### **Can I use alternative Role(s) on the report_view ACLs?**

- Custom roles can be used.

### **How long should the scan run?**

- The scan duration is directly related to the size of these 4 tables:
    - sys_report
    - sys_user
    - sys_user_has_role
    - sys_user_group
- Additionally, if the scan is configured to ignore the report_executions table, the duration will increase.
- The report may take minutes or many hours to complete. Test in a non-production instance with a recent clone of production data to get a good feel for assessment scan duration.

### **Can Report View ACLs be removed or intentionally disabled?**

- Removing or disabling Report View ACLs may have negative consequences to the accessibility of the reports within your ServiceNow instance(s) meaning that unintended audiences may be able to view reports.

### **Can I target reports or application modules from the assessment scan?**

- Yes. You can add a specific table for an assessment scan

### **Can the assessment scan include dot-walk tables in reports?**

- By default, the assessment scan does not target dot-walk tables used in reports. If you are interested in seeing impacted reports that accumulate data using the dot-walk feature, expand your search using the sn_report_acl.com.par_report_acl_assessment.collect_dotwalk system property
    - Please note this will increase your assessment scan duration

The suggested approach is to run the assessment scan without considering dot-walk tables and completing any remediation actions before adding the dot-walk tables to the scan results

### **How long will it take to remediate a report?**

- Remediating a report requires assigning the ACL role to the users deemed appropriate for continued access. The time it takes to remediate a report will be affected by many factors that go into making this decision. Using groups to assign the report view ACL role can be the quickest way to remediate user(s) in bulk.

### **Is there a bulk update feature?**

- No

### **What happens to the assessment scan data if I rerun a scan?**

- Previous assessment scan data is deleted. A new set of data is collected by the assessment scan based on current report access information

### **When opening a blocked ACL link from the app the results are empty or missing some ACLs, why?**

- The Report View ACL list view is based on the sys_security_acl_role table and if an ACL does not have a related role in that table the results will show empty.

### **How do I refresh the "Affected user" list?**

- Rerun the scan. When drilling into affected users on a report the data is sourced from the last scan, it's not sourcing the data directly in real-time.

### **What will the impact be for a user who has not been granted a report view ACL role after the ACL has been enabled?**

- When the user attempts to access the report, it will load but will not contain the data protected by the report view ACL.

### **Can I capture my changes for Report View ACLs with an Update Set and apply them to another instance?**

- No, modifying roles and groups are not captured in an update set and cannot be promoted from non-production instances to production.

### **Can I run the scan to view affected reports after the report_view ACLs are enabled?**

- Yes, the scan can be run after the report view ACLs have been enabled and will display the same affected report information.

### **How can I see who has accessed reports?**

- View the report_executions table to see a list of reports access by users of the instance. If you see users in this table, confirm they should have access to these reports.

### **I see a user on the report_executions list that I confirmed should not have access to a report, what do I do to remediate this?**

- Using the remediation scenarios provided above, determine how best to remediate for your instance.

## Related

- [[Security & ACL]]
- [[Alternative Encryption Products to GlideEncrypter]]
- [[How to replace usage of GlideEncrypter in Legacy W]]
- [[Confidential Attachments]]

### **Can I customize the look and feel of the app?**

- No

### **Why does the affected user's list include users that have been confirmed to have the required roles?**

- If an assessment scan has been run ignoring the report_executions data and the report in question has been shared with everyone, the affected users list can contain users that are not impacted. To remediate these reports, either remove "everyone" from shared to and rerun the scan to get the actual users affected or ensure all users on the instance have the required role.