---
title: "Receiving error smbios: failed to load SMBIOS: System does not export an SMBIOS table in Serial Number"
aliases:
  - KB0744463
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744463
kb_number: KB0744463
last_modified: 2024-04-07
---

## Receiving error smbios: failed to load SMBIOS: System does not export an SMBIOS table in Serial Number

  

### Issue

# Symptoms

Multiple Solaris Servers may only be discovered, but only one ci is created.  If you look at the CI record you may see the name changing several time.  You may also see the following error "smbios: failed to load SMBIOS: System does not export an SMBIOS table in Serial Number"

# Cause

When we run sneep to get the serial number information, the command was not found. Then discovery tires to get the serial number via the smbios command.   
  
Now, it returns "smbios: failed to load SMBIOS: System does not export an SMBIOS table" since the command also fails. We assigned that value as a serial number. The hardware identifier uses serial number as it's first identifier. Since, we're received the same error messages for the Solaris servers, discovery thinks it's the same device. 

\--example  
1\. It looks like it tried to run "sneep -T | grep ChassisSerialNumber", but the command was not found   
  
2\. Then it tries to get serial number for the smbios command and it's failing   
  
Get serial number using smbios command   
2019-03-12 08:14:06: Executing SSH command: smbios -t SMB\_TYPE\_SYSTEM | grep Serial | cut -d ':' -f2-   
2019-03-12 08:14:06: Command result: smbios: failed to load SMBIOS: System does not export an SMBIOS table   
2019-03-12 08:14:07: setAttribute(cmdb\_serial\_number\_temp,\[{serial\_number=smbios: failed to load SMBIOS: System does not export an SMBIOS table}\])   
2019-03-12 08:14:07: Execution time: 252 ms   
Insert serial numbers   
2019-03-12 08:14:07: setAttribute(cmdb\_serial\_number,\[{serial\_number\_type=SMB\_TYPE\_SYSTEM, serial\_number=smbios: failed to load SMBIOS: System does not export an SMBIOS table}\])   
2019-03-12 08:14:07: Execution time: 0 ms   
Insert serial number to Solaris CI   
2019-03-12 08:14:07: setAttribute(cmdb\_ci\_solaris\_server\[\*\].serial\_number,smbios: failed to load SMBIOS: System does not export an SMBIOS table)   
2019-03-12 08:14:07: Execution time: 0 ms   
  
  

# Resolution

1.  Modifying the Solaris discovery pattern to exclude the error message "failed to load".   
    a. Go to the solaris Server pattern and change step 6.1.3   
    b. add "failed to load" in the "Exclude Lines" area   
    c. Save   
    d. published.   
      
    2\. You can enter "failed to load SMBIOS" as an invalid serial number.   
    a. go to the invalid serial number table  
    b. click on new and add "failed to load SMBIOS"

          3.  Make sure that you have the correct permission to run the command to get the serial number: sneep smbios
