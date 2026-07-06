---
title: "How emails with duplicate Message ID's are handled in ServiceNow"
aliases:
  - KB0816001
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0816001
kb_number: KB0816001
last_modified: 2026-03-23
---

## How emails with duplicate Message ID's are handled in ServiceNow

  

### Summary

Some customer email systems can send SN instances multiple emails with the same Message-ID. By default the instance will save the first email into the \[sys\_email\] table, and then silently drop any subsequent ones with the same Message ID.

In order to see the emails with duplicate Message ID's that are being dropped, ensure the system property **glide.email.debug** is set to type _true|false_ and value **_true_**.

Emails that are dropped due to being duplicates will be logged as, for example:

2020-01-22 10:07:06 (056) worker.5 worker.5 txid=12f345bc1ba6 Message UID='00123f4e56789745' Message-ID='<AJGHEYTISMBTHAYAAAAAAAAAMEul/ioeqdYUIO1jyq7tY3CgAAAEAAAAICPx8Ch0U1Bu2IX+wLq2D0BBBBB==@example.com>' was previously read and will be ignored.

On more recent ServiceNow releases, the log message might look like:

2023-02-20 04:23:21 (041) worker.2 worker.2 txid=203c7c30dgds Message UID='01475aef57822l4p' Message-ID='<AJGHEYTISMBTHAYAAAAAAAAAMEul/ioeqdYUIO1jyq7tY3CgAAAEAAAAICPx8Ch0U1Bu2IX+wLq2D0BBBBB==@example.com>' was previously read (sys\_id of email='684cbc30dbcd29d051f961bb139665b3') and will be ignored 

### Release

All current ServiceNow versions

### Instructions

The default behaviour can be changed by setting the system property **glide.email.allow\_duplicate\_message\_ids** (of type _true|false_) to the value **_true_**.

This change has implications, in particular that matching of reply emails based on the In-Reply-To header will pick up a random email from the duplicates.

After this change has been applied the emails with duplicate Message IDs will be stored on Email\[sys\_email\] as normal. However note that when searching on the Email\[sys\_email\] table for emails with duplicate Message ID you must search by Type (e.g Received) and Message ID, otherwise the system will not be using the out-of-box index on _type,message-id_.

### Related Links

The ServiceNow platform by default assumes that Message IDs are unique. Ref. _3.6.4. Identification Fields_ in relevant specification [https://tools.ietf.org/html/rfc5322#section-3.6.4](https://tools.ietf.org/html/rfc5322#section-3.6.4) _:_

_Though listed as optional in the table in section 3.6, every message_

_SHOULD have a "Message-ID:" field. Furthermore, reply messages_

_SHOULD have "In-Reply-To:" and "References:" fields as appropriate_

_and as described below._

_The "Message-ID:" field contains a single unique message identifier._
