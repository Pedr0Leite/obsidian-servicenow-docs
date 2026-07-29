---
title: Links to records in email notifications
description: Adding the $\{URI\} parameter to an outbound email body or template creates a link to a specific record.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-administration/c\_EnablingLinksToServiceNowRecords.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create an email notification, Email and SMS notifications, System notifications, Notifications, Configure core features, Administer the ServiceNow AI Platform]
tags:
  - platform-administration
  - type-concept
---

# Links to records in email notifications

Adding the **$\{URI\}** parameter to an [[ia-outbound-email-il|outbound email]] body or template creates a link to a specific record.

When a user clicks the word LINK, the instance prompts the user to log in if not already logged in, and then redirects the user to the record specified in the URI.

\[Omitted image "EmailURI.png"\] Alt text:

The $\{URI\} parameter has an extension called the $\{URI+\} format to specify additional arguments in the email link, such as sysparm terms, in addition to the automatically created URI. For example \(whitespace added for improved readability\):

```
${URI+&sysparm_scriptlet=current.assigned_to=gs.getUserID()
&sysparm_scriptlet_condition=current.assigned_to.nil()
&sysparm_view=incident_active}
```

This example executes the JavaScript:

```
current.assigned_to=gs.getUserID()
```

when the condition of

```
current.assigned_to.nil()
```

is satisfied. Additionally, the script sets the view to `incident_active`.

## Linking to a record in Workspace

The `${URI}` and `${URI_REF}` variables don't apply to records in Workspace. To link to a record in Workspace, create a mail script and [[reference-email-admin|reference]] it in your notification. For more information on using mail scripts, see .

The mail script that you create should print a URL to the notification. The URL must have the following format:

```
https://<instance_name>/now/workspace/<workspace_name>/record/<table_name>/<sys_id>
```

The following example script shows the logic that a mail script must include to create a link to a record in Workspace.

```
// Dynamically construct an Agent Workspace URL and insert a link in the notification
  var agentURL = '<a href="' + gs.getProperty('glide.servlet.uri') + '/now/workspace/agent/record/'+ current.getTableName() + '/' + current.sys_id + '">' + current.number + '</a>';
  template.print(agentURL + "<br />");
```

-   **[[c_EnableLinksToServiceNowRecords|Enable links to records]]**  
Adding the special **$\{URI\}** parameter to an outbound email body or template creates a link to a specific record.
-   **[[c_ChangeTheLinkText|Change the link text]]**  
To show the display value of the record as the link text instead of the word LINK, use the $\{URI\_REF\} parameter instead of the $\{URI\} parameter.
-   **[[c_LinkToRelatedRecords|Link to related records]]**  
A notification can link to a related record by specifying a reference field in front of the**$\{URI\}** or **$\{URI\_REF\}** [[r_DirectJDBCProbeParameters|parameters]].
-   **[[c_LinkingToContentPages|Content page links in email notifications]]**  
Links to CMS pages can be put in [[notifications|notifications]] to make it easy for the reader to access the pages.

**Parent Topic:**[[t_CreateANotification|Create an email notification]]

## Related

- [[c_EnableLinksToServiceNowRecords|Enable links to records]]
- [[c_ChangeTheLinkText|Change the link text]]
- [[c_LinkToRelatedRecords|Link to related records]]
- [[c_LinkingToContentPages|Content page links in email notifications]]
- [[t_CreateANotification|Create an email notification]]
- [[ia-outbound-email-il|Outbound email]]
- [[reference-email-admin|Reference]]
- [[r_DirectJDBCProbeParameters|Parameters]]
- [[notifications|Notifications]]
