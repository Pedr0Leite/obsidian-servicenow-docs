---
title: "How to force download an attachment instead of showing the preview"
aliases:
  - KB0785245
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0785245
kb_number: KB0785245
last_modified: 2025-01-02
---

## How to force download an attachment instead of showing the preview

  

### Issue

Usually, if there are huge attachments (of size more than 25MB) on any knowledge records, they get opened up in a new tab and a preview is shown.

This generally happens if you have a video (.mp4 or .mov) type attachment on any KB articles. These huge attachments will be shown as a preview in a new tab when the user clicks on them. There is a possibility that the attachments (.mp4 or .mov) will take a lot of time to load while showing the preview. Also, user cannot perform/carry out other transactions while the video preview is loaded.

### Release

All Releases

### Resolution

This behavior of showing video preview can be avoided. There are two system properties which control the way attachments are previewed/downloaded in the ServiceNow platform:  
  
1) '**glide.ui.attachment.force\_download\_all\_mime\_types**' and set the value to true.  
This will cause the attachments to download when the user clicks on them (preview will be disabled)  
\[OR\]  
2) '**glide.ui.attachment.download\_mime\_types**' to force download only mp4/mov video type attachments instead of showing a preview  
Add "video/mp4" \[or\] "video/mov" according to the video types you want the user to force download.  
  
In either of the above methods, when the user clicks on a video attachment on the KB article in the service portal, the attachment will get downloaded to the user's local machine.  
This way we can avoid the preview video loading time issue. (Also, please be noted that until the file attachment gets downloaded completely on users local machine, user cannot navigate through other ServiceNow pages, which is a platform behavior)

Example: '**glide.ui.attachment.force\_download\_all\_mime\_types**' value is set to true.

![When sys property Force download all is true](/sys_attachment.do?sys_id=6b57856293f6da90f538fb2d6cba10f5 "Only able to download attachment")

Example: '**glide.ui.attachment.force\_download\_all\_mime\_types**' value is set to false.

![When sys property download all attachments is false](/sys_attachment.do?sys_id=b097cda293f6da90f538fb2d6cba10c7 "Able to view PDF attachment")

### Related Links

[Force Download MIME types (instance security hardening)](https://www.servicenow.com/docs/csh?topicname=force-download-mime-types.html&version=latest "Force Download MIME types (instance security hardening)")

Note: If you set the Force Download MIME Types property to true, it overrides the Downloadable MIME types property, which is a comma-delimited listing of downloadable MIME types. To learn more, see [Force download MIME types](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/security/reference/force-download-mime-types.html "Use the glide.ui.attachment.force_download_all_mime_types property to force the download of all MIME type attachments.").

[Downloadable MIME types (instance security hardening)](https://www.servicenow.com/docs/csh?topicname=download-mime-types.html&version=latest "Downloadable MIME types (instance security hardening)")
