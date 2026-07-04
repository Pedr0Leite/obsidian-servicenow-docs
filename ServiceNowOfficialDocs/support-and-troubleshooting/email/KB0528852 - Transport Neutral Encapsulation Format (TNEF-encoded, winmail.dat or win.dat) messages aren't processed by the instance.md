---
title: "Transport Neutral Encapsulation Format (TNEF-encoded, winmail.dat or win.dat) messages aren't processed by the instance"
aliases:
  - KB0528852
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0528852
kb_number: KB0528852
last_modified: 2026-05-28
---

## Transport Neutral Encapsulation Format (TNEF-encoded, winmail.dat or win.dat) messages aren't processed by the instance

  

### Issue

Transport Neutral Encapsulation Format (TNEF-encoded, winmail.dat or win.dat) messages aren't processed by the instance Transport Neutral Encapsulation Format or TNEF is a proprietary email attachment format used by Microsoft Outlook and Microsoft Exchange Server. An attached file with TNEF encoding is most often named winmail.dat or win.dat, and has a MIME type of Application/MS-TNEF.  

These files are not understood by the instance

### Symptoms

-   Emails from some Microsoft clients or using Exchange server do not get processed.
-   Incoming emails from those clients contains a winmail.dat file attached
-   The body of the email does not contains the information required.

### Release

  N/A

### Cause

Processing of rich formatting or TNEF-encoded messages is not available at this time.   
  
When customers send TNEF-encoded messages to technical support, it includes two parts:  
TNEF-encoded, base64 strings which contain rich-text that Outlook understands but most mail clients don't (also images and attachments)  
Plain text versions of the text.  
  
Often, these messages include an attachment named "winmail.dat".

### Resolution

Customers can disable **TNEF** on their Exchange server for messages sent to ServiceNow, thereby forcing the messages to send in MIME-types encoding instead.  
  
The exchange setting that can be enabled per-domain to resolve this: [Set-RemoteDomain](http://technet.microsoft.com/en-us/library/aa997857.aspx)

**TNEFEnabled:** 

The TNEFEnabled parameter specifies whether Transport Neutral Encapsulation Format (TNEF) message encoding is used on messages sent to the remote domain. Valid values for this parameter are $true, $false, or $null. The action associated with each value is as follows:   
\- $true TNEF encoding is used on all messages sent to the remote domain.   
\- $false TNEF encoding isn't used on any messages sent to the remote domain.   
\- $null TNEF encoding isn't specified for the remote domain.

TNEF encoding for recipients in the remote domain may be specified by the following:   
\- Value of the UseMapiRichTextFormat parameter for any mail user or mail contact objects   
\- Sender's per-recipient settings in Microsoft Office Outlook   
\- Sender's default Internet message settings in Outlook   
\- The default value is $null

It should be possible to set this to $false for "service-now" in the Exchange server, which should force the message to be sent with a plain text portion and an HTML portion, both of which should be readable by the system. Your exchange admin can consider trying this option for the service-now domain.
