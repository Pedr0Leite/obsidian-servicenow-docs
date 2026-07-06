---
title: "Import set transform is throwing error \"Operation against file 'incident' was aborted by Business Rule 'Transform synchronously^XXXXXXXX'. Business Rule Stack:Transform synchronously\"
aliases:
  - KB0813377
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813377
kb_number: KB0813377
last_modified: 2025-08-20
---

## Import set transform is throwing error "Operation against file 'incident' was aborted by Business Rule 'Transform synchronously^XXXXXXXX'. Business Rule Stack:Transform synchronously"

  

### Issue

While using a SOAP web service to import , there is an error reported on Transform history and transform is shown as failed

Error : Operation against file 'incident' was aborted by Business Rule 'Transform synchronously^XXXXXXXX'. Business Rule Stack:Transform synchronously

### Release

All Release

### Cause

Enable the business rule debug property "glide.businessrule.callstack" and try to re-run the transform. This will show all the business rules associated in this process along with few exceptions

If you see the below error, follow the suggested solution

\======

SOAPProcessorThread27f267a5dbba0c54f45f927adb961975 6FF2E3A5DBBA0C54F45F927ADB961953 txid=6bf2a7a5dbba WARNING \*\*\* WARNING \*\*\* Attempt to get cipher for encryption context '' without authorization

SOAPProcessorThread27f267a5dbba0c54f45f927adb961975 6FF2E3A5DBBA0C54F45F927ADB961953 txid=6bf2a7a5dbba SEVERE \*\*\* ERROR \*\*\* Error while creating cipher for encryption context.

SOAPProcessorThread27f267a5dbba0c54f45f927adb961975 6FF2E3A5DBBA0C54F45F927ADB961953 txid=6bf2a7a5dbba SEVERE \*\*\* ERROR \*\*\* java.lang.NullPointerException

\======

### Resolution

Remove the fields from the Transform map which are associated under the "Encryption context" found in the Business Rule debug and re-run the transform. This should bypass the error leading to a successful transform.
