---
title: "Long-running SSH task produces no output"
aliases:
  - KB0750844
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750844
kb_number: KB0750844
last_modified: 2024-04-07
---

## Issue

# Overview

This article explains what happens when you test an SSH activity with the long running parameter enabled .

# Context

When you run the SSH activity, it will create a directory under the /tmp with ".run.(parameter name="ssh\_long\_id" value="<id>") . This parameter can be found in the ecc queue input   record. 

So if the output of the actvity contains, sncrun:.run.<ssh\_long\_id>, the hidden directory is created in the following format . 

/tmp/..run.(parameter name="ssh\_long\_id" value="<id>") 

In this directory are the following files as logged in the ecc input:   
  
command   
complete   
nohup.out   
nohup.out2   
stub2 

If you set "long running" in SSH activity and run the activity using Test button, the MID will response with acknowledge that it received the long running command. When the long running command completes, then the actual execution data will be sent back in the ECC queue. If you can look at the ECC queue for the "SSHCommandLong" input entry, you will see the same ECC result as you see in the activity designer test window.

If you use the TEST button, the activity will not wait the final execution results. It returns the first handshake with the MID, this is why you will get " sncrun:run.<ssh\_long\_id>"

If you run the long running SSH activity in the WorkFlow, the activity will wait the final output comes back from the ECC queue, the activity completes with the final execution result.

# Example

Please find the example output in the![](sys_attachment.do?sys_id=b9fb6ceadb42b450e515c223059619ae) screenshot

# Additional Information

More detailed implementation details are found in the below community article :   
  
[https://community.servicenow.com/community?id=community\_article&sys\_id=d3430119db91bb48200f0b55ca9619d7](https://community.servicenow.com/community?id=community_article&sys_id=d3430119db91bb48200f0b55ca9619d7)
