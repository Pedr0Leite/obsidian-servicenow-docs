---
title: "Image-based links are not working on Welcome Banner (CD) in employee service center(esc)"
aliases:
  - KB0869020
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869020
kb_number: KB0869020
last_modified: 2023-12-19
---

## Issue

-   There is a requirement to use Welcome Banner (CD) widget instead of Carousel widgets. So same widget was used and users could place images on the page through the portal content. But links associated with the image is not working as the normal carousel tile works. Page and widget created under the content delivery scope only.  
    

## Resolution

1.  You can achieve this by making few changes to widget code .  
    See the screenshot below of changes that needs to be added to support the link based image.

![](sys_attachment.do?sys_id=1fa4f2511b7960100b8a9979b04bcbcf)

  
  
**html Template change** :  
_ng-click="navigateToImageBasedLink(bannerItem)"_  
  
_Client Script change :_  
_$scope.navigateToImageBasedLink = function(bItem){_  
_if (!bItem.use\_custom\_html && bItem.show\_button == "false" && bItem.url != ""){_  
_$window.open(bItem.url);_  
_}_  
_}_  
  

_Note :_ 

\- The support for Banner widget is Content Type "Banner" and styles content .  
  
\- The code workaround that we provided you was to just help you with an ability to use the banner widget if you wish to but we do not support it OOB.  
  
\- Also, we don't have currently image based link support fo carousel.
