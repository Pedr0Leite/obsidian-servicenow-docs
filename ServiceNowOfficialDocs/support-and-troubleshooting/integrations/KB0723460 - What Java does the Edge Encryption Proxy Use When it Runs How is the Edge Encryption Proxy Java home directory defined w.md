---
title: "What Java does the Edge Encryption Proxy Use When it Runs? How is the Edge Encryption Proxy \"Java home directory\" defined when enabling 256-bit encryption keys for Java 8?"
aliases:
  - KB0723460
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0723460
kb_number: KB0723460
last_modified: 2024-04-07
---

## Issue

# Description

* * *

This article explains which Java an Edge Encryption Proxy uses when it is running and how to configure that Java to allow the use of 256-bit encryption keys.

# Procedure

* * *

(1) First precedence is the $JAVA\_HOME (for Windows %JAVA\_HOME%) variable as set for the operating system user that starts the proxy.  This is an example of a $JAVA\_HOME variable setting:

$ echo $JAVA\_HOME

/home/sn/jre\_1.8.0\_181

Where the content of that directory looks as follows:

$ pwd

/home/sn/jre\_1.8.0\_181

$ ls

bin        man      THIRDPARTYLICENSEREADME-JAVAFX.txt

COPYRIGHT  plugin   THIRDPARTYLICENSEREADME.txt

lib        README   Welcome.html

LICENSE    release

(2) Second in precedence, if the $JAVA\_HOME variable is not set at all for the operating system user that starts the proxy, the proxy uses the setting in /<proxy install location>/conf/wrapper.conf property: wrapper.java.command, for example:

wrapper.java.command=/Library/Java/jdk1.8.0\_191/jre/bin/java

Where the “java” at the end is the executable java file, not a directory, this is an example of the contents of the …/jre/bin directory where the “java” executable exists:

$pwd

/Library/Java/jdk1.8.0\_191/jre/bin

$ls

java        jjs        keytool        orbd        pack200        policytool    rmid        rmiregistry    servertool    tnameserv    unpack200

Note: if using the wrapper.java.command property do not precede the one you want to use with one that is commented out with a **#** symbol, the system will still use that setting even if it is commented out with **#**

(3) How to allow the use of 256-bit encryption keys with the edge proxy - see:

[For Java 8 update 141 (8u141) or earlier](https://docs.servicenow.com/csh?topicname=256-bit-encryption.html&version=latest "For Java 8 update 141 (8u141) or earlier")

[For Java 8 update 151 (8u151) or later](https://docs.servicenow.com/csh?topicname=256-bit-encryption.html&version=latest#enable-256-bit-encryption-Java8u151 "For Java 8 update 151 (8u151) or later")

From the two links above the “Java home directory” mentioned is defined in points (1) or (2) above.
