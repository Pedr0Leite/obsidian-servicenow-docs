---
title: "Recommended procedure to Re-Install/Upgrade the SN odbc driver"
aliases:
  - KB0621675
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621675
kb_number: KB0621675
last_modified: 2025-01-03
---

## Recommended procedure to Re-Install/Upgrade the SN odbc driver

  

### Issue

Many times when uninstalling the ODBC driver if any windows or connections are left open, the uninstall process will not remove those items. In addition, it leaves the registry with old values that need to be cleaned up before reinstalling the now driver.  The following steps are recommended to reinstall/upgrade and configure the ODBC driver.

1.  Make sure all driver connections are closed.
    
2.  Run the uninstall via the Windows Add/Remove programs.
    
3.  Once the uninstall is complete, the driver can leave registry settings behind depending on user permissions.
    
    We need to clean this up before the reinstall.
    
4.  Access the registry and validate that all SN ODBC KEY entries have been removed. If not, manually remove them.
    
    The locations will be different in the registry depending on the bit level of the driver:
    
    -   64-bit: Key Entries will be found in the following locations:  
        
        HKEY\_LOCAL\_MACHINE\\SOFTWARE\\ODBC\\ODBC.INI  
        HKEY\_LOCAL\_MACHINE\\SOFTWARE\\ODBC\\ODBCINST.INI\\ODBC DRIVERS  
        HKEY\_LOCAL\_MACHINE\\SOFTWARE\\ODBC\\ODBCINST.INI\\ServiceNow ODBC Driver 64-bit
        
    -   32-bit: Key Entries will be found in the following locations:  
        
        HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Wow6432Node\\ODBC\\ODBC.INI  
        HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Wow6432Node\\ODBC\\ODBCINST.INI\\ODBC Drivers  
        HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Wow6432Node\\ODBC\\ODBCINST.INI\\ServiceNow ODBC Driver 32-bit
        
    
    Once all registry settings are validated and removed, install the driver.
    
5.  Using the latest ODBC install package, right-click on the installer and select Run as admin.
    
    Note: The bit level of the driver to use depends on the bit level of the binding application; not necessarily the OS. For example, if using a 64-bit OS with 32-bit version of Crystal, use the 32-bit ODBC driver.
    
6.  Select all defaults on the driver installation.
    
7.  Once the installation is complete, access the MS ODBC administrator and configure the DSN.
    
    You do not need to configure anything in the SN ODBC Management console, unless the customer has a proxy.
