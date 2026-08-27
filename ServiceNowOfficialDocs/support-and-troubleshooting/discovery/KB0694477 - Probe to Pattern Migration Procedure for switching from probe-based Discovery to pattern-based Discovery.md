---
title: "Probe to Pattern Migration: Procedure for switching from probe-based Discovery to pattern-based Discovery"
aliases:
  - KB0694477
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694477
kb_number: KB0694477
last_modified: 2025-06-24
---

## Probe to Pattern Migration: Procedure for switching from probe-based Discovery to pattern-based Discovery

  

### Issue

This probe to pattern migration process is supported only for customers running on New York release or later and currently using probes for Discovery.

<table class="tocTable" style="height: 280px; width: 228px;" width="220"><tbody><tr style="height: 8px;"><td style="width: 203px; height: 10px;"><h3><a name="toc"></a>Table of Contents</h3></td></tr><tr style="height: 8px;"><td style="width: 203px; height: 10px;"><a title="Overview" href="#description">Overview</a></td></tr><tr style="height: 8px;"><td style="width: 203px; height: 10px;"><a href="#scripts">What these scripts do</a></td></tr><tr style="height: 8px;"><td style="width: 203px; height: 10px;"><a href="#prerequisites">Prerequisites</a></td></tr><tr style="height: 8px;"><td style="width: 203px; height: 10px;"><a href="#procedure">Procedure</a></td></tr><tr style="height: 8px;"><td style="width: 203px; height: 10px;"><a href="#problems">Known Issues</a></td></tr><tr style="height: 10px;"><td style="width: 203px; height: 10px;"><a href="#faqs">FAQs</a></td></tr></tbody></table>

  

### Overview

Horizontal Discovery patterns have become the standard for discovering Configuration Items (CIs). Patterns provide a simpler and more intuitive way to debug and troubleshoot discovery compared with legacy probes and sensors.

Probe-based discovery and pattern-based discovery use different mechanisms of saving data in the CMDB. Using both discovery methods together may result in duplicate data in the CMDB. In addition, pattern-based discovery relies on relationships, while the legacy probe-based discovery uses references.

For detailed information about the difference between probe-based and pattern-based horizontal discovery, refer to the product documentation [Using Patterns For Horizontal Discovery](https://docs.servicenow.com/csh?topicname=c-UsingPatternsForHorizontalDiscovery.html&version=latest "product documentation UsingPatternsForHorizontalDiscovery").

**This process is only intended for instances running on New York release or later.  
There is a high risk of invalid and/or duplicate data if trying to run this migration on releases prior to New York.**

### What these scripts do

These migration scripts will do the following:

1.  Add the appropriate relationships needed for pattern Discovery to continue to identify the current CIs that are being discovered via probes.
2.  Update certain relationships that may have different relationship types or have different parent/child values.
3.  Update the appropriate Discovery Classification records (_discovery\_classy_) to convert the Triggers probes records (_discovery\_classifier\_probe_) to use pattern-related probes.

### Prerequisites

**Starting in the Orlando release, there is a Script Include called _ProbeToPatternPrerequisiteScript_ that can be used to run most of these checks prior to starting the migration.**  
**For more information on this script, and for those on New York who wish to import this Script Include to use on their instances, please refer to [KB0750351](https://hi.service-now.com/kb_view.do?sysparm_article=KB0750351 "KB0750351").**

1.  Should be on New York release or later **and** currently using probes for OS Discovery.
2.  Should deactivate all Discovery and Service Mapping jobs as well as any Import jobs that may affect CMDB data during migration.
3.  Needs to have the **Horizontal Pattern** probe record in the _discovery\_probes_ table, similar to the following screenshot.
    
    ![](sys_attachment.do?sys_id=3ac92d5a1ba660103013751f034bcb5b)  
      
    
4.  Should have the following out-of-box relationship type records (_cmdb\_rel\_type_) existing on their instance.  
    -   **Runs on::Runs** (_sys\_id: 60bc4e22c0a8010e01f074cbe6bd73c3_)
    -   **Owns::Owned by** (_sys\_id: 25242fb2377a9200738d021a54990e88_)
    -   **Contains::Contained by**  (_sys\_id: 55c95bf6c0a8010e0118ec7056ebc54d_)
    -   **Uses::Used by** (_sys\_id: cb5592603751200032ff8c00dfbe5d17_)
    -   **Defines resources for::Gets resources from** (_sys\_id: de5aeb6a0ab3015854626f204fb7b1c0_)
    -   **Virtualized by::Virtualizes**  (_sys\_id: d93304fb0a0a0b78006081a72ef08444_)
    -   **Provides::Provided by** (_sys\_id: f67e9ecdff602000dada361332f49d35_)
    -   **Provided By::Provides** (_sys\_id: 4afd799338a02000c18673032c71b817_)
    -   **Members::Member of** (_sys\_id: 55c913d3c0a8010e012d1563182d6050_)
    -   **Registered on::Has registered** (_sys\_id: aa9434870ab301544ce2943bf03fd7a8_)  
        **NOTE: If any of these records no longer exist or if they exist but with a different sys\_id value (i.e. if the record is custom created), see the [FAQ](#faqs "FAQ") section below for how this can be addressed.**
5.  Should have the following classifier records with these exact names.  
    -   **Windows**  
        -   Windows 2000 Server
        -   Windows 2003 Server
        -   Windows 2008 Server
        -   Windows 2012 Server
        -   Windows 2016 Server
        -   Windows NT Server
        -   Windows
        -   Hyper-V Server
    -   **Unix**  
        -   Linux
        -   Solaris
        -   HP-UX
        -   AIX
    -   **SNMP**  
        -   Standard Network Router
        -   Standard Network Switch
        -   F5 BIG-IP Load Balancer
        -   A10 Load Balancer
        -   Alteon Load Balancer
        -   ACE Load Balancer
        -   Netscaler Load Balancer
        -   Radware - AppDirector - Load Balancer  
            
    -   **Processes (Starting in Orlando)**  
        
        -   Apache Server
        -   JBoss Server
        -   Weblogic Server
        -   MySQL Server
        -   Microsoft SQL Server
        -   Tomcat
        -   Microsoft IIS Server
        -   PostgreSQL Instance
        -   Oracle Instance  
            
        
        **NOTE: If any of these records no longer exist or if the name has been changed on these records, see the [FAQ](#faqs "FAQ") section below for how this can be addressed.**
6.  For any of the classifiers mentioned in step 4, check the _Triggers probes_ list. There should be an existing record to run the Horizontal Pattern that should be set as **active = false**, similar to the screenshot below.
    
    ![](sys_attachment.do?sys_id=7ec92d5a1ba660103013751f034bcb5c)
    

If any or all of the classifiers do not have records like the above in the _Triggers probes_ list, the fix scripts can create those as necessary.  
However, we will need to verify that the instance has the following pattern records (_sa\_pattern_) to be able to link to based on the name.

-   **Windows**  
    -   Windows OS - Servers
    -   Windows OS - Desktops
    -   Hyper-V Server
-   **Unix**  
    -   Linux Server (see example below)
    -   Solaris Server
    -   HP-UX Server
    -   AIX Server

-   **SNMP**  
    -   Network Router
    -   Network Switch
    -   F5 Load Balancer
    -   A10 Load Balancer
    -   Alteon Load Balancer
    -   ACE Load Balancer by SSH
    -   Netscaler Load Balancer
    -   AppDirector Load Balancer

-   **Processes (Starting in Orlando)**  
    -   Apache On Windows
    -   Apache on UNIX based OS
    -   Jboss
    -   WebLogic
    -   My SQL server On Windows and Linux
    -   MSSql DB On Windows
    -   Tomcat
    -   IIS
    -   PostgreSQL DB
    -   Oracle DB On Windows
    -   Oracle DB On Unix

  

![](sys_attachment.do?sys_id=b2c92d5a1ba660103013751f034bcb5e)

  

**NOTE: If any of these patterns records no longer exist or if the name has been changed on these records, see the [FAQ](#faqs "FAQ") section below for how this can be addressed.**

### Procedure

**NOTE: Starting in Orlando, there is now a UI Page to be able to execute this migration process. Please refer to [KB0781470](https://hi.service-now.com/kb_view.do?sysparm_article=KB0781470 "KB0781470") for more details.  
Below procedure is only applicable for customers on New York release.**

* * *

There are two possible ways to use these conversion scripts. Please choose the option that is most appropriate based on the size of your CMDB.

**NOTE: This probe to pattern migration process is only meant to run one time and only in one direction.  
We do not support reverting back to using probes, as this will likely cause data issues in the CMDB if this is done.**

1.  The preferred approach is to run the individual conversion scripts below one at a time. For example, if starting with the **Windows** script, follow the process below.  
    1.  Navigate to _System Definition -> Scheduled Jobs_
    2.  In the Scheduled Jobs table, click _New_ and select the option **Automatically run a script of your choosing.**
    3.  Put these values below for this script:  
        1.  Name = Migrate Probe to Pattern Windows
        2.  Active = True
        3.  Run = Once
        4.  Starting = \[Choose the date/time you want to run this script\]
        5.  Conditional = False
        6.  Run this script =
            
            var fix = new FixWindowsModelForPatterns();  
            fix.addMissingRelationsForWindows();
            
    4.  Click _Submit_ and then wait for this script to run at the Starting time that was provided.
    5.  Once this is completed, repeat this process for the other CI types below.
        
        **Unix:**  
        Name = Migrate Probe to Pattern Unix  
        Run this script = 
        
        var fix = new FixUnixFamilyModelForPatterns();  
        fix.addMissingRelationsForUnix();
        
        **Routers & Switches:**  
        Name = Migrate Probe to Pattern Network  
        Run this script =
        
        var fix = new FixSwitchAndRouterModelForPatterns();  
        fix.addMissingRelationsForSwitchesAndRouters();
        
        **Load Balancers:**  
        Name = Migrate Probe to Pattern Load Balancers  
        Run this script =
        
        var fix = new FixPatternLoadBalancersModel();  
        fix.addMissingRelationsForLoadBalancers();
        
2.  To run the conversion process on all the classifiers in one step, follow this process.  
    
    **NOTE: This is only recommended for smaller CMDBs**
    
      
    1.  Navigate to _System Definition -> Scheduled Jobs_.
    2.  In the Scheduled Jobs table, click _New_ and select the option **Automatically run a script of your choosing.**
    3.  Put these values below for this script:  
        1.  Name = Migrate Probe to Pattern Full
        2.  Active = True
        3.  Run = Once
        4.  Starting = \[Choose the date/time you want to run this script\]
        5.  Conditional = False
        6.  Run this script = 
            
            FixMissingRelationsFromProbesToPatterns.moveProbesToPatterns();
            
    4.  Click _Submit_ and then wait for this script to run at the Starting time that was provided.

**NOTE: These scripts could also be run in Scripts-Background, although this is only recommended for smaller CMDBs.**

###   

### Known Issues

**\*\*\* There is a known issue with Duplicate Storage Devices that can occur during Windows migration. Please refer to [KB0748332](https://hi.service-now.com/kb_view.do?sysparm_article=KB0748332 "KB0748332") (login needed) for more details. \*\*\***

**\*\*\* "glide.discovery.ip\_based.active" not updated during migration as expected, PRB1368993. If so, manually update the property value to false.**

**\*\*\* OS Packages migration is supported in Orlando Patch 7 and Paris Patch 1 onwards. Please refer to [KB0827777](https://hi.service-now.com/kb_view.do?sysparm_article=KB0827777 "KB0827777") (login needed) for more details. \*\*\***

**\*\*\* There are also some additional known differences between probes and patterns not handled by the migration. See [KB0827212](https://hi.service-now.com/kb_view.do?sysparm_article=KB0827212 "KB0827212") for more details. \*\*\***

### FAQs

#### 1) What if we are using custom probes in the classifiers? How should these be handled?

The migration process is intended to set up the instance to use patterns as if we are enabling Discovery for the first time.

By default, any custom probes that may have been added to a classifier that we are migrating will be made **active = false**.  
This is to help prevent any potential issues that may arise with data being discovered by these custom probes interfering with new data being discovered by patterns.

These custom probes can always be re-activated by navigating to the respective classifier and set the _Triggers probe_ record back to **active = true**.

![](sys_attachment.do?sys_id=f6c92d5a1ba660103013751f034bcb5f)

  

#### 2) What if we do not have some of the default relationship type records as mentioned from the Prerequisites list?

In the Script Include **FixPatternsModelBasic**, this is where these relationships are defined as such.

![](sys_attachment.do?sys_id=3ec92d5a1ba660103013751f034bcb60)

If any of these relationships are missing, we need to reinsert the default versions of these records.  
This can be done by seeing if the missing records are existing in the deleted records table (_sys\_audit\_delete_) and then [restore the deleted records](https://docs.servicenow.com/csh?topicname=t_RestoreADeletedRecordAndRef.html&version=latest "restore back the deleted record") or if possible you may need to request from Technical Support to import the missing records from an out-of-box instance.

If any of these relationships are existing, but instead have a different sys\_id value, the recommendation is to restore the default version of the relationship if possible and remove the custom version.  
This may also include having to update any existing relationship records (_cmdb\_rel\_ci_) that may be using this custom relationship type to instead use the default value. 

However, if this is not possible, then this **FixPatternsModelBasic** script will need to be manually updated to replace the default value with the custom value that is being used.  
For example, if you have a record for the relationship Runs on::Runs, but with a different sys\_id (_ex. 517ab95338a02000c18673032c71b904_), then you will need to replace the appropriate variable value to reference this new sys\_id value like below.

_this.RUNS\_ON = "517ab95338a02000c18673032c71b904";_

  

#### 3) What if we do not have specific classifier records or pattern records with the names as mentioned from the [Prerequisites](#prerequisites "Prerequisites") list (ex. Instead of _Windows 2008 Server_, we are using a custom classifier called _Windows 2008 Custom_)?

In the individual "Fix" Script Includes (ex. _FixWindowsModelForPatterns_, _FixUnixFamilyModelForPatterns_, etc.), the migration process converts the classifiers from probes to patterns using function calls like this below.

_migrate.enablePattern('windows', 'Windows 2008 Server', 'Windows OS - Servers');_

This function call passes three parameters:

-   The first parameter helps to identify which _discovery\_classy_ table we are targeting against (ex. _discovery\_classy\_windows_).
-   The second parameter tells us which classifier record we are targeting against (ex. **Windows 2008 Server**).
-   The third parameter tells us which pattern we should use if we need to crate a new _discovery\_classifier\_probe_ record to trigger the pattern (ex. **Windows OS - Servers**).

If there is a different classifier record that needs to be updated or if the pattern has a different name, then this function call can be modified to pass in the appropriate values.  
For instance, if in this example mentioned above we need to use _Windows 2008 Custom_ instead of _Windows 2008 Server_, you can make the following change:

_migrate.enablePattern('windows', 'Windows 2008 Custom', 'Windows OS - Servers');_

Or, if the pattern that is being used is also different then you can change to something like this:

_migrate.enablePattern('windows', 'Windows 2008 Custom', 'Windows OS - Custom');_

**This should only be done if you are using customized classifiers or patterns and are not using, or no longer have the out-of-the-box classifiers or patterns.**

#### 4) Are there any System Properties affected by this change?

There is a System property named **glide.discovery.ip\_based.active** that will get set to a value of **false** when these migration scripts are run.  
This property is mainly a reference that Discovery is now using patterns instead of probes.

#### 5) What should be done if there is an error that occurs during the migration process? What logs should be collected?

When running the migration scripts, most of the details about what is happening during this process will get logged in the _syslog_ table and will have a Source value of **DiscoveryMigrateToPatterns**.  
See example screenshot below.

![](sys_attachment.do?sys_id=72c92d5a1ba660103013751f034bcb62)

Starting in Orlando, there is also a new log table (_probe\_to\_pattern\_log_) where this log information will be stored as well. Please refer to [KB0781470](https://hi.service-now.com/kb_view.do?sysparm_article=KB0781470 "KB0781470") for more details.

Investigating these log details, along with looking into other typical node logs, can be helpful to see when and where any issues may occur.

If further assistance is needed, you can open a case with Technical Support to investigate accordingly.

### Release

New York to current release

### Resolution

.
