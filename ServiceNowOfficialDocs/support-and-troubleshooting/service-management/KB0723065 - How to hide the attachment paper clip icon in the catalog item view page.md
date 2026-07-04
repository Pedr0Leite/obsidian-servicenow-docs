---
title: "How to hide the attachment paper clip icon in the catalog item view page?"
aliases:
  - KB0723065
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723065
kb_number: KB0723065
last_modified: 2026-05-15
---

## How to hide the attachment paper clip icon in the catalog item view page?

  

### Issue

 

Onload client script can be used to hide the attachment paper clip icon in the catalog item view page

### Release

London and below (at the time of this writing)

### Resolution

1\. Go to the catalog item Centralized Services  
2\. Under "Catalog Client script" Related list, click new  
3\. Give a name and select the type as "onLoad" and UI Type as "Desktop"  
4\. Paste the following code  
function onLoad() {  
//Type appropriate comment here, and begin script below  
document.getElementById("sc\_attachment\_button").hide();

}  
5\. save the record
