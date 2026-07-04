---
title: "Issue when using REST to submit to string field"
aliases:
  - KB0549983
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549983
kb_number: KB0549983
last_modified: 2024-04-26
---

## Issue when using REST to submit to string field

  

### Issue

Issue when using REST to submit to multi line text field | Optional

  
  

# Details

* * *

Using a carriage return in a string field, such as description field when submitting a REST message it returns an "Invalid Request" response. 

This is experienced if using a REST message to insert or update a field of type string, having a the contents separated by a carriage return.

To avoid the "Invalid Request" response, substitute the carriage return with a "\\n" in the REST message.

# Symptom

* * *

Getting "Bad Request" when using REST message to insert or update a table in ServiceNow and the error message is:

{  
error: {  
message: "Exception while reading request"  
detail: "Verify Request body and Content-type headers. Not able to parse request"  
}-  
status: "failure"  
}

 

# Cause

* * *

 Using the carriage return breaks the message and results in that the text message is not terminated correctly

# Solution

* * *

The text submitted in the REST message must be correctly terminated.

Use a "\\n" in place of the actual carriage return. 

Example:

Bad Request will contain the following:

{"short\_description":"SN-REST Test", "description":"This is a line with  
a second line"}

When processed the following response is received:

![](/sys_attachment.do?sys_id=dc3dec62db82b450e515c223059619ed)

Please refer to "REST Message Bad Request response.png" attached

![](/sys_attachment.do?sys_id=d83dec62db82b450e515c223059619fd)

**Successful request will contain the following:**

{"short\_description":"SN-REST Test", "description":"This is a line with \\n a second line"}

 

The response will contain the details of the created record

Please refer to "REST Message - Successful.png" attached.![](/sys_attachment.do?sys_id=6c3d20a2db82b450e515c22305961988)
