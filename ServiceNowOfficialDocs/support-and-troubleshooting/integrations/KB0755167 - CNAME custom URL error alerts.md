---
title: "CNAME custom URL error alerts"
aliases:
  - KB0755167
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755167
kb_number: KB0755167
last_modified: 2024-11-08
---

## CNAME custom URL error alerts

  

### Issue

For instances that use the Custom URL feature we monitor the CNAME DNS entry for the custom url that is used to link to your instance to make sure that it is valid. If we detect an issue, a case is automatically created title "CNAME custom URL error".

You can check the CNAME DNS entry for your domain by typing in the terminal (and replacing '<example.domain.com>' with the domain you want to check)

$ dig -t CNAME <example.domain.com> +noall +answer  
  

For instances that use the Custom URL feature we monitor the CNAME DNS entry for the custom url that is used to link to your instance to make sure that it is valid. If we detect an issue, a case is automatically created title "CNAME custom URL error".

### Cause

As part of configuring a Custom URL for your instance we make sure that there is a valid CNAME entry on the DNS servers for the domain you wish to use to point to the instance. An example valid CNAME entry on the DNS would look like this:

example.domain.com. 60 IN **CNAME** instance.service-now.com.  
  

If we detect that this CNAME entry on the DNS does not point to your instance we will create an alert to let you know as the custom URL will not point to your instance when you try to access it. 

Please note A records are NOT supported and the DNS record needs to be defined as **CNAME**

Also, defining the custom URL against a 3rd party reverse proxy is not supported.

### Resolution

Please confirm that you are using the custom URL feature

1.  If the Custom URL is still being used on your instance (there is a custom URL record) then you will need to contact the admin that is responsible for the DNS entry for your domain and ask them to update the CNAME entry to point to the instance.  
      
    
2.  If you are no longer using the Custom URL feature then please remove the custom URL record from the instance. You should then notify support on the alert to let them know that it is no longer being used for the instance. You can find the custom URL record and delete button on the following screenshot:
    
    ![Delete Custom URL](sys_attachment.do?sys_id=05c9dcf493bdde505736b25d6cba1059 "Delete Custom URL")
