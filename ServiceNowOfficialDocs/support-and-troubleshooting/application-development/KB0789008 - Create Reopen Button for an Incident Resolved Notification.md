---
title: "Create Reopen Button for an Incident Resolved Notification"
aliases:
  - KB0789008
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0789008
kb_number: KB0789008
last_modified: 2025-01-03
---

## Create Reopen Button for an Incident Resolved Notification

  

### Summary

This Knowledge article shows how to create a Reopen Button for the Incident Resolved Notification.

### Instructions

If an incident is resolved, "Incident Resolved" Inbound action will be triggered with the details of the incident. The Reopen can be achieved using a link set in the notification/email template or by creating a button that will send an email to the ServiceNow instance to reopen the incident.

In order to reopen a ticket, the email that you send should have a reply prefix "Re:", incident/ticket number and with the subject line "Please reopen".

To send a notification with a reopen link: 

ServiceNow has an out of the box template mailto.unsatisfied this can be used in the notification or in the email template referred to in the notification like **${mailto:mailto.unsatisfied}**. Below is the view of the link;

![](/sys_attachment.do?sys_id=5f2f9001db44b8d066e0a345ca9619a7)

To Send notification with a reopen button:

Please create a Notification Email Script with the below script: (Attached the XML of the script to the article)

var link = gs.getProperty("instance\_name")+ "@service-now.com";  
var backgroundColor = 'background-color: #278efc;';  
var border = 'border: 1px solid #0368d4;';  
var color = 'color: #ffffff;';  
var fontSize = 'font-size: 16px;';  
var fontFamily = 'font-family: Helvetica, Arial, sans-serif;';  
var textDecoration = 'text-decoration: none; border-radius: 3px;';  
var webKitBorder = '-webkit-border-radius: 3px;';  
var mozBorder = '-moz-border-radius: 3px;';  
var display = 'display: inline-block;';  
var padding = 'padding: 5px;';  
  
var newLink = "mailto:" + link + "?subject=Re:" + current.number + " - Please reopen";  
template.print('<a href="' + newLink + '"');  
  
template.print('style="' + backgroundColor + border + color + fontSize + fontFamily + textDecoration + webKitBorder + mozBorder + display + padding);  
template.print('"> Click here if your issue was not properly resolved : ' + current.number);

 Please use the script in the notification or in the email template referred in the notification like **${mail\_script:reopen\_button}**. Below is the view of the button;

![](/sys_attachment.do?sys_id=572f9001db44b8d066e0a345ca9619a5)

[Sample Notification Script](sys_attachment.do?sys_id=d72f9001db44b8d066e0a345ca9619a9 "Sample Notification Script")
