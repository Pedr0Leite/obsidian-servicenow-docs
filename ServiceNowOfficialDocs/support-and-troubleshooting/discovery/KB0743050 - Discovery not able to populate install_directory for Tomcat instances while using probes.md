---
title: "Discovery not able to populate \"install_directory\" for Tomcat instances while using probes"
aliases:
  - KB0743050
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0743050
kb_number: KB0743050
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

Discovery not able to populate "install\_directory" for Tomcat instances while using probes.

# Steps to reproduce

* * *

01) Run discovery on any Unix machine which runs a Tomcat server on it.

02) Please make sure that you are using probes under processes classifier 'Tomcat'.

# Cause

* * *

For probes and sensors we did not populate this data.

From the docs, it is mentioned that we collect installation directory information for unix and source of the data was "server.xml".   
  
[https://docs.servicenow.com/csh?topicname=r\_DataCollDiscoTomcatServers.html&version=latest](https://docs.servicenow.com/csh?topicname=r_DataCollDiscoTomcatServers.html&version=latest)   
  
But while looking at the probe Tomcat - Get server.xml, we don't see anywhere getting installation directory information.

# Resolution

* * *

We suggest using the "Tomcat" pattern if this information is needed.   
  
There is no fix for this, as this is expected result using probes.
