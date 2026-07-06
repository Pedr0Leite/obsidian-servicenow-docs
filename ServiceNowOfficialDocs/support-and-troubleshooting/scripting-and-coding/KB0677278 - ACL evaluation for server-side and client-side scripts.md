---
title: "ACL evaluation for server-side and client-side scripts"
aliases:
  - KB0677278
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0677278
kb_number: KB0677278
last_modified: 2026-06-17
---

## ACL evaluation for server-side and client-side scripts

  

### Issue

This article explains when Access Control Rules (ACLs) are evaluated for Business Rules, UI Scripts, Script Includes, background scripts, UI Actions, and Client Scripts at runtime.

When working with Business Rules, UI Scripts, Script Includes, background scripts, UI Actions, and Client Scripts, it is important to understand when ACLs are evaluated at runtime. A lack of understanding of this behaviour is a common source of frustration when investigating issues related to client-side and server-side JavaScript.

Three key facts apply:

1.  All scripts mentioned above run in the context of the current user.
2.  Scripts that use the ServiceNow server-side JavaScript API classes to create, read, update, and delete records are not subject to passing or failing ACLs. The **GlideRecordSecure** class is the exception.
3.  Scripts that use the ServiceNow client-side JavaScript API functions always observe ACLs.

### Release

  All releases

### Resolution

#### Approving records without write access to the State field

A single UI Action demonstrates all three facts above. The UI Action can be viewed at the following URL on a test instance:

https://instance-name.service-now.com/nav\_to.do?uri=sys\_ui\_action.do?sys\_id=8468ee55c611227d01a072a67bdbd3e7

The Client checkbox on this UI Action is not checked, meaning it runs server-side JavaScript. The script sets the state of the current record to "approved" and then updates the record. Because ACLs are not observed on the server side by default, any user with access to the UI Action form button can approve the current approval record regardless of whether they pass or fail the ACLs on table **sysapproval\_approver**.

The condition to see the UI Action form button requires that the current record's state is "requested" and that the current user is either the approver on the record or a delegate of the approver. Problems occur when the condition is relaxed to allow more end users to see the button, on the assumption that ACLs on the table will prevent approval by users without write permissions.  
  

#### Test 1: Server-side JavaScript ignores ACLs by default

1.  Change the condition on the UI Action from:

current.state == 'requested' && isApprovalMine(current)

to:

current.state == 'requested'

Search for Debug in the Application Navigator and select Debug Security.

Impersonate the ITIL user.

1.  The ITIL user can read all records on table **sysapproval\_approver** but will not pass the write ACL for the State field on a base system instance.
2.  Navigate to:

https://instance-name.service-now.com/nav\_to.do?uri=sysapproval\_approver\_list.do

1.  Open any record where the state is "requested".
2.  Search the browser page for the text "state/write". On a Mac, search in Chrome with ⌘+Enter. On Windows, use Ctrl+F. The results confirm that the ITIL user fails the write ACL for **sysapproval\_approver.state**.
3.  Select the Approve UI Action button.

Although ACLs might be expected to prevent the ITIL user from writing to the State field, the server-side JavaScript in the UI Action updates the State field without checking ACLs. The record is approved by a user that cannot pass the write ACL for the State field, because that user was given access to the Approve UI Action form button.  
  

#### Options for enforcing ACLs in server-side scripts

To enforce ACLs in server-side scripts, use one of the following options:

-   Use the **canCreate(), canRead(), canWrite(), and canDelete()** functions of the server-side **GlideRecord** class, or the **canRead() and canWrite()** functions of the server-side **GlideElement** class. Use the **GlideRecord** functions to check ACLs at the table level and the **GlideElement** functions to check ACLs at the field level. These functions are straightforward — they return true if the user can perform the action and false if they cannot.
-   Use the **GlideRecordSecure** class. This class works the same way as **GlideRecord** except that it observes ACLs on the table it is reading from or writing to.

#### Test 2: Enforcing ACLs with **canWrite()**

1.  Confirm the condition on the UI Action is still:

  
current.state == 'requested'

1.  Change the script from:

current.state='approved';
current.update();

to:

if(current.state.canWrite()){
    current.state='approved';
    current.update();
}

1.  Save the changes to the UI Action, impersonate the ITIL user, and try to approve a request on table **sysapproval\_approver**.

The State field no longer changes from "Requested" to "Approved". The **canWrite()** function of the GlideElement class checks whether the ITIL user can pass the write ACLs on **sysapproval\_approver.state** before allowing any update. The user fails the ACL check and cannot change the State field.

#### Test 3: Enforcing ACLs with GlideRecordSecure

1.  Confirm the condition on the UI Action is still:

current.state == 'requested'

1.  Change the script from:

if(current.state.canWrite()){
    current.state='approved';
    current.update();
}

to:

var grs = GlideRecordSecure('sysapproval\_approver');
grs.get(current.sys\_id);
grs.state='approved';
grs.update();

1.  Save the changes to the UI Action, impersonate the ITIL user, and try to approve a request on table **sysapproval\_approver**.

The result is the same as Test 2 — the ITIL user cannot change the State field. The technique differs but the outcome is identical.

How client-side JavaScript handles ACL enforcement

Client-side JavaScript API functions always observe ACLs because there is no control over who runs them. Any technically proficient end user can open the JavaScript console in the browser and run any client-side JavaScript.

This can be demonstrated by changing the previous UI Action to run client-side JavaScript, using the client-side GlideRecord class to set the State field to "Approved" and update the record.

#### Test 4: Client-side JavaScript observes ACLs automatically

1.  Confirm the condition on the UI Action is still:

current.state == 'requested'

1.  Check the Client checkbox.
2.  Populate the Onclick field with:

approve()

1.  Change the script from:

var grs = GlideRecordSecure('sysapproval\_approver');
grs.get(current.sys\_id);
grs.state='approved';
grs.update();

to:

function approve(){
    var gr = new GlideRecord('sysapproval\_approver');
    gr.get(g\_form.getUniqueValue());
    gr.state = 'approved';
    gr.update();
}

1.  Save the changes to the UI Action, impersonate the ITIL user, and try to approve a request on table **sysapproval\_approver**.

No special effort is required to ensure ACLs are observed. The ServiceNow client-side JavaScript APIs always observe ACLs. Understanding these differences is key to resolving issues related to the ServiceNow JavaScript API.

### Related Links

[GlideRecord - Scoped](https://www.servicenow.com/docs/r/api-reference/server-api-reference/c_GlideRecordScopedAPI.html?section=SGR-addUserEncodedQuery_S "GlideRecord - Scoped")

[Using GlideRecordSecure](https://www.servicenow.com/undefined?section=c_UsingGlideRecordSecure "Using GlideRecordSecure")
