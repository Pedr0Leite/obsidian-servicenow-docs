---
title: "MID Server Java runtime - Information on Bundled and Compatible versions, Upgrading or Replacing"
aliases:
  - KB0719830
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0719830
kb_number: KB0719830
last_modified: 2026-07-03
---

## MID Server Java runtime - Information on Bundled and Compatible versions, Upgrading or Replacing

  

### Issue

Since 2019 ServiceNow's own OpenJDK JRE build is bundled with MID Servers. **Oracle licenses are not required.**

This OpenJDK JRE is what all MID Server-related release testing has been done with. It's the same build that instance app nodes run on, although the MID Server version tends to be ahead. Apart from the occasional important patch, the bundled JRE has been updated to a more recent version or patch with every major instance release.

**The bundled JRE does not have to be used** (see resolution instructions at the end). You may have a requirement to use the latest Java patch instead, for security reasons, or because you need to customize the JRE and not have it overwritten at each upgrade.

MID Server officially [documents that it supports all Oracle and OpenJDK JREs, not just our own build and patch level](https://www.servicenow.com/docs/csh?topicname=r_MIDServerSystemRequirements.html&version=latest "documents that it supports all Oracle and OpenJDK JREs of Java 8 (patch 161 and above) and Java 11"), although **only Java 17 should be used since Washington DC, and Java 21 since Australia**. If there is a problem running ServiceNow features and code on a MID Server with one of those non-bundled JREs then it **will still be treated as a product defect** and we will try to provide a workaround or fix. Be prepared for Tech Support to ask you to temporarily switch back to the bundled ServiceNow OpenJDK build to confirm if the JRE version is relevant to the reported issue or not.

If custom JavaScript or imported Java classes no longer work in the MID Server platform after ServiceNow upgrades or patches to the JRE, customers or 3rd party vendors are responsible for maintaining those scripts or upgrading those additional external java classes to be compatible with current Java requirement. The agent\\lib\\dependencies.txt file lists which 3rd party java libraries are part of the MID Server platform, with their versions.

| MID Server Installer  | Java Runtime |
| --- | --- |
| Brazil | 
Probably 21.0.11 - TBC.

 |
| Australia | 

A ServiceNow build of **OpenJDK 21.0.7** is bundled (21.0.7-sncmid1)

Australia Patch 1 (EA2) MID Server JREs:  
Windows x86-64  [mid-jre.australia-02-11-2026\_\_patch1-03-23-2026\_03-31-2026\_1137.windows.x86-64.zip](https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/03/31/mid-jre.australia-02-11-2026__patch1-03-23-2026_03-31-2026_1137.windows.x86-64.zip)  
Linux x86-64 [mid-jre.australia-02-11-2026\_\_patch1-03-23-2026\_03-31-2026\_1137.linux.x86-64.zip](https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/03/31/mid-jre.australia-02-11-2026__patch1-03-23-2026_03-31-2026_1137.linux.x86-64.zip)

Note: This Java 21 JRE should not be used with earlier instance versions. They require Java 17.

 |
| Zurich | 

A ServiceNow build of **OpenJDK 17.0.15** is bundled (17.0.15-sncmid1)

Zurich Patch 0 (CA) MID Server JREs:  
Windows x86-64 [mid-jre.zurich-07-01-2025\_\_patch0-07-15-2025\_07-23-2025\_1759.windows.x86-64.zip](https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2025/07/23/mid-jre.zurich-07-01-2025__patch0-07-15-2025_07-23-2025_1759.windows.x86-64.zip)   
Linux x86-64 [mid-jre.zurich-07-01-2025\_\_patch0-07-15-2025\_07-23-2025\_1759.linux.x86-64.zip](https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2025/07/23/mid-jre.zurich-07-01-2025__patch0-07-15-2025_07-23-2025_1759.linux.x86-64.zip)  

 |
| Yokohama | 

A ServiceNow build of **OpenJDK 17.0.12** is bundled (17.0.12-sncmid1)  
  
Starting with the Yokohama release, the MID Server is compiled using Java 17 and is incompatible with any Java version below 17 for runtime execution. See [KB1704368 MID Server JRE Minimum Version Requirement Update to JRE 17 Starting from Yokohama Release](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1704368) for information about mandatory procedures before upgrading the instance.

 |
| Xanadu | 

A ServiceNow build of **OpenJDK 17.0.10** is bundled (17.0.10-sncmid1)

 |
| Washington DC | 

A ServiceNow build of **OpenJDK 17.0.8.1** is bundled (17.0.8.1-sncmid1)

Administrators will need to make sure any 3rd party JAR files for Credential resolvers, JDBC drivers, etc. are compatible with Java 17 and 'strong encapsulation', before upgrading.  
More information: [KB1273036 MID Server - JRE 17 Upgrade](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1273036)

 |
| Vancouver Patch 4 (GA) | 

A ServiceNow build of **OpenJDK 11.0.20.1** is bundled (11.0.20.1-sncmid1)

 |
| Vancouver Patch 1 (GA) | 

A ServiceNow build of **OpenJDK 11.0.16.1** is bundled (11.0.16.1-sncmid1)

Note: The GA release of Vancouver reverted back to Java 11 due to CVE-2022-45146 in BCFIPS 1.0.2.jar with Java 17.

 |
| Vancouver Patch 0 (EA) | 

A ServiceNow build of **OpenJDK 17.0.5** was planned for Vancouver, but reverted to Java 11 for the General Availability (GA) release.

 |
| Utah | 

A ServiceNow build of **OpenJDK 11.0.16.1** is bundled (11.0.16.1-sncmid1)

[KB1124078 MID Server JRE version minimum requirement change to JRE 11 from Utah release onwards](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1124078)

TLS 1.1 and below will no longer be supported. An email was sent out on 2022-02-14, with subject "MID Server support notification: Be informed".  
For workaround see: [KB1006178 - Issue with discovering certain certificates via "11.0.12" JRE mid](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1006178) 

<table border="0" cellspacing="0" cellpadding="0"><tbody><tr><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2023/04/10/mid-jre.utah-12-21-2022__patch2-03-30-2023_04-10-2023_1543.windows.x86-64.zip">mid-jre.utah-12-21-2022__patch2-03-30-2023_04-10-2023_1543.windows.x86-64.zip</a></td></tr><tr><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2023/04/10/mid-jre.utah-12-21-2022__patch2-03-30-2023_04-10-2023_1543.linux.x86-64.zip" target="_parent" rel="noopener noreferrer">mid-jre.utah-12-21-2022__patch2-03-30-2023_04-10-2023_1543.linux.x86-64.zip</a></td></tr></tbody></table>

 |

You can confirm the Java version of your MID Server install by looking in this file:  
<install path>\\agent\\jre\\release

### Symptoms

### Facts

### Release

all

### Cause

### Resolution

## Changing to your JRE

If you chose to use your own Oracle/OpenJDK JRE with the MID Server, perhaps to use a more recent patch, then follow these instructions:

1.  Using the vendor's own instructions, Install the JRE in the normal way but be sure to install it **outside of the MID Server's "agent" install folder**. MID Server upgrades can replace anything included within the agent folder, and do regularly delete and replace everything in the bundled JRE's agent/jre/ folder.
2.  Edit the agent/conf/wrapper-override.conf file to tell the MID Server to use the newly installed external JRE. (Use Wordpad and not Notepad on windows, as this is a Unix format file)
3.  Restart the MID Server service.

################################################################################  
\# External JRE  
################################################################################  
\# Uncomment and edit if an external JRE is preferred. By default,  
\# the internal JRE distribution is used.  
#  
\# OPTIONAL: The path (relative to agent dir or absolute) to the java bin  
**wrapper.java.command**\=C:\\ServiceNow\_MID\_Servers\\OpenJDK\\8u251\\jre\\bin\\java

Warnings:

-   **You are now responsible for keeping the JRE maintained**. ServiceNow upgrades will not touch this JRE.
-   If you customize the JRE, perhaps by swapping .jar files within the JRE for different versions, then this JRE will no longer be supported by servicenow.
-   If you have added certificates to the Java Keystore, .\\agent\\jre\\lib\\security\\**cacerts**, then that file will need copying to the equivalent folder in your new JRE, or integrations, including the connection to the instance, may not work due to MID Security Policy errors..
-   **Search the [knowledge base for known problems](https://support.servicenow.com/kb?id=kb_browse&kb_knowledge_base=a5f38d0b2be931002f42729fe8da1594 "knowledge base for known problems")** with compatibility with the versions you intend to use. The list above only lists some main ones known to the author.

## Changing it back to the bundled Open JDK JRE

If you no longer want to use your own OpenJDK JRE with the MID Server, then follow these instructions:

1.  Edit the agent/conf/wrapper-override.conf file to **comment out the wrapper.java.command line.** Without that override, the same read only property in the wrapper.conf file will tell the MID Server to use the bundled OpenJDK JRE. (Use Wordpad and not Notepad on windows, as this is a Unix format file)
2.  Restart the MID Server service.

#wrapper.java.command=C:\\ServiceNow\_MID\_Servers\\OpenJDK\\8u251\\jre\\bin\\java

### Related Links
