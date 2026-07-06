---
title: "Debugging Service Portal Widgets"
aliases:
  - KB0677496
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0677496
kb_number: KB0677496
last_modified: 2026-05-04
---

## Debugging Service Portal Widgets

  

### Issue

# Overview

* * *

This article sets out a standard set of Service Portal Widget debugging techniques and is intended both for informational and training purposes. For many incidents, an understanding of the "Basic Techniques" section will suffice. For higher priority incidents on heavily customized instances, a firm grasp of the "Advanced Techniques" may be required. The techniques in this article are a compilation of techniques gathered from currently available ServiceNow resources and new techniques which are documented for the first time.

All examples in this article are run on a widget called "Global Objects Demo Widget". To run the examples in the article you will need to see section "**Running the Example Tests**" at the end of the article to get setup.

### Release

All releases

### Resolution

# Basic Techniques

* * *

## 1\. Logging to the JavaScript console

The console.log() function will log data to the JavaScript console in the browser. This technique will work in the Client Script of the widget and also in the Server Script.

### Example

If you look at line 3 and line 16 of the Server Script of the Global Objects Demo Widget, you'll notice that the "input" and "data" objects are logged to the console.

 ![Console Log the input and output data](sys_attachment.do?sys_id=3fed151793e083947c79b36d6cba104d "Console Log the input and output data")

Open the JavaScript console in Chrome developer tools. Refresh the preview pane and you'll notice the following result in the console:

The input object is undefined and the data object is printed to the console.

 ![output data in console log](sys_attachment.do?sys_id=3bed151793e083947c79b36d6cba1057 "output data in console log")

## 2\. Using the inbuilt _debugger_ function in Chrome and Firefox

The debugger function can be used in the Client Script of the widget but not the Server Script. Adding the debugger function is like inserting a breakpoint into your code allowing you to step through the code line by line.

### Example

In the Client Script of the widget, add the code debugger; at line 23.

 ![log debugger function](sys_attachment.do?sys_id=bbed151793e083947c79b36d6cba1052 "log debugger function")

Open Chrome Developer Tools. Save the widget and refresh the preview pane. Press the "server.get({collectionName: "presidents"})" button. The JavaScript execution will stop at the word debugger. To see the "response" object contents, hover your mouse over the word "response" in line 14 of the code in devtools.

 ![place debugger function in the code](sys_attachment.do?sys_id=b7ed151793e083947c79b36d6cba105c "place debugger function in the code")

To step into the next line in the code use the down arrow button. To allow the JavaScript execution to proceed without stopping, press the "Resume script execution" button.

 ![step thru the debugger ](sys_attachment.do?sys_id=bfed151793e083947c79b36d6cba1083 "step thru the debugger output")

## 3\. Log the widget's "scope" object to the console

Hold down the control key and right-click on the widget.  Choose "Log to console: $scope.data" or "Log to console: $scope". The only difference is whether you want to log the entire scope object to the console or only the data property of the scope object.

### Example

Navigate to the following URL: https://<yourinstancename>.service-now.com/sp?id=demo\_widget\_example

Hold down the control key and right-click on the widget. Choose "Log to console $scope.data".  Open Chrome Developer Tools and expand the object dumped to the console and verify that the value of $scope.data.prop1 is "Apple".

 ![see the props in developer tools log](sys_attachment.do?sys_id=33ed151793e083947c79b36d6cba107f "see the props in developer tools log")

# Advanced Techniques

* * *

 The advanced debugging techniques described below can be highly effective when troubleshooting on a production instance where it is not possible to make any changes. All the techniques below are run through Chrome Developer Tools.

## 1\. Creating a reference to the widget's scope in the console ("The puppet main"):

You can think of this technique as an analogy to a puppet show. The puppeteer activates and manipulates the puppets (widgets) with a set of strings. In this case, we are creating a second set of strings to the puppet so that we can activate and manipulate the widget from the JavaScript console!

This technique allows you to:

-   Change the widget's scope data
-   Run widget scope function
-   Re-run the widget Server Script

### Steps to get a reference to the widget's scope in the JavaScript console:

1.  Right-click on the widget and choose "Inspect"
2.  In dev tools Elements tab, click on the element with attribute widget="widget". It should be a few elements above the currently inspected element. This points the $0 scripting tool at the widget.
3.  In the Javascript console, run the following code:
    
    var scopeRef = angular.element($0).scope();
    

### Changing the widget's scope data:

Once you have a reference to the widget in the JavaScript console, you can take any piece of data in the widget's scope and just change it. After changing a value, run the AngularJS $apply() function on the scope to apply your changes to the page.

#### Example

After getting a reference to the Global Objects Demo Widget in the console, run the following code:

scopeRef.data.prop1 = "Pear";
scopeRef.$apply();

 ![Global Objects Demo Widget in the console](sys_attachment.do?sys_id=7bed151793e083947c79b36d6cba1037 "Global Objects Demo Widget in the console")

### Running the widget's Client Controller functions from the console

Any function that is defined in the Client Script (client controller) of the widget is available from the widget's scope. This means that once you have a reference to a widget's scope in the console you will not only be able to change data in the scope object but you can also run any of the client controller functions!

#### Example

The getPrettyData() function is defined in the Client Script of the Global Objects Demo Widget. Now that we have a reference to the widget's scope in the console, we can run the function directly from the JavaScript console.

![run props ](sys_attachment.do?sys_id=f7ed151793e083947c79b36d6cba103c "run props ") 

### Re-run the widget's Server Script

Let's say that we've made some changes to the scope of the widget with the techniques above, we've got our reference to the widget in the console, and we want to see what happens when the server refreshes the data sent to the client controller. We can re-run the widget's Server Script from the console as per below:

scopeRef.server.refresh();

## 2\. Debugging and editing the widget client script directly from the Chrome dev tools "Sources" panel

The client controller scripts for all widgets on the page can be found in the "Sources" panel of Chrome Developer Tools. If you look at the screen capture below, you'll notice that they are all listed under the "top" window then under the "(no domain)" section. Clicking on the script will open it in the Sources panel code editor window. Most of the widget client controller scripts are listed as <widget\_id>.js, others will be listed by the id attribute value of the top-level HTML element of the widget.

![client controller scripts in developer tools](sys_attachment.do?sys_id=3fed151793e083947c79b36d6cba1088 "client controller scripts in developer tools") 

Once the client controller script is open in devtools you can begin debugging directly from there.

### Making local changes to the client controller code from devtools

#### Example

Navigate to the following URL: https://<yourinstancename>.service-now.com/sp?id=demo\_widget\_example.

Open Chrome developer tools.

Click on the "Sources" panel in devtools.

Open the global-objects-demo-widget.js file

 !["Sources" panel in devtools](sys_attachment.do?sys_id=c4fd151793e083947c79b36d6cba108d "\"Sources\" panel in devtools")

Between lines 7 and 8 add the following line of code:

alert("Server script now refreshed");

Right-click in the script editor window and Save. Do not refresh the page.

 ![Save script ](sys_attachment.do?sys_id=23ed151793e083947c79b36d6cba100f "Save script ")

Click the "server.refresh()" button in the widget.

Notice the alert window pops up showing that you've been able to alter the widget directly from devtools! This is a powerful technique when debugging production instances.

### Adding breakpoints to widget client controllers from within devtools

Another great thing about having access to the client controller code from within devtools is that you can add in breakpoints. Breakpoints can be added to the code by clicking on the line numbers in the code editor window of the "Sources" panel.

#### Example

Navigate to the following URL: https://<yourinstancename>.service-now.com/sp?id=demo\_widget\_example

Open Chrome developer tools.

Click on the "Sources" panel in devtools.

Open the global-objects-demo-widget.js

Click online number 15 to add in a breakpoint.

 ![Pointing to line 15 in the script widget](sys_attachment.do?sys_id=ffed151793e083947c79b36d6cba1014 "Pointing to line 15 in the script widget")

Click on the "server.get({collectionName: "presidents"})" button.

Notice that JavaScript execution stops directly at line 15.

Hover the mouse over the "data" in line 15 to inspect the response.

 ![Object props values in object](sys_attachment.do?sys_id=7fed151793e083947c79b36d6cba1019 "Object props in values object")

Resume JavaScript execution with the button to the right of the code editor window.

# Running the example tests

* * *

Attached to this KB article you'll find a update set which contains one Service Portal widget called "Global Objects Demo Widget" and one Service Portal page called "demo\_widget\_example". The demo page contains one instance of the demo widget.

To import the update set to your test instance:

1.  Click on "Retrieved Update Sets" in the Application Navigator.
2.  Click on the Related Link "Import Update Set from XML" at the bottom of the page.
3.  Click "Choose File", location the downloaded update set from the KB article and press the "Upload" button
4.  Click on the newly uploaded update set in the list of Retrieved Update Sets. The name will be "Service Portal Global Objects Demo"
5.  Click the Preview Update Set button in the header.
6.  Click on Commit Update Set.

To run the tests, it's good to have two browser tabs open; one with the widget's code and preview pane and the other with the demo page shows.

Tab 1: https://<yourinstancename>.service-now.com/sp\_config?id=widget\_editor&sys\_id=072cfcbc4f04130050d128201310c7d7&spa=1

Tab 2: https://<yourinstancename>.service-now.com/sp?id=demo\_page 

In the widget editor, you can enable a preview pane to test any changes that you've made to the widget. To do this click on the hamburger menu at the top right of the editor and select "Enable Preview". Then just use the eye button toggle the widget preview on and off.

 ![ "Enable Preview" from the menu](sys_attachment.do?sys_id=37ed151793e083947c79b36d6cba1061 " \"Enable Preview\" from the menu")

After every test remember to remove any changes made and resave the widget.
