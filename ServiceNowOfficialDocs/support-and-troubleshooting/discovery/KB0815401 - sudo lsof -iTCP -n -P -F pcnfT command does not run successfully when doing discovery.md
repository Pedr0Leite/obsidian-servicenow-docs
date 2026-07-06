---
title: "\"sudo lsof -iTCP -n -P -F pcnfT\" command does not run successfully when doing discovery"
aliases:
  - KB0815401
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815401
kb_number: KB0815401
last_modified: 2026-05-22
---

## "sudo lsof -iTCP -n -P -F pcnfT" command does not run successfully when doing discovery

  

### Issue

Getting error "Exit status: 1 User DiscoUser has no right to run lsof -iTCP -n -P -F pcnfT under sudo;" when running discovery on unix machines.

The command is working fine and returning results when executing it from the pattern in debug mode and also from the user session (interactive SSH session)

Horizontal discovery is working fine if granted with all sudo rights in sudoers file.

### Release

ALL

### Cause

The /etc/sudoers has been configured with below commands to work:

User <user> may run the following commands on <server>:  
(root) NOPASSWD: /bin/cat \*.properties, /bin/cat \*.conf, /bin/cat \*.cfg, /bin/cat \*.ini, /bin/cat \*.cnf, /bin/cat \*.discovery, /bin/cat \*.prop, /bin/cat \*.config, /bin/cat /proc/\*/environ, /bin/cat \*/bootstrap.kubeconfig, /bin/cat \*.sh, /bin/cat \*.yaml, /usr/local/sbin/di, /bin/dir, /sbin/dmidecode, /sbin/dmsetup ls, /sbin/dmsetup table \*, /sbin/dmsetup info \*, /sbin/fdisk -l, /bin/find, !/bin/find \* -delete \*, !/bin/find \* -exec\*, /usr/sbin/httpd2-worker -V, /usr/sbin/httpd2-prefork -V, /usr/sbin/httpd -V, /bin/ls, /sbin/lsof, /sbin/multipath -ll, /bin/ps  
  

As per documentation below, The /etc/sudoers file should specifically mention "DiscoUser ALL=(root) NOPASSWD:/usr/sbin/dmidecode,/usr/sbin/lsof,/sbin/ifconfig"

[https://docs.servicenow.com/csh?topicname=r\_SSHCredentialsForm.html&version=latest](https://docs.servicenow.com/csh?topicname=r_SSHCredentialsForm.html&version=latest)

### Resolution

To resolve error "User DiscoUser has no right to run lsof -iTCP -n -P -F pcnfT under sudo;" on "AIX - Application Dependency Mapping" probe add MID server parameter "mid.ssh.disable\_privilege\_check" = true and restart the MID server and re-run discovery.

  
Alternatively, you can modify the /etc/sudoers file to be similar with below if MID server parameter cannot be "mid.ssh.disable\_privilege\_check" added/modified  
\====

FROM:  
Matching Defaults entries for linuxdisc on this host:  
syslog=auth, always\_set\_home, env\_reset, logfile=/var/log/sudo.log  
  
User linuxdisc may run the following commands on this host:  
(root) NOPASSWD: /usr/bin/find, (root) !/usr/bin/find \* -delete \*, (root) !/usr/bin/find \* -exec\*, (root) /bin/cat \*.cfg, (root) /bin/cat \*.cnf, (root) /bin/cat \*.conf, (root) /bin/cat \*.discovery, (root) /bin/cat \*.ini, (root) /bin/cat \*.properties, (root) /bin/cat \*.prop, (root) /bin/cat  
\*.conf, (root) /bin/cat /proc/\*/environ, (root) /bin/cat \*/bootstrap.kubeconfig, (root) /bin/cat \*.sh, (root) /bin/cat \*.yaml, (root) /usr/local/sbin/di, (root) /usr/bin/dir, (root) /usr/sbin/dmidecode, (root) /sbin/dmsetup ls, (root) /sbin/dmsetup table \*, (root) /sbin/dmsetup info \*, (root)  
/sbin/fdisk -l, (root) /usr/sbin/httpd2-worker -V, (root) /usr/sbin/httpd2-prefork -V, (root) /usr/sbin/httpd -V, (root) /usr/sbin/ls, (root) /usr/bin/lsof, (root) /sbin/multipath -ll, (root) /bin/ps, (root) /bin/netstat, (root) /sbin/rabbitmqctl status, (root) /sbin/haproxy -version

TO:  
Matching Defaults entries for DiscoUser on this host:  
syslog=auth, always\_set\_home, env\_reset, logfile=/var/log/sudo.log  
  
User DiscoUser may run the following commands on this host:  
(root) NOPASSWD: /usr/bin/find  
(root) NOPASSWD: !/usr/bin/find \* -delete \*  
(root) NOPASSWD: !/usr/bin/find \* -exec\*  
(root) NOPASSWD: /bin/cat \*.cfg  
(root) NOPASSWD: /bin/cat \*.cnf  
(root) NOPASSWD: /bin/cat \*.conf  
(root) NOPASSWD: /bin/cat \*.discovery  
(root) NOPASSWD: /bin/cat \*.ini  
(root) NOPASSWD: /bin/cat \*.properties  
(root) NOPASSWD: /bin/cat \*.prop  
(root) NOPASSWD: /bin/cat \*.conf  
(root) NOPASSWD: /bin/cat /proc/\*/environ  
(root) NOPASSWD: /bin/cat \*/bootstrap.kubeconfig  
(root) NOPASSWD: /bin/cat \*.sh  
(root) NOPASSWD: /bin/cat \*.yaml  
(root) NOPASSWD: /usr/local/sbin/di  
(root) NOPASSWD: /usr/bin/dir  
(root) NOPASSWD: /usr/sbin/dmidecode  
(root) NOPASSWD: /sbin/dmsetup ls  
(root) NOPASSWD: /sbin/dmsetup table \*  
(root) NOPASSWD: /sbin/dmsetup info \*  
(root) NOPASSWD: /sbin/fdisk -l  
(root) NOPASSWD: /usr/sbin/httpd2-worker -V  
(root) NOPASSWD: /usr/sbin/httpd2-prefork -V  
(root) NOPASSWD: /usr/sbin/httpd -V  
(root) NOPASSWD: /usr/sbin/ls  
(root) NOPASSWD: /usr/bin/lsof  
(root) NOPASSWD: /sbin/multipath -ll  
(root) NOPASSWD: /bin/ps  
\====
