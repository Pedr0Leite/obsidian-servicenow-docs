---
title: "How to grab older MID Server Agent logs,  for when agent0.log.0 entries don't go back far enough"
aliases:
  - KB0685661
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0685661
kb_number: KB0685661
last_modified: 2025-01-03
---

## How to grab older MID Server Agent logs, for when agent0.log.0 entries don't go back far enough

  

### Issue

A MID Server record has the Related Link **"Grab MID Logs"** which will retrieve the current wrapper and agent log from the MID Server, and leave it as an attachment in the ECC Queue. Only agent0.log.0 and wrapper.log will be fetched. However the agent log file contains only the most recent log entries because the logs rotate every 10MB. If you have MID Server debugging turned on during a large Discovery run for example, you may even have less than an hour's worth of logging in that file.

Older logs agent0.log.1, agent0.log.2,..., agent0.log.9 will exist in the ~\\agent\\logs\\ folder that you also may need, and this procedure shows an easy way to grab those too.

### Release

This procedure is now more-or-less obsolete since the introduction of the MID Logs Viewer in New York, and the new related link to go with it. There is a business rule that runs on input, which then creates an output for the older logs.

### Resolution

1.  Open a MID Server form and "Grab MID Logs" in the normal way. You are redirected to an ecc\_queue list that is filtered for the GrabLogs jobs. Refresh this list until the inputs for agent0.log.0 and wrapper.log appear.  
      
    ![](sys_attachment.do?sys_id=653960eedb02b450e515c2230596199d)  
    ![](sys_attachment.do?sys_id=693960eedb02b450e515c223059619a2)  
      
    
2.  Open the Output record for agent0.log.0 in a form, and modify the Name field value "agent0.log.0" to one of the older filenames, such as "agent0.log.1", or anything from 1 to 9.  
      
    ![](sys_attachment.do?sys_id=2d3960eedb02b450e515c223059619a7)  
      
      
      
    
3.  Now click the related link "Run Again".  You will now see a new Output for that other agent log file in the ecc\_queue. Refresh the list until the input arrives back from the MID Server.   
      
    ![](sys_attachment.do?sys_id=ed3960eedb02b450e515c223059619ac)
