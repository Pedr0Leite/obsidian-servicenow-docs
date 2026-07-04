---
title: "Inserting hyperlinks: Methods and Tips"
aliases:
  - KB0529465
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0529465
kb_number: KB0529465
last_modified: 2024-09-30
---

## Inserting hyperlinks: Methods and Tips

  

### Overview

A hyperlink (or link) is a word, group of words, or image that you can click on to jump to another document. In addition to general elements such as paragraphs and lists, HTML documents can express hyperlinks. Hyperlinks allow users to navigate to other related web pages. This article illustrates how to create a hyperlink to another page or to an email address. Once you learn the format, you can make as many links as you want to any other page you want.

### Procedure

Use the **Insert/Modify Link** dialog window to create and edit hyperlinks that allow users to click through to web pages on the Internet, including other knowledge articles or the documentation site.

 **Note:** To ensure the hyperlink always opens the latest published version of the article, use the **Permalink** of the article. To copy the Permalink of the article, click "**Copy Permalink**" right under the title.  
Example of permalink: _**https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=<KB\_NUMBER>**_

To insert a hyperlink:

1.  In the text pane, select the text you want to use to create the hyperlink.
2.  In the toolbar, click the **Insert/Edit Link** icon.  
    ![Screenshot of the insert/edit link button](sys_attachment.do?sys_id=2090500a93b45218def533527cba10cf)  
    The Insert/Edit Link dialog window appears (see screenshot below).
3.  In the **URL** field, enter the full URL of the web page you want to open.
4.  The **Text to display** field defaults to the text selected to create the hyperlink and can be modified if necessary.
5.  In the **Open link in...** field, select one of the following choices:  
    
    -   **None (use implicit)** - Opens the linked document in the same space of the article.
    -   **New window (\_blank)** - Opens the linked document in a new window or tab. **\[Recommended\]**
    -   **Same frame (\_self)** - Opens the linked document in the same frame as it was clicked.
    -   **Top frame (\_top)** - Opens the linked document in the full body of the window.
    
    ![Insert/Modify Link window with the option to add a URL and Text, and select a Target from the choice list.](sys_attachment.do?sys_id=1090500a93b45218def533527cba10ca "Insert/Modify Link")
    
6.  Add a title if needed. This text will appear as a tooltip when hovering over the link.
7.  Click **Save**.   
    
     **Note:** Article links work only when the article is in _View_ mode. Links do not work when tested in the edit form.
    

### Email Links

Create links users can click to send an email to a specified address. Email links use the HTML `mailto` command.

To create an email link:

1.  In the Text pane, enter the text you want to use to create the email link.
2.  In the design toolbox, click the **Edit HTML Source** icon.
3.  The HTML Source Editor dialog window, search for the text you want to use to create the email link.
4.  Apply the following HTML code to the text using the email address to which you want the email to be sent.
    
    `<a href= "mailto:abc@example.com">Email Example</a>`
    
    **Note**:
    
     **Note**. By adding additional attributes, the subject and body of the email can be automatically populated. For more details, refer to [Create HTML Email](http://www.tizag.com/htmlT/email.php "Create HTML Email").
    
5.  Click **Update**. 
6.  Once the article content is complete, click the **View Article** link to view the final version of the article.
    
     **Important:** Article links work only when the article is in _View_ mode. Links will only in the edit form if you right-click and select "Open link in New Tab" (the name of the menu item may vary depending on the browser you use.
