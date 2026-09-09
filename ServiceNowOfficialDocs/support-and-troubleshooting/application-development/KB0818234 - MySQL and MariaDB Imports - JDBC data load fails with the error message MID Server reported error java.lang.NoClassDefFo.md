---
title: "MySQL and MariaDB Imports - JDBC data load fails with the error message \"MID Server reported error: java.lang.NoClassDefFoundError: Could not initialize class.\""
aliases:
  - KB0818234
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818234
kb_number: KB0818234
last_modified: 2024-04-08
---

## MySQL and MariaDB Imports - JDBC data load fails with the error message "MID Server reported error: java.lang.NoClassDefFoundError: Could not initialize class."

  

### Issue

During data load phase of imports from MySQL or MariaDB servers fail with the following error message on ServiceNow instance user interface:

```
java.lang.NoClassDefFoundError: Could not initialize class org.mariadb.jdbc.internal.util.PidFactory$CLibrary
```

and the following error message and the stack trace exist before the above error message in **agent.log** of MID Server **which is deployed on a Linux server**:

```
2020-03-13 06:09:54  (390) Worker-Standard:JDBCProbe-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx SEVERE *** ERROR *** java.lang.UnsatisfiedLinkError: /tmp/jna-3506402/jna7843338838921309827.tmp: /tmp/jna-3506402/jna7843338838921309827.tmp: failed to map segment from shared object: Operation not permitted    at java.lang.ClassLoader$NativeLibrary.load(Native Method)    at java.lang.ClassLoader.loadLibrary0(ClassLoader.java:1941)    at java.lang.ClassLoader.loadLibrary(ClassLoader.java:1824)    at java.lang.Runtime.load0(Runtime.java:809)    at java.lang.System.load(System.java:1086)    at com.sun.jna.Native.loadNativeDispatchLibraryFromClasspath(Native.java:851)    at com.sun.jna.Native.loadNativeDispatchLibrary(Native.java:826)    at com.sun.jna.Native.<clinit>(Native.java:140)
```

### Release

Madrid and onwards.

### Cause

A new version of MariaDB JDBC driver is bundled with the MID Servers for Madrid and onwards releases. This driver's implementation is different than the previous releases and it tries to invoke a native Operating System (OS) library call while initializing connection to the DB Server.

The OpenJDK distributed with MID Server is making use of the OS designated temporary file directory (typically `/tmp`) while making this native call, and the Linux system may be configured to restrict code executions from this directory for security reasons. Typically this will be a mount point with a flag of `NOEXEC`.

For example from the example stack trace, we can see the temporary folder is `/tmp` and when we check the contents of the `/etc/fstab` file we may see the flag for `NOEXEC` like the following line:

```
....../dev/mapper/volgroup1-tmp /tmp   xfs     rw,nodev,noexec,nosuid 0 0......
```

### Resolution

In order to overcome this restriction, you will need to redirect OpenJDK (Java VM) to a different directory for temporary file creation and execution. Please follow the below steps:

1.  Login to your Linux host where you have deployed the MID Server
2.  Switch to the MID Server home directory (typically the directory named `agent`)
3.  Create a folder with the name of `tmp` with the command:  
      
    mkdir tmp  
      
    
4.  Switch to the wrapper configuration folder with the following command:  
      
    cd conf  
      
    
5.  Edit `wrapper-override.conf` file with a text editor like `vi` or `pico` and add the following to the bottom of the file:  
      
    wrapper.java.additional.299=-Djava.io.tmpdir=tmp  
      
    Notice that the number `299` should be unique and there shouldn't be any other line with the wrapper.java.additional.299 parameter. If there is any other, please use a different number higher than `200`.  
      
    
6.  Save the file and restart your MID Server.

Next time you invoke a JDBC data load against a MySQL or MariaDB database, MID Server OpenJDK will use the new folder for the execution of OS native calls.
