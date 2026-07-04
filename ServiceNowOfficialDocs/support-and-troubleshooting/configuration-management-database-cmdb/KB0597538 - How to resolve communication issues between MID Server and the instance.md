---
title: "How to resolve communication issues between MID Server and the instance"
aliases:
  - KB0597538
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597538
kb_number: KB0597538
last_modified: 2025-04-07
---

## How to resolve communication issues between MID Server and the instance

  

### Issue

Table of Contents

1.  [MID Server to instance network interruption](#serviceInterrupt)
2.  [MID Server host environment requires instance IPs as well as DNS name](#dns)
3.  [MID Server cannot connect to the ServiceNow download link](#download)
4.  [MID Server host cannot reach instance on port 443](#server443)
5.  [MID Server requires proxy](#proxy)

Symptoms

-   The MID server was unable to download files as reported in the agent log. [More info](/kb_view.do?sysparm_article=KB0596459)

The MID Server requires a clear communication path to the instance. Interruption of the communication also interrupts all services being supported by the MID Server, even if the MID Server service is up and running. The MID server's communication can be affected by proxy settings, firewall settings, user permissions, loss of network communication, and port availability. Typically, solving the communication issues of the environment in which the MID server is installed will restore the service without ever modifying the MID Server configuration itself.

Communication Between MID Server and Instance

-   **MID Server to instance network interruption**

Making sure the network is up and can reach any external website is easy to test. From the host machine where the MID server is installed, attempt to open any web site. If there is no way to reach an external network, there is no way for the MID Server to communicate with the instance.

**SOLUTION:** Contact your network administrator to correct the network issue.

-   **MID Server host environment requires instance IPs as well as DNS name**

Some host environments require static IP addresses for configuration purposes. If this is the case in your environment, there are some cautions to consider. In particular, the MID Server needs to be able to access the upgrade site. The IP address of this site is not guaranteed and the DNS lookup is strongly recommended.

**SOLUTION:** [Review this Knowledge article](/kb_view.do?sysparm_article=KB0538621) to learn how to obtain data center information specific to your instance.

-   **MID Server cannot connect to the ServiceNow download link**

In order for a MID Server to upgrade, it needs to be able to reach install.service-now.com. In the past, administrators have installed the current IP address of install.service-now.com into the firewall allow-list. However, the IP address is not guaranteed to be consistent. On the other hand, the install.service-now.com DNS lookup is consistent. To ensure the MID Server will be able to download the installation and upgrade packages, log on to the MID Server's host machine, and from a command prompt type the following: _**ping install.service-now.com**_. If you do not get a positive data response, then the host will not be able to access install or upgrade packages.

**SOLUTION:** Contact your network or security administrator to correct the firewall security settings that are blocking the ability of the MID Server to adequately communicate. [More info](https://docs.servicenow.com/)

-   **MID Server host cannot reach instance on port 443**

The MID Server communicates with the instance on the HTTPS secure port of 443. To ensure the MID Server can download the installation and upgrade packages, log on to the MID Server's host machine, and from a command prompt type the following: _**telnet {{instance name}}.service-now.com 443**._ If you do not acquire a connection, the MID Server will also be unable to acquire a connection.

**SOLUTION:** Contact your network or security administrator to correct the firewall security settings that are blocking the ability of the MID Server to adequately communicate. [More info](https://docs.servicenow.com/)

-   **MID Server requires proxy to reach instance**

Oftentimes, the MID Server host machine is not connected directly to the internet. Rather, it is connected to a proxy server that acts as an intermediary between client machines and outside sources. In order for the MID Server to function, it must also connect through this proxy server.

**SOLUTION:** Contact your network administrator to obtain the following data points of the proxy: host name, username, password, and port. Once you have this information, you will need to [stop the MID server](https://docs.servicenow.com/csh?topicname=mid-server-installation.html&version=latest) service so that you can update the configuration file of the MID server.

Once the service is stopped, navigate to the agent folder on the MID host machine and open the config.xml file. Search for the proxy parameters and fill in the appropriate settings:

-   -   -   mid.instance.use\_proxy or mid.proxy.use\_proxy (set to **true**)
        -   mid.proxy.host
        -   mid.proxy.port
        -   mid.proxy.username
        -   mid.proxy.password

Now that the MID Server has been made aware of the proxy settings, [restart the MID server](https://docs.servicenow.com/csh?topicname=mid-server-installation.html&version=latest). If the proxy settings are correct, the MID Server will start processing work from the instance.

  

[\[Back to top\]](#toc)
