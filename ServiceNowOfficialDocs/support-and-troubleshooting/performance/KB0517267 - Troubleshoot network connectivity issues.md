---
title: "Troubleshoot network connectivity issues"
aliases:
  - KB0517267
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0517267
kb_number: KB0517267
last_modified: 2026-04-14
---

## Troubleshoot network connectivity issues

  

### Issue

 

Troubleshoot network connectivity issues that affect your ServiceNow instance, including inability to connect, slow or intermittent availability, and authentication failures. This article provides steps to verify network connectivity and test the connection from your instance to your Lightweight Directory Access Protocol (LDAP) server.

### Release

All releases

### Cause

Network connectivity issues can result from:

-   No network connectivity between your location and the instance
-   The instance cannot connect to the LDAP server

### Resolution

To troubleshoot network connectivity issues in your ServiceNow instance, you must gather data from each network. Until this data is collected, there is no way to determine if the issue originated from the ServiceNow network, the internet service provider, your internal network, or a combination of these. If your browser displays an error, capture the error number or take a screenshot to help with troubleshooting.

Follow the steps in order. Do not skip any step.

 **Important:** If you are able to connect to the instance but cannot authenticate or log in, skip to the **[To verify connectivity from the instance to your LDAP server](#test_ldap_conn)** section.

#### Verify network connectivity

1.  Open a terminal session on your computer:
    -   Windows: Select **Start > Run**, enter `cmd`, and press Enter.
2.  Once in the Terminal, type ping to test the connectivity to the instance and press Enter to initiate the ping command.
    
    The following image displays the results after running the ping command. The output displays the instance hostname needed to troubleshoot the network issue. The Internet Protocol (IP) address can also be used; in this case, it is 199.91.140.73. Depending on the computer, the ping command can run indefinitely, so use <Ctrl> + C to kill the transaction, if necessary. The ping command output shows that there are three packets, every 64 bytes, and the round-trip time (latency) is approximately 100ms.
    
    ![Ping command output displaying three packets of 64 bytes and a latency of roughly 100ms.](sys_attachment.do?sys_id=1da7fafc87dc8fd057288519dabb3573 "Ping command")
    
    The following image shows the result of running **ping** on an IP address that returned no response. If there is no response, but ping can be sent successfully from another location, a routing issue exists between the user and the instance. If so, run the ping command on another target, for example, www.google.com. If the site cannot be reached, then the issue is likely on the user's side.
    
    ![Ping command on an IP address with no response.](sys_attachment.do?sys_id=59a7fafc87dc8fd057288519dabb3579 "Ping command with no response")
    
     **Important:** If you are able to reach the objective site but not the instance, escalate the issue to the Technical Support - Network Engineering team for further investigation.
    
    Some useful options for the ping command include setting the count limit, changing the number of packets per second, or increasing the packet size, depending on the troubleshooting scenario. Unless you have a reason to change either of these settings, the default is usually the best option. For more options using the ping command, use the manual (_man_) pages for ping on Mac or _help_ on Windows:
    
    -   Mac: man ping
    -   Windows: ping /?  
          
        
3.  Use the traceroute command to test the route (path) and measure packet transit delays across the instance IP network.
    
    The image below indicates that the last hop is service-now.car1.washington1.level3.net. This means the packets are reaching the ServiceNow data center provider. Additional information may be needed to determine whether the address is a ServiceNow provider.
    
    ![Traceroute command indicating that the last hop is service-now.car1.washington1.level3.net.](sys_attachment.do?sys_id=d5a7fafc87dc8fd057288519dabb35d5 "Traceroute command")
    
     **Note:** The Traceroute command will always time out before reaching the destination due to the ServiceNow proxy configuration. Ping and traceroute are point-in-time snapshots. To obtain a more accurate image, run these commands multiple times and calculate an average.
    
    Interpreting the response times depends on the user's location and the type of Internet connection. 
    
    As a reference, ping times are usually within the following ranges:
    
    -   100ms within the United States.
    -   100 - 150ms from the United Kingdom to the United States.
    -   200 - 300ms from the United States to Europe, the Middle East, and Africa.
    
      
    
     **Important:** Results may vary greatly. Running multiple ping tests using multiple web sites is highly recommended. If latency (ping times) or packet loss is suspected to be part of the issue, escalate the issue to the Technical Support - Network Engineering team for further investigation.
    

#### To verify connectivity from the instance to your LDAP server

 **Note:** If you are part of the ServiceNow Technical Support team, please refer to [Verifying connectivity from an instance to a LDAP server](/kb_view.do?sysparm_article=KB0517974 "Verifying connectivity from an instance to a LDAP server") for details on the internal process.

 **Note:** The following steps use a fake instance name that is experiencing network connectivity issues. The IP address in the LDAP server record is a Google web server, and port 80 is used for the connection. LDAP commonly uses port 389 and Secure LDAP (LDAPS) uses port 636, but both can be modified if necessary. It is important to test the connection using the port that is configured in the same instance that is presenting network issues.

1.  Navigate to **System LDAP > LDAP Servers** to obtain the LDAP IP and port information.
    
    ![System LDAP, LDAP Servers navigation menu displaying LDAP IP and port information.](sys_attachment.do?sys_id=15a7fafc87dc8fd057288519dabb35da "System LDAP navigation menu")
    
2.  Navigate to **System Diagnostics > Stats** to determine the name of the server hosting the instance.
    
    ![System diagnostics stats page displaying statistics for the demo amc instance, including the name of the server hosting the instance.](sys_attachment.do?sys_id=51a7fafc87dc8fd057288519dabb35df "System Diagnostics Stats")
    
3.  Log in to the server where the instance is hosted.
4.  Run the telnet command to the IP of the LDAP server and specify the port that is being used.
    
    In the image below, please note that there is a successful connection to 75.125.226.243 on port 80. If there is a successful connection here, but you are not able to establish a connection using the **Test Connection** link in the instance, then examine the credentials and verify that the customer's LDAP server allows connections from the outgoing IP address. For more details, refer to the IP Information article in the ServiceNow Datacenter Knowledge Base.
    
    ![Telnet command displaying a successful connection to IP address, 75.125.226.243 on port 80.](sys_attachment.do?sys_id=1da7fafc87dc8fd057288519dabb35fc "Telnet command")
    

If the issue continues to exist after following the steps in this article:

-   Clearly identify the issue or question.
-   Visit the ServiceNow [product documentation](https://docs.servicenow.com/ "product documentation").
-   Search the [ServiceNow Community](http://community.service-now.com "ServiceNow Community").
-   Post a question on the ServiceNow [Community forums](http://community.service-now.com/forums "Community forums"). New users must [create an account](http://community.service-now.com/user/register "Create an Account") on the ServiceNow Community in order to post.
-   [Contact ServiceNow Customer Support](http://www.servicenow.com/support/contact-support.html "Contact ServiceNow Customer Support"). 

### Related Links

Product documentation:

-   [MID Server System Requirements](https://docs.servicenow.com/csh?topicname=r_MIDServerSystemRequirements.html&version=latest "MID Server Requirements")
-   [Active Directory Application Mode (ADAM)](https://docs.servicenow.com/csh?topicname=c_ActiveDirectoryApplicationMode.html&version=latest "Active Directory Application Mode (ADAM)")
-   [ODBC Driver](https://docs.servicenow.com/csh?topicname=c_ODBCDriver.html&version=latest "ODBC Driver")
-   [LDAP Integration](https://docs.servicenow.com/csh?topicname=c_LDAPIntegration.html&version=latest "LDAP Integration")
-   [Network Response Times](https://docs.servicenow.com/csh?topicname=c_NetworkResponseTimes.html&version=latest "Network Response Times")

Knowledge base:

-   [Troubleshooting slow performance](/kb_view.do?sysparm_article=KB0517241 "Troubleshooting slow performance")
