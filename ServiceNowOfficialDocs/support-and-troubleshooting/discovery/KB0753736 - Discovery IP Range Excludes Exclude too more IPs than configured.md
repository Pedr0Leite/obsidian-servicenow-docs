---
title: "Discovery IP Range Excludes: Exclude too more IPs than configured"
aliases:
  - KB0753736
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753736
kb_number: KB0753736
last_modified: 2024-04-07
---

## Issue

# Symptoms

Have a very large discovery schedule with many IPs.

Have also configured this schedule to exclude a large portion of IPs. 

When running the schedule, some of the IPs that are not supposed to be excluded from discovery are excluded. 

# Release

This solution can only be implemented on instances that are on Kingston Patch 6 and higher.

# Cause

The cause stems from the large size of the shazzam payloads; since each excluded IP is individually added to the shazzam payload package. The Shazzam payload that is set out and set back is much too large and may not capture everything during processing. 

This makes processing of the payload inefficient and in some cases breaks the shazzam payload altogether. 

# Resolution

See: [Control Shazzam Payload Size](https://docs.servicenow.com/csh?topicname=t_ConfigureTheShazzamProbe.html&version=latest#configure-shazzam-payload-size "Control Shazzam Payload Size")

Add system property as defined in that document.

Property to add: glide.discovery.shazzam\_ranges\_json

Set value to true.

1.  In the navigation filter, type sys\_properties.list and press Enter.
2.  Click New in the list view of system properties.
3.  Complete the form, using these field values:
    
    -   Name: glide.discovery.shazzam\_ranges\_json
    -   Description: Encodes the Shazzam payload in JSON.
    -   Value: true
    
4.  Click Submit.

This will convert shazzam payload from XML to JSON format.

JSON format decreases the physical size of the payload greatly and makes processing of the payload much faster and efficient. 

You may want to do this change regardless if this issue or not as it will help with shazzam probe processing. 

# Additional Information

Some instances may already have this property set to true. 

If it is set already and IPs are still excluded, please open a Case with Technical Support.
