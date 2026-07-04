---
title: "Troubleshooting SAML or SSO issues in ServiceNow"
aliases:
  - KB0539112
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0539112
kb_number: KB0539112
last_modified: 2025-10-16
---

## Issue

This article guides you through the process of troubleshooting SAML or SSO issues in ServiceNow. It provides steps to help you eliminate common causes for your problems by verifying that the configuration of your networking is correct.

Symptoms may include:

-   The users are unable to log in to the system.
-   A single user is unable to log in to the system.
-   The incorrect user is logged in to the system.
-   The user could not validate the SAML response.
-   The SAML is not correctly setting CMS redirects.
-   The user cannot log in after a clone.
-   There is an ADFS error on logout.

## Resolution

Determine whether any of the troubleshooting steps below are true for the environment. Each step provides a link to an article that helps users eliminate possible causes and take corrective action as necessary.

1.  Determine if SAML or LDAP is being used in the instance. For more information, see [KB0538787: Determining if SAML or LDAP is being used in the instance](/kb_view.do?sysparm_article=KB0538787 "KB0538787: Determining if you are using SAML or LDAP in your instance").
2.  Contact the administrator to determine if there is an ADFS configuration issue.
3.  Determine if SAML is misconfigured. For more information, see [Configuring ADFS 2.0 to Communicate with SAML 2.0](https://docs.servicenow.com/csh?topicname=c_ADFSIntegrationWithSAML2.0.html&version=latest "Configuring ADFS 2.0 to Communicate with SAML 2.0") in the product documentation.
4.  Confirm if the SAML certificate is correct. For more information, see [KB0538763: Determining if the SAML certificate is incorrect](/kb_view.do?sysparm_article=KB0538763 "KB0538763: Determining a bad SAML certificate").
5.  Confirm that ADFS is receiving the signed request. For more information, see  
    -   [KB0538765: Determining if ADFS is receiving a signed request](/kb_view.do?sysparm_article=KB0538765 "KB0538765: Determining if ADFS is receiving a signed request")
    -   [Configuring ADFS 2.0 to Communicate with SAML 2.0](https://docs.servicenow.com/csh?topicname=c_ADFSIntegrationWithSAML2.0.html&version=latest "Configuring ADFS 2.0 to Communicate with SAML 2.0").
6.  Confirm that properties were preserved during a clone. For more information, see [KB0538768: Determining if the properties from the source are copied over a target](/kb_view.do?sysparm_article=KB0538768 "KB0538768: Determining if the properties from the source were copied over a target").
7.  Confirm whether customer scripts are working after an upgrade. For more information, see [KB0538769: Determining if SAML issues are occurring due to customer scripts no longer working after upgrade](/kb_view.do?sysparm_article=KB0538769 "KB0538769: Determining if SAML issues are occuring due to customer scripts no longer working after upgrade").
8.  Confirm if the user is locked out. For more information, see [KB0538770: Determining if the SAML issue is the result of a user being locked out](/kb_view.do?sysparm_article=KB0538770 "KB0538770: Determining if SAML issue is the result of a user being locked out").
9.  Determine if the user has a duplicate record. For more information, see [KB0538780: Determining if the SAML issue is the result of the user having a duplicate record](/kb_view.do?sysparm_article=KB0538780 "KB0538780: Determining if the SAML issue is the result of of the user having a duplicate record").
10.  Confirm if there are leading or trailing spaces in the user ID. For more information, see [KB0538781: Determining if the SAML issue is caused by leading or trailing spaces](/kb_view.do?sysparm_article=KB0538781 "KB0538781: Determining if SAML issue is caused by leading or trailing spaces").
11.  Confirm whether different timestamps are impacting SAML. For more information, see [KB0538782: Determining if different timestamps are impacting SAML](/kb_view.do?sysparm_article=KB0538782 "KB0538782: Determining if different time stamps are impacting SAML").
12.  Confirm the current version of SAML is being used. For more information, see [KB0538786: Determining if the user has an older version of SAML](/kb_view.do?sysparm_article=KB0538786 "KB0538786: Determining if you are using an older version of SAML.").

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="https://support.servicenow.com/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;" width="100%"><strong>Note:</strong> If the problem still exists after trying the steps in this article, submit a case to Technical Support, and note this Knowledge Base article ID (KB0539112) in the problem description. For more information, see <a title="Submitting an Incident" href="https://support.servicenow.com/kb_view.do?sysparm_article=KB0547260" target="_blank" rel="noopener noreferrer">ServiceNow Technical Support</a>.</td></tr></tbody></table>
