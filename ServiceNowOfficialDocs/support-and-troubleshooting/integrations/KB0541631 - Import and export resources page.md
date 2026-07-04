---
title: "Import and export resources page"
aliases:
  - KB0541631
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0541631
kb_number: KB0541631
last_modified: 2024-10-09
---

## Import and export resources page

  

### Issue

## Table of Contents

-   [Product documentation](#mcetoc_1f08tv6nn14)
-   [Feature description/How to](#feature_desc)
-   [Troubleshooting Import Issues](#mcetoc_1f08tv6nn16)
-   [Troubleshooting Export Issues](#mcetoc_1f08tv6nn17)
-   [Export Problems](#export_problems)
-   [Export Solutions](#export_solutions)
-   [Videos](#mcetoc_1f08tv6nn18)  
    -   [Import](#mcetoc_1f08u8ei21e)
    -   [Export](#mcetoc_1f08tv6nn19)
-   [Community (Import/Transform)](#community_import_transform)
-   [Community (Export)](#mcetoc_1f08tv6nn1a)

## Product documentation

-   [Import sets](https://docs.servicenow.com/csh?version=latest&topicname=import-sets-landing-page.html "Import sets")
-   [Export sets](https://docs.servicenow.com/csh?version=latest&topicname=c_ExportSets.html "Export sets")

## Feature description/How to

-   [Developer blog: Import Series Part 1 - Getting Started with Import Sets](https://developer.servicenow.com/blog.do?p=/post/getting-started-with-import-sets/)
-   [Developer blog: Import Series Part 2 - Anatomy of an Import Set](https://developer.servicenow.com/blog.do?p=/post/import-series-part-2-anatomy-of-an-import-set/)

## Troubleshooting import issues

-   [KB0867752: Import/Transform Execution Flow and Table Reference](/kb?id=kb_article_view&sysparm_article=KB0867752)  
    -   If you are a novice, this KB will help you understand the feature.
    -   If you are an expert in import/transform, then this KB may serve as a reference or cheat sheet.
-   [KB0870045: Import/Transform Summary Tool](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0870045 "KB0870045: Import/Transform Summary Tool")  
    -   This is a helpful tool when troubleshooting Imports.  This tool will give you the configuration and runtime summary for an Import Set.
-   [KB0793356: Import Set Performance](/kb?id=kb_article_view&sysparm_article=KB0793356)  
    -   Brief summary of import/transform execution flow and troubleshooting slow import/transform issues.
-   [KB0814735: Troubleshooting Slow Import Sets](/kb?id=kb_article_view&sysparm_article=KB0814735)  
    -   Tips and Tricks when working on slow import set issues
-   [KB0538436: Troubleshooting an import that is taking a long time to complete](/kb?id=kb_article_view&sysparm_article=KB0538436)
-   [KB0538437: Troubleshooting an import that does not complete or is missing data](/kb?id=kb_article_view&sysparm_article=KB0538437)
-   [KB0538434: Troubleshooting an import that fails](/kb?id=kb_article_view&sysparm_article=KB0538434)
-   [KB0564204: Troubleshooting inbound integrations performance](/kb?id=kb_article_view&sysparm_article=KB0564204)  
    -   Tips and tricks when troubleshooting slow imports using Web Services Import Set API
-   [KB0720801: Understanding Concurrent Import Sets](/kb?id=kb_article_view&sysparm_article=KB0720801)  
    -   Overview of how hierarchical scheduled and concurrent imports work in Madrid
-   [KB0832611: Concurrent Import Sets are not created even with the "Concurrent Import" option selected on the Scheduled Import Set record](/kb?id=kb_article_view&sysparm_article=KB0832611)
-   [KB0753011: Concurrent import set running synchronously](/kb?id=kb_article_view&sysparm_article=KB0753011)  
    -   Users may complain that they have enabled a concurrent import set but that it is running under one Import Set or not at all.
-   [KB0755790: Import Deleter schedule job doesn't clean up 7 days older data in ImportSet tables](/kb?id=kb_article_view&sysparm_article=KB0755790)  
    -   If this cleaner job fails to delete data in the import set tables, follow this procedure to run the table cleanup job manually
-   [KB0538459: Troubleshooting issues with transform maps](/kb?id=kb_article_view&sysparm_article=KB0538459)  
    -   Landing page for issues during the transform phase
-   [KB0747613: When importing data, some staging table records are duplicating or an Import set row is duplicating](/kb?id=kb_article_view&sysparm_article=KB0747613)
-   [KB0818304: How to identify slow data import due to coalesce?](/kb?id=kb_article_view&sysparm_article=KB0818304 "KB0818304: How to identify slow data import due to coalesce?")
-   [KB0793315: For a Large Volume of REST Import Set API Calls, Which Import Set Mode is Recommended for Best Performance Synchronous or Asynchronous?](/kb?id=kb_article_view&sysparm_article=KB0793315 "KB0793315: For a Large Volume of REST Import Set API Calls, Which Import Set Mode is Recommended for Best Performance Synchronous or Asynchronous?")  
    -   Best practice is to use Asynchronous mode. Let the platform accept any number of import REST calls, then perform a bulk transform at a later time.
-   [KB0781666: Making import sets created for Import Set API calls "Asynchronous" to prevent Synchronous transform, for specific imports](/kb?id=kb_article_view&sysparm_article=KB0781666 "KB0781666: Making import sets created for Import Set API calls \"Asynchronous\" to prevent Synchronous transform, for specific imports")  
    -   Tip for making web service import sets a bit faster by performing transform at a later time.
-   [KB0538460: Troubleshooting Import - Missing data when importing from JDBC source via MID server](/kb?id=kb_article_view&sysparm_article=KB0538460)
-   [KB0538154: Determining if all columns are mentioned](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538154)
-   [KB0538132: Determining if the coalesced field is configured](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538132)
-   [KB0538161: Determining if a business rule is running on top of the transform map](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538161)
-   [KB0786280: Impossible to Import a CSV file with duplicate column names in header](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0786280)

## Troubleshooting Export Issues

-   [Export FAQ](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0993378)
-   [KB0538458: Troubleshooting export issues](/kb?id=kb_article_view&sysparm_article=KB0538458)  
    -   Landing page for troubleshooting export issues.
-   [KB0538304: Troubleshooting export - Determine if there is a custom script manipulating data at the record level](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0538304 "KB0538304: Troubleshooting export - Determine if there is a custom script manipulating data at the record level")
-   [KB0518655: Export Limit/Max Overview (Excel, CSV, PDF, Database Views)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0518655 "KB0518655: Export Limit/Max Overview (Excel, CSV, PDF, Database Views)")
-   Export Sets:  
    -   [KB0727047: Export set "Scheduled Data Exports" intermittent 'Completed with errors'](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727047 "KB0727047: Export set \"Scheduled Data Exports\" intermittent 'Completed with errors'")
    -   [KB0860033: Export Set are not placing the Files in the Expected Mid Server](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0860033 "KB0860033: Export Set are not placing the Files in the Expected Mid Server")

## Export Problems

-   [KB0791852/PRB1366882: Users are unable to export from a list view if the user id is longer than 40 characters](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791852 "KB0791852/PRB1366882: Users are unable to export from a list view if the user id is longer than 40 characters")
-   [KB0676116: Export "Active Transactions (All Nodes)" on v\_cluster\_transaction table fails with 0 rows](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0676116 "KB0676116: Export \"Active Transactions (All Nodes)\" on v_cluster_transaction table fails with 0 rows")
-   Export Sets  
    -   [KB0860658/PRB1434384: "No sensors defined" Error for Export Set ExportSetResult ECC Queue input records, because skip\_sensor=true is missing from the StreamPipeline ECC queue output record](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0860658 "KB0860658/PRB1434384: \"No sensors defined\" Error for Export Set ExportSetResult ECC Queue input records, because skip_sensor=true is missing from the StreamPipeline ECC queue output record")
    -   [KB0694628/PRB1237002: Export Definition Preview UI action doesn't work when List V3 is enabled](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694628 "KB0694628/PRB1237002: Export Definition Preview UI action doesn't work when List V3 is enabled")
-   Export to PDF  
    -   [KB0746820/PRB1321127: Exporting a Multi-Level Pivot table type report to PDF failed](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746820 "KB0746820/PRB1321127: Exporting a Multi-Level Pivot table type report to PDF failed")
    -   [KB0967318/PRB1504794: Exporting a Pivot Table Report to PDF produces a blank report...](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0967318 "KB0967318:Exporting a Pivot Table Report to PDF produces a blank report...")
    -   [KB0745494/PRB1319548: Multilevel report export to PDF is broken with unexpected error](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0745494 "KB0745494/PRB1319548: Multilevel report export to PDF is broken with unexpected error")
    -   [KB0622686: Exporting to PDF a record with a journal field with HTML tags will display them](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622686 "KB0622686: Exporting to PDF a record with a journal field with HTML tags will display them")
    -   [KB0725032/PRB602070:PDF exported knowledge articles is losing formatting of how it appears in ServiceNow](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725032 "KB0725032/PRB602070:PDF exported knowledge articles is losing formatting of how it appears in ServiceNow")
    -   [KB0522719/PRB575855: Activity information is not available on PDF export](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0522719 "KB0522719/PRB575855: Activity information is not available on PDF export")
    -   [KB0853013/PRB1416199: Exporting record with lots of data to pdf is taking too long to process in Orlando](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0853013 "KB0853013/PRB1416199: Exporting record with lots of data to pdf is taking too long to process in Orlando")
    -   [KB0827963: Total page numbering is wrong when exported in PDF](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0827963 "KB0827963: Total page numbering is wrong when exported in PDF")
    -   [KB0755229: PDF Export is not available to normal users even if they are able to see the record](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755229 "KB0755229: PDF Export is not available to normal users even if they are able to see the record")
    -   [KB0869769/PRB1434927: "OutOfMemoryError: Java heap space java.lang.OutOfMemoryError"while exporting a big report to PDF](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0869769 "KB0869769/PRB1434927: \"OutOfMemoryError: Java heap space java.lang.OutOfMemoryError\"while exporting a big report to PDF")
-   Export to XML  
    -   [KB0715440/PRB1311273: Export/Import XML of a KB Article containing images does not show the images in the target instance](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715440 "KB0715440/PRB1311273: Export/Import XML of a KB Article containing images does not show the images in the target instance")
-   Export to CSV  
    -   [KB0695242/PRB963728: CSV Export fails for large reports data causing an out of memory Java error](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0695242 "KB0695242/PRB963728: CSV Export fails for large reports data causing an out of memory Java error")
-   Export to Excel  
    -   [KB0724250: Export stopped due to excessive size. Use CSV for a complete export](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724250 "KB0724250: Export stopped due to excessive size. Use CSV for a complete export")
    -   [KB0678177/PRB645055: Users With user\_name Over 40 Characters Cannot Download Exported Excel Files](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0678177 "KB0678177/PRB645055: Users With user_name Over 40 Characters Cannot Download Exported Excel Files")
    -   [KB0621801/PRB864664: Japanese currency field is exported with additional decimals](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621801 "KB0621801/PRB864664: Japanese currency field is exported with additional decimals")
    -   [KB0596007/PRB682833: Export to Excel creates a corrupt Excel file if there is a currency field in the list](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596007 "KB0596007/PRB682833: Export to Excel creates a corrupt Excel file if there is a currency field in the list")

## Export Solutions

-   [KB0788372: Currency conversion on Export \[XML/PDF/Excel\] doesnt show user's locally set currency as expected in any instances exports.](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0788372 "KB0788372: Currency conversion on Export [XML/PDF/Excel] doesnt show user's locally set currency as expected in any instances exports.")
-   [KB0712564: Right click on form header missing options such as Configure or Export](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0712564 "KB0712564: Right click on form header missing options such as Configure or Export")
-   [KB0676119: How to restrict the Export option on lists to not show for certain tables](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0676119 "KB0676119: How to restrict the Export option on lists to not show for certain tables")
-   [KB0791043: How to export work notes information for incident?](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791043 "KB0791043: How to export work notes information for incident?")
-   Export Sets  
    -   [KB0687104: Export Sets not running for missing MID Server record in ecc\_agent\_status](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0687104 "KB0687104: Export Sets not running for missing MID Server record in ecc_agent_status")
-   Export to PDF  
    -   [KB0752531: Export Variables in RITM (to PDF)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0752531 "KB0752531: Export Variables in RITM (to PDF)")
    -   [KB0694524: Troubleshooting Report Export - Resolve connection refused error when exporting a report](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694524 "KB0694524: Troubleshooting Report Export - Resolve connection refused error when exporting a report")
    -   [KB0754273: PDF export is showing the error "An unexpected error has occured . Please see the instance logs for more details"](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0754273 "KB0754273: PDF export is showing the error \"An unexpected error has occured . Please see the instance logs for more details\"")
    -   [KB0696160: How to modify or remove the table details on the exported PDF](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0696160 "KB0696160: How to modify or remove the table details on the exported PDF")
    -   [KB0818411: Export to PDF functionality for Knowledge articles](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0818411 "KB0818411: Export to PDF functionality for Knowledge articles")
    -   [KB0715653: Some Fields Excluded from PDF Export of Form](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715653 "KB0715653: Some Fields Excluded from PDF Export of Form")
    -   [KB0675016: Report export shows message "Too much data to export"](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0675016 "KB0675016: Report export shows message \"Too much data to export\"")
    -   [KB0815422: Export of list view reports to PDF does not display the list column headers](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815422 "KB0815422: Export of list view reports to PDF does not display the list column headers")
-   Export to XML  
    -   [KB0858692: What's Needed to Export/Import Additional Comments and Worknotes between Instances](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0858692 "KB0858692: What's Needed to Export/Import Additional Comments and Worknotes between Instances") 
    -   [KB0622059: Currency field value on a table is not exported via XML export](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622059 "KB0622059: Currency field value on a table is not exported via XML export")
    -   [KB0852765: Unable to export to XML for non-admin users such as ITIL](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0852765 "KB0852765: Unable to export to XML for non-admin users such as ITIL")
-   Export to CSV  
    -   [KB0621445: When exporting from a list view or export set using CSV, column lengths are restricted to 32,000 characters](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0621445 "KB0621445: When exporting from a list view or export set using CSV, column lengths are restricted to 32,000 characters")
    -   [KB0684580: Unable to export reports as csv files](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0684580 "KB0684580: Unable to export reports as csv files")
-   Export to Excel  
    -   [KB0748698: Export of more than 32000 records to Excel results in creation of more than one worksheet](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748698 "KB0748698: Export of more than 32000 records to Excel results in creation of more than one worksheet")

## Videos

### Import

-   [Import Sets: Troubleshooting Truncated Data](http://youtu.be/ffmQg8aOXEo)
-   [Import Sets: Troubleshooting Missing Data in Date Fields](http://youtu.be/AXpfvXo1JN8)

### Export

-   [Troubleshooting ServiceNow Export Limits](http://youtu.be/jZna_EtZFZ4)

## Community (Import/Transform)

-   [Transform Map Best Practices](https://community.servicenow.com/community?id=community_blog&sys_id=8fc14160db18681011762183ca961935)

## Community (Export)

-   [Increasing the Export Limit for Excel](https://community.servicenow.com/message/1080541#1080541 "Increasing the Export Limit for Excel")
-   [Exporting large data sets into Excel](https://community.servicenow.com/community?id=community_blog&sys_id=0c2de2e5dbd0dbc01dcaf3231f961930 "Exporting large data sets into Excel")
-   [Using export sets for SFTP file transfer](https://community.servicenow.com/community?id=community_blog&sys_id=475eeaaddbd0dbc01dcaf3231f96198a "Using export sets for SFTP file transfer")
