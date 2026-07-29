---
title: "Employee Document Management (EDM) troubleshooting and FAQ"
aliases:
  - KB0963986
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0963986
kb_number: KB0963986
last_modified: 2026-01-27
---

## Employee Document Management (EDM) troubleshooting and FAQ

  

Troubleshoot common issues with Employee Document Management (EDM) and the EDM Bulk Imports feature. EDM provides centralized storage and a complete view for all employee documents. The Bulk Imports feature copies employee documents from an external third-party cloud-based storage location or a local network directory to Employee Document Management.

This article covers common EDM issues, with a focus on bulk import troubleshooting. 

### In this article:

**Import errors**

-   [Import Capture fails: Failed to get HTTP Response](#import-capture-no-http-reply)
-   [Import Capture fails: No sensors defined](#import-capture-no-sensors-defined)
-   [Import Capture fails: Invalid URI](#import-capture-invalid-URI)
-   [Import Verify fails: No credential found](#import-verify-fails)

**Configuration**

-   [Specify a MID Server for bulk import](#specify-mid-server-bulk-import)
-   [Windows-based MID Server compatibility](#windows-mid-server-compatibility)

**Connectivity and debugging**

-   [Debug SSH connection issues](#debug-ssh-connection)
-   [Debugging tips for EDM import issues](#debug-edm-import)
-   [Tips for debugging bulk import jobs](#debug-bulk-import)

**Document management**

-   [Retention policy not purging documents](#retention-policy-not-purging)
-   [Doc viewer does not support non-PDF files](#doc-viewer-pdf-files)
-   [PDF attachments deleted automatically](#auto-delete-pdf-attachments)

#### **Import Capture fails: Failed to get HTTP Response**

**Error messages:**

-   "Failed to create attachment: Failed to get HTTP Response"
-   MID Server logs show: "Unbuffered entity enclosing request can not be repeated"

**Cause:** This is a MID Server permission issue. The AttachmentSink API on the MID Server cannot upload files to the instance.

**Solution:** Assign one of the following role configurations to the MID Server user:

-   sn\_hr\_ef.admin role

Or both of the following:

-   sn\_hr\_ef.document\_import role
-   sn\_hr\_ef.document\_writer role

#### Import Capture fails: No sensors defined

**Error messages**:

-   "Unable to complete file capture step. Failure details: Failed to create attachment: Failed to get HTTP Response"
-   ECC queue shows: "No sensors defined"

**Cause**: The configured user (user name in the SSH credentials) does not have admin access.

**Solution**: Verify the SSH credential user has admin access. For verification steps, see [EDM Bulk Imports](https://docs.servicenow.com/bundle/utah-employee-service-management/page/product/human-resources/concept/edm-bulk-uploads.html).

#### Import Capture fails: Invalid URI

**Error message**: "java.lang.IllegalArgumentException: Invalid uri" (visible in the ECC queue response)

**Cause**: File names contain spaces, which causes the capture process to fail.

**Solution**: Apply the workaround documented in this [known error article](/kb?id=kb_article_view&sysparm_article=KB0965070).

**Note**: This issue occurs in the Paris release and is fixed in Orlando

#### **Import Verify fails: No credential found**

**Error message:** "Configuration test was unsuccessful. Change the configuration values and try again. Error: No credential found for types \[SSH Password,SSH Private Key\] with credential tag \[sn\_hr\_ef.file\_import\]"

**Cause:** Either SSH credentials are not configured correctly, or the import is not using the correct MID Server.

**Solution:**

1.  Verify SSH credentials are configured and working. See [Debug SSH connection issues](#debug-ssh-connection-issues).
2.  Check the ECC queue to confirm the correct MID Server is being used. See [Specify a MID Server for bulk import](#specify-a-mid-server-for-bulk-import).

#### **Specify a MID Server for bulk import** 

To specify which MID Server handles the bulk import job, use one of the following methods.

**Method 1: Create a custom capability**

1.  Create a new unique capability:
    -   Go to **MID Server** > **Capabilities**.  
        (Direct URL: <instance-name>/nav\_to.do?uri=%2Fecc\_agent\_capability\_list.do%3Fsysparm\_userpref\_module%3D0de137980a0006bc653cf70209afd11f%26sysparm\_clear\_stack%3Dtrue)
2.  Add the new capability to the MID Server you want to use for bulk import:
    -   Open the MID Server record.
    -   In the **Capabilities** related list, add the new capability.
    -   Remove the **All** capability from the MID Server.
    -   Verify the SSH capability is added.
3.  Update the ef\_LocalFileCapture::findMidServerForConfig method. Replace the following line:  
      
    var serverList = String(new sn\_automation.AutomationAPI().selectUpMidServers(null, \[host\], null)).split(',');  
      
    With  
      
    var capabilities = \[{capability: 'EdmBulkImport'}\];  
    var serverList = String(new sn\_automation.AutomationAPI().selectUpMidServers(null, \[host\], capabilities)).split(',');  
      
    
4.  Update the Test configuration activity:
    -   Go to **Orchestration** > **Activity Designer Activities**.
    -   Open the **Test configuration** activity.
    -   Select **Checkout**.
    -   On the **Execution Command** tab, add **EdmBulkImport** to the **Required MID Server capabilities** field.
    -   Save and publish.
5.  Update the **Get file names** activity:
    -   Go to **Orchestration** \> **Activity Designer Activities**.
    -   Open the **Get file names** activity.
    -   Select **Checkout**.
    -   On the **Execution Command** tab, add **EdmBulkImport** to the **Required MID Server** capabilities field.
    -   Save and publish.

**Method 2: Use application-based MID selection**

Add a new application for your MID selection criteria and associate it only with the MID Server you want to use. The MID selector then selects the MID Server with the corresponding application.

#### Windows-based MID Server compatibility

**Can I use a Windows-based MID Server for EDM import? What about the file server?**

The MID Server can run on either Windows or Linux. In the default configuration examples, both the MID Server and file server use Linux. Other configurations require custom development.

#### **Debug SSH connection issues**

If you see the error "Cannot connect, status is TCP\_CONNECTION\_DROPPED", use the following steps to debug:

1.  Test the SSH connection from the MID Server host using an SSH client such as OpenSSH or PuTTY.
2.  Review the security logs on the server. The**/var/log/secure** file often contains useful information.
3.  Enable debug logging on the SSH server:
    -   For OpenSSH, edit **/etc/ssh/sshd\_config** and set **loglevel=debug3**.
    -   Restart sshd.
    -   Check the logs in **/var/log/secure**.
4.  Start the MID Server in debug mode:
    -   Set **mid.ssh.debug=true** and **mid.log.level=debug**.
    -   Reproduce the problem.
    -   Review the agent log.
    -   For more information, see [MID Server parameters (product documentation)](https://docs.servicenow.com/bundle/utah-servicenow-platform/page/product/mid-server/reference/mid-server-parameters.html#d2631379e776).
5.  Verify that port 22 is open and the firewall allows traffic on port 22.

#### Debugging tips for EDM import issues

Use the following tips to debug EDM import issues:

**Directory path configuration**

When specifying the directory value in the Employee document import configuration, use a path relative to the home directory. For example, if the full path is ~/Documents/import, enter Documents/import as the directory value.

**Enable logging**

-   Set the **mid.show.queries** property parameter to enable MID Server logging. For more information, see [MID Server parameters](https://docs.servicenow.com/bundle/utah-servicenow-platform/page/product/mid-server/reference/mid-server-parameters.html#d2430021e1603).
-   Set the **glide.http.log\_debug** system property to enable HTTP debug logging.
-   Review MID Server agent and wrapper logs.

**Check the ECC queue**

The ECC queue record contains information about commands sent to or received from the MID Server. For more information, see:

-   [Discovery Status ECC Queue](https://docs.servicenow.com/bundle/utah-it-operations-management/page/product/discovery/reference/r_DiscoveryStatusECCQueue.html?cshalt=yes)
-   [MID Server Troubleshooting](https://docs.servicenow.com/bundle/utah-servicenow-platform/page/product/mid-server/reference/r_MIDServerTroubleshooting.html?cshalt=yes)

#### Tips for debugging bulk import jobs

Use the following process to debug bulk import jobs:

**Prerequisites**

Set up a MID Server to communicate with the file server and the instance.

**Configuration**

1.  Go to **HR Administration** > **Bulk Import** > **Import Configuration**.
2.  Open the desired configuration.
3.  Set **Staging Record State** to **Ready**.

**Debugging process**

1.  Select **Start Verify Configuration**. This verifies credentials and MID Server connectivity to the file server.
2.  Resolve any connectivity errors before proceeding.
3.  If verification passes, select **Start staging job**. This retrieves metadata about files ready for transfer.
4.  If staging succeeds, select **Start capture job**. Because the state is set to Ready, this job downloads all Ready files from the file server to the MID Server, then from the MID Server to the instance (Attachments \[sys\_attachment\] table).
5.  If the job fails, check the **Document Staging** related list. Each failed file shows an Error state with error details.

#### Retention policy not purging documents

**Symptom**: Documents are not being purged as expected after creating a retention period or policy.

**Cause**: The scheduled job's "Run as" user does not have the required role.

**Solution**: Assign the sn\_hr\_ef.admin role to the "Run as" user for the scheduled job. After adding this role, the scheduled jobs run correctly and the purge and notification flow works as expected.

#### Doc viewer does not support non-PDF files

**Symptom:** The employee document upload custom UI page does not support viewing non-PDF files using the doc viewer.

**Cause:** When EDM was first developed (London release), the doc viewer supported only PDF format. This limitation remains in the base system.

**Workaround:**

1.  Update the **canView** property to **true** in the **Employee document Upload** UI page. This displays the View button for other document types.
2.  Add an OR query in the condition builder for the ACL with sys\_id **a10c0618dbcac4102207f1471d96192f**:
    -   **table\_name = sys\_attachment**

#### PDF attachments deleted automatically

**Symptom**: PDF attachments in employee document records are deleted automatically.

**Cause**: The platform scheduled job Clean up converted documents generated by PDF Generation Utilities plugin deletes these attachments.

The job queries the PDF Generation Status \[sys\_pdf\_generation\_status\] table for records that meet the following criteria:

-   sys\_updated\_on is older than the retention period (default: 7 days)
-   conversion\_status is complete
-   converted\_attachment\_id is not null

The job deletes matching attachments and updates the status to expired.

**Workaround**:

Use one of the following options:

**Option 1: Increase the retention period**

1.  Go to **System Properties** > **All Properties**.
2.  Search for **com.snc.documentviewer.retention\_days\_converted\_file**.
3.  Set the **Value** field to a number greater than 7.

**Option 2: Disable the scheduled job**

Disable the scheduled job: Clean up converted documents generated by PDF Generation Utilities plugin.

### Related links

**Product documentation**

[Employee Document Management overview](https://docs.servicenow.com/bundle/utah-employee-service-management/page/product/human-resources/concept/hr-employee-doc-management.html)

[EDM Bulk Imports overview](https://docs.servicenow.com/bundle/utah-employee-service-management/page/product/human-resources/concept/edm-bulk-uploads.html) 

[Employee Document Management Bulk Import functionality (Community)](https://www.servicenow.com/community/hrsd-articles/employee-document-management-bulk-import-functionality/ta-p/2309316)

**Additional resources** 

-   [EDM Implementation Guidance (Community)](https://community.servicenow.com/community?id=community_blog&sys_id=d73496aedb6f00542be0a851ca96198a "EDM Implementation Guidance and Best Practice")
-   [EDM community resource page](https://www.servicenow.com/community/hrsd-articles/employee-document-management-resources/ta-p/2312162 "EDM community resource page")
