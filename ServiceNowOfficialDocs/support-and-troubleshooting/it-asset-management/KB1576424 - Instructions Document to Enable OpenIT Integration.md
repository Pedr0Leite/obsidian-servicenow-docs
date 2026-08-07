---
title: "Instructions Document to Enable OpenIT Integration"
aliases:
  - KB1576424
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1576424
kb_number: KB1576424
last_modified: 2026-06-30
---

## Text

1.0 Introduction

The update set provided is part of the Engineering Applications publisher pack that is part of the Software Asset Management product. Customers who are currently on Utah or Vancouver will have to install this update set before integrating with a ServiceNow partner OpenIT. This step is a pre- requisite before the OpenIT store app is integrated with Servicenow.

2.0 Installing the update sets

Verify if you are currently on Utah or Vancouver release of Software Asset Management. To install this update, you will need **sys\_admin** privileges.

2.1  The update sets

1.  Role required: sys\_admin
2.  The zip file (check update\_set\_for\_openit\_integration.zip in attachments) provided to you contains two folders ‘Utah’ & ‘Vancouver’ that contain the update sets for the respective releases.
3.  Use the correct update sets based on release version you are currently on.
4.  Each folder contains three update sets.

2.2  Importing the update sets  
**Note**: First Preview & Commit the update set where Application is ‘Global’ (as in image below). The other two update sets can be committed in any order.  
  
![](/sys_attachment.do?sys_id=ebc26dcf97aab510539e35d11153af93)

The update set is provided to you as an XML file. Follow the steps below to import these into your instance:

1.   Navigate to System Update Sets > Retrieved Update Sets.
2.   Click the ‘Import Update Set from XML’ link (see image below)
3.   Click Choose File and select the xml file. Click Upload.

![](/sys_attachment.do?sys_id=cea3ed4397eab510539e35d11153af56)

Repeat above three steps for all three files. Once Upload is done you will see update sets similar to below image.

![](/sys_attachment.do?sys_id=ebc26dcf97aab510539e35d11153af93)

Open each update set record now. Use the UI action ‘Preview’ to preview each update set. Fix any problems that are reported before you commit the update set.
