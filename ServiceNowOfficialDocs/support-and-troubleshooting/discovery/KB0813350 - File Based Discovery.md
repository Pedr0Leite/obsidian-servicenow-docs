---
title: "File Based Discovery"
aliases:
  - KB0813350
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0813350
kb_number: KB0813350
last_modified: 2026-01-26
---

## File Based Discovery

  

### Summary

File-based Discovery helps you identify what software is running on your Windows and UNIX servers and devices. You can then manage and maintain records of your software licenses, check for unlicensed files, detect forbidden or damaged files, and help evaluate any threats from unwanted files. This information is stored in the File Information \[cmdb\_file\_information\] table with a reference to the CI of the server. File-based Discovery is triggered in the exploration phase of normal Discovery. File-based Discovery probes execute a scan searching for specific file extensions or file names in paths that you configure. The resulting file information is returned in the probe payload. The sensor attempts to match the discovered files with installed software, using the file name, size, and version returned by the probe. For more information see document [File-based Discovery](https://docs.servicenow.com/csh?topicname=file-based-discovery.html&version=latest "File-based Discovery"). If SAMP is active on the instance, File-based Discovery creates or updates identified software products in the Software Installation \[cmdb\_sam\_sw\_install\] table and updates the licenses of matched software packages. Without SAMP, no software records are created and only the file information goes into the File Information \[cmdb\_file\_information\] table.

Required Plugin

The File-based Discovery \[com.snc.discovery.file\_based\_discovery\] plugin is required for file signature filtering.

Configuration

Once the File-based Discovery plugin is active, configuration will be performed in the Discovery Configuration Console, under "Discovery Definition > Configuration Console".

Script includes

-   DiscoveryFBDConditions
-   FileBasedDiscoveryUtils

Properties  

**Note**: Use the Configuration Console to update these properties.

<table style="border-collapse: collapse; width: 100%; height: 195px;" border="1"><tbody><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">&nbsp;Name</td><td style="width: 87.7724%; height: 13px;">Description (All Controlled via Configuration Console)</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.enabled</td><td style="width: 87.7724%; height: 13px;">Use this flag to turn on/off File Based Discovery which will attempt to discover software on Unix and Windows computers via file signatures.</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.path.windows</td><td style="width: 87.7724%; height: 13px;">A list of Windows file paths to scan for file signatures.</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.ignore_path.windows</td><td style="width: 87.7724%; height: 13px;">A list of Windows file paths to ignore when scanning for file signatures.</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.blacklist.windows</td><td style="width: 87.7724%; height: 13px;">A list of Windows file extensions to ignore during file discovery scan.</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.wildcard.windows</td><td style="width: 87.7724%; height: 13px;">Any file in the scan path that matches an extension in this list will be discovered. This is in addition to the list of files that are already discovered by default. Adding to this list might impact performance.</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.skip_hidden_folders.windows</td><td style="width: 87.7724%; height: 13px;">Use this flag to turn on/off whether File Based Discovery will search inside hidden folders for files on Windows devices.</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.use_rp_path.windows</td><td style="width: 87.7724%; height: 13px;">Determines whether to use running process paths during Windows FBD.</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.scan_swid.windows</td><td style="width: 87.7724%; height: 13px;">Scan for .swidtag files and use the information therein to create software install records (when SAMP activated).</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.sleeptime.windows</td><td style="width: 87.7724%; height: 13px;">Length of time to sleep in milliseconds during each throttling interval while scanning for Windows files. Default is 10000.</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.throttle.windows</td><td style="width: 87.7724%; height: 13px;">Number of files to scan on windows before sleeping. Default is 500.</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.skip_hidden_folders.unix</td><td style="width: 87.7724%; height: 13px;">Use this flag to turn on/off whether File Based Discovery will search inside hidden folders for files on Unix devices.</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.use_rp_path.unix</td><td style="width: 87.7724%; height: 13px;">Determines whether to use running process paths during Unix FBD.</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.ignore_path.unix</td><td style="width: 87.7724%; height: 13px;">A list of Unix file paths to ignore when scanning for file signatures.</td></tr><tr style="height: 13px;"><td style="width: 12.2276%; height: 13px;">glide.discovery.file_discovery.path.linux</td><td style="width: 87.7724%; height: 13px;">A list of Unix file paths to scan for file signatures.</td></tr><tr><td style="width: 12.2276%;">glide.discovery.file_discovery.frequency</td><td style="width: 87.7724%;">Defines the frequency for running file-based Discovery on a CI. After Discovery runs and returns file information for a CI, it will not execute file-based Discovery again on that target until the interval has expired. Choosing a frequency higher than "Monthly" is not recommended due to performance considerations.</td></tr><tr><td style="width: 12.2276%;">glide.discovery.file_discovery.max_file_number</td><td style="width: 87.7724%;">Number of files that can be discovered per target machine. Default is 100000.</td></tr></tbody></table>

Probes Triggered By

https://<instance\_name>.service-now.com/discovery\_sensor\_probe\_conditional\_list.do?sysparm\_query=condition\_scriptLIKEDiscoveryFBDConditions

File-based Discovery Filtering Flow

![File Based Discovery Filtering Flow](sys_attachment.do?sys_id=f693543797623a1068d477121153af0f "File Based Discovery Filtering Flow")

Issues

**Error**: FBD is disabled via system property but is being triggered one last time to clean up any remaining FBD results on the target.  
**Cause**: glide.discovery.file\_discovery.enabled = false.  
**Solution**: Navigate to "Discovery Definition > Configuration Console" and enable file based discovery.

**Error**: Not triggering FBD since its probes have not been built (CDS content has probably not been synched yet)  
**Cause**: Properties file\_discovery.unix\_filename.timestamp and file\_discovery.windows\_filename.timestamp under table discovery\_private\_properties have value of 1970-01-01 12:00:00, which means the CDS content has not been downloaded yet.  
**Solution**: By default, the content is downloaded once every week. Navigate to table cds\_client\_schedule and search for records where field "table" value are one of samp\_file\_name, samp\_file\_map, samp\_file\_set . Click on the records and then on "Execute Now" to trigger an immediate download from the CDS.

**Note**: It can take a while for the content do be fully downloaded. Navigate to "System Logs > Outbound HTTP Requests" to review the download of the content and ensure that the "Response status" is 200 for http logs where the "URL hostname" is sncdataservices.service-now.com.

**Error**: Not triggering FBD since interval has not passed  
**Cause**: Interval since last FBD has not passed.  
**Solution**: Navigate to "Discovery Definition > Configuration Console" and configure the interval accordingly. 

Also see [File-based Discovery issue resolution](https://docs.servicenow.com/csh?topicname=run-file-based-discovery.html&version=latest#file-based-discovery-troubleshooting "File-based Discovery issue resolution").

### Related Links

-   [Run File-based Discovery](https://docs.servicenow.com/csh?topicname=run-file-based-discovery.html&version=latest#file-based-discovery-troubleshooting "Run File-based Discovery")
-   [File-based Discovery tables](https://docs.servicenow.com/csh?topicname=file-based-discovery-references.html&version=latest "File-based Discovery tables")
-   [File Signature Normalization](https://docs.servicenow.com/csh?topicname=sam-file-based-discovery.html&version=latest "File Signature Normalization")
