---
title: "MID Server agent log is not updated"
aliases:
  - KB0725019
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725019
kb_number: KB0725019
last_modified: 2024-04-07
---

## MID Server agent log is not updated

  

### Issue

# Description

* * *

You observe the agent logs are not being updated/created and the following error message in the wrapper.log:

SEVERE: Failed to resolve default logging config file: config/java.util.logging.properties

# Solution

* * *

1.  Run the following from MID Server > Scripts - Background:  
    ms.log(Packages.java.lang.System.getProperty('java.util.logging.config.file')); 
2.  If the value is null, this means that the client has overwritten the java property for defining the logging directory.   
      
    
3.  This value is set in wrapper.conf:  
    wrapper.java.additional.101=-Djava.util.logging.config.file=properties/glide.properties 
4.  When investigating java errors, some solutions found state to set additional java parameters. If copied and pasted (additional.101), this could be overriding the above parameter. It may also be overridden in a custom JAR file.
5.  Revert the changes, or change the logging config statement to an unused parameter value. 

# Applicable Versions

* * *

All

# Additional Information

* * *

Note that this can apply for other java parameters that the client may accidentally override in the configuration files or with a custom JAR
