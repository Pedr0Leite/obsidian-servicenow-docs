---
title: "[SAMP - Content Service] How to keep track of the SAMP Content Service related changes"
aliases:
  - KB0745493
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745493
kb_number: KB0745493
last_modified: 2024-04-07
---

## \[SAMP - Content Service\] How to keep track of the SAMP Content Service related changes

  

### Issue

# Symptoms

The SAMP content service can be configured (opt-in or opt-out of the content service) by using the [Content Service Setup](https://docs.servicenow.com/csh?topicname=t_EnableSAMContentService.html&version=latest "Content Service Setup"). If more than one admins/samp\_admins working on it sometimes we may want to keep track of the changes on all these configurations. This article provoides details how we can achieve this.

![](/sys_attachment.do?sys_id=23db64eadb42b450e515c22305961950)

# Release

Jakarta or later.

# Environment

All environments.

# Where are these configurations

Using the configuration page we enable or disable different levels of opt-ins for content service. Below are the two main files that are responsible for this set-up.

_**UI Page**_: [content\_service\_setup](https://instance_name.service-now.com/nav_to.do?uri=sys_ui_page.do?sys_id=af0cc777c37432002757dccdf3d3ae8b "content_service_setup") (Replace instance\_name with your instance name)

_**Script Include**_: [ContentServiceOptUtil](https://instance_name.service-now.com/nav_to.do?uri=sys_script_include.do?sys_id=9a53e6aac3b032002757dccdf3d3ae00 "ContentServiceOptUtil") (Replace instance\_name with your instance name)

_**Table**_: samp\_configuration

# Resolution

[Enable auditing](https://docs.servicenow.com/csh?topicname=t_EnableAuditingForATable.html&version=latest "Enable auditing for the above table") for the above table for this table and it should take care of enabling the track of all changes.

# Additional Information

[Content Service Setup](https://docs.servicenow.com/csh?topicname=t_EnableSAMContentService.html&version=latest "Content Service Setup")
