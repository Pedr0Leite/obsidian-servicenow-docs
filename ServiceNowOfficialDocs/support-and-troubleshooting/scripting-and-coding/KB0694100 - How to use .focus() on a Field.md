---
title: "How to use .focus() on a Field"
aliases:
  - KB0694100
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694100
kb_number: KB0694100
last_modified: 2025-01-16
---

## How to use .focus() on a Field

  

### Issue

A common request from ServiceNow users is how to set the focus on a field. If you don't know what this is, bringing focus to a field refers to making said field active which will normally cause a web page to scroll the underlying HTML element into view for the user.

This action is desired in many situations, though it is mainly requested when a user attempts to submit a form with missing information. The field is set to mandatory and the focus is set to the field which the user will see and finish filling out the form.

### Resolution

**DISCLAIMER**: The following procedure uses functions that are not provided by ServiceNow. As such, they are out of ServiceNow Support's scope. Should the functionality provided by these functions cause issues or stop working, it is the implementer's responsibility to correct the issues.

* * *

Documentation for the .focus() method states it "is used to give focus to an element (if it can be focused)". This means the method can only be used on HTML elements, and not all elements support the function: [https://www.w3schools.com/jsref/met\_html\_focus.asp](https://www.w3schools.com/jsref/met_html_focus.asp)

With that in mind, we first need to get the HTML element for the field on the form we want to use the .focus() method on. ServiceNow's client-side "GlideForm" API provides a few functions that can do this, like getControl() and getElement(). You can find links to the documentation for GlideForm below in the Additional Information section.

Choose one of the two methods and you can now pair it with the .focus() function.

![](/sys_attachment.do?sys_id=ea934232db01099007ab826305961987)

There may be times when the .focus() function may appear to not work (i.e. the field is not brought into the user's view).

This is most likely due to the element already being active. What the .focus() function does is it sets the provided element as the 'active' element on the form, which will then cause the web page to scroll that element into view. However, if you try to use .focus() on an element that is already active, expected JavaScript behavior is to ignore the request as you cannot set an element active when it already is.

You can test this out from your browser's console. Open an Incident form and then open the console:

1\. In the console, use "var element = g\_form.getControl('short\_description').focus();". You should see the form scroll the Short Description field into view (if it is not already).

2\. Now enter "element;" into the console and you should see an HTML element for Short Description as the output. 

3\. Now enter "document.activeElement;" into the console and you should see the same HTML element as the output.

4\. Without clicking anything on the form, scroll the page until the Short Description field is out of view.

5\. Enter "element.focus();" into the console and you will notice that the form does not move.

This behavior can lead many developers to believe that the focus() function does not work, when in fact it is.

If you find that setting the focus to a field is not behaving as you require, there is an alternative way to scroll the form and bring a field into view for the user. JavaScript contains another function called .scrollIntoView()

[https://www.w3schools.com/jsref/met\_element\_scrollintoview.asp](https://www.w3schools.com/jsref/met_element_scrollintoview.asp)

The description for this function reads "scrolls the specified element into the visible area of the browser window". This function does not take into consideration if an element is already active.

![](/sys_attachment.do?sys_id=ae934232db01099007ab82630596195d)

One Last Thing...

* * *

If you are trying to implement this type of functionality on a form to call attention to a mandatory field when a form is submitted, you may notice that neither .focus() or .scrollIntoView() work. One possible reason for this may be due to a banner message being added to the form that is informing the user of the mandatory fields:

![](/sys_attachment.do?sys_id=22934232db01099007ab826305961986)

This message is added to the form using GlideForm's 'addErrorMessage()' function. It just so happens that using this function will set the form focus to the newly created message, which can explain why it may appear that the focus is not being set to the field you specify. The focus IS being set to the field, but due to the error message being added AFTER, the focus shift to the new message. So the focus is being set correctly, it just changes really fast!

### Related Links

Documentation:- [GlideForm](https://docs.servicenow.com/csh?topicname=c_GlideFormAPI.html&version=latest "GlideForm")
