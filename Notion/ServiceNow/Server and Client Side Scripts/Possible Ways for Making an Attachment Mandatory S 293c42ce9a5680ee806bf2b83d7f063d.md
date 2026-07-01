---
aliases:
  - "Possible Ways for Making an Attachment Mandatory S"
tags:
  - client-script
  - service-portal
  - catalog-item
  - ui-policy
  - glide-ajax
---

# Possible Ways for Making an Attachment Mandatory : Service Portal/Native UI

**Problem Statement: Need to check if attachment is added or not when user submit a request through service catalog.**

I know, there are lots of post regarding making attachments mandatory  on Native UI and Service Portal. But very few of them are on working state.

I am tried to summarized all possible ways for making attachment mandatory on different UI types, ServiceNow Versions.

So, Let’s get started…….

**Option 1: ServiceNow Madrid Release Feature: Mandatory Attachment with No scripting**

If you are using ServiceNow Madrid or later release, then with the help of checkbox available on catalog item you can make attachment mandatory. Also, you can hide a paperclip i.e. attachment icon. Follow the steps as below:

1. Search **Maintain items** in Filter navigator and click on **Maintain items**
2. Select a any catalog item for that you want to make attachment/ hide attachment
3. In portal Setting Tab / Section, you will find out two checkbox fields named as : **Mandatory Attachment**
4. You just need to Mark them true/checked as below.
5. If you want to make it mandatory, then click on **Attachment Mandatory: TRUE/Checked.**

[find_real_file.png](https://www.servicenow.com/community/image/serverpage/image-id/147215i6331222F1323B5BC/image-size/large?v=v2&px=999)

You can go to Portal/Native UI and check if attachment is made mandatory/hidden.

**Option 2: Using UI Script, JS Theme, and Client script**Here is other ways that you may have a look as well.

**1. ADD A UI SCRIPT**       In the Left Navigator Bar, go to System UI > UI Scripts. Click New        **UI Script:** GlobalCatalogItemFunctions        **Global**: true        **Script**:        function getSCAttachmentCount() {        var length;        try {                length = angular.element("#sc_cat_item").scope().attachments.length;        } catch(e) {        length = -1;        }        return length**;**       }

**2. ADD A JS THEME:**

1. In the Left Navigator Bar, go to Service Portal > Portals
2. Click the Portal you want to adjust. It may be the one with URL suffix of "sp".
3. Click the "info" button for the Theme Field. The standard theme is "Stock"
4. Add your JS Include there
5. Create New JS Theme Display Name: GlobalCatalogItemFunctions UI Script: GlobalCatalogItemFunctions

**3. CREATE A CATALOG CLIENT SCRIPT:** For your catalog item you want to require attachments, use this client script.

function onSubmit() {

//Works in non-portal ui

try {

var attachments = document.getElementById('header_attachment_list_label');

if (attachments.style.visibility == 'hidden' || attachments.style.display == 'none' ) {

alert('You must attach the completed form before submitting this request.');

return false;

}

}

//For Service Portal

catch(e) {

var count = getSCAttachmentCount();

if(count <= 0) {

alert('You must attach the completed form before submitting this request.');

return false;

}

}

}

**Option 3: Using DOM Manipulation in Client script:**

Well with the introduction of London came a new field called 'isolate script'. New client-scripts are run in strict mode, with direct DOM access disabled. Access to jQuery, prototype and the window object are likewise disabled. To disable this on a per-script basis, configure this form and add the "Isolate script" field. To disable this feature for all new globally-scoped client-side scripts set the system property "glide.script.block.client.globals" to false.

Before running this script, **Make an Isolate script: False** on client script / catalog client script.

1. This script will run UI Types: Native and Service Portal

function onSubmit() {

if(this.document.getElementsByClassName('get-attachment').length == 0) {

alert(''You must add an attachment before submitting this request.');

return false;

}

}

2.This script will run UI Types: **Native UI**

function onSubmit() {

var attachments = document.getElementById('header_attachment_list_label');

if (attachments.style.visibility == 'hidden' || attachments.style.display == 'none' ) {

alert('You must add an attachment before submitting this request.');

return false;

}

}

**Option 4: OnSubmit Client Script with the help of GlideRecord:**

GlideRecord and g_form.getReference() are also available for retrieving server information. However, these methods are no longer recommended due to their performance impact in client script. Both methods retrieve all fields in the requested GlideRecord when most cases only require one field.

This script will run on both Native and portal UI as well.

function onSubmit() {

var cat_id = g_form.getValue('sysparm_item_guid');

var gr = new GlideRecord("sys_attachment");

gr.addQuery("table_name", "sc_cart_item");

gr.addQuery("table_sys_id", cat_id);

gr.query();

if (!gr.next()) {

alert("You must add an attachment before submitting this request.");

return false;

}

}

**Option 5: OnSubmit Client Script with the help of GlideAjax:**

If you are not in Madrid release, then above option is not available for you. In that case, with the help of client

script, you can achieve the above functionality for making attachment mandatory.

Before running this script, Make an ISOLATED SCRIPT: FALSE on client script / catalog client script.

Below script will run on Native UI (Non portal UI).

Client script Code:

function onSubmit() {

// var formID = gel('sysparm_item_guid').value;

// var formID= document.getElementById('sysparm_item_guid').value;

var formID = g_form.getValue('sysparm_item_guid');

// alert("Form ID: "+formID);

var ab = new GlideAjax('global.hasAttachment');

ab.addParam('sysparm_name', 'attachment');

ab.addParam('sysparm_form_id', formID);

ab.getXMLWait();

var isTrue = ab.getAnswer();

if(isTrue == 'yes'){

alert("Kudos to you!! You have added attachment");

return true;

} else if(isTrue == 'no'){

alert("You must attach document before submitting the form.");

return false;

}

Script include Code:

Name: hasAttachment

Client callable: TRUE

Script:

var hasAttachment = Class.create();

hasAttachment.prototype = Object.extendsObject(AbstractAjaxProcessor, {

attachment: function(){

var formID = this.getParameter('sysparm_form_id');

//gs.log("AG formID"+ formID);

var gr = new GlideRecord("sys_attachment");

gr.addQuery('table_name', "sc_cart_item");

gr.addQuery('table_sys_id', dataCheck);

gr.query();

if (gr.next()) {

//gs.log("Kudos to you!! You have added attachment ");

return 'yes';

}else{

//gs.log("You must attach document before submitting the form.");

return 'no';

}

},

type: 'hasAttachment'

});

**Advantage:**

The server processes the request synchronously and will not process further requests from the client until finished.Using getXMLWait() ensures the order of execution. So this script will give you a correct output on Native UI.

**Drawback:**

As getXMLWait() is not available to scoped applications and Service Portal does not support synchronous GlideAjax. So, this script will run on portal, but you will not get correct result.

Apart from all the above, you can create a custom Solution by creating a custom widget and make use of it. You can keep this attachment widget at any position on the catalog form. Please check out the below link:

[Require Attachments](https://serviceportal.io/downloads/require-attachments/)Hope you will find this article helpful. Please let me know if any other way to achieve this, any suggestions on this.

As the old saying goes, there is more than one way to skin a cat.

The same can be said when configuring ServiceNow.

There are often many ways of doing things; some good, some bad, and some ugly. The chosen 'way' is situational, depending on the exact use case and the version of the platform being used, which may offer alternate configuration options with codeless opportunities. Each way generally has a method or pattern that can be used to achieve the outcome. Sometimes patterns can become 'anti-patterns' when they are used in the wrong scenario.

Today, the cat is 'Attachments' and the skin is 'Making them mandatory in the Service Portal'. It is a fairly common requirement to make attachments mandatory in the Service Portal, and there are a few different ways to do it (with numerous blog posts).

This isn't just your standard blog post aggregating old ideas.

I've found a **new way** to make Attachments conditionally mandatory that I believe makes for a better UX (pre-Paris) and also incorporates recent changes in **Paris.**

The requirements for mandatory attachments usually take one of the following forms:

1. **I need attachments to always be mandatory**
2. **I need an attachment to be conditionally mandatory (e.g. When variable X is Y, Attachment is mandatory)**
3. **I need to enforce the attachment of X files**

The common solution for pattern 2 is to implement a script that counts the number of attachments. I don't like this solution and have come up with a different approach for this, which is similar - but different (Make Attachment Widget Mandatory).

I present to the Community a Configuration Pattern Version Matrix for these requirement patterns. I am not covering Use Cases for UI16 here.

# **Mandatory Attachment (SP only) Pattern Matrix**

| **Version / Requirement** | **Attachment Always Mandatory** | **Attachment Conditionally Mandatory** | **Count Attachments** |
| --- | --- | --- | --- |
| **Paris** | [Catalog Item Portal Settings](https://www.servicenow.com/community/servicenow-ai-platform-blog/making-attachments-mandatory-in-sp-the-ultimate-guide-including/ba-p/2281436#catalog_item) | [Attachment Variable & UI Policy](https://www.servicenow.com/community/servicenow-ai-platform-blog/making-attachments-mandatory-in-sp-the-ultimate-guide-including/ba-p/2281436#variable) | [Multiple Attachment Variables](https://www.servicenow.com/community/servicenow-ai-platform-blog/making-attachments-mandatory-in-sp-the-ultimate-guide-including/ba-p/2281436#multiple_var) |
| **Orlando** | [Catalog Item Portal Settings](https://www.servicenow.com/community/servicenow-ai-platform-blog/making-attachments-mandatory-in-sp-the-ultimate-guide-including/ba-p/2281436#catalog_item) | [Make Attachment Widget Mandatory with Client & UI Script](https://www.servicenow.com/community/servicenow-ai-platform-blog/making-attachments-mandatory-in-sp-the-ultimate-guide-including/ba-p/2281436#widget) | [Count Attachments via Client & UI Script](https://www.servicenow.com/community/servicenow-ai-platform-blog/making-attachments-mandatory-in-sp-the-ultimate-guide-including/ba-p/2281436#count) |
| **New York** | [Catalog Item Portal Settings](https://www.servicenow.com/community/servicenow-ai-platform-blog/making-attachments-mandatory-in-sp-the-ultimate-guide-including/ba-p/2281436#catalog_item) | [Make Attachment Widget Mandatory with Client & UI Script](https://www.servicenow.com/community/servicenow-ai-platform-blog/making-attachments-mandatory-in-sp-the-ultimate-guide-including/ba-p/2281436#widget) | [Count Attachments via Client & UI Script](https://www.servicenow.com/community/servicenow-ai-platform-blog/making-attachments-mandatory-in-sp-the-ultimate-guide-including/ba-p/2281436#count) |

Please note that this advice is general in nature and you should always take your own circumstances into consideration before picking an approach!

The links will take you to the content below in this article.

[Closing thoughts](https://www.servicenow.com/community/servicenow-ai-platform-blog/making-attachments-mandatory-in-sp-the-ultimate-guide-including/ba-p/2281436#closing_thoughts) at the bottom of this blog.

# **Patterns**

### **Catalog Item Portal Settings**

Open the Catalog Item for which you would like to have attachments always mandatory.

Navigate to the Portal Settings tab and check 'Mandatory Attachment'.

[find_real_file.png](https://www.servicenow.com/community/image/serverpage/image-id/173061iD29FC49C1B2A6939/image-size/large?v=v2&px=999)

The Attachment Widget is now mandatory and will your item will require a file to be attached prior to submitting.

### **Attachment Variable & UI Policy**

Paris has introduced a new feature called Attachment variables.

[Paris - Types of service catalog variables](https://docs.servicenow.com/bundle/paris-servicenow-platform/page/product/service-catalog-management/reference/r_VariableTypes.html)

[find_real_file.png](https://www.servicenow.com/community/image/serverpage/image-id/173069i4252BFAF1586F882/image-size/large?v=v2&px=999)

This allows the Catalog Designer to add specific context around attachments. Not only that, since they are variables, they can be made mandatory via UI Policy. There is no longer a need for Client Scripts that rely on the DOM.

If you are using Paris, using any other pattern than this is arguably an anti-pattern, as you are adding risk to your system by using custom code.

### **Make Attachment Widget Mandatory with Client & UI Script**

I recently had a requirement to make attachments mandatory based on a dynamic condition. Browsing the Community Forums, I found many articles that outlined how to implement an attachment check based on a variable value. These articles all used a UI Script to check the attachment count and served an error message back to the user upon submission via an onSubmit Client Script. The error message is often served up in the form of an old-school alert box. I can't stand alert boxes! The sound effect! The blocking of the whole browser (not just the current tab!) I can't think of a worse UX than alert boxes!

Wanting a better user experience (and having a gripe for alert boxes), I thought to myself - the existing solution isn't actually making attachments mandatory perse - it is just doing a count of the number of files attached to the form.

Now that ServiceNow has a mechanism for making the Attachments widget mandatory through Portal Settings on the Catalog Item, surely it would be possible to trigger the mandatory check mechanism rather than counting and frustrating the user at the last moment!

### **Making the Attachments Section Mandatory**

Below is an extract of the Attachment HTML in the Widget sc_cat_item

```markup
<div ng-if="c.showAttachments()" class="wrapper-md row no-margin"><now-attachments-list template="sp_attachment_single_line" ></now-attachments-list><div ng-class="{'flex-center attachment-height': options.native_mobile == 'true', 'flex-end': options.native_mobile != 'true'}"><label ng-if="!submitting && !submitted" style="font-weight:normal;cursor:pointer;"><sp-attachment-button></sp-attachment-button><span class="fa fa-asterisk mandatory"ng-if="data.sc_cat_item.mandatory_attachment"ng-class="{'mandatory-filled': data.sc_cat_item.mandatory_attachment && (data.sc_cat_item.attachment_submitted || attachments.length > 0)}"
            style="vertical-align:super"></span><span>${Add attachments}</span></label></div></div></div>
```

We can see that the Mandatory Asterix is controlled by the data.sc_cat_item.mandatory_attachment. This is set by the 'Mandatory attachment' flag.

Rather than counting the number of attachments, let's lean on the OOTB functionality for consistent user experience. We can simply toggle the mandatory check with the following JavaScript

```jsx
angular.element("#sc_cat_item").scope().c.data.sc_cat_item.mandatory_attachment = true;
```

Now, the Attachments clip at the bottom goes mandatory (denoted by the red star) and you are prompted by ServiceNow to add an attachment prior to submitting.

### 

### **UI Script - setAttachmentMandatory**

```jsx
(function() {
    "use strict";

    return {

        setAttachmentMandatory: function(isMandatory) {
            var isSuccess;
            try {
                angular.element("#sc_cat_item").scope().c.data.sc_cat_item.mandatory_attachment = isMandatory;
                isSuccess = true;
            } catch (e) {
                isSuccess = false;
                console.log('setAttachmentMandatory() failed: ' + e);
            }

            return isSuccess;
        },

        type: "AttachmentUtil"
    };
})();

```

**Note:** Set UI Type to Mobile / Service Portal

### **Client Script**

```jsx
function onChange(newValue, oldValue) {

g_ui_scripts.getUIScript('setAttachmentMandatory').then(function(script) {
   script.setAttachmentMandatory(true);
});
}
```

**Note:** UI Script must be named 'setAttachmentMandatory' and Client Script UI Type set as 'Both'

How easy was that!

You can also add the UI Script to your portal theme and call the script directly.

### 

### **Count Attachments via Client & UI Script**

I'm not going to re-invent the wheel here. There are tonnes of existing posts that show how to do this.

[https://community.servicenow.com/community?id=community_article&sys_id=0f0c5290dbe7f380d82ffb2439961...](https://community.servicenow.com/community?id=community_article&sys_id=0f0c5290dbe7f380d82ffb24399619f5)

### **Multiple Attachment Variables**

Using the same method for making attachments conditionally mandatory in Paris, follow the [Attachment Variable & UI Policy](https://www.servicenow.com/community/servicenow-ai-platform-blog/making-attachments-mandatory-in-sp-the-ultimate-guide-including/ba-p/2281436#variable) pattern but make a distinct variable for each attachment that is required. For example, if you require 5 files to be attached, created a variable for each one, named as desired. Save the Attachment widget for supporting attachments.

## Related

- [[Server and Client Side Scripts]]
- [[ServiceNow – Service Portal]]
- [[ServiceNow – Service Catalog]]