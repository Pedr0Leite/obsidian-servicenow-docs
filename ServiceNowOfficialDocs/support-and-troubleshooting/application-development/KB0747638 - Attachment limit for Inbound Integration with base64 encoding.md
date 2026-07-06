---
title: "Attachment limit for Inbound Integration with base64 encoding"
aliases:
  - KB0747638
  - Attachment limit for Inbound Integration with base64 encoding
tags:
  - servicenow
  - support-kb
  - rest-api
  - attachments
  - integration
  - base64
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0747638
kb_number: KB0747638
last_modified: 2025-05-08
---

## Attachment limit for Inbound Integration with base64 encoding

  

### Issue

REST API returns an error similar to the following:

Response: {"error":{"message":"Exception while reading request","detail":"Rejected large REST payload with content-length = 15105102 bytes. Max allowed: 10485760 bytes."},"status":"failure"

Localhost logs will also indicate messages similar to the following in the stack trace.

Caused by: com.glide.rest.domain.UserException: Rejected large REST payload with content-length = 13012943 bytes. Max allowed: 10485760 bytes.

### Cause

This seems to depend on the `glide.rest.max_content_length` property which is defaulted at 10MB, min is 1MB, max is 25MB on the target instance.

The size includes the size of the attachment after the value is base64 encoded.

### Resolution

Users must ensure that the size of the attachment including the encoding is within the value specified in this property. If this property is not present on the instance, it can be created as - 

1.  In filter navigator, type **sys\_properties.list** to open the properties table
2.  Click on **New**
3.  In the **Name** field - Enter `glide.rest.max_content_length`
4.  In the type select `Integer`
5.  In **Value** enter **`25`**, if you want to set the max value. This value is in MB.

There are two other properties mentioned on the product documentation page, please refer to the following page for additional reference: [Controlling Max Request Size](https://docs.servicenow.com/csh?topicname=r_ControllingMaxRequestSize.html&version=latest)

### Related Links

As mentioned in the following reference article, when the text of size 'n' is base encoded its size will increase by ceil(n / 3) \* 4, [Base64: What is the worst possible increase in space usage?](https://stackoverflow.com/questions/4715415/base64-what-is-the-worst-possible-increase-in-space-usage "Base64: What is the worst possible increase in space usage?") \[Stackoverflow\].

By a rough approximation, the size of data would be increased to 4/3 of the original.

## Related

- [[KB0748767 - Rest API Explorer is escaping the special characters like single quote in the xml payload content.]]
- [[r_ControllingMaxRequestSize|Controlling Max Request Size]]
- [[KB0718496 - Outbound REST Webservice call with a large JSON Payload in the response body is not processed by the instance]]
