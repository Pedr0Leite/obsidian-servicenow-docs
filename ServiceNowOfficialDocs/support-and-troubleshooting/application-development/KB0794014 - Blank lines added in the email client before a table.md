---
title: "Blank lines added in the email client before a table"
aliases:
  - KB0794014
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794014
kb_number: KB0794014
last_modified: 2024-04-08
---

## Blank lines added in the email client before a table

  

### Issue

When a <table> HTML tag is used in an email client template, multiple blank lines are unexpectedly added before the table element in the email client even though no line breaks exist in the email client template. For example:

![](/sys_attachment.do?sys_id=78426c89db0cb4d04cfbeeb5ca9619d7)

In the email client popup window, if you click the Source Code button from the Tiny MCE editor menu, you'll see multiple line break tags <br /> added to the HTML before any <table> tag:

<p><br /><br /><br /><br /><br /><br /></p>  
<table>

### Release

All releases.

### Cause

The system property glide.ui.escape\_text is set to false. The default and recommended value for this property is true. See [High Security Settings](https://docs.servicenow.com/csh?topicname=c_HighSecuritySettings.html&version=latest "High Security Settings")

### Resolution

As a user with the admin role:  
1\. Elevate to the security\_admin role.  
2\. In the Navigator field, enter sys\_properties.list  
3\. Find and open the record for glide.ui.escape\_text  
4\. On the form change the Value from false to true.  
5\. Save or Update.

After these steps, the unexpected break lines should no longer appear in the email client before any <table> tags.
