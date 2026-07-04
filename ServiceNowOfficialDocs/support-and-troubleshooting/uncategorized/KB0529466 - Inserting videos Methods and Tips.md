---
title: "Inserting videos: Methods and Tips"
aliases:
  - KB0529466
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0529466
kb_number: KB0529466
last_modified: 2024-09-30
---

## Inserting videos: Methods and Tips

  

## Overview

You can add media elements, like videos, to knowledge articles. However, due to how the platform stores and manages attachments (see: [Administering Attachments](https://docs.servicenow.com/csh?topicname=r_AdministeringAttachments.html&version=latest "Administering Attachments")), it's **not recommended** to use the embedded content editor (the icon) to attach video files to an article. Instead, it's encouraged to embed videos from a streaming service, such as YouTube, Vimeo, etc. 

## Procedure

To embed a video in a knowledge article:

1.  In the Text pane, select the space where you want to the video to display.
2.  Obtain the embedded HTML code from the site where the video is hosted. This will vary depending on the website; search for a way to "**Share**" the video, and choose the "**Embed**" option; this should provide HTML code with <iframe> tags.
3.  Go back to your article and, in the toolbar, open the **Source Code** view of your article with the   button.
4.  Paste the HTML code you obtained in step 2 and click OK to save your edits, you should see the video in the text pane:
    -   -   Example from YouTube:
            
        -   Example from Vimeo:
            
5.  Be aware that the embedded editor may remove some of the source code when saving the article. This will depend on how HI is set up to filter accepted HTML.
