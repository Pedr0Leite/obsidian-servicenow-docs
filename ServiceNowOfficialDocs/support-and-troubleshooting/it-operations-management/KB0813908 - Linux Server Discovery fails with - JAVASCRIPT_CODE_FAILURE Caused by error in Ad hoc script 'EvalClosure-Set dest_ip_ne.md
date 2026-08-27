---
title: "Linux Server Discovery fails with - JAVASCRIPT_CODE_FAILURE: Caused by error in Ad hoc script 'EvalClosure-Set dest_ip_network for each route' at line 6"
aliases:
  - KB0813908
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813908
kb_number: KB0813908
last_modified: 2025-06-06
---

## Linux Server Discovery fails with - JAVASCRIPT\_CODE\_FAILURE: Caused by error in Ad hoc script 'EvalClosure-Set dest\_ip\_network for each route' at line 6

  

### Issue

When running a Discovery on a Linux Server, below error may be encountered.

Failed Exploring CI Pattern, Pattern name: Linux Server, To Check Pattern Log Press

![HorDisc](sys_attachment.do?sys_id=a5b32009dbc8f0d016d2a345ca961973 "Horizontal Discovery")  
  

Here is the text of the error message

```
Set dest_ip_network for each route2019-10-14 15:05:23: JAVASCRIPT_CODE_FAILURE: Caused by error in Ad hoc script 'EvalClosure-Set dest_ip_network for each route' at line 63: var SncIPAddressV4 = Packages.com.snc.commons.networks.IPAddressV4;4: var SncIPNetmaskV4 = Packages.com.snc.commons.networks.IPNetmaskV4;5:==> 6: var ip = SncIPAddressV4(route_table___destination);7: var netmask = SncIPNetmaskV4(route_table___mask);8: var network = SncIPNetworkV4(ip, netmask);9:com.snc.commons.networks.Address32Bit.stringToBytes(Address32Bit.java:363)com.snc.commons.networks.Address32Bit.stringToBytes(Address32Bit.java:323)com.snc.commons.networks.Address32Bit.<init>(Address32Bit.java:114)com.snc.commons.networks.IPAddressV4.<init>(IPAddressV4.java:77)sun.reflect.GeneratedConstructorAccessor145.newInstance(Unknown Source)sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)java.lang.reflect.Constructor.newInstance(Constructor.java:423)org.mozilla.jav
```

On reviewing the pattern logs, we can see that the above error is triggered by step 'Set dest\_ip\_network for each route' in 'Linux Server' pattern

![pattern](sys_attachment.do?sys_id=2db32009dbc8f0d016d2a345ca961991 "Pattern")

The cause cause of failure from the above steps is actually the logic used in the previous step 'Extract routes'.  Reference the screenshot below and notice that the first entry returned is a text and not a valid IP.

![pattern](sys_attachment.do?sys_id=a1b32009dbc8f0d016d2a345ca961993 "pattern")

### Release

Any

### Cause

-   At Step 4.2.19, you will notice that Pattern captures the route information, by running the "route -n" command. The result of it is then stored in the table named "$routeOut"
-   After that, the pattern uses this information in step 4.2.25, as demonstrated in the screenshot in the description.
-   It seems the rule here is capturing the headers as well, which is not desired.
-   In the screenshot, the headers (Ziel, Router, Genmaks, Flags, etc) are highlighted, which means that they are being captured with the parsing type we are using on that step.
-   Finally, on step 4.2.26 the eval script is failing, because we are expecting a Valid IP, however, we encounter a string.

### Resolution

To fix this issue below changes must be made:

1.  Updated the 'Shared Libraries' - "**4\. Linux - Identity**" and "**4.2. Linux - Network**".  
    -   Updated Workaround for both Shared Libraries are attached to this KB, in XML format.  The files can be imported using [this document](https://docs.servicenow.com/csh?topicname=t_ImportARecordAsXMLData.html&version=latest "this document").
2.  On Step 'Get the routes and gateway' notice that  
    -   The command is changed from "route -n" to "route -n | egrep -v -i 'flags|kernel'"
    -   Both Include and Exclude lines are cleared and left empty.
3.  On Step "4.2.20. Extract the gateway", notice that the word "Destination" is removed from Exclude Lines.  It is empty.
4.  On Step "4.2.25. Extract routes", notice that both Include and Exclude lines are cleared and left empty.
