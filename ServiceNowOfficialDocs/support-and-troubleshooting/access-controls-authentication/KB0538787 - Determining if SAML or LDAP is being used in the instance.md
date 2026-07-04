---
title: "Determining if SAML or LDAP is being used in the instance"
aliases:
  - KB0538787
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538787
kb_number: KB0538787
last_modified: 2025-10-21
---

## Issue

Users are unsure if they are using SAML SSO or LDAP.

## Resolution

1.  Check if the **Integration – Multiple Provider Single Sign-On Installer** or **SAML 2.0 Single Sign-On - Update 1: security enhancements** plugins are activated and enabled. 
2.  If only the **SAML 2.0 Single Sign-On – Update 1: security enhancements** is activated, use SAML SSO and set glide.authenticate.external to **true**. Otherwise, simply check if glide.ldap.authentication is set to **true**.
3.  If the **Integration - Multiple Provider Single Sign-On Installer** plugin is enabled, the user can use both LDAP and SAML.

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="https://support.servicenow.com/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;" width="100%"><strong>Note:</strong> Configuring SAML requires special maintenance access. To request the <strong>SAML 2.0 Single Sign-On - Update 1: security enhancements&nbsp;</strong>plugin, please contact <a title="TEchnical Support" href="http://www.servicenow.com/support/contact-support.html" target="_blank" rel="noopener noreferrer">Customer Support</a>. The plugin applies updated versions of the <strong>SAML2SingleSignon</strong> installation exit (login script), <strong>SAML2Logout</strong> installation exit (logout script), and <strong>SAML2</strong> script include (script object).</td></tr></tbody></table>

For information on upgrading your existing SAML 2.0 integration, see [SAML 2.0](https://docs.servicenow.com/csh?topicname=c_SAML2.0WebBrowserSSOProfile.html&version=latest "SAML 2.0").
