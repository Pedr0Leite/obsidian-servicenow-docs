---
aliases:
  - "UI Page Tips and Tricks"
area: "Random Scripts"
source: notion-export
tags:
  - ui-page
  - jelly
  - glide-modal
  - angularjs
  - client-scripts
  - random-scripts
---

# UI Page Tips and Tricks

When I developed a quite complex UI Page in ServiceNow I found that 
many helpful steps and code snippets are spread all over the internet. 
So I decided to collect what helped me and create a short UI Page cheat 
sheet.

Here we go:

## Referencing the current record when the UI Page was opened in a GlideModal

If your UI Page is shown in a GlideModal popup from a form and you 
need to know which record it was opened from then you can simply pass 
the sys_id as a parameter:

```jsx
function showDialog(){
    var gm = new GlideModal("x_1234_custom_ui_page");
    gm.setTitle('Tips and Tricks');
    gm.setPreference('sysparm_record', g_form.getUniqueValue());  // pass the sys_id
    gm.render();
}
```

In the UI Page itself you can then access it in the HTML like so:

```markup
<g:evaluate var="jvar_current" expression="RP.getParameterValue('sysparm_record')"/>
```

Note that this creates a new Jelly variable "jvar_current" and assigns the value of the parameter "sysparm_record".

## Passing data to the Client script

If you need some values from the HTML in the Client script then you can use the following construct:

```markup
<script>
    var current_26bcb4f507e11010b6eef0118c1ed078 = "${JS:jvar_current}";
    var object_26bcb4f507e11010b6eef0118c1ed078 = "${JS:jvar_object}";
</script>
```

Please note that the variables defined here will be global for the 
whole ServiceNow page. To prevent duplicates or overlaps it is a good 
practice to add the sys_id of your UI Page at the end of each variable 
(like I did in my example).

Then in the Client script you can access the defined variable. If it is a JSON object you can parse it and use its fields.

```jsx
var current = current_26bcb4f507e11010b6eef0118c1ed078;
var object = JSON.parse(object_26bcb4f507e11010b6eef0118c1ed078);
```

## Passing data to the Processing script

To get data into the Processing script from the HTML you need to 
follow a different approach. You first need to create a hidden input 
field with the correct value assigned. Note that the id and name 
attributes are mandatory.

```markup
<input type="hidden" id="current" name="current" value="${jvar_current}"/>
```

Then in the Processing script you can access the values with the name of your input element:

```jsx
var currentSysId = request.getParameter('current');
```

Of course this also works for JSON objects which you can parse to use their fields:

```jsx
var object = JSON.parse(request.getParameter('object'));
```

## Calling the Processing script for submission

When the user is done with his work in the UI Page he will most 
probably want to submit and trigger a server update. To leave the UI 
Page and execute the code in the Processing Script you can submit a 
Jelly ui_form. Here is a basic but complete HTML that does this:

```markup
<?xml version="1.0" encoding="utf-8" ?>
<j:jelly trim="false" xmlns:j="jelly:core" xmlns:g="glide" xmlns:j2="null" xmlns:g2="null"><g:ui_form><div><!-- add all your input elements or other HTML tags here -->
        </div><button type="submit" class="btn btn-primary">Submit</button></g:ui_form></j:jelly>
```

Important here is that you use the "</g_ui:form>" tag and define a button of type "submit" inside.

## Using AngularJS in UI Pages

If you are like me and don’t want to hustle with Jelly but use 
AngularJS instead to build your UI Page then I recommend you to check 
out my detailed post about this topic here:

[https://community.servicenow.com/community?id=community_article&sys_id=f8c9d98c1b521850305fea89bd4bc...](https://community.servicenow.com/community?id=community_article&sys_id=f8c9d98c1b521850305fea89bd4bcb08)

## Staying on the current form after submitting the UI Page (when opened in a GlideModal)

By default when you submit a UI Page then you are redirected to the 
UI Page again. That means when you opened it in a GlideModal and click 
on submit then after the execution of the Processing script you will be 
redirected to the UI Page in the full window.

What you probably want is to stay on the current form and just close 
the popup. This can be achieved by adding the following two lines to the
 end of the Processing Script:

```jsx
var urlOnStack = gs.getSession().getUrlOnStack();
response.sendRedirect(urlOnStack);
```

## Related

- [[Random Scripts]]
- [[AngularJS in SN]]
- [[Confidential Attachments]]