---
title: "Custom solution to gather editions in SCCM"
aliases:
  - KB0721360
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0721360
kb_number: KB0721360
last_modified: 2025-07-03
---

## Custom solution to gather editions in SCCM

  

### Issue

### Introduction

Edition information for installed products is not captured by SCCM OOB processes and each publisher stores in a unique location. This custom solution parses through registry keys to gather edition for products such as Adobe Acrobat, Microsoft SQL Server, and Windows Exchange Server. One can choose to add additional modules to gather for other products. 

### Requirements

1.  Need to have SCCM integration plugin and Software Asset Management Professional plugin installed
2.  All the client machines should have PowerShell installed
3.  Product and Publisher values in the PowerShell script are hardcoded and is following the convention below. It is required to follow the convention in order to identify the right software install to populate the edition.  
    1.  The product should be an exact match from the samp\_sw\_product table and prod\_name field which is the normalized product on software install record
    2.  The publisher should be an exact match from the samp\_sw\_product table and publisher field which is the normalized publisher on software install record

### How it works

Service Graph Connector for Microsoft SCCM Software Edition data source brings in the edition records from SCCM DB, each row is transformed using a script and processed in two phases. If a matching install is found in phase one, its edition override field is populated and proceeds to next row. If match not found, goes into phase two and tries to find a matching install. If both fail, it skips the row and moves onto the next row. Below are the matching criteria in both the phases:

1.  Phase 1  
    1.  normalized product
    2.  normalized publisher
    3.  version
    4.  installed on (CI)
    5.  created by application pattern = false
    6.  empty edition override
2.  Phase 2  
    1.  normalized product
    2.  normalized publisher
    3.  empty version
    4.  installed on (CI)
    5.  created by application pattern = false
    6.  empty edition override

### Setup

Two types of setup are required, one on SCCM Manager and the other on ServiceNow instance.

### SCCM Manager Setup 

1\. Create a shared folder on the same machine as SCCM manager and copy the network path. For example, mine is called \\\\SAMLABVM501\\Shared

![](/sys_attachment.do?sys_id=0d95a6be93df9610def533527cba10e8)

Download **[fetchEditions.txt](/sys_attachment.do?sys_id=709566be93df9610def533527cba10f9 "fetchEditions.txt")** and save in the above created shared folder.

**Note:** Fix the extension to .**ps1** which denotes PowerShell script (it's currently .txt) and **should not** be deleted since its required by SCCM manager to execute on schedule.

**Note:** If implementing for the first time, proceed to step 2. If upgrading the current implementation (the above file when download will have version=2.0)

-   Replace original fetchEditions.ps1 file with newly downloaded fetchEditions.ps1 file in the shared folder.
-   Go to SCCM manager -> software Library -> Application Management -> Packages. Right click on the package you had previously created to fetch editions and select "Update Distribution Points" as documented by Microsoft [here](https://docs.microsoft.com/en-us/mem/configmgr/apps/deploy-use/packages-and-programs#monitor-packages-and-programs "here"). Click OK. 
-   This is to instruct client machines to fetch information as per 2.0 changes.

2\. Go to SCCM manager -> Software Library -> Application Management -> Packages. Click “Create Package” on the top left to create a new package

3\. Fill out the Package information as shown below and make sure the source folder has the network path you copied in step 1 and click Next

![](/sys_attachment.do?sys_id=8595a6be93df9610def533527cba10c7)

4\. Select Standard Program and click Next

5\. Fill out the next set of fields as shown in below snapshot (**Note**: file name at the end of the command should match to the file copied to the shared folder) and click Next

      **Command line**:

      "C:\\Windows\\sysnative\\WindowsPowerShell\\v1.0\\powershell.exe" -ExecutionPolicy Bypass -Command .\\fetchEditions.ps1

![](/sys_attachment.do?sys_id=d595a6be93df9610def533527cba10f8)

6\. Go to the shared folder and look up the size of the PowerShell script. Change the maximum allowed run time to 15 minutes instead of the default and populate disk space as below and click Next.

![](/sys_attachment.do?sys_id=4d95a6be93df9610def533527cba10f6)

7\. Shows a summary of all the configuration we did from step 4-7, click Next.

8\. You will see a successful completion dialog, click Close.

9\. The package we just created will show up in Software Library -> Application Management -> Packages as below:

![](/sys_attachment.do?sys_id=4195a6be93df9610def533527cba10b5)

10\. Right click on the package name and click Distribute Content:

11\. Click Next

![](/sys_attachment.do?sys_id=4195a6be93df9610def533527cba10cb)

12\. Select Add and select the method of distribution you need, I am choosing Distribution Point. 

![](/sys_attachment.do?sys_id=8195a6be93df9610def533527cba10b3)

![](/sys_attachment.do?sys_id=d595e6be93df9610def533527cba1005)

![](/sys_attachment.do?sys_id=d195e6be93df9610def533527cba1002)

Click Next.

13\. Shows the summary, click Next.

14\. After completed successfully, click Close.

15\. Right click on the package name again and click Deploy

16\. Select the collection you want to deploy the package to as below and click Next

![](/sys_attachment.do?sys_id=4595a6be93df9610def533527cba10ad)

17\. A distribution point should be pre-selected, if not, go ahead and Add and click Next: 

![](/sys_attachment.do?sys_id=0995a6be93df9610def533527cba10e5)

18\. Make sure the Purpose is set to Required and click Next.

![](/sys_attachment.do?sys_id=0195a6be93df9610def533527cba10cd)

19\. Click New to create an Assignment schedule as below:

![](/sys_attachment.do?sys_id=059566be93df9610def533527cba10fd)

Click schedule:

![](/sys_attachment.do?sys_id=0195a6be93df9610def533527cba10b7)

Create a custom schedule, I opted as below and click OK: 

![](/sys_attachment.do?sys_id=0d95a6be93df9610def533527cba10de)

Click OK:

![](/sys_attachment.do?sys_id=5995e6be93df9610def533527cba1000)

Make sure Rerun Behavior is set to Always rerun program as below and click Next:

![](/sys_attachment.do?sys_id=0195a6be93df9610def533527cba10e2)

20\. Check and uncheck fields as below and click Next:

![](/sys_attachment.do?sys_id=dd95a6be93df9610def533527cba10fe)

21\. Switch both options to Run program from distribution point since this is a fairly small program and click Next as below: 

![](/sys_attachment.do?sys_id=5195a6be93df9610def533527cba10fa)

22\. Shows the Summary, click Next

23\. Click Close on the successfully completed screen

24\. Give it a few minutes and check to make sure the package is executed successfully on all client machines

Go to SCCM Manager -> Monitoring -> Deployments and find the package you just created.           

![](/sys_attachment.do?sys_id=d995a6be93df9610def533527cba10fb)

Double click on it and you should see as below under success tab: 

![](/sys_attachment.do?sys_id=f09566be93df9610def533527cba10fb)

**Note:** If you see entries in the Error tab as below, then go back to Software Library -> Packages -> find your package, right click and click Update Distribution Points. Give it a few mins and go back to Monitoring -> Deployments and check again.

![](/sys_attachment.do?sys_id=5595a6be93df9610def533527cba10fd)

![](/sys_attachment.do?sys_id=4d95a6be93df9610def533527cba10e3)

Click OK

![](/sys_attachment.do?sys_id=0195a6be93df9610def533527cba10cf)

25\. Add the newly created WMI class (created in the PowerShell script we downloaded) to hardware inventory. Go to SCCM Manager -> Administration -> Client Settings

![](/sys_attachment.do?sys_id=c995a6be93df9610def533527cba10d0)

Right click on Default Client Settings and click on Properties as below: 

![](/sys_attachment.do?sys_id=8195a6be93df9610def533527cba10e7)

Go into Hardware Inventory and click Set Classes as below:

![](/sys_attachment.do?sys_id=0595a6be93df9610def533527cba10af)

Click on Add as below:

![](/sys_attachment.do?sys_id=5195e6be93df9610def533527cba1007)

Click on Connect as below. When we deployed the package, it ran successfully on client machines (on SAMLABVM303 in snapshot), I will need to connect to that machine to pick the WMI class.

![](/sys_attachment.do?sys_id=0595a6be93df9610def533527cba10c9)

![](/sys_attachment.do?sys_id=c195a6be93df9610def533527cba10b1)

Find and check against SN\_SAMP\_ADD\_REMOVE\_PROGRAMS\_EDITION and click OK as below:

![](/sys_attachment.do?sys_id=8595a6be93df9610def533527cba10c5)

It shows up selected on the Hardware Inventory Classes as below and click OK and click OK on the Default Settings screen.

![](/sys_attachment.do?sys_id=5d95e6be93df9610def533527cba1003)

If you go into all the other custom client settings -> Properties -> Hardware Inventory -> Set Classes, you should see SN\_SAMP\_ADD\_REMOVE\_PROGRAMS\_EDITION checked already as below:

![](/sys_attachment.do?sys_id=8595a6be93df9610def533527cba10e0) 

Once client machines receive new machine policy and hardware inventory changes, in the next hardware inventory collection cycle, the WMI class (SN\_SAMP\_ADD\_REMOVE\_PROGRAMS\_EDITION) data will be sent back. This class creates a view in SCCM DB called v\_GS\_SN\_SAMP\_ADD\_REMOVE\_PROGRAMS\_EDITION

### ServiceNow Setup

On the left navigation:

1.  Go to Integration – Service Graph Connector for Microsoft SCCM Software Edition. To enable it, check the Active field and click Update
2.  Go to Integration – Service Graph Connector for Microsoft SCCM -> Click on the related list transforms, Update software install with edition transform. To enable it, check the Active field and click Update

### Verification

1.  Make sure there are entries in SCCM database -> Views -> v\_GS\_SN\_SAMP\_ADD\_REMOVE\_PROGRAMS\_EDITION view
2.  Run Integration - Service Graph Connector for Microsoft SCCM –> Scheduled Import
3.  Go to Integration - Service Graph Connector for Microsoft SCCM –> Progress and click All on the filter, you should see an entry for Creating import set: sn\_sccm\_integrate\_sccm\_2019\_software\_edition or Creating import set: with Completion Code Success. This ensures Software Edition data source executed successfully
4.  Edition data should be populated on the edition override field on the software install records
5.  This would trigger a re-normalization of the discovery model associated with the install record. Normalization uses content rules / packages to map the number formatted editions (7760) to text editions (Professional) and updates the discovery model accordingly. No changes will be made to the install records after re-normalization.

### Troubleshooting

1.  If the desired software install is not updated with edition, check following  
    1.  Make sure Service Graph Connector for Microsoft SCCM Software Edition scheduled import record is active
    2.  Make sure Update software install with edition transform map is active
    3.  Test the Service Graph Connector for Microsoft SCCM Software Edition data source
    4.  Make sure the product and publisher used to populate in PowerShell script is exists in the samp\_sw\_product table.
2.  If the V\_GS\_ SN\_SAMP\_ADD\_REMOVE\_PROGRAMS\_EDITION view has no records, on any of the client machines, check CCM log (execmgr.log), it should read “Script for Package:P0100009, Program: Fetch Editions succeeded with exit code 0”. Failed execution will say something like: “Script for Package:P0100007, Program: Fetch Editions failed with exit code 1”

### Disable Software Edition Solution

In case the user is having unexpected issues with the above solution and would like to discontinue its execution they can follow the step below:

1\. Disable this schedule import Service Graph Connector for Microsoft SCCM 'Software Edition' on the instance by unchecking the 'Active' field checkbox to have this import as Active = false going forward which will not make it execute.
