---
title: "Troubleshooting LDAP issues in ServiceNow"
aliases:
  - KB0539111
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0539111
kb_number: KB0539111
last_modified: 2025-10-20
---

## Troubleshooting LDAP issues in ServiceNow

  

### Issue

This article guides you through the process of troubleshooting Lightweight Directory Access Protocol (LDAP) issues in ServiceNow. It provides steps to help eliminate the common causes of your problems by verifying that the configuration of your networking is correct.

Symptoms may include:  

-   Users are unable to log in to the system.
-   A single user is unable to log in to the system.
-   The login screen shows an invalid user name or password.
-   Authentication is slow.
-   The user cannot connect to the LDAP server.

### Resolution

Determine whether any of the troubleshooting steps below are true for the environment. Each step provides a link to an article to help users eliminate possible causes and take corrective action as necessary:

1.  Determine if SAML or LDAP is being used in the instance. For more information, see [KB0538787: Determining if SAML or LDAP is being used in the instance](/kb_view.do?sysparm_article=KB0538787 "KB0538787: Determining if you are using SAML or LDAP in your instance").
2.  Talk to your system administrator to determine if there was a change to the network, including VPN and firewalls.
3.  Verify whether the OU definition has changed. For more information, see [KB0538642: Determining if the OU definition has changed](/kb_view.do?sysparm_article=KB0538642 "KB0538642: Determining if the OU definition has changed").
4.  Verify whether the certificate is expired on the instance. For more information, see [KB0538674: Determining if the certificate is expired on the instance](/kb_view.do?sysparm_article=KB0538674 "KB0538674: Determining if the certificate is expired on the instance").
5.  Confirm that the LDAP server is running properly. For more information, see [KB0538675: Determining if the LDAP server is down](/kb_view.do?sysparm_article=KB0538675 "KB0538675: Determining if the LDAP server is down").
6.  Confirm that the LDAP main and failover servers are running. For more information, see [KB0538724: Determining if the main and failover LDAP servers are running](/kb_view.do?sysparm_article=KB0538724 "KB0538724: Determining if the main and failover LDAP servers are running").
7.  Confirm that the LDAP source field is correctly populated. For more information, see [KB0538740: Determining if the LDAP source is missing or misconfigured](/kb_view.do?sysparm_article=KB0538740 "KB0538740: Determining if the LDAP source is missing or misconfigured").
8.  Confirm that the correct LDAP server is configured. For more information, see [KB0538726: Determining if the wrong LDAP server is configured](/kb_view.do?sysparm_article=KB0538726 "KB0538726: Determining if the wrong LDAP server is configured").
9.  Verify if a user is marked inactive or locked. For more information, see [KB0538725: Determining if a user is marked inactive or locked](/kb_view.do?sysparm_article=KB0538725 "KB0538725: Determining if a user is marked inactive or locked").

  

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="https://support.servicenow.com/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;" width="100%"><strong>Note:</strong> If the problem still exists after trying the steps in this article, submit a case to Technical Support and note this Knowledge Base article ID (KB0539111) in the problem description. For more information, see <a title="ServiceNow Technical Support" href="/kb_view_customer.do?sysparm_article=KB0547260" target="_blank" rel="noopener noreferrer">ServiceNow Technical Support</a>.</td></tr></tbody></table>
