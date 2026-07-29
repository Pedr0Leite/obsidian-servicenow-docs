---
title: "Password Reset Credential Store"
aliases:
  - KB0598300
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0598300
kb_number: KB0598300
last_modified: 2025-01-03
---

## Issue

Credential Store | Table of Contents

<table class="tocTable" style="height: 189px;" width="339"><tbody><tr><td><a style="text-decoration: none;" href="#Details">Details</a></td></tr><tr><td><a style="text-decoration: none;" href="#Type">1. Type</a></td></tr><tr><td><a style="text-decoration: none;" href="#Hostname">2. Hostname</a></td></tr><tr><td><a style="text-decoration: none;" href="#ScriptInclude">3. Script Include References<br>&nbsp;&nbsp;&nbsp;</a><a style="text-decoration: none;" href="#AutoGenerate">3.1 Auto Generate Password</a><br>&nbsp;&nbsp;&nbsp;<a style="text-decoration: none;" href="#UserLookup">3.2 User Account Lookup</a></td></tr><tr><td><a style="text-decoration: none;" href="#Policy">4. Enforce History Policy</a></td></tr><tr><td><a style="text-decoration: none;" href="#PasswordRule">5. Password Rule</a></td></tr><tr><td><a style="text-decoration: none;" href="#Strength">6. Password Strength (Starting Istanbul)</a></td></tr><tr><td><a style="text-decoration: none;" href="#References">References</a></td></tr></tbody></table>

**Details**

* * *

By default, if the customer has included the "Demo Data" when installing these plugins, they will have these Credential Store records included by default that they could use when setting up their Password Reset process

-   _Local ServiceNow Instance_
-   _Sample AD Credential Store_ (Installed with "Password Reset - Orchestration Add-on")
-   _Sample Remote ServiceNow Instance_ (Installed with "Password Reset - Orchestration Add-on")

Most times, the customer will just modify these records to update with their own data.

Here are potential areas to check for if you suspect there may be an issue with the Credential Store

![](sys_attachment.do?sys_id=5a2d6c62db82b450e515c22305961938)

[\[Back to Top\]](#TOC)

  

**Type**

* * *

For the "Type" field, this will reference a "Password Reset Credential Store Type" record.

Similar to the Credential Store record, there are some out-of-box Credential Type records

-   _Local ServiceNow Instance_ - Linked to the "Local ServiceNow Instance" Credential Store record
-   _AD Credential Store_ - Linked to the "Sample AD Credential Store" Credential Store record
-   _Remote (SOAP) ServiceNow_ -Linked to the "Sample Remote ServiceNow Instance" Credential Store record

In these "Credential Store Type" records, this is where we define the different workflows that will be called upon for different processes, such as the "**Connection test workflow**" and the "**Password reset workflow**". See example below.

![](sys_attachment.do?sys_id=e22d6c62db82b450e515c22305961956)

If these values have been changed or these workflows have been modified, please check them accordingly to make sure they are still following a working process.

You can also reference this article here for how the default process works for some of these out-of-box version of these workflows.

[\[Back to Top\]](#TOC)

  

**Hostname**

* * *

For the "Hostname" field, make sure this has the IP or hostname value that can be accessed from your Orchestration MID Server(s) that you are using for this Password Reset Process.

Many customers will put the name instead of the IP, especially in situations where the IP of the LDAP server may change dynamically or if they are using Load Balancing.

This is where using the "Save & Test Connection" UI Action is helpful, which in turn calls this Script Include "PwdTestCredStoreConnectionWorker" that triggers the "Pwd Connection Test - Master" workflow.

[\[Back to Top\]](#TOC)

  

**Script Include References**

* * *

_Auto Generate Password_

By default, this references a Script Include "PwdDefaultAutoGenPassword", which contains a process to generate a "random" Password value that can be used if the "Auto-generate password" value is checked on the corresponding Password Reset Process record.

This likely should not be modified at all, unless the customer has some reasoning for a different mechanism for auto-generating a Password.

_User Account Lookup_

By default, at least in the "Sample AD" and "Sample Remote" Credential Store records, this references a Script Include "PwdDefaultUserAccountLookup", which determines the account name to lookup based on the "user\_name" value of the sys\_user record.

This is called upon in workflows such as "Pwd Get Lock State - Master", "Pwd Change - Master" and "Pwd Unlock Account - Master"

This likely should not be modified at all, unless the customer has some reasoning to use a different field on the sys\_user record as the name value to lookup for in their AD.

\*\*\* For both fields, by default when creating a new Credential Store record, these fields will be set as "-- None --" and can be saved this way, however this can cause issues down the road if they are empty, so it is highly suggested that these fields be populated, at least with these default values as mentioned.

[\[Back to Top\]](#TOC)

  

**Enforce History Policy**

* * *

This checkbox is only made visible by default if _Type_ is set as "AD Credential Store", as per a UI Policy "Show "Enforce history policy" for AD"

This is to handle situations if the customer's AD setup has some Password History policies in place, like if you can't reuse a certain number of previous passwords.

By default, this is only referenced in the out-of-box "Pwd Reset - AD" workflow, namely starting in the activity "Consolidate AD input parameters", where we set the scratchpad with the value from this checkbox.

![](sys_attachment.do?sys_id=662d6c62db82b450e515c2230596196f)

This, along with checking the "User must reset password" value from the Password Reset Process record, will determine how many times the Password actually gets changed during a specific instance of running this Process.

This is explained more in this "Pwd Reset - AD" Workflow article.

[\[Back to Top\]](#TOC)

**Password Rule**

* * *

The "Password Rule" and "Password Rule Hint" boxes are there in case the customer wants or needs to enforce a specific set of rules with regards to creating a new Password.

This only applies where the end user is typing in their new password to be used when going through this Password Reset process, not when auto-generating a Password.

This does require a knowledge of Regex to be able to create or modify this "Password Rule" value appropriately.

In the example mentioned above, the Regex provided checks for what is mentioned in the "Password Rule Hint", where you need to have at least 8 characters \[.{8,}$\], at least 1 Uppercase and 1 Lowercase letter \[(?=.\*\[a-z\])(?=.\*\[A-Z\])\] and at least one number \[(?=.\*\\d)\]

If the customer has modified this Password Rule on their environment, they can use an online Regex Tester (ex. [Regexr](http://regexr.com/ "Regexr")) to be able to test and see if this is valid and if the passwords that they may be attempting to use meet the standards of the Password Rule they have set up.

[\[Back to Top\]](#TOC)

  

**Password Strength**

* * *

Starting in Istanbul, we have included these fields "Enable Password Strength" and "Strength Rule".

The "Enable Password Strength" is a Checkbox and the "Strength Rule" will only show by default if "Enable Password Strength" is set as "True".

This does not necessarily have to coincide with the Password Rule details provided above.

[\[Back to Top\]](#TOC)

**References**

* * *

-   [Credential Stores](https://docs.servicenow.com/csh?topicname=c_CredentialStores.html&version=latest "Credential Stores")
-   [Credential stores for Password Reset](https://docs.servicenow.com/csh?topicname=c_CredentialStores.html&version=latest "Credential stores for Password Reset")
-   [Credential Store Configuration](https://docs.servicenow.com/docs.servicenow.com/bundle/madrid-servicenow-platform/page/administer/login/task/config-ad-credential-store.html "Credential Store Configuration")
-   [Create a credential store type for Password Reset](https://docs.servicenow.com/csh?topicname=t_CreateACredentialStoreType.html&version=latest "Create a credential store type for Password Reset")
-   [Credential Store Type Configuration](https://docs.servicenow.com/csh?topicname=t_CreateACredentialStoreType.html&version=latest "Credential Store Type Configuration")

[\[Back to top\]](#TOC)
