---
title: "Connecting Salesforce Test Org or Custom Domain to Software Asset Management"
aliases:
  - KB0821146
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0821146
kb_number: KB0821146
last_modified: 2025-01-03
---

## Connecting Salesforce Test Org or Custom Domain to Software Asset Management

  

### Summary

As of the Orlando release, when creating an integration for Salesforce, Software Asset Management assumes you will be integrating with a Salesforce domain that is login.salesforce.com, a standard domain for production instances.

When integrating a test instance (test.salesforce.com) or an organization with a custom domain that is not login.salesforce.com, you must first change the instance domain in the Salesforce Application Registry record.

Note: It is advisable to recreate the SAAS profile from scratch and before your request a token do the below steps.

Here is how to change it:

1\. Type "OAuth" into the filter navigator, and open Application Registry under System OAuth.

2\. Then find and open the Salesforce App Registry record.

3\. Edit the Authorization URL and Token URL to match the domain of the account you wish to connect. 

4\. Update to save. 

5\. On the integration profile, re-run the Get OAuth Token call, go through the OAuth flow and approve the connection. 

  

Following these steps will allow you to connect to a Salesforce org with a domain different from login.salesforce.com.
