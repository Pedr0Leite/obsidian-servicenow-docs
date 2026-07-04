---
title: "Walk-up \"Check in\" button is broken"
aliases:
  - KB0814941
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0814941
kb_number: KB0814941
last_modified: 2024-04-08
---

## Walk-up "Check in" button is broken

  

### Issue

Within the user's custom walk\_up\_online\_check\_in\_experience page, the "Check-in" button was grayed out. They wanted to know why.

### Resolution

The answer to why the "Check-in" button was permanently grayed out is a two-part answer:

-   PART 1:  
      
    -   On the wu\_location\_queue record, there is a related list for Reason for visit. In this, the user can enable a "display text area" option. If this is enabled, it will show an extra text area on the screen where the user can enter additional information.  
          
        Note that if this field is enabled for a reason, it is mandatory to submit additional information or else the "Check-in" button remains disabled (grayed out).
-   PART 2:  
      
    -   It was noticed that after disabling this option, the button was working as expected.  
          
        However, if it was enabled, the UI was not rendering the additional text area block.  
          
        On further troubleshooting, it was found that the Out of Box (OOB) template for reason for visit select has the correct code (sp\_ng\_template\_39bb784e23c02300139f121727bf65d7) ...  
          
        ... yet the user was utilizing a cloned widget which had an older version of this template and which did not contain the "fix" to resolve this issue.  
          
        The "fix" was to make sure the system uses a boolean check-in condition ng-show="c.showTextArea".   
          
        Once the above pieces were noted and resolved, everything worked perfectly for the user.
