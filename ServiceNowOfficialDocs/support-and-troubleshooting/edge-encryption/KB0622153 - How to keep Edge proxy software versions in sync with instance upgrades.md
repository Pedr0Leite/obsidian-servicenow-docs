---
title: "How to keep Edge proxy software versions in sync with instance upgrades"
aliases:
  - KB0622153
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622153
kb_number: KB0622153
last_modified: 2024-04-07
---

## How to keep Edge proxy software versions in sync with instance upgrades

  

### Issue

How to keep Edge proxy software versions in sync with instance upgrades 

  
  
  
How To

* * *

If you are running an instance with Edge Proxy, you will want to make sure that your Edge Proxy software version is in sync with the instance version. When an instance is patched or upgraded to a new version, it may be necessary to also upgrade the Edge Proxies as the Edge Proxy software may have also been updated to match with the instance upgrade.

There is some level of backward compatibility. For example, if an instance is upgraded to Istanbul, the Edge Proxies will run if they are still on Geneva, but you will be missing problem fixes and new features that may come with the new Edge Proxy version. The recommended practice is to keep the Edge Proxy versions in sync with the instance versions.

This article tells you how to keep instance and Edge Proxy versions in sync with each other. 

Note that starting in the Jakarta release the proxy version is in the UI at Edge Encryption Configuration -> Proxies in the Proxy version and Proxy build columns.  Also in Jakarta and above you can schedule upgrades from the UI at Edge Encryption Configuration -> Proxies -> Upgrade Schedules

1.  After an instance is upgraded to a new major version, patch set, or hot fix, check the Edge Proxy version that has come with the new instance version
    -   Navigate to **Edge Encryption Configuration > Installation and Downloads > Downloads  
        **  
        ![](sys_attachment.do?sys_id=5d7eb062db0ab450e515c223059619f3)
    -   From there, select the appropriate download link based on the operating system where the Edge Proxy is installed, and the operating system is 32-bits or 64-bits.
        -   For example, if the 64-bit Linux link is selected, you will see something like this: [https://install.service-now.com/glide/distribution/builds/package/edgeencryption/3.1.2/edgeencryption-dist-3.1.2-linux-x86-64.zip](https://install.service-now.com/glide/distribution/builds/package/edgeencryption/3.1.2/edgeencryption-dist-3.1.2-linux-x86-64.zip)
    -   The Edge Encryption Proxy version is the three digit number shown in the file path and in the .zip file, the version here being 3.1.2:
        1.  From the file path > **/3.1.2/**
        2.  From the file name > **edgeencryption-dist-3.1.2-linux-x86-64.zip**
2.  Check the version that the Edge Proxies are running on.
    -   Navigate to each proxy and do a directory listing at the top level of the proxy installation. For example, from Linux:   
          
        \[sn@sn-training dist\]$ ls  
          
        bin   edgeencryption-3.1.1.jar  keys      lib   README.txt  scripts                                           shutdown.sh  startup.sh  
          
        conf  java                      keystore  logs  rules       ServiceNow Open Source Disclosure 100316IEE0.pdf  sql          tmp  
        The version of the jar file here shows the version of the Edge Proxy:  
          
        edgeencryption-3.1.1.jar  
          
        The version of the proxy is 3.1.1 - in this case, since step (1) is showing a version of 3.1.2 on the instance, an update of the proxy is necessary.
3.  The Edge Proxy upgrade procedure is described in the product documentation, specified if you are running the proxy on Windows or Linux.
    -   The upgrade procedure should be done on each proxy that exists on the instance, one proxy at the time. 
    -   For production instances where there should be multiple proxies, you should remove the proxy from the load balancer pool first and monitor the client connections to the proxy. Once those connections have drained off you can proceed with the upgrade. 
    -   Once the upgrade is complete, you can bring the upgraded proxy back into the load balancer pool and move onto the next proxy:
        
        -   Helsinki documentation:  
            https://docs.servicenow.com/csh?topicname=c\_UpdateEdgeEncryptionProxy.html&version=latest
        -   Istanbul documentation:  
            https://docs.servicenow.com/csh?topicname=c\_UpdateEdgeEncryptionProxy.html&version=latest
        
          
        Notice that the topics discussed there cover proxy backward compatibility, Linux and Windows upgrades, and upgrade rollbacks:  
          
        ![](sys_attachment.do?sys_id=917ef062db0ab450e515c22305961903)  
          
        For later releases, check the documentation for the specific release.  
        -   Geneva documentation:  
            https://docs.servicenow.com/csh?topicname=c\_UpdateEdgeEncryptionProxy.html&version=latest
        -    Upgrade command for Geneva:  
            java -jar edgeencryption-SOME-RELEASE.zip -m dist-upgrade -c <proxy directory>
4.  The upgrade procedure will automatically stop the proxy, do the upgrade, then start the proxy running on the new version.  You may verify the new version is applied by going to each proxy and do a directory listing at the top level of the proxy installation, for example from linux:  
      
    \[sn@sn-training dist\]$ ls  
      
    bin   edgeencryption-3.1.2.jar  keys      lib   README.txt  scripts                                           shutdown.sh  startup.sh  
      
    conf  java                      keystore  logs  rules       ServiceNow Open Source Disclosure 100316IEE0.pdf  sql          tmp  
      
    This shows that the version of the proxy is now upgraded to 3.1.2 from the version shown in edgeencryption-3.1.2.jar.
5.   For Istanbul these are the corresponding Proxy versions (edgeencryption-x.x.x.jar) that match the Istanbul instance patch versions:

<table style="box-sizing: border-box; border-collapse: collapse; border-spacing: 0px; color: #485563; font-family: SourceSansPro, 'Helvetica Neue', Arial; font-size: 13px; height: 200px;" border="1" width="226"><tbody style="box-sizing: border-box;"><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0px;">&nbsp;Proxy version</td><td style="box-sizing: border-box; padding: 0px;">Istanbul patch version</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0px;">&nbsp;3.0.9</td><td style="box-sizing: border-box; padding: 0px;">&nbsp;IP0&nbsp;</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0px;">&nbsp;3.1.1</td><td style="box-sizing: border-box; padding: 0px;">&nbsp;IP1</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0px;">&nbsp;3.1.1</td><td style="box-sizing: border-box; padding: 0px;">&nbsp;IP2&nbsp;</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0px;">&nbsp;3.1.2</td><td style="box-sizing: border-box; padding: 0px;">&nbsp;IP3</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0px;">&nbsp;3.1.2</td><td style="box-sizing: border-box; padding: 0px;">&nbsp;IP4</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0px;">&nbsp;3.5.1</td><td style="box-sizing: border-box; padding: 0px;">&nbsp;IP5</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0px;">&nbsp;3.5.1</td><td style="box-sizing: border-box; padding: 0px;">&nbsp;IP6</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0px;">&nbsp;3.5.1</td><td style="box-sizing: border-box; padding: 0px;">&nbsp;IP7</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0px;">&nbsp;3.5.1</td><td style="box-sizing: border-box; padding: 0px;">&nbsp;IP8</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0px;">&nbsp;3.5.1</td><td style="box-sizing: border-box; padding: 0px;">&nbsp;IP9</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0px;">&nbsp;3.8.2</td><td style="box-sizing: border-box; padding: 0px;">&nbsp;IP10</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0px;">&nbsp;3.8.2</td><td style="box-sizing: border-box; padding: 0px;">&nbsp;IP11</td></tr></tbody></table>
