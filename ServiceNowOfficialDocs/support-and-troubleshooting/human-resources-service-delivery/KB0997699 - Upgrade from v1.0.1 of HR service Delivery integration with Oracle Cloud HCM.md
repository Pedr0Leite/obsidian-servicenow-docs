---
title: "Upgrade from v1.0.1  of HR service Delivery integration with Oracle Cloud HCM"
aliases:
  - KB0997699
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0997699
kb_number: KB0997699
last_modified: 2025-02-18
---

## Text

To upgrade from v1.0.1 of HR service Delivery integration with Oracle Cloud HCM, please follow below steps. Please make sure that the job is not running while performing these steps. You can inactivate the scheduled flow to make sure that the job doesn't start during this process.

1.  After upgrading the app, import and commit the attached update set file with name "Update\_Set\_HRSD\_Oracle\_Integration\_1\_0\_3.xml".  
    Note: In case of any conflicts, please make sure that the changes from this update set should get applied along with your customisation. 
2.  Navigate to Fix script and import the attached fix script. Refer attached file "Fix\_Script\_HRSD\_Oracle\_Integration.xml".
3.  In the Fix script list, search for fix script with name “Fix correlation id - Oracle HCM cloud”.
4.  Open the fix script and click on "Run Fix Script". You **MUST** run the fix script in background as this might take few minutes to fix the data. You can track the progress by clicking on “Show Progress Workers” on fix script details page.
5.  After successful execution of fix script, run the oracle integration job with property full\_pull set to true. After successful run of job you can set it back to false as required.
6.  For better performance, make sure that you have index on coalesce fields in [transform maps](https://docs.servicenow.com/bundle/rome-employee-service-management/page/product/human-resources/reference/oracle-hcm-transform-maps.html "Transform maps specify data relationships between a source table and a target table.") and an index on the employee number field in HR Profile table. For more information, see [create a table index](https://docs.servicenow.com/bundle/rome-platform-administration/page/administer/table-administration/task/t_CreateCustomIndex.html)

Once the fix script execution is done and the job gets executed successfully with full\_pull as true, you are all set with the upgrade.
