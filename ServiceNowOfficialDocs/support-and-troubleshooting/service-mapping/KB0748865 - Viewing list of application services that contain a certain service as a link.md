---
title: "Viewing list of application services that contain a certain service as a link"
aliases:
  - KB0748865
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748865
kb_number: KB0748865
last_modified: 2024-04-07
---

## Issue

As a Service Mapping administrator, you may split large maps into segments to manage them effectively. When you transfer a map segment into another application service, you create a link between the original application service and the application service into which you planted the map segment. The connection to the top CI in the segment becomes an entry point when you transfer it into another, existing or new, application service.

You can easily navigate into the transferred map segment by clicking its icon in the map.

![](sys_attachment.do?sys_id=52eb68eadb42b450e515c22305961971)

However, if you are looking at the map of the transferred segment, you cannot return to the map of the original service from which this segment was removed. Service maps contain no indication of transferred services being linked to their original services. You may need to know if a service is a part of another, larger service when dealing with changes or incidents.

Such information may be required when a change or incident on a CI leads to some service, but this service is part of a larger one.

Use the attached updateset to add the ability to view the list of all application services that contain a certain service as a link. 

After you import the updateset attached to this article, the Parent Services link appears under Related Links on the Service form.

![](sys_attachment.do?sys_id=6aeb68eadb42b450e515c223059619e6)

Clicking the **Parent Services** link displays the list of services that contain the link to this service.

![](sys_attachment.do?sys_id=62eb68eadb42b450e515c223059619ec)

Use the standard import updateset functionality to import this file.

 For more information about transferring map segments into another application services, see refer to the [Service Mapping documentation](https://docs.servicenow.com/csh?topicname=add-segment-to-business-service-map.html&version=latest).
