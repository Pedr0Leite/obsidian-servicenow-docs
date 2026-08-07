---
title: "How to go back to using the application repository after commiting changes to an application via update set"
aliases:
  - KB0715422
tags:
  - servicenow
  - support-kb
  - scoped-applications
  - application-repository
  - update-sets
  - GlideRecord
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715422
kb_number: KB0715422
last_modified: 2026-05-21
---

## How to go back to using the application repository after commiting changes to an application via update set

  

### Issue

Do not combine the usage of both Update Sets and the Application Repository for scoped app development. This will result in numerous issues, including skipped changes, commit errors, and more.

Once you have installed an application from the Application Repository, you must continue to develop and publish to the Application Repository for all future development. If you decide to develop an application using update sets, you must continue to use that method exclusively.

### Release

All supported releases

### Resolution

Although difficult, you can work your way back to using the Application Repository for development if you have mistakenly committed update sets for a scoped app and wish to go back to using the previous method.

**NOTE:** This method will not work if you have never used the Application Repository for your app. If the application was originally installed via update set, the only way to switch is to completely delete the app and perform a fresh install from the Application Repository.

The solution is to revert the entire application to its base system version from the application repository. Doing so requires some special steps to prevent all of the previously-committed update sets from causing conflicts:

1.  Publish the application to the Application Repository on the development instance. This will package and publish the most current version of the application to the repo, ready to install on the target instance.
2.  On the target instance, you must set the replace\_on\_upgrade field to true on _all_ sys\_update\_xml records for the application. This will prevent these updates from causing conflicts when you install the application from the Application Repository. This step is best performed via script. An example of such a script can be found below.
3.  Once all sys\_update\_xml records for the app have been updated, install the latest version of your application on the instance. If executed properly, this will apply the base system version of each application file in the app.

What follows is an example of a script that can be used to set replace\_on\_upgrade to true on every existing sys\_update\_xml record for the specified application.

**NOTE:** This script is only provided as an example. Usage of this script is done at your own risk. Modification of this script can result in irreversible corruption of sys\_update\_xml data.

```
preventConflicts('12345678ABCDEFGH12345678ABCDEFGH'); // Sys ID of your app's sys_store_app record
function preventConflicts(appid) {
    var gr = new GlideRecord('sys_update_xml');
    gr.addQuery('application', appid);
    gr.query();
    while(gr.next()) {
        gr.replace_on_upgrade = true;
        gr.update();
    }
}
```

**WARNING:** This script will convert EVERY update / customization to be replaced on upgrade, be aware of things like specific instance configurations which are expected to be customized per instance. Updating a field with replace\_on\_upgrade set can cause data loss if the configuration would shrink the max length of a column.

## Related

- [[KB0695169 - Changes to a scoped application are not being applied when the update is installed]]
- [[KB0695379 - Files still left in Changed Files list after committing a scoped application to source control]]
- [[KB0695295 - Resolve The operation encountered an unexpected error when linking source control to a Git repository]]
- [[app-repo]]

## Related Notes

- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695169 - Changes to a scoped application are not being applied when the update is installed|Changes to a scoped application are not being applied when the update is installed]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695379 - Files still left in Changed Files list after committing a scoped application to source control|Files still left in Changed Files list after committing a scoped application to source control]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0656366 - Relationship between Business Rules and Access Control Rules (ACLs)|Relationship between Business Rules and Access Control Rules (ACLs)]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/access-controls-authentication/KB0687531 - Authorship of application was lost after clone|Authorship of application was lost after clone]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0695295 - Resolve The operation encountered an unexpected error when linking source control to a Git repository|Resolve \"The operation encountered an unexpected error\" when linking source control to a Git repository]]
- [[ServiceNowOfficialDocs/support-and-troubleshooting/application-development/KB0718655 - Scripted (incorrect) query is unexpectedly returning all records|Scripted (incorrect) query is unexpectedly returning all records]]
