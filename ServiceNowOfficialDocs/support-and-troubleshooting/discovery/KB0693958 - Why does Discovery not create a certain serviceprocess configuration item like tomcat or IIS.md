---
title: "Why does Discovery not create a certain service/process configuration item like tomcat or IIS ?"
aliases:
  - KB0693958
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693958
kb_number: KB0693958
last_modified: 2024-04-07
---

## Why does Discovery not create a certain service/process configuration item like tomcat or IIS ?

  

### Issue

Discovery is not creating a running service CI for example Tomcat CI cmdb\_ci\_app\_server\_tomcat when the name of the tomcat service does not match tomcat process classifier's criteria. 

### Resolution

 For example, in order to classify a tomcat process, the process name should match the conditions of the process classifier.

{Parameters contains org.apache.catalina.startup.Bootstrap  
OR   
Name starts with tomcat   
OR   
Name starts with k\_nt\_service  
OR   
Name starts with Tomcat  
}   
OR  
{  
Name starts with java   
OR   
Parameters contains tomcat  
}

If the naming convention of your service doesn't match the criteria so the process classifier will not pass and the probe or horizontal pattern responsible on discovering the service will not be triggered.
