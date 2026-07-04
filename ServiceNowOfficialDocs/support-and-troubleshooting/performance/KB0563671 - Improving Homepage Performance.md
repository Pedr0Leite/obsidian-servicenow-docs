---
title: "Improving Homepage Performance"
aliases:
  - KB0563671
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0563671
kb_number: KB0563671
last_modified: 2026-05-04
---

## Issue

Homepages are a very powerful part of ServiceNow. They allow users or groups to keep their eye on important metrics, increasing productivity and team coordination. However, because of the flexibility and power of homepages, they are also a common area of performance issues for many customers. The article contains recommendations that may help your organization make the most out of homepages. As a ServiceNow administrator, you can use these recommendations to review your current configuration and ensure your users have the most optimal combination of powerful functionality and efficient performance.

### Recommendations for improving homepage performance

**Set your global default homepage user preference to a very lightweight homepage**  
  

1.  Navigate to **User Administration > User Preferences**.
2.  Query to see if there is any record where:  
    -   **Name** = homepage
    -   **System** = true
3.  If yes, select and copy the sys\_id in the **Value** field into your clipboard. If no, proceed to step 4.  
    -   Determine the current default global homepage by going to: https://<instancename>.service-now.com/sys\_portal\_page.do?sys\_id=<sys\_id\_you\_copied\_in\_step\_3>
    -   If the homepage is lightweight already then there is nothing further to do. If not, delete the user preference in step 3 and proceed to step 4
4.  Click **New**.  
    -   Set the following:  
        -   **Name** to homepage
        -   **Value** to <sys\_id\_of\_lightweight\_homepage>
        -   **User** to blank
        -   **System** to true
    -   Click **Submit**.

**Aim for no more than 4 gauges per pages**

Split into other pages if more are needed.  
  

**Always report on current (active=1) data**

Gauges that show trending on historical or inactive data should be moved to Reports.  
  

**Maximize Homepage multi-threading**

Homepage refresh causes session synch waits and causes other transactions to be queued waiting for homepage reloads to complete. Allow multi-threaded homepage rendering. Tune if already allowed. Do not put slow gauges on the same page as fast gauges - this defeats the advantage of multi-threading  
  

**Troubleshoot and fix the slowest/most common homepages**

1.  Use **Transaction Logs** to pinpoint users with consistently slow homepages.  
    -   Filter for **Created** = Last week (this might be too much data for your instance depending on usage - reduce time frame if necessary)
    -   Filter for **URL** STARTSWITH "/home.do"
    -   Filter for **Response** is greater than 8000 milliseconds
    -   Group by **Created By** to see the users viewing their homepage most frequently
2.  Search the **User Preferences** table to determine what homepage users have set as their default homepage.
3.  After you have identified a slow/frequent homepage that you want to improve, use Debug Homepage Render to pinpoint problematic gauges.  
      
    

**Think carefully about allowing non-admin users to create their own custom homepages**

Limiting the number of custom homepages can improve performance.

**Force all users to hit a standard simple landing page after login**  
  
This solution involves the creation of a customer page. Some advanced scripting knowledge is required. For all users, instead of going directly to their homepage after login, they are directed instead to a simple page that loads quickly. The page will have a link to go to their custom homepage if they want (this speeds up log in and isolates user-specific behaviors).

Configuring a standard simple landing page:

1.  Set the property **glide.login.home** to **loginredirection.do**.
2.  Create a custom processor called **Login Redirect** with a path of **loginredirection**. Use script such as:  
    
    if (gs.getUser().isMemberOf("grp-dtc-demandeur-manuel-portail")){  
        g\_response.sendRedirect("dtc");  
    } else {  
        if (!gs.getUser().hasRole("admin")) {  
           if (!gs.getUser().hasRole("itil")) {  
            g\_response.sendRedirect("Welcome.do");  
           } else {  
            g\_response.sendRedirect("Welcome.do");  
           }  
        } else {  
           g\_response.sendRedirect("Welcome.do");  
        }  
    }  
    
3.  Define a custom Jelly UI page named Welcome.do that contains the HTML you want to put on the screen, together with the link to view your homepage (/home.do). In addition to the link in the custom UI page, users can still navigate to their homepage via the homepage drop-down selections in the upper right corner of the ServiceNow header bar or using the **Self Service - homepage** module (in the Application Navigator).

## Resolution

.
