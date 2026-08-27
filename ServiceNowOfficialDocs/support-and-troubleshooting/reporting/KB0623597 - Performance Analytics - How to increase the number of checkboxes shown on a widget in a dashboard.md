---
title: "Performance Analytics - How to increase the number of checkboxes shown on a widget in a dashboard"
aliases:
  - KB0623597
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623597
kb_number: KB0623597
last_modified: 2024-04-07
---

## Performance Analytics - How to increase the number of checkboxes shown on a widget in a dashboard

  

### Issue

By default, the number of checkboxes shown on a widget in a dashboard is 25. This number can be increased.

  

Steps to Reproduce

In an instance that has the **Performance Analytics - Premium** plugin enabled:   
  
1\. Create an interactive filter or using an existing one e.g. one with Lookup name "Incident Assignment Group - Single"   
2\. Create some additional groups to ensure you have more than 25 records matching your filter.   
3\. Set your UI control type to Checkbox   
4\. Add your interactive filter to a PA dashboard.   
5\. Notice the widget on the dashboard only shows 25 checkboxes even though you have more. 

   
  

  

### Resolution

The system property "**glide.homepage\_interactivity.ui\_ctrls\_max\_display\_options**" controls the number of elements that will be displayed. This property can be added to your instance and modified to increase the number of checkboxes that can be displayed.

Keep in mind this is global setting and will affect all the widgets on the instance that have checkboxes.
