---
title: "vCenter probe hangs when target does not respond on port and causes discovery schedule to be cancelled"
aliases:
  - KB0713750
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0713750
kb_number: KB0713750
last_modified: 2024-04-07
---

## vCenter probe hangs when target does not respond on port and causes discovery schedule to be cancelled

  

### Issue

# Overview

* * *

vCenter probes may be triggered incorrectly when discovering IPs where there is no vcenter application. The probe then hangs when the target does not respond. This will cause the discovery schedule to be cancelled if there is a maximum time configured, or be stuck if a maximum time is not configured.

# Steps to reproduce

* * *

1.  Open "Discovery Definition > IP Services"
2.  Search for records where name contains "vmap" and collect the number from the port column
3.  Discover a device where such ports are open but no vcenter application is installed
4.  The probes will be triggered and hang

# Root Cause

* * *

The first phase of discovery, Shazzam, checks for open ports on a target IP address. Probes will be triggered accordingly depending on the open ports. Such ports can be configured under "Discovery Definition > IP Services".

# Solution

* * *

The issue is resolved via PRB1073935 in Kingston. Starting in kingston, a probe parameter was created to pre-validate the vcenter application before sending requests.

To turn on pre-validation: 

1.  Go to "Discovery Definition > Probes"
2.  Open the "VMWare - vCenter Datacenters" probe
3.  Add parameter prevalidate\_vcenter = true  
    ![Pre validate vcenter parameter](sys_attachment.do?sys_id=fa5be86adb42b450e515c223059619b2 "Pre validate vcenter parameter")

For versions prior to Kingston, or depending on the kingston release, the fix can be back ported as follows:

**Warning:** Any changes should be tested in non-production instances first

1.  Add prevalidate\_vcenter = true parameter to "VMWare - vCenter Datacenters" probe
2.  Go to "MID Server > Script Includes"
3.  Open "AVMWareProbe"
4.  Add the following code before the line containing "this.\_getServiceInstance();"
    
    if (this.getParameter('prevalidate\_vcenter') == 'true') {  
        request = new Packages.com.glide.communications.HTTPRequest(this.vmHost + '/vimservice.wsdl');  
        request.setContentType('application/xml');  
        request.setHttpTimeout(30000);  
        response = request.post('<?xml version="1.0" encoding="UTF-8"?>' +  
            '<soapenv:Envelope xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" ' +  
            'xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" ' +  
            'xmlns:xsd="http://www.w3.org/2001/XMLSchema" ' +  
            'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">' +  
            '<soapenv:Body><RetrieveServiceContent xmlns="urn:vim25">' +  
            '<\_this type="ServiceInstance">ServiceInstance</\_this></RetrieveServiceContent>' +  
            '</soapenv:Body></soapenv:Envelope>');  
      
        if (!response || (response.getStatusCode() != 200)) {  
            this.setError('Not exploring as vCenter: unable to fetch WSDL. The WSDL check is controller by the probe parameter "check\_wsdl".');  
            return;  
        }  
    }
