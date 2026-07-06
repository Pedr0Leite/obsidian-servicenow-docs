---
title: "How to discover SSH Servers by port other than 22"
aliases:
  - KB0696915
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696915
kb_number: KB0696915
last_modified: 2025-08-07
---

## How to discover SSH Servers by port other than 22

  

### Issue

This article describes two ways to configure Discovery to discover SSH Servers on ports other than the default 22.

**Note:** Throughout this KB we will use port 22000 as an example. However, this port can be changed to the port that best fits the environment (the port where SSH devices are listening on). Thus, wherever you see "22000", replace it with the desired port.

### Release

All

### Resolution

### Adding an IP Service

1.  Go to "**Discovery Definition > IP Services**" and add a New entry with the following information:  
    -   **Name**: SSH on 22000
    -   **Service name**: Secure Shell Service on 22000
    -   **Port**: 22000
    -   **Protocol**: TCP
    -   **Creates**: None  
          
        
2.  Go to "**Discovery Definition > Port Probes**" and edit the entry "ssh"  
    -   Unlock the field "**Triggered by services**"
    -   Add "SSH on 22000" to it
    -   Save the Discovery Port Probe.

The next time you run Discovery, by default both ports 22 and 22000 will be scanned. The port that answers will be the one used for the SSHCommand probes triggered through the rest of the discovery. The only disadvantage is that both ports 22 and 22000 will be scanned for each scan.

In a very special situation, it can also be that both ports 22 and 22000 are available, both with an SSH server but you want the one on 22000 to be used. These disadvantages can be worked around by using [Behaviors](https://docs.servicenow.com/csh?topicname=c_DiscoveryBehaviors.html&version=latest "Behaviors"). 

### Using Behaviors

1.  Go to "**Discovery Definition > IP Services**" and add a New entry with the following information:  
    -   **Name**: SSH on 22000
    -   **Service name**: Secure Shell Service on 22000
    -   **Port**: 22000
    -   **Protocol**: TCP
    -   **Creates**: None  
          
        
2.  Go to "**Discovery Definition > Port Probes**" and add a new entry (this is almost a copy of "ssh"):   
    -   **Name**: SSH on 22000
    -   **Description**: Secure Shell on 22000 Login
    -   **Scanner**: Generic TCP with Banner
    -   **Triggered by services**: SSH on 22000
    -   **Triggers probe**: UNIX - Classify
    -   **Use classification**: UNIX Classification
    -   **Classification priority**: 2
    -   **Active**: true
    -   **CIs**: true
    -   **IPs**: true 

When Discovery starts a discovery process it sends the Shazzam probe that includes, by default, the Port Probes defined in the Functionality Definition "All".

The Functionality Definition "All" includes by default:

-   wmi
-   snmp
-   ssh
-   http
-   wins
-   dns
-   printer
-   osx
-   ip\_phone
-   slp
-   wbem

If you know that you want to discover ONLY devices that are listening on 22000, you could create a **Functionality Definition** that includes only "SSH on 22000" (or even both "ssh" and "SSH on 22000"). Then you just need to create a Behavior that uses that functionality and when you run a Discovery Schedule tell it to use that behavior.

The Discovery Schedule will discover only devices that are in that behavior/functionality.

3.  Go to "**Discovery Definition > Functionality Definition**" and add a New entry  
    
    -   **Name**: SSH on 22000
    -   **Port probes**: SSH on 22000
    
    In case you want both 22 and 22000, you could call this functionality definition "SSH MyName" or whatever and include both port probes "ssh" and "ssh on 22000".
    
4.  Go to "Discovery Definition > Behavior" and add a New entry:  
    -   **Name**: Ssh Ipsos
    -   **Save**
    -   Open the entry and add a new entry in the related list "**Discovery Functionality**":  
        -   **Phase**: 0
        -   **Functionality definition**: SSH on 2000 (the name used in step 3)
        -   **MID servers**: Add the MID server (1 or more) to run this functionality.
5.  In your **Discovery Schedules**, set the field **Behavior** to "SSH NyName".  
    That would cause that when the schedule starts, the Shazzam probe sent will only scan the ports corresponding to the Port Probes included in the Functionality Definition as explained in step 3).   
      
    Observe that the field "MID server" disappears from the Discovery Schedule. That is so because you already indicated what mid server(s) have to process this schedule.

All this has a lot of flexibility and of course, there is more to consider, especially when mid servers are set up in a load-balancing cluster. 

### Patterns

If the device being discovered makes use of patterns, also add MID server property mid.sa.ssh.port:

1.  Navigate to ecc\_agent\_property table
2.  Click new
3.  Set name to mid.sa.ssh.port
4.  Set value to a comma separated list of ports
5.  Set the MID server to empty for the property to take effect on all MID servers or specify a MID server

**Note:** If the environment is hybrid, meaning there are devices listening on 22 or 22000, set the property value to 22,22000.

### Probes triggered by sensor

Some sensors may trigger additional probes and not pass the "port" parameter. If this happens, the triggered probes will default to port 22. In such case, the code in the sensor needs to be updated to pass the "port" probe parameter.

Out of box, the following probes come into this issue:

-   <instance>.service-now.com/discovery\_sensor\_list.do?sysparm\_query=scriptLIKETriggerProbe%5Ereacts\_to\_probe.ecc\_queue\_topic%3DSSHCommand

An entry on table ip\_service\_affinity will be create showing the port used to successfully discover the device once successfully discovered on the alternative port and system property glide.discovery.ip\_service\_affinity = true. This can be used in order to add the port to such probes triggered from within a sensor. Example code to be added:

var ip = this.getSource();  
var sa = new GlideRecord('ip\_service\_affinity');  
sa.addQuery('ip\_address',ip);  
sa.query();  
  
// If we find an affinity, get the port and add to the probe as a parameter  
if(sa.next()){  
    // Check that ip\_service and ip\_service\_port are not empty, to avoid any potential nullpointers  
    if(!gs.nill(sa.ip\_service) && !gs.nill(sa.ip\_service.port)){  
        // Now that we have the port, lets add it to the probe  
        probe.addParameter("port", sa.ip\_service.port);  
    }  
}

There is a attached update set on this KB with the changes necessary to OOB sensors. If you decide to use the update set, please test in a non-production environment first.

### Related Links

You can even define a behavior where a MID server is used for discovering devices on port 22, another MID server for port 22000 and another MID server for WMI. You just create behaviors including different functionalities. That way when a schedule runs with that behavior, Discovery will select the appropiate MID server for each device found.

Please find more information on our documentation site: [Discovery Behaviors](https://docs.servicenow.com/csh?topicname=c_DiscoveryBehaviors.html&version=latest "Discovery Behaviors")
