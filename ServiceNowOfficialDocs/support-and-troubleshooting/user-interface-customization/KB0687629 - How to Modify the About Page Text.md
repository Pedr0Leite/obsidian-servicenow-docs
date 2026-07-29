---
title: "How to Modify the About Page Text"
aliases:
  - KB0687629
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687629
kb_number: KB0687629
last_modified: 2025-01-07
---

## How to Modify the About Page Text

  

### Issue

  
  

# Description

* * *

By default, the About page displays text describing ServiceNow and its benefits. This text is as follows:

ServiceNow is changing the way people work. With a service-orientation toward the activities, tasks and processes that make up day-to-day work life, we help the modern enterprise operate faster and be more scalable than ever before. Customers use our service model to define, structure and automate the flow of work, removing dependencies on email and spreadsheets to transform the delivery and management of services for the enterprise. ServiceNow provides service management for every department in the enterprise including IT, human resources, facilities, field service and more. We deliver a "lights-out, light-speed" experience through our enterprise cloud – built to manage everything as a service. To find out how, visit [www.servicenow.com](http://www.servicenow.com).

This article describes how to provide your own custom text.

# Procedure

* * *

1.  Navigate to sys\_home.list or go to https://<instance-name>.service-now.com/sys\_home\_list.do.
    
2.  Find the record with the Short Description "About ${gs.getProperty('glide.product.name', 'ServiceNow')}" or go to  
    https://<instance-name>.service-now.com/sys\_home.do?  
    sys\_id=c4a9a9fcc611227501be3bb27e26243c.
    
3.  Scroll to the Text field and modify the text.
    
4.  Click Update to save the record.
