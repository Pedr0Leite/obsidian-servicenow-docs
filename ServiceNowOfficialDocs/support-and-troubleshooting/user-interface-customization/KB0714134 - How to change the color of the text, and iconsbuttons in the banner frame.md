---
title: "How to change the color of the text, and icons/buttons in the banner frame?"
aliases:
  - KB0714134
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714134
kb_number: KB0714134
last_modified: 2025-01-03
---

## How to change the color of the text, and icons/buttons in the banner frame?

  

### Issue

  
  

# Description

* * *

How to change the color of the text, and icons/buttons in the banner frame?

![](/sys_attachment.do?sys_id=c00d6c22db82b450e515c223059619d2)

Procedure

* * *

In Jakarta, there is not a supported way to change that color as you want. However, a user can try the following:

1- Go to System UI > Themes.

2- Select an existing theme such as Black and White (or click the button New to create a new theme)

3- Add the code below into the field CSS:

$navpage-header-button-color: addacolorhere       

4- Save the record.

5- Witch your instance to the theme Black and White (or to the new theme created).

6- The color may be applied to the text and buttons/icons from the banner frame. 

Applicable Versions

* * *

Jakarta, Kingston, London

# Additional Information

* * *

Check out this doc about [Customizing instance appearance](https://docs.servicenow.com/csh?topicname=customizing-instance-appearance.html&version=latest "Customizing instance appearance")
