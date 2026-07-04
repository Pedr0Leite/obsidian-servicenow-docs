---
title: "Unable to upgrade MID server to matching version due to \"Unable to refresh packages. Unable to find version when calling.\" error."
aliases:
  - KB0635726
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635726
kb_number: KB0635726
last_modified: 2024-04-07
---

## Unable to upgrade MID server to matching version due to "Unable to refresh packages. Unable to find version when calling." error.

  

### Issue

Unable to upgrade MID server version with error "Unable to refresh packages"

# Issue

* * *

The MID server is unable to perform an auto-upgrade due to the following error:

StartupSequencer SEVERE \*\*\* ERROR \*\*\* Unable to refresh packages. Unable to find version when calling \`<JRE bin folder path>/java -version\`. Received: xxxx version "xxxxx" 

For example:

StartupSequencer SEVERE \*\*\* ERROR \*\*\* Unable to refresh packages. Unable to find version when calling \`/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.71-1.b15.el6\_7.x86\_64/jre/bin/java -version\`. Received: openjdk version "1.8.0\_71"

# Solution

* * *

The root cause of the issue is that the external JRE no longer valid. You can either use the JRE shipped with the MID server or specify the correct external JRE.

By default, the MID server uses the JRE shipped with the base system (located at <MID-Server-install-path>/jre). However, you can specify an external JRE to use via the wrapper-override.conf (<MID-Server-install-path>/conf).

For example:

wrapper.java.command=/usr/lib/jvm/jre-1.8.0-openjdk.x86\_64/bin/java

To resolve the issue, comment out the section to force the MID server to use the base system JRE.

For example:

\# wrapper.java.command=/usr/lib/jvm/jre-1.8.0-openjdk.x86\_64/bin/java
