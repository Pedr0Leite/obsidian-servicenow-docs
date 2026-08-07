---
title: "How to fix unexpected HTML display in email preview tools"
aliases:
  - KB0743622
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743622
kb_number: KB0743622
last_modified: 2025-10-28
---

## How to fix unexpected HTML display in email preview tools

  

### Issue

When you use ServiceNow email preview tools, like Preview HTML Body or Notification Preview, HTML may display incorrectly with unexpected fonts or formatting, while the same content appears normal in email clients and activity streams. 

### Release

All supported releases

### Cause

The ServiceNow platform sanitizes HTML when you use the Preview HTML Body and Notification Preview email functions.

This occurs when your HTML is invalid, even though browsers and email clients might allow invalid HTML. You have full control over HTML, so no sanitization happens when emails are sent or displayed in the activity stream of records.

The sanitization process corrects invalid HTML, which can make it appear incorrect when displayed in preview tools.

### Resolution

To see the difference between sanitized and unsanitized HTML, run a script to output the sanitized version of an email record from **Scripts** - **Background**: 

var gr1 = new GlideRecord('sys\_email');   
gr1.get('<email sys\_id>');   
gs.print(SNC.GlideHTMLSanitizer.sanitize(gr1.body));

You can save the output to an .html file and view it in a browser. This applies to any custom HTML in email notifications, email templates, or email scripts.

For example, this email script uses the deprecated font tag:

(function runMailScript(current, template, email, email\_action, event) {  
template.print("<font size='2' face='tahoma,arial,helvetica,sans-serif'>");  
})(current, template, email, email\_action, event);

The font tag is deprecated. Use CSS to style fonts instead.

This is just one example of invalid HTML. Check that your HTML is valid and conforms to HTML specifications.

### Related Links

[How to strip formatting from text pasted in the Message HTML field of an email notification record](https://support.servicenow.com/kb_view.do?sysparm_article=KB0686053 "How to strip formatting from text pasted in the Message HTML field of an email notification record")

[Email notification shows HTML tags and markup in sent email](https://support.servicenow.com/kb_view.do?sysparm_article=KB0727884 "Email notification shows HTML tags and markup in sent email")
