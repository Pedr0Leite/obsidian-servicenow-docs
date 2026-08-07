---
aliases:
  - "How to import a CSV file from a Mid Server"
area: "Mid Server"
source: notion-export
tags:
  - mid-server
  - ecc-queue
  - csv-import
  - attachment-api
---

# How to import a CSV file from a Mid Server

### Issue

This
 KB is applicable if you want to import a file from a MID server. You 
can export a file to a mid server, but there is no out of the box 
feature to import a file from the MID server

### Cause

This
 functionality was not made available with a simple UI interface. The 
MID server was not designed from the ground up for BIG data transfer and
 to stream large files uplink.

This means that there are limitations due to the way Tomcat was 
configured and this kind of requests in split up in small chunks and 
this is not ideal for performance reasons, so we really advise against 
very large files  as this can cause an Out of memory issue and the 
instance would stop responding.

### Resolution

## There are different workarounds

- [Import file into instance using SOAP inbound requests.](https://support.servicenow.com/kb#mcetoc_1gco83gm8c)
- [Direct CSV or Excel (XLS) File Import (Not Specific to MID Server)](https://support.servicenow.com/kb#mcetoc_1gco83gm8d)
- [Attaching Files Directly using the Attachment API or MID Command Probes](https://support.servicenow.com/kb#mcetoc_1gco83gm8e)
- [Custom code (Not developed, tested or supported by ServiceNow)](https://support.servicenow.com/kb#mcetoc_1gco83gm8f)

### Import file into instance using SOAP inbound requests.

[Send a SOAP message through a MID server](https://docs.servicenow.com/csh?topicname=c_SendSOAPMsgMIDServer.html&version=latest)

When importing large file attachment , for example 250MB into ServiceNow, you will hit SOAP maximum request size limits

The maximum heap memory on one instance is 2GB by default.

The
 memory to process XML payload (all SOAP request information is in XML 
format) may take 10~20 times of the payload size so ServiceNow instance 
can not handle more than 100MB SOAP payload.

Anything SOAP payload 
size bigger than this will be very risky to crash your instance as it is
 very close to reach the upper limit of heap memory.

The default 
value is 70MB for property "glide.soap.max_inbound_content_length" we 
always recommend to tweak the value a little bit more and test to see if
 any performance impact on their instance.

The best solution to import the large attachment is to use attachment API instead. Refer to [Attachment API](https://docs.servicenow.com/bundle/sandiego-application-development/page/integrate/inbound-rest/concept/c_AttachmentAPI.html) for more details.

You can refer to below links for the same discussion on our community website as well.

[What is the maximum size of JSON message that ServiceNow can receive in a single REST call?](https://community.servicenow.com/community?id=community_question&sys_id=31841425db2dbfc0d82ffb2439961945)

### Direct CSV or Excel (XLS) File Import (Not Specific to MID Server)

Using the built-in /sys_import.do 'API' it's possible to import CSV
 or Excel files directly. There's no need to use a MID Server for this, 
it can be done from any host where you have the relevant tools (either a
 script that can do POST requests or a program such as Postman). Note 
that there's also nothing stopping you doing this import from a MID 
Server host.

This is documented on [Post CSV or Excel files directly to an import set](https://docs.servicenow.com/csh?topicname=t_PostCSVOrExcelFilesToImportSet.html&version=latest)

Example scripts are provided here: [Posting a CSV file - Perl and Java examples](https://docs.servicenow.com/csh?topicname=r_PerlExample.html&version=latest)

**Note**:
 the file content itself must be uploaded as a POST request, as a 
multi-part attachment. The name (key) of this parameter can be called 
anything you like.

As well as the above script examples you can also test this on Postman:

- Create a simple test CSV file
- Upload the CSV file once
manually using 'Load Data' on the instance, to create the necessary
Import Set Staging table (e.g. u_mytestimport)
- Delete the uploaded data from the Import Set Staging table (e.g. u_mytestimport)
- POST request to
https://INSTANCENAME.service-now.com/sys_import.do?sysparm_import_set_tablename=u_mytestimport&sysparm_transform_after_load=false
    
    (Where u_mytestimport is the Import Set Staging Table, this must 
    have already been created by manually uploading a CSV with the same 
    columns once)
    
- Authorization: Basic authentication
- Body: form-data
(for multi-part attachment). Create a parameter (this will be a POST
parameter) with Key set to anything you like ('uploaded_csv_file',
'somefile' etc) of type File (select from dropdown) and for Value set
the location of the file
- Send, the data will now appear in the Import Set Staging table

### Attaching Files Directly using the Attachment API or MID Command Probes

Recommended Method ('Push' the file from the MID Server Host)

You can have the file attached to an existing record, such as an 
incident, by using the out-of-box (and supported) Attachment API. Of 
course this approach relies on you having a program or script running on
 the MID server host that can make that API call to insert the file. How
 you implement this on the MID server host (e.g. Powershell script on 
Windows, or bash script using cURL on Linux) would be out of our support
 scope and not something we can help with.

Customization (Pull the File From the MID Server Host via a Script on the Instance)

If that's not an option and you need to pull from the MID Server 
host, you can take advantage of the MID Server command probe. This 
allows you to run shell commands on the system. What this would look 
like is a script similar to this (you can run it as a Scheduled Job if 
needed):

Linux or Macos:

var probe = SncProbe.get("Command");

probe.setName("cd /Users/me/Desktop && cat example.csv | base64");

probe.create("<MID Server Name>");

Windows:

A suggestion for an equivalent Windows command (that returns the content of a file as a base64-encoded string) is here: [https://stackoverflow.com/questions/37046771/base64-encode-string-command-line-windows](https://stackoverflow.com/questions/37046771/base64-encode-string-command-line-windows)

Create an ECC Queue record using this script, replace 
mid.server.<MID SERVER NAME GOES HERE> with 
mid.server.NAME_of_MID_Server (copy from another ECC queue output record
 if in doubt) and <COMMAND TO RUN> with the Powershell command to 
run (not inside '< >'):

// based on [Executing powershell command on mid server](https://community.servicenow.com/community?id=community_question&sys_id=19c8336adbe323c0f21f5583ca96198b)

var payload = '<parameters>' + '<parameter 
name="probe_name" value="Windows - Powershell"/>' + '<parameter 
name="script.ps1" value="<COMMAND TO RUN>"/>' + '<parameter 
name="skip_sensor" value="true"/>' + '</parameters>';

var sysid = '';

var grECC = new GlideRecord('ecc_queue');

grECC.initialize();

grECC.agent = 'mid.server.<MID SERVER NAME GOES HERE>';

grECC.topic = 'Powershell';

grECC.name = 'Windows - PowerShell';

grECC.source = '127.0.0.1';

grECC.queue = 'output';

grECC.payload = payload;

sysid = grECC.insert();

The response to this will be a base64 encoded string of the file 
that will get written to ECC Queue in the response. You can then turn 
this into an attachment with a Business Rule on the instance:

Create a new Business Rule with:

Name: whatever makes sense, e.g "Process Input ECC queue command entries"

When to run->When: After, Insert: ticked, Order: 100

When to run->Condition:

- Name is cd /Users/me/Desktop && cat example.csv | base64 (Note: this has to be the exact command you're running in the probe.setName()
call, OR for Windows what you're setting with grECC.name, OR
alternatively leave out this condition and use if statements in the
script to set a condition)
- Topic is Command
- Queue is input
- State is ready

Tick Advanced, then Advanced->Script should be (replace 
'incident', 'b1d588a21bab101093c210ea274bcbb7' with the table name and 
sys_id of the record to which you want the attachments added):

(function executeRule(current, previous /*null when async*/) {

var encStr = gs.getXMLText(current.payload, "//stdout");

gs.info("Text was " + encStr);

var stringUtil = GlideStringUtil;

var attachment = new Attachment();

attachment.write('incident',
 'b1d588a21bab101093c210ea274bcbb7', 'example.csv', 'text/csv', 
stringUtil.base64DecodeAsBytes(encStr));

})(current, previous);

This method has been tested on a Paris test instance using a Linux 
MID server host and it does work (note that using Powershell with a 
Windows MID host has not yet been tested). However it's a customisation 
and this information is intended as a suggestion for your own developers
 to work further on, and may not have been fully tested. ServiceNow 
cannot provide support for customisations.

###

## Related

- [[Mid Server]]
- [[Run Commands on Mid Servers]]
- [[How the ECC Queue table records get processed from]]
- [[Installation]]