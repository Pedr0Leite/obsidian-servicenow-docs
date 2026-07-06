---
title: "User gets logged out immediately after logging in"
aliases:
  - KB0778207
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778207
kb_number: KB0778207
last_modified: 2024-04-26
---

## User gets logged out immediately after logging in

  

### Issue

The multiple provider single sign-on feature allows organizations to use several SSO identity providers (IdPs) to manage authentication as well as retain local database (basic) authentication.

Installation exits are customizations that exit from Java to call a script before returning to Java. They are usually related to login, logout, validate password and external authentication. The installation exits are located on **System Definition > Installation Exits.** Some installation exits can be overridden with a custom script that replaces the one in the default installation exit.

Each SSO plugin comes with its installation exits.

When the  Multi-SSO plugin is installed it comes with its installation exits, the previous SAML installation exits are no longer required and the system will make them inactive.

### Release

Helsinki and later

### Cause

After enabling Multi-SSO, some SSO validations may fail if the Multi-SSO installation scripts do not execute first.

There are some exceptional cases where some SAML\* installation exits remain active (incorrectly) after the Multi-SSO plugin is installed.

e.g. If SAML is already active at the time you activated Multiple Single Sign-On and if you already customized the SAML installation exits.

This could cause the logs will show the following errors:

WARNING \*\*\* WARNING \*\*\* Evaluator: org.mozilla.javascript.EcmaError: Cannot convert null to an object.

Caused by error in Script Include: 'SAML2\_update1' at line 35

32: this.lastGeneratedRequestID = null;

33: this.inResponseTo = null;

34: this.logoutFailureEventId = "saml2.logout.validation.failed";

\==> 35: this.certGR = this.getCertGR();

36:

37: // Keep SAMLAssertion object for validation

38: this.SAMLResponseObject = null;

### Resolution

To resolve the problem, if Multi-SSO is installed correctly, validate the following installation exits have Active set to False:

<table border="1" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top" width="212"><p><strong>Installation exit</strong></p></td><td valign="top" width="32"><p>&nbsp;</p></td><td valign="top" width="238"><p><strong>Active</strong></p></td></tr><tr><td valign="top" width="212"><p>SAML2Logout</p></td><td valign="top" width="32"><p>=</p></td><td valign="top" width="238"><p>false</p></td></tr><tr><td valign="top" width="212"><p>SAML2Logout_update1</p></td><td valign="top" width="32"><p>=</p></td><td valign="top" width="238"><p>false</p></td></tr><tr><td valign="top" width="212"><p>SAML2SingleSignon</p></td><td valign="top" width="32"><p>=</p></td><td valign="top" width="238"><p>false</p></td></tr><tr><td valign="top" width="212"><p>SAML2SingleSignon_update1</p></td><td valign="top" width="32"><p>=</p></td><td valign="top" width="238"><p>false</p></td></tr><tr><td valign="top" width="212"><p>MultiSSO</p></td><td valign="top" width="32"><p>=</p></td><td valign="top" width="238"><p>true</p></td></tr><tr><td valign="top" width="212"><p>MultiSSOLogin</p></td><td valign="top" width="32"><p>=</p></td><td valign="top" width="238"><p>true</p></td></tr><tr><td valign="top" width="212"><p>MultiSSOLogout</p></td><td valign="top" width="32"><p>=</p></td><td valign="top" width="238"><p>true</p></td></tr></tbody></table>

Here is the result:

![](/sys_attachment.do?sys_id=cf9863211b3f7f88fff162c4bd4bcb9b)
