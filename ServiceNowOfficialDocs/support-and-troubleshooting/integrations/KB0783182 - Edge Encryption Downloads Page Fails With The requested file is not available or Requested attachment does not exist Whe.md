---
title: "Edge Encryption Downloads Page Fails With \"The requested file is not available\" or \"Requested attachment does not exist\" When Selecting \"Download Interactive Installer\" or \"Download the command line installer\"
aliases:
  - KB0783182
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783182
kb_number: KB0783182
last_modified: 2024-04-07
---

## Issue

In the UI you go to the Edge Encryption Configuration -> Installation & Downloads -> Downloads page

It may appear completely normal like in this:

![](/sys_attachment.do?sys_id=6382d370db4030905a959c41ba961976)

But when selecting either the "Download Interactive Installer" or "Download the command line installer" it fails with "Requested attachment does not exist":

![](/sys_attachment.do?sys_id=eb82d370db4030905a959c41ba961974)

Or when going to Downloads you may see this "The requested file is not available" and there are no options to select the "Download Interactive Installer" or "Download the command line installer":

![](/sys_attachment.do?sys_id=6b82d370db4030905a959c41ba961970)

## Resolution

To resolve this issue do the following for cause 1:

(1) Create a new delete ACL on sys\_attachment with Admin overrides off and Requires role security\_admin and Condition File name starts with edgeencryption- as in this screen shot:

![](/sys_attachment.do?sys_id=ef82d370db4030905a959c41ba961971)

(2) Go to sys\_attachment.list as a security admin roled user with Elevated Roles active

(a) Filter on:

File name starts with edgeencryption- you will see a lot of these download files listed as in this screen shot:

![](/sys_attachment.do?sys_id=e782d370db4030905a959c41ba961977)

There may be multiple versions of files as well, in the example above there are only files for Madrid Patch 7a, but other version and releases may also exist here in the listing.

(b) Find the current version that the instance is on, these will be the only download files you need, all of the others can be deleted, say the instance is on Madrid Patch 7a, you will only need to keep one copy of these two files:

edgeencryption-madrid-12-18-2018\_\_patch7a-10-01-2019\_10-03-2019\_1530-all.jar  
edgeencryption-madrid-12-18-2018\_\_patch7a-10-01-2019\_10-03-2019\_1530-installer.jar

Proceed to delete all of the other copies of the two files above any any other files that are on earlier releases.

After this you should be able to go to the Downloads page and download both "Download Interactive Installer" and "Download the command line installer" without issue.

To resolve this issue do the following for cause 2:

Go to the page System Properties -> Security - then the property:

"List of file extensions (comma-separated) that can be attached to documents via the attachment dialog. Extensions should not include the dot (.) e.g. xls,xlsx,doc,docx. Leave blank to allow all extensions."

Add jar to the list of allowed extensions, e.g.:

xls,xlsx,doc,docx,pdf,ppt,pptx,xml,png,jpg,zip,mpp,sql,txt,ini,dll,bmp,ps,csv,dtd,xsd,cer,der,ps1,msg,pem,jar
