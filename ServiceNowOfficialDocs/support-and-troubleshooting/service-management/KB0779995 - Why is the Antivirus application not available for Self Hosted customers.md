---
title: "Why is the Antivirus application not available for Self Hosted customers?"
aliases:
  - KB0779995
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779995
kb_number: KB0779995
last_modified: 2024-04-08
---

## Why is the Antivirus application not available for Self Hosted customers?

  

### Issue

Why is the Antivirus application not available for Self Hosted customers?

### Resolution

Unfortunately, ServiceNow does not support Antivirus scanning for self hosted\\on premise environments.  
  
Currently, antivirus scanning is a shared service architecture(sort of like microservices).  
  
We currently have two antivirus scanning servers in each datacenter. Each instance which resides on a specific Data Center uses these servers to scan their attachments.  
  
This is why Self Hosted customers are unable to leverage Antivirus application as your instances do not reside in our Data Centers.  
  
In regards to building a custom Antivirus application, we use a third-party tool to scan attachments. Unfortunately, we are not authorized to share the architecture with other users.
