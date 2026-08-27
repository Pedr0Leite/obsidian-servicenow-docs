---
title: "How to use the OOB 'Incident Survey' notification when incident gets closed. Is it possible to use that notification where it contains, Incident and Survey link in the HTML body?"
aliases:
  - KB0831415
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0831415
kb_number: KB0831415
last_modified: 2024-04-08
---

## How to use the OOB 'Incident Survey' notification when incident gets closed. Is it possible to use that notification where it contains, Incident and Survey link in the HTML body?

  

### Issue

-   When incident is getting closed, a survey notification should send out and it should contain Survey and Incident link like the OOB notification 'Incident Survey'.

### Release

-   All releases.

### Cause

-   N/A

### Resolution

-   Make sure the repeat interval of trigger condition is all set to oo.
-   Incident Survey Notification can be used and furthermore, a below email script should be created and attached to the notification email scripts of the Incident Survey Notification.
-   Email Script = incident\_survey\_link\_assessment\_2
    
      
    (function runMailScript(current, template, email, email\_action, event) {  
    gs.log("KO: current.getUniqueValue(): " + current.getUniqueValue());  
      
    var gr = new GlideRecord('asmt\_assessment\_instance');  
    gr.addQuery('task\_id', current.getUniqueValue());  
    gr.setLimit(1);  
    gr.orderByDesc('number');  
    gr.query();  
    gs.log("KO: getRowCount(): " + gr.getRowCount());  
    if (gr.next()) {  
    var link = new AssessmentUtils().getAssessmentInstanceURL(gr.getUniqueValue());  
    gs.log("KO: link: " + link);  
      
    template.print('<p><font size="4" color="#999999" face="helvetica">');  
    template.print(gs.getMessage('We value your input. Please help us by taking the time to fill out this short survey:'));  
    template.print('</font></p>');  
    template.print('<p><font face="helvetica">');  
    template.print('<a style="font-size: 16px; font-family: Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; border-radius: 3px; -webkit-border-radius: 3px; -moz-border-radius: 3px; background-color: #278efc; border: 1px solid #0368d4; display: inline-block; padding: 5px" href="' + link + '">' + gs.getMessage('Click here to take the survey') + '</a>');  
    template.print('</font></p>');  
    }  
      
    })(current, template, email, email\_action, event);
