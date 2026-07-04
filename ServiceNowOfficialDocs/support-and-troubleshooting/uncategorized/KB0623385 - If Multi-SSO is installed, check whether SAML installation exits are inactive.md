---
title: "If Multi-SSO is installed, check whether SAML installation exits are inactive"
aliases:
  - KB0623385
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0623385
kb_number: KB0623385
last_modified: 2026-05-04
---

## If Multi-SSO is installed, check whether SAML installation exits are inactive

  

### Issue

After installing Multi-SSO plugin, check whether SAML installation exits are disabled. Doing so will save you time on troubleshooting. Do a similar check for other scripts that have been customized, such as script includes, business rules, and so on. Update versions to the most current script manually.

#### Symptoms

After enabling Multi-SSO, some SSO validations might fail if the Multi-SSO installation scripts do not execute first.

There are some exception cases where some SAML\* installation exits remain active (incorrectly) after the Multi-SSO plugin is installed, for example, if SAML is already active at the time you activated Multiple Single Sign-On and if you already customized the SAML installation exits.

This could cause the logs to show the following errors:

<table><tbody><tr><td><pre>&nbsp;&nbsp;&nbsp; WARNING *** WARNING *** Evaluator: org.mozilla.javascript.EcmaError: Cannot convert null to an object.<br><br>&nbsp;&nbsp;&nbsp; Caused by error in Script Include: 'SAML2_update1' at line 35<br> &nbsp;&nbsp; 32: this.lastGeneratedRequestID = null;<br> &nbsp;&nbsp; 33: this.inResponseTo = null;<br> &nbsp;&nbsp; 34: this.logoutFailureEventId = "saml2.logout.validation.failed";<br> &nbsp;&nbsp; ==&gt; 35: this.certGR = this.getCertGR();<br> &nbsp;&nbsp; 36:<br> &nbsp;&nbsp; 37: // Keep SAMLAssertion object for validation<br> &nbsp;&nbsp; 38: this.SAMLResponseObject = null;</pre></td></tr></tbody></table>

### Release

All releases

### Cause

Multi-SSO is replacing the previous SAML installation exits; however, in some cases, the previous SAML installation exits are not disabled.

### Resolution

To resolve the problem, if Multi-SSO is installed correctly, validate that the following installation exits have Active set to False:

-   SAML2Logout
-   SAML2Logout\_update1
-   SAML2SingleSignon
-   SAML2SingleSignon\_update1

### Related Links

-   [Multiple provider single sign-on](https://docs.servicenow.com/csh?topicname=c_MultipleProviderSingleSignOn.html&version=latest) (Multi-SSO)
-   [Installation exits](https://docs.servicenow.com/csh?topicname=r_InstallationExits.html&version=latest "Installation exits")
