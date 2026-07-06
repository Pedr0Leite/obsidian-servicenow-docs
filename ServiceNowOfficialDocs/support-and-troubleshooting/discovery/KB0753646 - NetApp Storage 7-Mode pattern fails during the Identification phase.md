---
title: "NetApp Storage 7-Mode pattern fails during the Identification phase"
aliases:
  - KB0753646
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753646
kb_number: KB0753646
last_modified: 2024-04-07
---

## Issue

# Symptoms

-   Discovery towards the NetApp 7 mode storage server fails using the OOTB "NetApp Storage 7-Mode" pattern during the Identification phase with below error in the input payload.

{  
"status" : "FAILED",  
"message" : "Identification sections in pattern failed: section: identification, error: JAVASCRIPT\_CODE\_FAILURE: Caused by error in Ad hoc script 'EvalClosure-Filter invalid serials' at line 5\\n\\n 2: var rtrn = '';\\n 3: var currentSerialNumber = cmdb\_serial\_number\_\_\_serial\_number;\\n 4: \\n==> 5: rtrn = currentSerialNumber.match(/unknown|empty/i)?\\"true\\":\\"false\\";\\n. ",  
"log" : "H4sIAAAAAAAAAO1abW/aSBD+ftL9hxFf0kpAeUka1SfuxIFTcWoB1eSup1BZG3uAVexdd3dNyqX5\\n713bmJfEuZRT2JwqPoE99jwz88w8Xq988/NPACVGQiyBBaUulR6fo1jAOz4tlVOjVETFMjWftXvv\\nzj/YS4M3o4EvkCWmC7hJzm36cjBAT1E2hSFRCgWDCRdgf0EvVpSzzIm+gfrp5RKVG2UXuqmP3L6B\\n75x3OrbjrEwBzjFILI38TIhSkinKrZjW51MvjVr9TaX2ulKvQb1h1Y+t41Mrj9GCPqp2FIGjuNA3\\nwGnlPfexlDm6Le/iUmfUVkrQy1jhi2Vq5UL3L/OMknR1ToKqRcaH/fv52xwcPuVZqkWU4fYHfTs1\\nryNbE0B9ZIpOqEe26v0Qnw8xuunyLSqQC6kwBMomfDPsB1na5KlZvlu+u0ztXFgiprK8UcB/K+E2\\ngztDfY71ZJSz/CtTVJWkBmagBco4UB91l87KCqUymPBAdHgYEuYbBJbz0BSpaf+wOAgMZrYnuBOr\\n2bDWCguKhmjB8XHz9ARC+d14K53ZVBpnZA/d0d9Du0gKt/TBxzn1ECY6R9AgckN7jOlEVgkjOlEA\\ndU8nlmUwg77Phi6A22dDv05G6H5DN+q1N4YausckCt3TRBFQHLzQv3Q96srs8e1qo4Y13t5ZXbZo\\nKI6sfPHJGC01s5RMqAiviUB3OVy70tMfDPdHjaMwAo8zn6YFohImJJBYBZkYGFeAafXQr/5o9HQE\\nEoW6OQUlAbA4vESRzY/g1/+HSckic7PI3CQyV0dWvrjZMrRuf9jJiYhYreKXNOnZKS7LYXaegaBt\\nbpYjlMvbFk8HekzS0/b95fD8V2aeYU2wFZUKo/tCp3Pdo9g9EpHpcJ6rd85ooHSvUDYnAfWXHSSL\\nu+TOtszTd8kf7T/bTudDbzhyO4Ou7S4BLeiQWKIPlwtAIXgSLrR9mHEPpCdopODI1vF3Ai5jgZXi\\nnI6AKAgoQzgZszHLYtJvDXMiQCjBoAVHR7/khmZm8GIhkCknddHP5qpVMFauu3288qOzGrNW61f9\\n98TKcQq8VkOivNmLVzG7YvyafcUwUotX9OVv45ISMY5L1riUCtq4pH1XD6X63lKZGthm/ekndr2z\\nen9HeXVXr2v3R72zXqc96g36rmN30t+Vn9zL2kctOy4c1Me3jUZEXiWPVxEzluyi6wq873Uhe6eB\\nv9pOv/vRqTXqw2rAWaPqe1VJFakSFKt92YdKs7FbvNvuVaF+b6j1fgALXmuNgkacB4YgaeQS3xf6\\nXsM56hWdEjwIjBd3zoM4REOgE0+TKZQpMqUnqYtfDEIyVNdcXOkmIpEyxqUuq9Es896Z0ADljAhT\\n7eNTeXUQvIPgHQTvIHgHwXsaqPybD73MTRb4bsh9LM+4oP/oASXB48D5svvuRxG33wBV3e3e3CIA\\nAA==",  
"results" : {  
}  
}

-   Also in the respective "NetApp Storage 7-Mode" Pattern log could see below errors in the Identification steps "Filter invalid serials",

Filter invalid serials   
2019-07-01 10:02:54: JAVASCRIPT\_CODE\_FAILURE: Caused by error in Ad hoc script 'EvalClosure-Filter invalid serials' at line 5   
  
2: var rtrn = '';   
3: var currentSerialNumber = cmdb\_serial\_number\_\_\_serial\_number;   
4:   
\==> 5: rtrn = currentSerialNumber.match(/unknown|empty/i)?"true":"false";   
. JAVASCRIPT\_CODE\_FAILURE: Caused by error in Ad hoc script 'EvalClosure-Filter invalid serials' at line 5   
  
2: var rtrn = '';   
3: var currentSerialNumber = cmdb\_serial\_number\_\_\_serial\_number;   
4:   
\==> 5: rtrn = currentSerialNumber.match(/unknown|empty/i)?"true":"false";   
2019-07-01 10:02:54: Execution time: 0 ms   
2019-07-01 10:02:54: JAVASCRIPT\_CODE\_FAILURE: Caused by error in Ad hoc script 'EvalClosure-Filter invalid serials' at line 5   
  
2: var rtrn = '';   
3: var currentSerialNumber = cmdb\_serial\_number\_\_\_serial\_number;   
4:   
\==> 5: rtrn = currentSerialNumber.match(/unknown|empty/i)?"true":"false";   
. JAVASCRIPT\_CODE\_FAILURE: Caused by error in Ad hoc script 'EvalClosure-Filter invalid serials' at line 5   
  
2: var rtrn = '';   
3: var currentSerialNumber = cmdb\_serial\_number\_\_\_serial\_number;   
4:   
\==> 5: rtrn = currentSerialNumber.match(/unknown|empty/i)?"true":"false";   
2019-07-01 10:02:54: Execution time: 0 ms 

# Release

-   Kingston and later releases.

# Environment

-   Discovery that can find NetApp servers, using patterns.

# Cause

-   The connectivity between the MID server host and target NetApp server couldn't establish due to incorrect/bad Basic Authentication provided.

# Troubleshooting

In order to troubleshoot further follow the below steps,

-   Enable the parameter "mid.log.level" to "debug" and restart the MID server service.
-   Post the service restart, re-run the discovery towards the target NetApp server.
-   Once completed grab the "agent.log" and you could able to see below errors,

07/03/19 09:53:13 (169) Worker-Interactive:HorizontalDiscoveryProbe-3b08d4a3dbd6ff40dc0aea42ca9619de DEBUG: **NetAppConnectionFactory: Can't connect to the device with the following credentials: 7 mode testing 2, using HTTPS.**  
**Reason: Connection timed out: connect**&#13;  
07/03/19 09:53:17 (325) RefreshMonitor.65 DEBUG: Event: RGRPerfMetricEvent&#13;  
07/03/19 09:53:17 (450) RefreshMonitor.65 DEBUG: Event: RefreshInstanceInformationEvent&#13;  
07/03/19 09:53:34 (200) Worker-Interactive:HorizontalDiscoveryProbe-3b08d4a3dbd6ff40dc0aea42ca9619de DEBUG: **NetAppConnectionFactory: Can't connect to the device with the following credentials: 7 mode testing 2, using HTTP.**  
**Reason: Connection timed out: connect**&#13;  
07/03/19 09:53:34 (200) Worker-Interactive:HorizontalDiscoveryProbe-3b08d4a3dbd6ff40dc0aea42ca9619de DEBUG: NetAppConnectionFactory: connection failed authentication for key NetAppConnectionPoolKey\[target:&amp;port:0&amp;fixed\_cred:&amp;tag:\]&#13;  
07/03/19 09:53:34 (200) Worker-Interactive:HorizontalDiscoveryProbe-3b08d4a3dbd6ff40dc0aea42ca9619de DEBUG: NetAppConnectionFactory: Authentication failure. Blacklisting key NetAppConnectionPoolKey\[target:&amp;port:0&amp;fixed\_cred:&amp;tag:\]&#13;  
07/03/19 09:53:34 (216) Worker-Interactive:HorizontalDiscoveryProbe-3b08d4a3dbd6ff40dc0aea42ca9619de \*\*\* Script: com.snc.automation\_common.integration.exceptions.AuthenticationFailedException: Adding target to blacklist. **No valid credential found for type \[BASIC\_AUTH\]**&#13;  
07/03/19 09:53:34 (216) Worker-Interactive:HorizontalDiscoveryProbe-3b08d4a3dbd6ff40dc0aea42ca9619de DEBUG: Event: GenericScalarMetricEvent&#13;  
07/03/19 09:53:34 (216) Worker-Interactive:HorizontalDiscoveryProbe-3b08d4a3dbd6ff40dc0aea42ca9619de Slow execution (42376ms) of script: ad\_hoc:EvalClosure-Get system info&#13;  
07/03/19 09:53:34 (216) Worker-Interactive:HorizontalDiscoveryProbe-3b08d4a3dbd6ff40dc0aea42ca9619de DEBUG: (82)EvalClosure - &lt;error&gt;  
**Failed connecting to device.**  
**Please verify you have valid credentials and the device is reachable via the MID server.**  
**For more information go to MID logs**

-   This message comes from NetApp API "**NaServer.invokeElem()**"
-   This is NetApp SDK.

# Resolution

-   The error reported in the agent.log is related to connectivity issues where the Basic Auth configured is incorrect.
-   In order to resolve this Customer should check their connectivity to the device using some 3rd party tool like ZAPI (zExplorer).
