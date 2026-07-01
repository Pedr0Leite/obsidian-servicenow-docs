---
aliases:
  - "How to use UI Actions in Workspaces"
tags:
  - workspace
  - ui-actions
  - declarative-actions
  - g-modal
---

# How to use UI Actions in Workspaces

---

## Overview

---

UI Actions are supported in both agent and configurable 
workspaces, but only in limited areas, such as the Action Bar component 
which is provided by default on the out-of-the-box record page. This 
means that UI Actions are only supported on forms in workspaces and not 
lists. If you have existing UI Actions on forms that you want to port 
over to your workspace or need to use the same UI Action on both a 
workspace and in the classic environment, you may be able to modify your
 UI Action code to do so. The [Set up custom UI actions in legacy workspace](https://docs.servicenow.com/csh?version=latest&topicname=configure-agent-workspace-ui-actions)
 product documentation has extensive information on creating UI Actions,
 and most of the information does still apply to both configurable and 
agent workspaces.

You can use Declarative Actions in the workspace ui on forms, 
lists, and related lists, and they work with both workspaces and UI 
Builder pages, so you don’t need to customize an out-of-the-box UI 
Builder page. For more information see our [COE article on Declarative Actions](https://community.servicenow.com/community?id=community_article&sys_id=cc635eafdb42c154e2adc22305961991).

---

## Fields and Tables

---

There are some main fields and tables you need to know to use 
UI Actions in configurable workspaces. When using Workspace options 
ensure the **Client** checkbox on the UI Action is set to **true**.

- **Workspace Form Button** - To make the UI Action appear on the list of UI Actions.
- **Workspace Form Menu** - To make the UI Action appear as a list item in the menu associated with UI Actions.
- **Workspace Client Script** - This is an optional field used to create a workspace-specific client script. Workspace has
similar client scripting limitations as Service Portal.
- **Format for Configurable Workspace** (Available
in San Diego) - Automatically creates the UX Form Action record needed
to link the UI Action to configurable workspaces.
- **UX Form Action** - Links a UI Action to use in configurable workspaces.

---

## Call a Server Side UI Action

---

Workspaces use client-side UI Actions, and a UI Action must be 
marked as Client in order for it to appear and function on a workspace. 
So what do you need to do if you want to re-use a server-side UI Action 
you've previously created or want to create in a workspace UI Action? 
You have some choices. You can create a server script Declarative Action
 for the Workspace, which is detailed in our [COE article on Declarative Actions](https://community.servicenow.com/community?id=community_article&sys_id=cc635eafdb42c154e2adc22305961991), or you could call the server-side UI Action from your client-side UI Action.

**Example**

```jsx
function onClick() {
  var actionName = g_form.getActionName();
  g_form.submit(actionName);
}
```

---

## Unsupported Methods

---

The workspace client scripting environment does not support the following global variables:

- this, window, document
- $, $$, jQuery, $j
- angular

In general, accessing globals is not behavior that should be 
relied upon. The client scripts should only access the registered 
objects i.e. documented client side methods within the scripting 
environment.

---

## Methods

---

### 

### GlideAgentWorkspace

This is a documented API, for more information on the methods see the documentation on the [developer site](https://developer.servicenow.com/dev.do#!/reference/api/latest/client/GlideAgentWorkspaceAPI).
 The g_aw API enables a UI Action or Client Script to open a specified 
record in a Workspace tab. Two methods are currently available, see the [Close tab and save-and-close tab UI Actions](https://docs.servicenow.com/csh?version=latest&topicname=close-tab-ui-action) product documentation for specific examples.

closeRecord()

openRecord()

You can also try the undocumented setSectionExpanded method to collapse or expand your sections.

**Example**

```jsx
g_aw.setSectionExpanded('Notes', false); // will collapse the Notes section
g_aw.setSectionExpanded('Resolution', true); // will expanded the Resolution section
```

### g_modal

A client scriptable API that allows the user to display an overlaid modal window and perform the following:

- Display input type fields in a modal window
- Show something else in a frame such as a UI Page or external link
- Perform action on confirm
- Load a component

**Common Properties for Methods**

title: The title of the Modal window

size: The size of the Modal window: sm, lg, xl, fw (fixed-width)

height: Height of the Modal window in pixels/em (optional)

---

### showFields

A g_modal method that displays a modal window with the fields 
defined in the UI Action Workspace Client Script. Displays the OK and 
Cancel buttons by default.

**Properties**

Accepts title, message, and callback as arguments and returns a
 promise. The fields property is required. If only one argument has 
been provided it will be treated as a fields parameter.

**fields:**

name: The name of the field, if using a reference field it is the name of the reference field on the form

type: textarea, choice, reference, boolean, string

label: How the field displays to the user

value: Initial value of the field, useful in choices or booleans

mandatory: true or false

**If type is reference:**

name: The reference field on the current record being used to search

reference: The table you're referencing

referringTable: The table you're referencing from

referringRecordId: The sys_id of the value you're calling in the UI Action form

value: Can use the g_form method here to get the value

displayValue: Display value must be used in conjunction with value

---

**Example**

This is a simple example of prompting a user for a reason using
 a modal window, and then passing it back to the Work notes field on the
 record. In the example below the **then()** method returns a Promise, which returns what the modal returns such as *fieldValues*
 in this example. In this example the work notes field on the client 
side with the field value are in the updatedFields array. Since only one
 field is being returned, the index/position was 0. If returning 
multiple fields just enter the position they are in.

```jsx
function onClick(g_form) {
    g_modal.showFields({
        title: "Enter your reason",
        fields: [{
            type: 'textarea',
            name: 'work_notes',
            label: getMessage('Reason'),
            mandatory: true
        }],
        size: 'lg'
    }).then(function(fieldValues) {
        g_form.setValue('work_notes', fieldValues.updatedFields[0].value);
        g_form.save();
    });
}
```

### 

[](https://www.servicenow.com/community/image/serverpage/image-id/154461iFF6F5927E76DFE76/image-size/large?v=v2&px=999)

This example expands on using more fields, such as a choice field and a reference field.

```jsx
function onClick(g_form) {

    var fields = [{
        type: 'textarea',
        name: 'work_notes',
        label: getMessage('Reason'),
        mandatory: true
    },
        {
            type: 'choice',
            name: 'reason_code',
            label: getMessage('Reason code'),
            value: getMessage(' -- Select -- '),
            choices: [{
                displayValue: 'Duplicate',
                value: 'duplicate'
            },
                {
                    displayValue: 'Canceled',
                    value: 'canceled'
                }
            ],
            mandatory: true
        },
        {
            type: 'reference',
            name: 'caller_id',
            label: getMessage('What is your name?'),
            mandatory: true,
            reference: 'sys_user',
            referringTable: 'incident',
            referringRecordId: g_form.getUniqueValue(),
			value: g_form.getValue('caller_id'),
			displayValue: g_form.getDisplayValue('caller_id')
        }
    ];

    g_modal.showFields({
        title: "Enter your reason",
        fields: fields,
        size: 'lg'
    }).then(function(fieldValues) {
        g_form.setValue('work_notes', fieldValues.updatedFields[0].value);
        g_form.setValue('caller_id', fieldValues.updatedFields[2].value);
        g_form.save();
    });
}

```

[](https://www.servicenow.com/community/image/serverpage/image-id/154469i1C7C34466207E9DF/image-size/large?v=v2&px=999)

### showFrame

A g_modal method to link to external URLs or UI Pages.

**Properties**

Accepts a title, message, and callback. The url property is 
mandatory. If only one property is provided it will be treated as a url 
parameter.

---

### 

### **Example**

```jsx
function onClick(g_form) {
    var kbId = '24d9243187032100deddb882a2e3ec33'; //sysId of KB article
    g_modal.showFrame({
        url: '/kb_view.do?sys_kb_id=' + kbId,
        title: 'Test Knowledge Article',
        size: 'lg',
        height: 500
    });
}
```

[](https://www.servicenow.com/community/image/serverpage/image-id/154463i12BF2CE3B478EE42/image-size/large?v=v2&px=999)

The next example is using a UI Page embedded and uses **window.parent.postMessage()** in the UI Page to pass data from the iFrame back to the workspace since **g_form** is not accessible in the UI Page when it is in the iFrame. In your instance or PDI the **Propose Major Incident** UI Action is a great resource to see how UI Pages are being called in workspaces.

```jsx
function onClick(g_form) {
	function proposeMIC(data) {
		var workNotes = data.msg + "\n" + data.workNotes;
		var notes = g_form.getValue('work_notes') + ' ' + workNotes;
		var bi = g_form.getValue('business_impact') + ' ' + data.businessImpact;
		g_form.setValue('work_notes', notes.trim());
		g_form.setValue('business_impact', bi.trim());
		g_form.submit('sysverb_mim_propose');
	}

	function openPopup() {
		if(!g_form.getControl('work_notes')) {
			getMessage('Cannot propose major incident as "Worknotes" is not visible', function(msg) {
				g_form.addErrorMessage(msg);
			});
			return false;
		}

		var url = "/sn_major_inc_mgmt_mim_propose.do?sysparm_stack=no&sysparm_workspace=" + true;
		g_modal.showFrame({
			title: getMessage("Propose Major Incident"),
			url: url,
			size: 'lg',
			autoCloseOn: 'URL_CHANGED',
			callback: function (ret, data) {
				if (ret)
					proposeMIC(data);
			}
		});
	}

	openPopup();
}
```

In the UI Page within the Client Script the following function 
is being used to handle the Cancel that you may need to use in your UI 
Pages as the native Cancel functionality does not work. The config to 
identify the workspace is set in the HTML.

```jsx
var config = {workspace: '${JS_STRING:RP.getParameterValue('sysparm_workspace')}' == 'true'};

function close() {
    if(!config.workspace)
        dialog.destroy();
    else
        window.location.href = window.location.href + '&sysparm_next_pg=true';
}
```

Also, if you log the data object it will return the following:

```jsx
data: {"msg":"Proposed as major incident candidate","workNotes":"work note note","businessImpact":"business impact note"}
```

[](https://www.servicenow.com/community/image/serverpage/image-id/154471iCE871007C69BC7A5/image-size/large?v=v2&px=999)

### Alert

Displays an alert to the user when performing an action. See 
the Confirm example below as an alert is displayed to the message if the
 user does not meet the requirements.

**Properties**

Accepts title, message, and callback as arguments and returns a
 Promise. Message is required, if only one argument has been provided it
 will be treated as a message parameter.

alert: getMessage(Title of the Modal), msg(Text to the user), callback

---

### 

### Confirm

Displays a confirmation to the user when performing an action.

**Properties**

Accepts title, message, and callback as arguments and returns a
 Promise. Message is required, if only one argument has been provided it
 will be treated as a message parameter.

confirm: getMessage(Title of the Modal), msg(Text to the user), callback

---

**Example**

This example is adopted from the End Chat UI Action on an 
Interaction, and is a good example of using if statements to determine 
when a user can take an action and performing the action when the 
user clicks OK versus Cancel for example setting the state of the record
 to Closed.

```jsx
function onClick(g_form) {

    if (g_user.userID != g_form.getValue('assigned_to')) {
        g_modal.alert('Only the assigned to can end this action.');
        return;
    }

    var msg = getMessage("Are you sure you want to take this action?");
    g_modal.confirm(getMessage("Confirmation"), msg, function (confirmed) {
        if (confirmed) {
            g_form.setValue('state', 'closed_complete');
            g_form.save();
        }
    });

    return false;
}
```

[](https://www.servicenow.com/community/image/serverpage/image-id/154473i584079118887A2F1/image-size/large?v=v2&px=999)

### Confirm Destroy

Similar to the Confirm method, except the confirm button is show as a destructive style.

**Properties**

Accepts title, message, and callback as arguments and returns a
 Promise. Message is required, if only one argument has been provided it
 will be treated as a message parameter.

confirmDestroy: getMessage(Title of the Modal), msg(Text to the user), callback

---

### action.openGlideRecord

This is another [documented API](https://developer.servicenow.com/dev.do#!/reference/api/latest/server/no-namespace/ActionAPIBoth#Action_openGlideRecord_O)
 that is very handy when using UI Actions in workspaces. Instead of 
using action.setRedirecrURL in the UI Action, action.openGlideRecord can
 be used instead, and will work for both platform and workspace.

**Example**

The following example is a simple server script with the **Workspace Form Button** and **Format for Configurable Workspace** options selected. Upon clicking the button the server script will run and open the new record in a sub-tab.

```jsx
var incGr = new GlideRecord('incident');
incGr.newRecord();
incGr.setValue('caller_id', current.getValue('contact'));
incGr.setValue('short_description', current.short_description);
incGr.insert();
action.openGlideRecord(incGr);
```

## Related

- [[Workspace]]
- [[Useful UI Actions]]
- [[Workspace App Shell UX Page Properties]]
- [[Workspace for a custom app forms]]

[](https://www.servicenow.com/community/image/serverpage/image-id/154477i1DFA9B8DD9771C6A/image-size/large?v=v2&px=999)

---

## Community Resources

---

We’ll link community articles that use the methods mentioned 
above as we find them. If you think an article should be listed here 
please comment.

[Replicate choice field on Workspace modal with g_modal](https://community.servicenow.com/community?id=community_article&sys_id=190860ecdb438d1039445ac2ca961966) by Aare Pujuste

- **92,952 Views**

Comments

[](https://www.servicenow.com/community/image/serverpage/avatar-name/ProfileAvatar/avatar-theme/candy/avatar-collection/ServiceNow_Avatars/avatar-display-size/profile/version/2?xdesc=1.0)

[khadija3](https://www.servicenow.com/community/user/viewprofilepage/user-id/127634)

Mega Guru

‎04-01-2022
	
		
		06:13 PM

Hello,

Thank you so much for the great article, are you aware of any property to remove the close icon in the popup ?

Regrads

[](https://www.servicenow.com/community/image/serverpage/avatar-name/ProfileAvatar/avatar-theme/candy/avatar-collection/ServiceNow_Avatars/avatar-display-size/profile/version/2?xdesc=1.0)

[F_lix Dion](https://www.servicenow.com/community/user/viewprofilepage/user-id/183204)

Kilo Expert

‎05-31-2022
	
		
		04:53 PM

Hi, thank you for your work. I learned everything I know about g_modal thanks to you and your website!

I've got a question for you. I managed to have my pop up window set 
up and working perfectly, but I am using it on two different UI Actions 
("save" button and "resolve" button).

As of right now, I duplicated the whole script in both actions so I 
was wondering if there would be a way to reuse the same code in 
different UI Actions.

I've tried with UI Script, Script Include and with gsftSubmit(null, 
g_form.getFormElement(), 'sysverb_ws_save'); but nothing seems to be 
working ...

Any suggestions?

Thank you!

[](https://www.servicenow.com/community/image/serverpage/avatar-name/ProfileAvatar/avatar-theme/candy/avatar-collection/ServiceNow_Avatars/avatar-display-size/profile/version/2?xdesc=1.0)

[F_lix Dion](https://www.servicenow.com/community/user/viewprofilepage/user-id/183204)

Kilo Expert

‎06-13-2022
	
		
		06:34 PM

Hi @Ashley Snyder,

Thank you so much for the content on the g_modal.

Quick question: I've been looking around and can't find anything to help me figure it out.

I set up my g_modal window to pop-up when an 
incident is set to resolved and everything works well, but I would like 
to add an action when the Agent clicks on Cancel or "X".

[](https://www.servicenow.com/community/image/serverpage/image-id/154465i08935F246F48CCB3/image-size/large?v=v2&px=999)

In fact, I want to refresh the page so that if
 they cancel, it will cancel the changes and trigger the g_modal again 
when they will hit resolve again.

As of right now, if an agent clicks cancel, 
the window closes but the form stays and if you hit resolve again, the 
data policy kicks in and show an error message instead of having the 
g_modal pop-up again.

[](https://www.servicenow.com/community/image/serverpage/image-id/154443i35777651F46D4694/image-size/large?v=v2&px=999)

Thank you for your time!