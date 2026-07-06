---
title: "Discovery Process Classifier Filter is Case Sensitive"
aliases:
  - KB0696691
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696691
kb_number: KB0696691
last_modified: 2024-04-07
---

## Issue

# Overview

* * *

Discovery Process Classifiers are used to launch probes or patterns so we can explore running applications in a  Configuration Item like for example a Linux or Windows Server.  These

process   classifiers  have conditions  which should match  one of the parameters in the running processes records which is created or updated during Discovery.   The  filters  are case

sensitive so if  you are creating custom classifiers you should take this into account.

# Example

* * *

 If we look at the out-of-the-box JBoss Server Process Classifier we have two conditions either of which should be met for the classifier to run.  The first condition is parameters contains

"org.jboss.Main" and the other condition is parameters contain "org.jboss.as".  Please note the upper case "M" in the first condition.  

![JBoss Process Classifier](sys_attachment.do?sys_id=15fb6ceadb42b450e515c22305961947 "JBoss Process Classifier")  

This means that we will be looking for running processes that has a parameter that contains "org.jboss.Main" as one of the conditions. The record being checked for the match is from the

Running Processes table which is normally in the related lists of the Unix, Linux or Window Server form. The image below is for illustration purposes and from an out-of-the box Linux Server 

form.  It does does not contain records to match the JBoss Process Classifier condition.  Note that the values in Parameters and Key Parameters are set as uppercase  and lowercase  letters

just as how the Discovery probes received the response from  the Servers.

![Running Processes](sys_attachment.do?sys_id=adfb6ceadb42b450e515c2230596194c "Running Processes")

# Additional Information

* * *

The Name and Command fields can also be used as one of the conditions and these are case sensitive as well.  The PID(process id) field is stored in the database without a comma "," so

don't use any comma when you want to use this as a condition.  But then again PIDs normally changes when an application restarts so it is not advisable to use this in the condition.
