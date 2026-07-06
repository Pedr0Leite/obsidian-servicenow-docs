---
title: "Edge Proxy Automatic Upgrade Fails With: Expected proxy to be running build 'edgeencryption-xxx__xxx-xxx' but it is actually running build edgeencryption-xxx__xxx-xxx"
aliases:
  - KB0685681
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0685681
kb_number: KB0685681
last_modified: 2024-04-07
---

## Edge Proxy Automatic Upgrade Fails With: Expected proxy to be running build 'edgeencryption-xxx\_\_xxx-xxx' but it is actually running build edgeencryption-xxx\_\_xxx-xxx'

  

### Issue

# Symptoms

* * *

You have scheduled an Edge Encryption automatic upgrade from Edge Encryption Configuration -> Upgrade Schedules the upgrade ends with a Status of Failed, the Failure reason shows something similar to the following:

Expected proxy to be running build 'edgeencryption-jakarta-05-03-2017\_\_patch8a-03-12-2018\_03-15-2018\_1411' but it is actually running build 'edgeencryption-jakarta-05-03-2017\_\_patch4-09-21-2017\_10-04-2017\_1643' 

This indicates that even though the proxy upgrade appeared to complete the proxy could not start on the upgraded proxy version so the proxy was started on the older version instead.

# Cause

* * *

To find the cause do the following:

(1) Go to the machine that is hosting the proxy that had the failed upgrade

(2) You will see that a new proxy directory was created as a result of the upgrade (if on a version below London, in London or above the old directory is re-used) attempt that appends a date and time stamp to the end of the directory name that corresponds to when the upgrade was done, e.g. $proxy\_installation\_directory/edgeproxy\_443\_2018-05-03-08-59

(3) Go into that directory then change directory to "logs" and list the directories there, you will notice that there is no edgeencryption.log there, but there is a wrapper\_<date>.log, in that log you will see the following:

STATUS | wrapper  | 2018/05/02 08:42:01.172 | --> Wrapper Started as Daemon

STATUS | wrapper  | 2018/05/02 08:42:01.373 | Launching a JVM...

ERROR  | wrapper  | 2018/05/02 08:42:01.374 | Unable to start JVM: No such file or directory (2)

ERROR  | wrapper  | 2018/05/02 08:42:01.374 | JVM exited while loading the application.

STATUS | wrapper  | 2018/05/02 08:42:05.480 | Launching a JVM...

ERROR  | wrapper  | 2018/05/02 08:42:05.481 | Unable to start JVM: No such file or directory (2)

ERROR  | wrapper  | 2018/05/02 08:42:05.481 | JVM exited while loading the application.

STATUS | wrapper  | 2018/05/02 08:42:09.587 | Launching a JVM...

ERROR  | wrapper  | 2018/05/02 08:42:09.588 | Unable to start JVM: No such file or directory (2)

ERROR  | wrapper  | 2018/05/02 08:42:09.588 | JVM exited while loading the application.

ERROR  | wrapper  | 2018/05/02 08:42:13.696 | JVM exited while loading the application.

STATUS | wrapper  | 2018/05/02 08:42:17.802 | Launching a JVM...

ERROR  | wrapper  | 2018/05/02 08:42:17.802 | Unable to start JVM: No such file or directory (2)

ERROR  | wrapper  | 2018/05/02 08:42:17.803 | JVM exited while loading the application.

FATAL  | wrapper  | 2018/05/02 08:42:17.803 | There were 5 failed launches in a row, each lasting less than 300 seconds.  Giving up.

FATAL  | wrapper  | 2018/05/02 08:42:17.803 |   There may be a configuration problem: please check the logs.

STATUS | wrapper  | 2018/05/02 08:42:17.903 | <-- Wrapper Stopped

This indicates that the JVM cannot be found so the proxy could not start.

(4) Go to the directory where the proxy was running before the upgrade attempt, e.g. $proxy\_installation\_directory/edgeproxy\_443 and change directory to the "conf" directory and look at the wrapper.conf file, check the setting for the field wrapper.java.command, in this example the setting points to a relative path to the JDK, e.g.:

wrapper.java.command=../jdk1.8.0\_152/jre/bin/java 

In this case a custom JDK has been installed at the location:

$proxy\_installation\_directory/edgeproxy\_443/jdk1.8.0\_152

And this works fine when the proxy is running out of the $proxy\_installation\_directory/edgeproxy\_443 directory path, but when the upgrade is done the $proxy\_installation\_directory/edgeproxy\_443/jdk1.8.0\_152 directory is not copied into the new upgraded directory at: $proxy\_installation\_directory/edgeproxy\_443\_2018-05-03-08-59, if it were it would look as follows:

$proxy\_installation\_directory/edgeproxy\_443\_2018-05-03-08-59/jdk1.8.0\_152

The upgrade does copy the wrapper.conf from $proxy\_installation\_directory/edgeproxy\_443 to the new directory at $proxy\_installation\_directory/edgeproxy\_443\_2018-05-03-08-59/jdk1.8.0\_152

So when the proxy tries to start from the new directory wrapper.java.command is still pointing to a relative directory path:

wrapper.java.command=../jdk1.8.0\_152/jre/bin/java 

And this cannot be found since $proxy\_installation\_directory/edgeproxy\_443\_2018-05-03-08-59/jdk1.8.0\_152 does not exist

# Resolution

* * *

**Note:** Starting in the Kingston release the JRE is no longer bundled with the proxy so relative paths inside of the proxy directory structure may no longer work, [Edge Encryption release notes](https://docs.servicenow.com/csh?topicname=edge-encryption-rn.html&version=latest "Edge Encryption release notes") for Kingston.

The most direct way to resolve this issue is to specify an absolute path to the JDK/JRE in the $proxy\_installation\_directory/edgeproxy\_443 version of the wrapper.conf file instead of a relative path, e.g.:

wrapper.java.command=/usr/local/servicenow/edgeproxy\_443/jdk1.8.0\_152/jre/bin/java 

**Note:** Do not have any other settings of wrapper.java.command in the wrapper.conf file besides the one you want to use, even if commenting out an unwanted setting for wrapper.java.command using the **#** symbol the system will still recognize it and try to use it.  If for some reason you want to keep more than one wrapper.java.command setting, be sure it is under the one you want to use in the wrapper.conf file, e.g. you should not do this in the file:

#wrapper.java.command=../jdk1.8.0\_152/jre/bin/java

wrapper.java.command=/usr/local/servicenow/edgeproxy\_443/jdk1.8.0\_152/jre/bin/java 

But this would be ok:

wrapper.java.command=/usr/local/servicenow/edgeproxy\_443/jdk1.8.0\_152/jre/bin/java 

#wrapper.java.command=../jdk1.8.0\_152/jre/bin/java

So when the wrapper.conf file is copied from the old proxy location to the new one the new directory will be able to find the JDK since it is specified in an absolute path.

Keep in mind if this is done you must never delete the /usr/local/servicenow/edgeproxy\_443/jdk1.8.0\_152 path or else later versions of the proxy will not be able to access the JDK.

You could also move or copy the location of the JDK outside of the proxy paths all together to a "safe" location that will never be deleted, in any case it is always better to use an absolute path instead of a relative one if you are using your own JDK.

After this is done restart the proxy in the old location, e.g. $proxy\_installation\_directory/edgeproxy\_443 and schedule the upgrade again from the UI, this time the upgrade should be successful.
