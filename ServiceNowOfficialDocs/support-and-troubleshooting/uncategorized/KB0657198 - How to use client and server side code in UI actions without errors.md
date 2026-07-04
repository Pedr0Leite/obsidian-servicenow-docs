---
title: "How to use client and server side code in UI actions without errors"
aliases:
  - KB0657198
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657198
kb_number: KB0657198
last_modified: 2023-12-26
---

## How to use client and server side code in UI actions without errors

  

### Issue

The purpose of this article is to describe how the client and server-side scripts work in a client-side UI Action. The interaction between the two is not the most intuitive thing and can lead to errors on a form if it is not handled correctly. The problem generally is that you will be using client-side APIs and server-side APIs as well as possibly referencing client-side and server-side objects all in the same script.

If it is not correct, the UI action will cause errors. Some symptoms of that may be a blank page loading after clicking the UI action, right-click context menu on the form failing to display, and possibly other unexpected results.

### Use functions

The key to getting this right is using functions to wrap your client and server-side code into separate closures. That way, if an API isn’t present at the time the script executes, it shouldn’t be a big deal as long as that function isn’t being called. When you click on a client-side UI action, the function specified in the Onclick field will be called.

![The Onclick field is populated with the function name doSubmit(), and the code for the function is defined in the Script field below it.](sys_attachment.do?sys_id=936ccd26975ff5908a073cbe2153af80)

This is where you should place any client-side code. In your Onclick function, you have access to the g\_form, g\_user, and any other client-side objects and APIs. You do not have access to server-side objects and APIs like current or gs methods here. In order to access server-side objects and APIs, you need another function and that needs to be called whenever the window object is not defined.

![The doServerStuff() function is defined in the Script field. The function contains a note: server side code goes here...](sys_attachment.do?sys_id=db6ccd26975ff5908a073cbe2153af7c)

Then, in your server-side function, you’ll have access to server-side objects and APIs like _current_, and the _gs_ methods but will **not** have access to client-side APIs like _g\_form_.

Note that if the UI Action runs both client-side and server-side code, the client side function must trigger the server-side function by calling **`gftSubmit()`** to trigger the UI Action again, this time running only the server-side code. Please refer to the documentation on [Create UI Action](https://docs.servicenow.com/bundle/paris-it-service-management/page/product/change-management/task/t_CreateNewUIAction.html "Create UI Action") for more information.

### Processing

When clicking the UI action the processing will look something like this:

1.  The Onclick function is called, which in this example is called **doSubmit**.  
    1.  The _window_ object is defined so nothing else should happen.  
          
        ![The window object is defined, so nothing else should happen, per the code on line 5 of the Script field.](sys_attachment.do?sys_id=9b6ccd26975ff5908a073cbe2153af84)  
          
        
2.  Once to the server, the UI action code executes a second time but this time, doSubmit is never called.  
    -   _window_ is not defined here so _doServerStuff_ is called.  
          
        
3.  _doServerStuff_ runs and does as intended.  
      
    ![The window object is not defined in this example, so doServerStuff is called and runs as intended.](sys_attachment.do?sys_id=976ccd26975ff5908a073cbe2153af82)

By using functions, you can control when certain parts of your code execute and avoid errors caused by an API or object being undefined.

### Addition Information

For additional troubleshooting tips, please see [KB0547282: How to troubleshoot UI Actions either or not showing or not working](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547282 "How to troubleshoot UI Actions either or not showing or not working")
