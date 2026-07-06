---
title: "How to configure a MID Server to use a proxy for all traffic and configure proxy bypass"
aliases:
  - KB0744474
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0744474
kb_number: KB0744474
last_modified: 2026-02-28
---

## Issue

MID Server configuration must be set by configuration parameters and properties - with default configuration, the MID Server will not route any traffic through a proxy.

Using incorrect proxy settings may result in a failed HTTP Request - commonly presenting an error message indicating a Socket Timeout Exception:

`java.net.SocketTimeoutException: connect timed out when posting to <URL>.`

There are two configuration options available:

-   MID to Instance traffic
    -   This is controlled by the proxy settings available in the installer and config.xml file
    -   Only controls HTTP traffic between MID Server and Instance
-   All traffic
    -   This is controlled by additional MID properties
    -   This controls all HTTP traffic, such as to all internal/external URLs
    -   An option is available for defining a Proxy Bypass list

## Resolution

The MID Server can be configured to use a proxy for all traffic - which may be useful when targeting internal or external endpoints - or just for the MID to Instance configuration. 

#### To configure a MID Server to use a proxy when connecting to the ServiceNow instance:

To begin, review the "Proxy Server Parameters" section in the [MID Server Parameters](https://www.servicenow.com/docs/r/servicenow-platform/mid-server/mid-server-parameters.html) documentation page.

As these settings define Proxy configuration for MID->Instance traffic, it is recommended to configure these parameters directly on the MID rather than through the instance - as configuring incorrect values could prevent the MID contacting the Instance.

These configuration parameters are commonly set during the Installation process - either set while running the Installer or applied directly into the config.xml file. 

To add these directly to the config.xml file:

First, uncomment the proxy section:

```
<!--
<parameter name="mid.proxy.use_proxy" value="true"/>
<parameter name="mid.proxy.host" value="YOUR_PROXY_HOST"/>
<parameter name="mid.proxy.port" value="YOUR_PROXY_PORT"/>
-->
```

Update the parameter values to the host and port values required for the proxy configuration.

If the proxy additionally requires Basic Authentication, uncomment the username and password section, and update the parameter values with the credentials used to authenticate with the proxy.

```
<!--
<parameter name="mid.proxy.username" value="YOUR_PROXY_USER_NAME"/>
<parameter name="mid.proxy.password" value="YOUR_PROXY_PASSWORD" encrypt="true"/>
-->
```

Save the config.xml file and restart the MID Server.

**Note:** These properties **only** apply to MID->Instance communication. They do not apply to other HTTP requests the MID Server may perform - such as API Requests made during Discovery, or to send external SOAP / REST Messages. 

#### To configure a MID Server to use a proxy for all traffic:

1.  Navigate to **MID Server** > **Servers**
2.  Select the desired MID Server record
3.  Select the **Properties** related list
4.  Add the following properties:

<table style="border-collapse: collapse; width: 100.038%; height: 607.916px;" border="1"><colgroup><col style="width: 24.174%;"><col style="width: 45.5167%;"><col style="width: 30.2719%;"></colgroup><tbody><tr style="height: 22.3958px;"><td style="height: 22.3958px;"><span style="font-family: lato;">Property</span></td><td style="height: 22.3958px;"><span style="font-family: lato;">Description</span></td><td style="height: 22.3958px;"><span style="font-family: lato;">Examples</span></td></tr><tr style="height: 99.1875px;"><td style="height: 99.1875px;"><span style="font-family: lato;">glide.http.proxy_host</span></td><td style="height: 99.1875px;"><span style="font-family: lato;">Specify the proxy server hostname or IP address.</span><ul id="c_WebProxy__ul_hcw_xfc_tx" style="list-style-position: inside;"><li>Type: string</li><li>Default value: none</li></ul></td><td style="height: 99.1875px;"><span style="font-family: lato;">proxy.company.com</span><br><span style="font-family: lato;">192.168.34.54</span></td></tr><tr style="height: 99.1875px;"><td style="height: 99.1875px;"><span style="font-family: lato;">glide.http.proxy_port</span></td><td style="height: 99.1875px;"><span style="font-family: lato;">Specify the port number for the proxy server.</span><ul id="c_WebProxy__ul_icw_xfc_tx" style="list-style-position: inside;"><li style="font-family: lato;"><span style="font-family: lato;">Type: string</span></li><li style="font-family: lato;"><span style="font-family: lato;">Default value: none</span></li></ul></td><td style="height: 99.1875px;"><span style="font-family: lato;">8080</span><br><span style="font-family: lato;">9100</span></td></tr><tr style="height: 121.583px;"><td style="height: 121.583px;"><div><div><span style="font-family: lato;">glide.http.proxy_username</span></div></div></td><td style="height: 121.583px;"><span style="font-family: lato;">Specify the username used to authenticate the proxy server.</span><ul id="c_WebProxy__ul_jcw_xfc_tx" style="list-style-position: inside;"><li>Type: string</li><li>Default value: none</li></ul></td><td style="height: 121.583px;"><span style="font-family: lato;">proxyuser</span></td></tr><tr style="height: 121.583px;"><td style="height: 121.583px;"><div><div><span style="font-family: lato;">glide.http.proxy_password</span></div></div></td><td style="height: 121.583px;"><span style="font-family: lato;">Specify the password used to authenticate the proxy server.</span><ul id="c_WebProxy__ul_kcw_xfc_tx" style="list-style-position: inside;"><li style="font-family: lato;"><span style="font-family: lato;">Type: string</span></li><li style="font-family: lato;"><span style="font-family: lato;">Default value: none</span></li></ul></td><td style="height: 121.583px;"><span style="font-family: lato;">password</span></td></tr><tr style="height: 143.979px;"><td style="height: 143.979px;"><div><div><span style="font-family: lato;">glide.http.proxy_bypass_list</span></div></div></td><td style="height: 143.979px;"><span style="font-family: lato;">Specify the semicolon-separated list of addresses that bypass the proxy server. Use an asterisk as a wildcard character to specify all or part of an address.</span><ul style="list-style-position: inside;"><li>Type: string</li><li>Default value: none</li></ul></td><td style="height: 143.979px;"><span style="font-family: lato;">127.0.0.1;*.internal.com;localhost</span></td></tr></tbody></table>

Once the properties have been added, restart the MID Server for the changes to take effect. 

**Warning**: When configuring these proxy properties, all MID Server communications route through the proxy, except to hosts defined in the proxy bypass list property. Busy proxies can cause connectivity problems, especially during Discovery operations - consider carefully if this is correct for the desired functionality. It can often make sense to provide dedicated MIDs for operations like Discovery or REST Message - and then apply the correct proxy configuration to each MID separately. 

 ![MID Server proxy settings](sys_attachment.do?sys_id=a362e85297573e105ad8f6e11153affe "MID Server proxy settings")

## Additional Information

[How to resolve communication issues between MID Server and the instance](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597538)

[MID Server Parameters](https://www.servicenow.com/docs/r/servicenow-platform/mid-server/mid-server-parameters.html)

[MID Server Properties](https://www.servicenow.com/docs/r/servicenow-platform/mid-server/r_MIDServerProperties.html)
