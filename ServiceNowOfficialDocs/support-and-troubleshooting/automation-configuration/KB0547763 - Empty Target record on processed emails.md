---
title: "Empty Target record on processed emails"
aliases:
  - KB0547763
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547763
kb_number: KB0547763
last_modified: 2025-09-26
---

## Empty Target record on processed emails

  

### Issue

The processed email records in the Received mailbox (System Mailboxes > Received) have an empty value in the Target field. The user does not know which record, or even if a record, was created or updated as a result of processing the email record.  
  
  
![Target Field is empty even after inbound action was processed](/sys_attachment.do?sys_id=f62dda11936f5e505736b25d6cba10f4 "Target Field is empty even after inbound action was processed")

### Symptoms

-   The email record has a state of Processed, but the Target field is empty.
-   The email log shows that there is an inbound action that was skipped because it did not update or create a record.

![Action was skipped because it did not create or update a record](/didnotCreateorupdateincident.pngx "Action was skipped because it did not create or update a record")

### Release

All releases

### Cause

When an inbound action processes an incoming email, it uses the variable current to represent the record that it affects.  
  
If a new record is to be created, then-current represents a new empty record for the target table suitable for the population before an insert.  
  

<table style="height: 200px; width: 1200px;" width="647"><tbody><tr><td><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12<br>13</pre></td><td><pre>//Sample inbound action script creates an incident record 

current.caller_id = gs.getUserID();
current.comments = "received from: " + email.origemail;
current.short_description = email.subject;

current.category = "request";
current.incident_state = 1;
current.notify = 2;
current.contact_type = "email";

current.insert(); //&lt;--When line completes, it will update the target <br>                  //   field on the email record with a reference to the created record                 
</pre></td></tr></tbody></table>

  
If an existing record is to be updated, then current represents a reference to the record that is to be updated.

<table style="width: 1206px;"><tbody><tr><td><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13</pre></td><td><pre>gs.include('validators');

if (current.getTableName() == "incident") {
    current.comments = "reply from: " + email.origemail;
    
    if (email.subject.toLowerCase().indexOf("please reopen") &gt;= 0) {
        current.state = "2";
        current.work_notes = "Issue was not resolved";
    }

    current.update(); //&lt;--When this line completes, it will update the Target field <br>                     //on the email record with a reference to the updated record
}
</pre></td></tr></tbody></table>

  
If the script does not use variable current to update or create a record, the system does not know which record was affected and therefore is not able to fill in the Target field.

### Resolution

-   Whenever possible, use the already-provided current to update or create the target record.  
    Or:
-   If this is not an option because the script updates a record that does not belong to the Target table, or if you update/create more than one record, then consider manually logging the changes made by your custom action using gs.log() as described in [product documentation](https://docs.servicenow.com/csh?topicname=c_InboundEmailActions.html&version=latest "product documentation").

<table style="width: 1183px;"><tbody><tr><td><pre>1
2
3
4
5
6
7
8</pre></td><td><pre>var grIncident = new GlideRecord('incident');
grIncident.initialize();
grIncident.caller_id=gs.getUserID();
grIncident.comments = "received from: " + email.origemail;
grIncident.short_description = email.subject;
grIncident.insert();
//create log entry to know what created/update by this action
gs.log("&lt;custom_action_name&gt; Created Incident:" + grIncident.number, "EMAIL." + sys_email.sys_id);</pre></td></tr></tbody></table>

        You should then be able to view the record that was created or updated in the email logs.

![](/custom_log.pngx)
