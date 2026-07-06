---
title: "Using a business rule to copy attachments from one record to another upon creation"
aliases:
  - KB0717827
tags:
  - servicenow
  - support-kb
  - business-rules
  - GlideSysAttachment
  - attachments
  - scripting
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0717827
kb_number: KB0717827
last_modified: 2026-02-20
---

## Issue

Copying attachments from a record from one table, to another record on another table with the use of a business rule upon creation.

The use of the system method GlideSysAttachment.copy seems straightforward most of the time, and it is. A simple structure of this would be:

GlideSysAttachment.copy('source\_table', 'Source\_record\_sys\_id', 'target\_table', 'target\_record\_sys\_id');

However, an issue occurs when you're trying to do this on an **Insert** business rule that is creating a **transferred to** (A child reference record) record from the primary record that the attachment is attached to. As you're able to see, the use of this is clear and understandable, you'd simply just want to run this within a business rule to copy the attachment across.

### Symptoms

1.  Firstly, an email is sent into an instance, which contains the correct conditions to create a call that has the call type set to 'incident'. (Done via an **onBefore** business rule)
2.  During this process, another business rule is triggered (**onBefore**) of which checks the record type and does the corresponding actions, in this case, creates an incident (the call type is set to 'incident' via step 1)
3.  This business rule creates the incident (the incident is being created from the call)
4.  The business rule also contains the _GlideSysAttachment.copy_ - of which here it copies the attachment from the call of which was sent in via the email.
5.  The call is then created.
6.  A field on the call, for example, 'transferred\_to' then links the incident to the call.

## Resolution

You can hardcode the sys\_id's of both the primary record and the transferred to record into the method (The primary and transferred to records of which has already previously been made, no attachments copied onto the transferred to record yet) and place this into the business rule to run.

Use and populate this test line:

GlideSysAttachment.copy('example\_table\_1', 'record\_sys\_id\_123456789abcdef', 'example\_table\_2', 'record\_sys\_id\_123456789fedcba'); 

You will be able to see how this works correctly and the attachment is copied across, this is because, in this scenario, there is already a primary record created for the attachment to have been attached to and then copied to the incident.

## Additional Information

<table class="noteTable"><tbody><tr><td class="c3"><img class="c2" title="Warning" src="/Warning_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Warning</strong>: Please fully test it on your development instance before making changes to the production instances.</td></tr></tbody></table>

## Related

- [[KB0696085 - Attachments in emails, filenames greater than 60 characters, are renamed to ATT.dat in Lotus Notes]]
- [[KB0718655 - Scripted (incorrect) query is unexpectedly returning all records]]
- [[c_GlideSysAttachmentScopedAPI]]
