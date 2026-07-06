---
title: "HTML Editor - Allow all content to be saved"
aliases:
  - KB0713612
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713612
kb_number: KB0713612
last_modified: 2025-01-03
---

## Issue

# Description

* * *

Often times, you will paste content into the source code within an HTML Editor (TinyMCE). However, when you close the source code dialog window and open it again, you'll notice that some of the content added was removed. Adding it again will not resolve the issue; The code will not persist. This is due to the TinyMCE editor beign configured to remove any markup it does not recognize/allow by default. You will need to add some attributes to the field in order to change this behavior.

# Procedure

* * *

1\. Open the sys\_dictionary record for the HTML field you want to modify (I'll be using the 'Text' field for KB Articles)

2\. Switch the form to 'Advanced' view.

3\. In the Attributes field, add these two attributes separated by a comma (do not remove the attributes already in there unless you know what they're for and do not wish to keep them):

-   html\_sanitize=false
-   tinymce\_allow\_all=true

![](/sys_attachment.do?sys_id=944f3c26db0ab450e515c22305961943)

 4. Save the record. You should now be able to save any content into the HTML editor field modified.

# Applicable Versions

* * *

All

# Additional Information

* * *

What do these two attributes do?

\- html\_santize controls whether or not the content that is sent to the server for this field is sanitized by the HTMLSanitizerConfig script include. You can find more information on this process here: [https://docs.servicenow.com/csh?topicname=c\_HTMLSanitizer.html&version=latest](https://docs.servicenow.com/csh?topicname=c_HTMLSanitizer.html&version=latest)

\- tinymce\_allow\_all is used to change the client-side behavior for an HTML editor field. By default, the editor will remove the majority of content added if it is not valid HTML (and even then it is still fairly strict with what is kept). You can change this to where all content added to the field is kept by adding this attribute and setting it to true.

-   Note: the tinymce\_allow\_all attribute is not documented by ServiceNow. In the event the attribute no longer works, ServiceNow Support cannot assist in the matter as undocumented features are out of scope.

You can find out more about Dictionary Attributes on our documentation here: [https://docs.servicenow.com/csh?topicname=c\_DictionaryAttributes.html&version=latest](https://docs.servicenow.com/csh?topicname=c_DictionaryAttributes.html&version=latest)
