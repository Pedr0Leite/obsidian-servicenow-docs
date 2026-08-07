---
title: "Would Custom URLs cause problems for MID Servers?"
aliases:
  - KB0781923
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0781923
kb_number: KB0781923
last_modified: 2025-11-14
---

## Would Custom URLs cause problems for MID Servers?

  

### Summary

A MID Server is set up with a URL parameter and will connect to the instance using that URL. This KB explains which URL should be used after activating Custom URLs.

### Release

Since the London release, there is a [Custom URLs plugin](https://docs.servicenow.com/search?q=Activate+Custom+URLs "Custom URLs plugin"), that can be used on instances with a dedicated VIP, to create custom URLs to access the instance.

This can lead to several URLs that the instance could be accessed using:

<table id="custom-url__table_hrm_pzh_sgb"><tbody><tr><td style="width: 174px;" headers="custom-url__table_hrm_pzh_sgb__entry__1 "><code>https://acme.service-now.com</code></td><td style="width: 856px;" headers="custom-url__table_hrm_pzh_sgb__entry__2 ">The initial domain name for Acme that came with the&nbsp;ServiceNow&nbsp;instance.</td></tr><tr><td style="width: 174px;" headers="custom-url__table_hrm_pzh_sgb__entry__1 "><code>https://support.acme.com</code></td><td style="width: 856px;" headers="custom-url__table_hrm_pzh_sgb__entry__2 ">A custom URL that associates with your ServiceNow instance. This URL is referred to as an alias (CNAME) of the initial domain name.</td></tr><tr><td style="width: 174px;" headers="custom-url__table_hrm_pzh_sgb__entry__1 "><code>https://US-support.acme.com</code></td><td style="width: 856px;" headers="custom-url__table_hrm_pzh_sgb__entry__2 ">A secondary custom URL that associates to a service portal on your instance. Your instance can support multiple custom URLs to the same service portal.</td></tr></tbody></table>

### Instructions

We recommend that the initial URL https://<instance name>.service-now.com is used. This is the URL that would be used even without the Custom URLs activated. This will allow the MID Server to connect regardless of what additional URLs are added or changed in the future, because this initial URL will always work.

Although a Custom URL could be used with a MID Server, it will depend on a CNAME record in your own DNS, which will point to the initial URL. There is no need to add that additional potential point of failure, so just use the initial URL. A secondary custom URL is not to be used, as MID Servers have nothing to do with Service Portals.

<table class="noteTable" style="border: 1px solid #e0e0e0; width: 100%; border-spacing: 5px; background-color: #f5f5f5;"><tbody><tr><td style="text-align: center; padding: 5px;" width="25"><img title="Note" src="/Note_25x.pngx" alt="Note icon" align="bottom"></td><td style="text-align: left; padding: 5px;"><strong>Note</strong>: If you need to configure Firewall rules to allow the MID Servers to access the instance, you may need to remember which URL the MID Servers are set up to connect to.</td></tr></tbody></table>
