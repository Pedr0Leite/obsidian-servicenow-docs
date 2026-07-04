---
title: "Running the Edge Encryption proxy server on Linux on a privileged port as a non-privileged user"
aliases:
  - KB0622995
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622995
kb_number: KB0622995
last_modified: 2024-04-07
---

## Issue

# Description

The Edge Encryption proxy server runs as a service on Windows and as a daemon on Linux. To install the Edge Encryption proxy server on Linux as a daemon and allow it to listen on a privileged port like 443 or 80, you can use authbind. Authbind is a standard Linux binary available for most distros. If using CentOS 6 or below, you will need to manually compile authbind. 

After installing and configuring authbind, you can optionally use the example scripts provided below to automatically start the proxy on startup.

# Procedure

##### Install authbind and configure the proxy server

1.  Install authbind.
    -   To install authbind on Ubuntu and other Debian based systems, run the following command: sudo apt-get install authbind
    -   To install authbind on Fedora and other RPM systems, run the following command: sudo yum install authbind
    -   CentOS 6 and below does not have a binary available as an RPM. You must compile authbind manually using the instructions in the next section.
2.  Create the authbind port configuration file for the proxy to use.
3.  Create a file under /etc/authbind/byport named after the port or ports necessary.
    -   File path for port 443: /etc/authbind/byport/443
    -   File path for port 80: /etc/authbind/byport/80
4.  These files have to be owned by the proxy service user, so change ownership using the following command: chown USER.USER /etc/authbind/byport/443
5.  Restrict file permissions: sudo chmod 500 /etc/authbind/byport/443.
6.  Configure the proxy server properties file to launch on port 80 and/or 443. 
    1.  Navigate to <proxy install directory>/conf/edgeencryption.properties. 
    2.  Configure the following properties as needed: 
        -   edgeencryption.proxy.http.port
        -   edgeencryption.proxy.https.port
7.  Because authbind does not support IPv6, configure the Edge Encryption proxy server wrapper file to use IPv4.
    1.  Navigate to <proxy install directory>/conf/wrapper.conf
    2.  Add the following to the wrapper.conf file:
        
        > #Authbind only supports IPv4. Do not use IPv6.  
        > 
        > #Use the next available numeral for the following parameter.
        > 
        > #For example if the previous parameter is numbered wrapper.java.additional.3
        > 
        > #then this should be numbered wrapper.java.additional.4
        > 
        > wrapper.java.additional.\*=-Djava.net.preferIPv4Stack=true
        
8.  Launch the Edge Encryption proxy server: authbind --deep ./startup.sh

<table class="noteTable" style="border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></td><td style="text-align: left;"><strong>Tip</strong>: To run the proxy server&nbsp;automatically on startup, use the script templates described in <a title="Define an Edge Encryption proxy server init.d script" href="#scripts" rel="nofollow">Define an Edge Encryption proxy server init.d script</a>. Newer distros tend to use <span style="font-family: 'courier new', courier;">system.d</span>. Legacy systems tend to use <span style="font-family: 'courier new', courier;">init.d</span>. Many distros support both. The <span style="font-family: 'courier new', courier;">init.d</span> method is being phased out by many major distributions.</td></tr></tbody></table>

##### Compile authbind manually for CentOS 6 and below

If using CentOS 6 or below, you must manually compile authbind. 

1.  Configure a new repository: svn co https://github.com/tootedom/authbind-centos-rpm.git
2.  Make a build folder: mkdir /root/rpmbuild 
3.  Get the authbind source: cp -R authbind-centos-rpm.git/trunk/authbind/\* /root/rpmbuild/
4.  Go to the rpmbuild folder and get the authbind TAR ball.
    
    > cd /root/rpmbuild/SOURCES  
    > wget http://ftp.debian.org/debian/pool/main/a/authbind/authbind\_2.1.1.tar.gz 
    
5.  Rename the TAR ball and build.  
    
    > mv authbind\_2.1.1.tar.gz authbind-2.1.1.tar.gz  
    > cd ../  
    > rpmbuild -v -bb --clean SPECS/authbind.spec  
    >   
    
    > RPM is built and available at /root/rpmbuild/RPMS/x86\_64/authbind-2.1.1-0.1.x86\_64.rpm  
    >   
    
6.  Install the RPM package.
    
    > cd /root/rpmbuild/RPMS/x86\_64/  
    > rpm -Uvh authbind-2.1.1-0.1.x86\_64.rpm
    

##### Define an Edge Encryption proxy server init.d script

You can use an init.d script to automatically start the proxy server on startup.

<table class="noteTable" style="border: 1px solid #e0e0e0;" align="left"><tbody><tr><td style="text-align: center;"><span style="color: #000000;"><img title="Note" src="/Note_25x.pngx" alt="" align="bottom" border="" hspace="" vspace=""></span></td><td style="text-align: left;"><span style="color: #000000;"><strong>Note</strong>: The <span style="font-family: 'courier new', courier;">init.d</span> method is being phased out by many major distributions. Newer distros tend to use <span style="font-family: 'courier new', courier;">system.d</span>. For more information on that method, see <span style="color: #0000ff;"><a style="color: #0000ff;" title="Define an Edge Encryption proxy server service file" href="system.d" rel="nofollow">Define an Edge Encryption proxy server service file</a></span>.</span></td></tr></tbody></table>

  
  
  

1.  Complete the steps in the [Install authbind and configure the proxy server](#authbind "Install authbind and configure the proxy server") section or the [Install setcap and configure the proxy server](setcap "Install setcap and configure the proxy server") [section.](#setcap "Install setcap and configure the proxy server")
2.  Create the following file: /etc/init.d/edge
3.  In the file, define the following script. Change the variables as needed.
    
    > #!/bin/bash
    
    >   
    > \# This init.d script takes care of starting and stopping  
    > \# the ServiceNow Edge Encryption proxy (edgeencryption).  
    > #  
    > \# chkconfig: 2345 80 20  
    > \# description: ServiceNow Edge Encryption proxy.  
    > \# processname: jsw, java
    
    >   
    > \### BEGIN INIT INFO  
    > \# Provides: edge\_proxy  
    > \# Required-Start:  
    > \# Required-Stop:  
    > \# Should-Start:  
    > \# Default-Start: 2 3 4 5  
    > \# Default-Stop: 0 1 6  
    > \# Short-Description: edge\_proxy  
    > \# Description: ServiceNow Edge Encryption Proxy  
    > \### END INIT INFO
    
    >   
    > \# Source LSB function library.  
    > . /lib/lsb/init-functions
    
      
    
    > \# Source networking configuration.  
    > . /etc/sysconfig/network
    
      
    
    > start() {  
    > 
    > > \# Start Edge Proxy
    > 
    > > #Path to startup.sh script MUST be in double quotes
    > 
    > > /usr/bin/authbind --deep "<PROXY INSTALL DIRECTORY>/proxy-daemon\_443/startup.sh"
    > 
    > } '
    
    >   
    > stop() {  
    > 
    > > \# Stop Edge Proxy
    > 
    > > <PROXY INSTALL DIRECTORY>/proxy-daemon\_443/shutdown.sh
    > 
    > } 
    
      
    
    > case "$1" in  
    > 
    > > start)  
    > > 
    > > > start
    > > 
    > > > ;;
    > > 
    > > stop)  
    > > 
    > > > stop
    > > 
    > > > ;;
    > > 
    > > restart)  
    > > 
    > > > stop  
    > > > start  
    > > > ;;
    > > 
    > > \*)  
    > > 
    > > > echo "Usage: $0 {start|stop|restart}"
    > 
    > esac
    
    >   
    > exit 0   
    >  
    
4.  Enable the service: sudo update-rc.d edge enable
5.  Start the service: sudo service edge start
6.  Stop the service: sudo service edge stop
7.  Restart the service: sudo service edge restart 

##### Define an Edge Encryption proxy server system.d

You can use a system.d service file to automatically start the proxy server on startup.

1.  Complete the steps in the [Install authbind and configure the proxy server](authbind "Install authbind and configure the proxy server") section or the [Install setcap and configure the proxy server](setcap "Install setcap and configure the proxy server") section.
2.  Create the following file: /etc/systemd/system/edge.service.  
    In the file, define the following script. Change the variables as needed.  
    
    > \# This unit file takes care of starting and stopping  
    > \# the ServiceNow Edge Encryption proxy (edgeencryption).  
    >   
    > \# Make sure it launches after MySQL.  
    > \# Necessary if you use tokenization.  
    > \[Unit\]  
    > After=mysql.service  
    >   
    > \# Service type is forking since the startup script forks off  
    > \# other processes.  
    > \# Replace USER\_NAME with your service user.  
    > \[Service\]  
    > Type=forking  
    > User=USER\_NAME  
    >   
    > \# Set the path to your startup and shutdown scripts, inclusive.  
    > \# Path to startup.sh script MUST be in double quotes  
    > ExecStart=/usr/bin/authbind --deep "/PATH/TO/YOUR/PROXY/INSTALL/startup.sh"  
    > ExecStop=/PATH/TO/YOUR/PROXY/INSTALL/shutdown.sh  
    >   
    > SyslogIdentifier=edge\_proxy  
    >   
    > \# Define restart behavior.  
    > \# Choices are: no, on-success, on-failure, on-abnormal, on-watchdog, on-abort, or always.  
    >   
    > \# "https://www.freedesktop.org/software/systemd/man/systemd.service.html"  
    > Restart=always  
    > RestartSec=4  
    >   
    > \# Launch the service when in multi-user mode.  
    > \[Install\]  
    > WantedBy=multi-user.target
    
3.  Enable the service: sudo systemctl enable edge.service
4.  Reload daemon: sudo systemctl daemon-reload
5.  Start the service: sudo systemctl start edge.service
6.  Stop the service: sudo systemctl stop edge.service
