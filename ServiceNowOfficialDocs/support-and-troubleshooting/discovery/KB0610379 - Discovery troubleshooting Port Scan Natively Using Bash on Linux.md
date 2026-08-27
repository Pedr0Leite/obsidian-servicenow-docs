---
title: "Discovery troubleshooting: Port Scan Natively Using Bash on Linux"
aliases:
  - KB0610379
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0610379
kb_number: KB0610379
last_modified: 2026-05-19
---

## Discovery troubleshooting: Port Scan Natively Using Bash on Linux

  

### Issue

When troubleshooting Discovery issues, carrying out a port scan of a device to see whether the ports are open and responding is often necessary. This scan is normally done from the MID server host server to the device that is not being discovered.

### Release

Any

### Resolution

Applications such as nmap and zenmap can be used to obtain this information, but it can also be done by using a small Bash script on Linux, which avoids having to install third-party software.

# Script Process

* * *

1.  Log in to the Linux MID server host server.
2.  Using the editor of your choice (for example, vim, gedit, or emacs), enter the following script. 
    
    **Note**: For this script to run properly, the timeout command, which allows commands to time out after a set period of time, must be installed.
    
    #!/bin/bash  
    \# Script: discoports.sh  
    \# Use: Checks for the ports required by Discovery, on a remote host.  
    # 
    
    remhost=""
    
    \# Script requires the "timeout" command - if it's not available, exit....  
    command -v timeout >/dev/null 2>&1 || { echo >&2 "timeout command is not available! Aborting."; exit 1; }
    
    \# Check for an argument being passed (should be the hostname/IP Address) if none passed, prompt for it!  
    if \[ -z "$1" \]  
    then  
       while \[ "$remhost" = "" \]  
       do  
          echo -n "Enter the hostname or IP Address of the remote host: "  
          read remhost  
       done  
    else  
       remhost=$1  
    fi
    
    \# Define the array that contains the port numbers we wish to check.  
    declare -a DPort=(22 53 80 135 137 161 427 443 515 548 5060 5480 5989 9100)
    
    # Run through the array, and display if the port is open or closed.  
    for i in "${DPort\[@\]}"  
    do  
       timeout 1 bash -c "cat < /dev/null > /dev/tcp/$remhost/$i"  
        if \[ $? -eq 0 \]; then        printf "%-5s %-4s %-10s\\n" "Port:" "$i" "--> Open"      else         printf "%-5s %-4s %-10s\\n" "Port:" "$i" "--> Closed"     fi  done
3.  Save the script as discoports.sh and make it executable (chmod ug+x discoports.sh).
    

# Example Use

* * *

1.  Log in to the Linux MID server host server.
2.  Run the script.
    
    You can either pass the TCP IP address/Hostname as an argument to the script or you will be prompted for it.
    
    The script as written will check all of the ports that are commonly used by Discovery. 
    
    -   $ **./discoports.sh hostname.com**
        
        This command would take the argument "hostname": hostname.com and attempt to check for open ports on that host.
        
    -   $ **./discoports.sh 10.1.10.10**
        
        This command would take the argument IP Address: 10.1.10.10 and attempt to check for open ports on that host.
        
    -   $ **./discoports.sh**
        
        Enter the hostname or IP Address of the remote host: 
        
        As no argument has been passed to the script, it will prompt for the hostname or IP Address of the remote host.
        
    
    The output from the script, will resemble the following example:
    
    **./discoports.sh myhost.com**
    
    Port: 22   --> Closed   
    Port: 53   --> Closed   
    Port: 80   --> Open   
    Port: 135  --> Closed   
    Port: 137  --> Closed   
    Port: 161  --> Closed   
    Port: 427  --> Closed   
    Port: 443  --> Open   
    Port: 515  --> Closed   
    Port: 548  --> Closed   
    Port: 5060 --> Closed   
    Port: 5480 --> Closed   
    Port: 5989 --> Closed   
    Port: 9100 --> Closed
