---
title: "Can a JAR file be pushed to a specific MID Server instead of all MID Servers?"
aliases:
  - KB0813383
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813383
kb_number: KB0813383
last_modified: 2025-11-14
---

## Can a JAR file be pushed to a specific MID Server instead of all MID Servers?

  

### Summary

You may want to add a JAR file to a MID Server, but not have that file synchronised to all other MID Servers as well. As of the Utah release, **there is no out-of-box feature to do this**.

Situation where this might be useful:

-   Testing a new JAR file, such as for an External Credential Store, or new JDBC Driver, on a single MID Server before releasing it to all MID Servers
-   Applying JAR files only to MID Servers that require it, such only the Discovery MID Servers that will use an external credential store, to apply additional required files to MID Servers running Java 11.
-   Have different versions of the same JDBC Driver on different MID Servers.

### Release

Any

### Instructions

Manually copying the JAR file to the MID Server install folder is not a solution, as to protect the MID Servers from unauthorised JAR files, any JAR file found on the disk during synchronisation that is not in the JAR Files table of the instance is deleted \[ecc\_agent\_jar\].

Synchronisation happens whenever changes are made to the JAR file table in the instance, or whenever a MID Servers Starts up. The MID Servers query the instance for the list of JAR files. A customization to hide records in that query is possible.

A query business rule can hide certain records, for certain users, for non-interactive sessions. The isInterractive() in the conditions is important so that normal users looking at the JAR file records in the instance are not going to have them hidden.

Note: This will not prevent all MID Servers getting SystemCommands for any new or changed JAR file, triggering a re-sync and possibly a MID Server restart, even though they won't then be able to see the file, so won't actually sync it. A before insert abort action business rule on ecc\_queue for these specific ecc\_queue outputs (source=FileChange, name=ecc\_agent\_jar, topic=SystemCommand, queue=output) could be created, and delay the next resync until the mid server is restarted. That's not something the author has tested.

**WARNING: Query business rules are tricky things. They hide records from out-of-box code as well as users and can cause unexpected behaviour, and side-effects in other code that wasn't considered when designing the business rule. This would be an unsupported customisation, and use this with care, and be sure to thoroughly test.**

if (gs.getUserName() !== 'test\_mid\_server\_user' && !gs.isInteractive()) {  
		current.addQuery('name','!=','Experimental JAR File');  
}

![](/sys_attachment.do?sys_id=d2521300931d72105736b25d6cba10ba)

### Related Links

Documentation: [Synchronize a JAR file to MID Servers](https://docs.servicenow.com/search?q=Synchronize+a+JAR+file+to+MID+Servers "Synchronize a JAR file to MID Servers")

There has been an [Idea on the Community site requesting per-MID Server JAR files](https://community.servicenow.com/community?id=view_idea&sysparm_idea_id=46895c24db3b54506621d9d96896192f&sysparm_idea_table=x_snc_com_ideation_idea&sysparm_module_id=enhancement_requests "Idea on the Community site requesting per-MID Server JAR files"), but the Product Managers closed this.

[KB1182832 Add or replace Java Classes in the MID Server, without using the JAR File synchronisation from the instance](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1182832)
