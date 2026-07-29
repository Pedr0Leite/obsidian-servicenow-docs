---
title: "How to bulk export attachments from a ServiceNow instance"
aliases:
  - KB0790002
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790002
kb_number: KB0790002
last_modified: 2026-02-10
---

## How to bulk export attachments from a ServiceNow instance

  

### Issue

Learn how to bulk export attachments from a ServiceNow instance using the REST Attachment API. The base system does not include a feature to directly download all attachments, but you can use the REST Attachment API with scripting to perform a bulk download.

### Release

All supported releases

### Cause

#### How attachments are stored

Attachments are stored in the Attachment \[sys\_attachment\] and Attachment Document \[sys\_attachment\_doc\] tables. Records are linked by the following relationships:

-   sys\_attachment.table\_sys\_id = sys\_id of the source record
-   sys\_attachment\_doc.sys\_attachment = sys\_id of the attachment record

### Resolution

#### Retrieve attachment metadata

Use the **Attachment - GET /now/attachment** REST Attachment API endpoint to retrieve the metadata for all Attachment \[sys\_attachment\] records on the instance. For details on this endpoint, see the Attachment API product documentation.

Example result:

  

{
  "result": \[
    {
      "size\_bytes": "106879",
      "file\_name": "4.3\_2\_modify-label-names.png",
      "sys\_mod\_count": "2",
      "average\_image\_color": "#ffffff",
      "image\_width": "800",
      "sys\_updated\_on": "2016-02-29 16:07:02",
      "sys\_tags": "",
      "table\_name": "sys\_product\_help",
      "sys\_id": "003a3ef24ff1120031577d2ca310c74b",
      "image\_height": "484",
      "sys\_updated\_by": "admin",
      "download\_link": "https://INSTANCENAME.service-now.com/api/now/attachment/003a3ef24ff1120031577d2ca310c74b/file",
      "content\_type": "image/png",
      "sys\_created\_on": "2016-02-29 16:07:02",
      "size\_compressed": "105563",
      "compressed": "true",
      "state": "",
      "table\_sys\_id": "750129c94f12020031577d2ca310c7a4",
      "chunk\_size\_bytes": "",
      "hash": "",
      "sys\_created\_by": "admin"
    }
  \]
}  
  
  

#### Extract download links

Parse the JSON response to extract the download links. The following example uses the jq program in a bash shell (Linux, macOS, or Windows WSL) to process a JSON file with 10 results from the Attachment - GET /now/attachment endpoint:

jq '.result\[\].download\_link' jsonfile\_10results  
"https://INSTANCENAME.service-now.com/api/now/attachment/003a3ef24ff1120031577d2ca310c74b/file"  
"https://INSTANCENAME..service-now.com/api/now/attachment/009c53e0bf1101007a6d257b3f0739c0/file"  
"https://INSTANCENAME..service-now.com/api/now/attachment/00e7525ddf710100a9e78b6c3df2639c/file"  
"https://INSTANCENAME..service-now.com/api/now/attachment/011049ba5f130100a9ad2572f2b4775d/file"  
"https://INSTANCENAME..service-now.com/api/now/attachment/011e08b5c311220071d07bfaa2d3ae2e/file"  
"https://INSTANCENAME..service-now.com/api/now/attachment/01b07a11dfb10100a9e78b6c3df26342/file"  
"https://INSTANCENAME..service-now.com/api/now/attachment/01e533a4bf1101007a6d257b3f0739a7/file"  
"https://INSTANCENAME..service-now.com/api/now/attachment/023b3dc0d7613100a9ad1e173e24d460/file"  
"https://INSTANCENAME..service-now.com/api/now/attachment/029382a947830100e43987e8dee49021/file"  
"https://INSTANCENAME..service-now.com/api/now/attachment/02c7308f40a97200964f0edb17b6d9d0/file"

#### Download the attachments

Script the download of attachments. The following example uses curl in a bash shell:

jq '.result\[\].download\_link' jsonfile\_10results > urls\_to\_download.txt

xargs curl -v < urls\_to\_download.txt

**Important**: ServiceNow Support does not provide assistance with custom scripting. The preceding examples are provided as a general guideline and can be accomplished in many ways, for example, using Python instead of a bash shell.

### Related Links

[How to export bulk data from ServiceNow using REST API pagination](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727636)

[Attachment API](https://docs.servicenow.com/csh?topicname=c_AttachmentAPI.html&version=latest)

## Related

- [[KB0727636 - How to export bulk data from ServiceNow using REST API pagination]] - companion table-data export procedure
