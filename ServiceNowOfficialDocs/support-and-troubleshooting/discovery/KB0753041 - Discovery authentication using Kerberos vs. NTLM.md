---
title: "Discovery authentication using Kerberos vs. NTLM"
aliases:
  - KB0753041
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753041
kb_number: KB0753041
last_modified: 2024-01-10
---

## Discovery authentication using Kerberos vs. NTLM

  

### Issue

When a Discovery authenticates to a host using Kerberos, the client requests a session ticket for the Service Principal Name (SPN). Discovery is IP Based, so Kerberos is generally not used (NTLM is more common), however, we do have a feature where we will attempt to make the connection by host name. This feature is triggered when:

1\. WinRM is enabled.  
2\. The target host is in a domain.  
3\. The target IP is not in the list of trusted hosts on the MID server host.  
4\. We successfully perform a reverse DNS lookup on the IP to get a host name.

\*All of these conditions must be met or Kerberos Authentication will not work.

Please keep in mind that if the DNS reverse lookup is not working correctly, Discovery will fall back to using an IP Address for authentication, which would cause Kerberos authentication to fail. Please plan accordingly.

### Related Links

For further information see:

[KB1156845 - Troubleshooting Kerberos authentication during Discovery](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1156845)
