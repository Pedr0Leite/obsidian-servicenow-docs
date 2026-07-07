---
title: "Running a pattern extension is returning \"Test failed: Make sure the steps are compatible with the current attributes and variables values\"
aliases:
  - KB0723732
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723732
kb_number: KB0723732
last_modified: 2024-07-31
---

## Running a pattern extension is returning "Test failed: Make sure the steps are compatible with the current attributes and variables values"

  

### Issue

Debugging a pattern's custom extension would show us an error as "Test failed: Make sure the steps are compatible with the current attributes and variables values". Example screenshot:

![](sys_attachment.do?sys_id=a94632b51b5ef014ed6c9979b04bcbe9)

### Cause

There is more than one reason why this error may happen.

#### Large payload

Debugging a pattern may bring in more data than a pattern can process. "mid.discovery.max\_pattern\_payload\_size" is the property that defines the maximum overall payload size for the payload of results that come from patterns. OOB this is default to 300000 bytes.

Refer more information from below documentation :

[https://docs.servicenow.com/csh?topicname=r\_MIDServerProperties.html&version=latest](https://docs.servicenow.com/csh?topicname=r_MIDServerProperties.html&version=latest)

#### Errors on previous section

This error may also happen if one of the previous sections being run is terminated due to an error in the pattern.

### Resolution

#### Large payload

1.  Run the pattern debug by enabling mid server debug and in the logs, look for an error that says.
    
    Step failed: Debugging Pattern Failed, Payload size is bigger than the Maximum Size : 5242880 Please check mid.discovery.max\_payload\_size property&#13;
    
    **Note:** Logs may show a property "mid.discovery.max\_payload\_size", but the actual property used for patterns is "mid.discovery.max\_pattern\_payload\_size"
2.  If the issue is because of the pattern payload size, Add/Update the value of property : "mid.discovery.max\_pattern\_payload\_size" to a bigger number.
3.  Property can be found under MID Server --> Properties
4.  Direct link for the mid server properties :  
    [MID Server Properties](https://instance_name.service-now.com/ecc_agent_property_list.do "MID Server Properties")

#### Errors on previous section

1.  Run the pattern in debug mode
2.  Make note of the last step which executed
3.  Review the mid server agent log for errors when executing step
4.  Investigate and resolve error
5.  Reach out to support if assistance is needed in resolving the error

### Related Links

-   [Pattern debugger sa\_mapping\_ext\_commands fails due to osFamily and osType set to proprietary](https://hi.service-now.com/kb_view.do?sysparm_article=KB0995089 "Pattern debugger sa_mapping_ext_commands fails due to osFamily and osType set to proprietary")
