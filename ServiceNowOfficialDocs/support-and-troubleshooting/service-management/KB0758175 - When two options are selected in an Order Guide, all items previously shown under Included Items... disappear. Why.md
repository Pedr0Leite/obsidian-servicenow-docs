---
title: "When two options are selected in an Order Guide, all items previously shown under \"Included Items...\" disappear. Why?"
aliases:
  - KB0758175
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0758175
kb_number: KB0758175
last_modified: 2024-04-07
---

## When two options are selected in an Order Guide, all items previously shown under "Included Items..." disappear. Why?

  

### Issue

Issue 1: On the order guide "New Employee", when the options "Does the new employee need a computer?" and "Does the new employee need a cellular?" are selected at the same time, all items disappear from the order guide.  
  
(Related) Issue 2: Also, there are three labels for the Catalog Item in question: "hardware", "option" and "business account". The items in "option" need to be in "hardware". There is an unexpected label of "Options". Where is this coming from, and why is it there?

### Resolution

-   Reason:  
      
    -   Regarding Issue 1: After conducting multiple, rigorous tests, it was found that the behavior seen is a result of the code in the deprecated SC Order Guide widget only.
-   Two main issues were faced:  
      
    -   Issue 1: Within the Order Guide "New Employee", when options "Does the new employee need a computer?" and "Does the new employee need a cellular?" were selected simultaneously, all items disappear from the order guide. Why?
    -   Issue 2: There were three labels within the Catalog Item: "Hardware", "Options", and "Business accounts". The items in the "Option" tree need to be under the "Hardware". There is an "Option" label appearing unexpectedly. Why?
-   Most Probable Cause:  
      
    -   As Issue 2 was resolved in an earlier update, Issue 1 will be focused on below:  
          
        The root of the odd behavior lay exclusively within the code of the deprecated SC Order Guide widget. The behavior does not happen in the current and supported SC Order Guide widget. The behavior has also changed in the current, supported widget, and is consistent between the Portal and the Platform UI.
-   Solution Proposed:  
      
    -   Please do not use the deprecated SC Order Guide widget. It is not supported. The behavior seen is isolated only to that widget, and again, the widget is deprecated. When the widget is changed to the current and supported version ("SC Order Guide"), the behavior is no longer an issue.  
          
        Instead of there being a pop-up section of "Included items...", the new widget allows the user to click the "Next" UI Action once they have filled out the initial order information. Then, they can see a tab for options to select on the computer (the first checkbox) and the cellphone (the second checkbox). Both appear just fine. The ordering interface is just a bit different.  
          
        It was confirmed that the Platform UI shares the same behavior as the current and supported widget.
-   Next Steps:  
      
    -   Please use the current and supported widget, "SC Order Guide". The code within the deprecated widget is not supported. To update from the deprecated widget to the current widget, please navigate to the below URL:  
          
        
        -   https://<instance\_name>.service-now.com/sp\_config?id=page\_edit&p=sc\_cat\_item\_guide&table=sp\_instance&sys\_id=10a030e347230200ba13a5554ee4904e
        
          
        At the bottom of the page, there is a "Widget" header where the "SC Order Guide Deprecated" widget is selected. Change this to "SC Order Guide", and the reported behavior ceases.
