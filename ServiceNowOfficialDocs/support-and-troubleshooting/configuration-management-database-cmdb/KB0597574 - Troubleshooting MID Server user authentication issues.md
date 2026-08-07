---
title: "Troubleshooting MID Server user authentication issues"
aliases:
  - KB0597574
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597574
kb_number: KB0597574
last_modified: 2025-04-07
---

## Troubleshooting MID Server user authentication issues

  

### Issue

Table of Contents

1.  [Is the MID Server user configured correctly in the config.xml?](#midUserInLog)
2.  [Is the MID password in the config.xml correct?](#midPassword)
3.  [Does the MID password have special characters?](#midPasswordSC)
4.  [Does the MID Server user in the config.xml file have correct roles on the instance?](#midRoles)
5.  [Is the MID Server user locked out on the instance?](#midUserLockedOut)
6.  [Was the instance recently cloned?](#instanceCloned)
7.  [Was the instance recently reinstalled?](#midReinstalled)

  

Symptoms

-   All MID Servers are down
-   CIs are duplicated during Discovery
-   The MID Server keeps going down
-   The MID agent log is reporting: 404, could not authenticate
-   The MID Server upgrade is hung
-   The MID Server cannot restart

Details

Along with a clear communication path to the instance, the MID Server requires a valid user to authenticate with. The inability of the MID Server to successfully authenticate with the instance will affect the MID Server's ability to install, upgrade, and execute services for the instance. Most authentication issues are reported either in the MID Server's agent log or wrapper log. 

Question and Answer

-   **Is the MID Server user ID entered accurately into the agent/config.xml on the MID host machine?**  
    -   _I don’t know._  
        -   To determine whether the MID Server user is properly entered into the config.xml:  
            1.  Log on to the host machine as a local admin or the MID Server user.
            2.  Navigate to the /agent directory where the MID was installed.
            3.  Edit the config.xml file.
            4.  Search for the parameter: **mid.instance.username.**
            5.  Copy the value of that parameter into your buffer.
            6.  Return to the instance.
            7.  In the text editor, navigate to **Organization > Users**.
            8.  Search for **User ID = \[the name in your buffer\]**.  
                -   NOTE: you could also attempt to log in to the instance from the browser of the host instance using the user name.
    -   **_Yes, the MID Server user is entered correctly in the Organization > Users database._**  
        -   If the MID Server user's ID is not the issue preventing successful authentication. Keep troubleshooting. [\[Back to top\]](#toc)
    -   **_No, the MID Server user does not exist in the user database on the instance._**  
        -   **ROOT CAUSE:** The MID Server user on the instance and the MID Server user in the config.xml must match. Sometimes after cloning a production instance to a development instance, there are mismatches in the user name and passwords as MID Servers are not cloned along with the instance.
        -   **SOLUTION**: Either update the MID Server user's user name on the instance or in the config.xml file. As a word of caution, often a single MID Server user name is used across multiple MID Servers and MID Server clusters. Therefore, updating the config.xml is the least problematic option.

  

-   **Is the MID Server user password properly entered into the agent/config.xml?**  
    -   _I don’t know_  
        -   If the MID Server user password is not correct, the agent log will report a 'failed to authenticate' error. To see if this is the case:  
            1.  Log on to the host machine of the MID Server in question.
            2.  Navigate to the agent/logs directory.
            3.  Edit the agent log.
            4.  Search for the phrase: **_failed to authenticate_**_._
            5.  If you find the authentication error, the MID Server user password is not correct providing you have already validated that the MID Server user ID is correct.
    -   **_Yes, the MID Server user password is properly entered into the agent/config.xml._**  
        -   An incorrect password in the config.xml file is not the issue preventing successful authentication. Keep troubleshooting. [\[Back to top\]](#toc)
    -   **_No, the MID Server user password is not properly entered into the agent/config.xml._**  
        -   **ROOT CAUSE:** The MID Server relies on the **mid.instance.password** parameter in the config.xml to provide the appropriate authentication to connect to the instance. The value set is typically entered in clear text, either directly in the config.xml or through the MID Installer. Once the MID Server reads the password, it rewrites the parameter value as the encrypted version of the password. Because of this, it is difficult to validate the password in the config.xml visually. You have to rely on the logs to do that. 
        -   **SOLUTION:** If you know the password, you can stop the MID using the scripts in the /agent directory on the host machine and edit the config.xml file with the correct known password. Restart the MID Server. If the password is correctly entered, the MID Server will resume service. If the password is not correct, you may need to [reset the MID Server user password](/kb_view.do?sysparm_article=KB0597570 "reset the MID Server user password").

  

-   **Does the MID Server user password contain special characters?**  
    -   **_Yes, the MID Server user password contains special characters._**  
        -   **ROOT CAUSE:** It is common practice to include special characters when creating a strong password, and they can be used, but the installer may not have encoded them for XML correctly. Passwords in the config.xml file are entered in clear text and encrypted and re-written as soon as the MID Server is started for the first time. 
        -   **SOLUTION:** [Change the MID User password](/kb?id=kb_article_view&sysparm_article=KB0746702 "Change the MID User password") and Manually encode the special characters as shown in [MID Server configuration: Using special characters in an XML file](https://docs.servicenow.com/bundle/madrid-servicenow-platform/page/product/mid-server/concept/c_MIDServerConfiguration.html "MID Server configuration: Using special characters in an XML file").
    -   **_No, the MID Server user password is now properly entered into the agent/config.xml._**  
        -   Special characters in the password is not the issue preventing successful authentication. Keep troubleshooting. [\[Back to top\]](#toc)

  

-   **Does the MID Server user exist on the instance with the appropriate roles?**   
    -   _I don’t know._  
        -   To find out if the MID Server user has appropriate role:  
            1.  Navigate to **Organization > Users**.
            2.  Search for **User ID = {{your MID Server user Name}}**
            3.  In the Related Lists section at the bottom of the form, select the **Roles** tab.
            4.  At a minimum, there should be an entry to **mid\_server**.
    -   _Yes, the MID Server user is assigned the mid\_server role._  
        -   Lack of mid\_server role is not the issue preventing successful authentication. Keep troubleshooting. [\[Back to top\]](#toc)
    -   _**No, the MID Server user is not assigned the mid\_server role.**_  
        -   **ROOT CAUSE:** In order for the MID Server user to have access to tables like the ECC queue and to have permission to execute tasks specific to managing MID Server requests, the user must be assigned at a minimum the role of mid\_server. Other services and applications, such as Discovery and Orchestration, may require other roles. [Read more about the list of roles that could be used by services provided by MID Server](https://docs.servicenow.com/search?q=roles&labels=20&labels=21&labels=22&labels=23&labels=24&labels=25&labels=26&labels=27&labels=28&labels=29 "Read more about the list of roles that could be used by services provided by MID Server").
        -   **SOLUTION:** Assign the MID Server role to the MID Server user. 

  

-   **Is the MID Server user locked out?**  
    -   _**I don't know.**_  
        -   To find out if the MID Server user has been locked out:  
            1.  Navigate to **Organization > Users** from the left navigation text filter.
            2.  Search for **User ID = to you MID Server user ID**.
            3.  Open the user record.
            4.  Locate the **Locked Out** field. If it is checked, the user is locked out.
    -   _**Yes, the MID Server user is locked out.**_  
        -   **ROOT CAUSE:** The password associated with your MID Server user ID is locked out. This is caused by a delta between what is in the config.xml of one of the MID Servers that the MID Server user is authenticating for, and the password in the user record. Some causes of this can be a newly installed MID with a typo in the config.xml, a recent clone of the instance that has running MID Servers running against an instance will attempt to log in several times and fail. This could cause the user to be auto-set to locked out. System administrators may also proactively set the user to locked out manually.
        -   **SOLUTION:** [Reset the MID Server user password](/kb_view.do?sysparm_article=KB0597570 "Reset the MID User password").
    -   _**No, the MID Server user is not locked out.**_  
        -   The MID Server user not being locked out is not the issue preventing successful authentication. Keep troubleshooting. [\[Back to top\]](#toc)

  

-   **Was the instance recently cloned?**  
    -   _**I don't know.**_  
        -   There is no way to determine if an instance has been cloned looking at the instance. The clone is initiated by your SNC Administrator from the source instance. Contact your Administrator for confirmation of a clone.
    -   _**Yes, the instance was recently cloned.**_  
        -   **ROOT CAUSE:** When an instance is cloned, MID Servers that are pointing to the cloned instance are not cloned over. Because of this, there may be a mismatch with your MID user and/or MID password if the sys\_user account for your MID Server gets modified or removed based on the clone (since sys\_user records are cloned over by default).
        -   **SOLUTION:** [Reset the MID Server user password](/kb_view.do?sysparm_article=KB0597570 "Reset the MID User password").
    -   _**No, the instance was not recently cloned.**_  
        -   Mismatched credentials due to MID Servers pointing to a cloned instance is not the issue preventing successful authentication. Keep troubleshooting. [\[Back to top\]](#toc)

  

-   **Was the MID Server recently reinstalled?**  
    -   _**I don't know.**_  
        -   There is no way to determine if MID Server has been reinstalled. The reinstallation of a MID Server is a manual process performed on the host machine of the MID. Contact your system administrator or network administrator to determine if the MID Server was reinstalled. 
    -   **_Yes, the instance was recently reinstalled_.**  
        -   **ROOT CAUSE:** When a MID Server is reinstalled, the MID Server must be re-validated from the instance. This requires a reset of the keystore on the MID Server host. 
        -   **SOLUTION:** [Reset the MID Server user password](/kb_view.do?sysparm_article=KB0597570 "Reset the MID User password").
    -   _**No, the instance was not recently reinstalled.**_  
        -   A corrupted keystore due to the MID reinstall is not the issue preventing successful authentication. Keep troubleshooting. [\[Back to top\]](#toc)
