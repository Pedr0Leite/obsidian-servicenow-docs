---
aliases:
  - "How the ECC Queue table records get processed from"
area: "Mid Server"
source: notion-export
tags:
  - ecc-queue
  - mid-server
  - integrationhub
  - discovery
  - sensors
---

# How the ECC Queue table records get processed: from output ready to input processed

# **1. Job is added to Output Queue**

A feature or application wants to do an integration that uses the ECC Queue, so does an insert into the ecc_queue table. A description of the fields from the Discovery point of view can be found in the [MID Server ECC Queue](https://docs.servicenow.com/csh?topicname=ecc-queue-mid-server.html&version=latest#ecc-queue-mid-server) documentation. More generally, they mean:

| Agent | What will run the job. If the Agent value starts with "mid.server." then it's a job for a MID Server, unless it is "mid.server.NODE_AGENT" which means the instance. e.g. NODE_AGENT value is used by RESTProbe when it's the instance doing the request directly.
If Agent is "mid.server.*", then the "Probe - All MIDs" Business Rule (BR) will insert copies of the record specific to every individual MID Server (regardless of their state). This is normally only used for system commands where all MID Servers need re-syncing with a change in the instance. |
| --- | --- |
| Queue | Output is the Job, Input is the result, **from the point of view of the instance**. |
| State | **Ready** means waiting/queued. **Processed or Error** means the job is finished. In between it is **Processing**, which doesn't mean the job has actually started to run yet because it may still be in MID Server internal queue. |
| Topic | The '**Probe**' that is to run for the job. This equates to a name of a Java object in the source code. (not to be confused with the 'Discovery Probe' name) |
| Name/Source | Specific to the Topic, but usually the **main probe parameters**. |
| Payload | **Additional probe Parameters** for the Probe. XML format. The ECC output parameters are also included in the EEC input, together with the result and errors. |
| Agent Correlator | Something to help **reference back to the code/task/schedule that created the job**, so that the sensor can pass the results back to the original thing. |
| Priority | 2=**Standard(default)**, 1=Expedited, 0=Interactive. Almost everything uses Standard. Only system commands, or things where users are waiting for a response after clicking something use higher priorities. |
| Sequence | The queue **Order**. It is a combination of Unix epoch timestamp, and a number in case there are multiple records at the same time, so within millisecond resolution. |
| Response To | For Inputs, this references the corresponding Output. |
| Processed | The **time the State changed from Ready to Processing**. For Outputs, it is when the queue.processing Input was inserted. For Inputs it is set by the sensor, which not all sensors set. |

# **2. MID Server (or instance code) picks up the job**

Note: These MID Server specific steps are not going to be involved if the Instance is running the jobs itself.

The MID Server needs to be **Up and Validated** in order to pick up jobs.

If the MID Server AMB Channel is working, the MID Server knows there is something new in the queue for it instantly. If not, the periodic ECCQueueMonitor thread runs to check.

MID Server queries the instance ecc_queue table using the normal SOAP Table API, via the app node's API_INT semaphores. It looks for any output records, with it as the Agent, and in Ready state. Only a certain number are fetched at a time, proportional to the MID Server thread count. On MID startup, it also queries for Processing state outputs, on the assumption that the MID Server may have died while processing them and needs to run them again.

The oldest records with the highest priority are fetched first.

[KB0743566 MID Server Max Threads, Worker Groups , Priority and Queues](https://hi.service-now.com/kb_view.do?sysparm_article=KB0743566) - Has more on ECC Sender folder, priority of sys_trigger jobs, and how many outputs are fetched at a time.

# **3. MID Server notifies the Instance that it has picked up the job**

MID Server writes a topic=queue.processing input to the ecc_queue to tell the instance what it has picked up. The payload looks like:

```
<queue.processing output_message_count="1"><sys_id state="processing">2401af2c1b8b1010254542e7cc4bcb5b</sys_id></queue.processing>
```

This may include multiple sys_ids, because the MID Server queries for new jobs in batches. That input triggers sensor Business Rule "ECC Queue - mark outputs state" to update those output records from Ready to Processing state.

# **4. MID Server executes the job**

In the MID Server, the input is held in a queue in memory until there is a free Worker Thread (the thread pool used depends on the priority), and then is passed to the java probe code specifically for the Topic, and runs it in a thread.

Given that, an ecc_queue output marked as Processing state doesn't mean it's running. It just means it is now in the MID Server's internal queue, and will run it at some point. The agent log entries include the sys_id of the ecc output record for confirmation of when it did run. Because of this the output record created, processed and updated timestamps give an idea of the wait time and processing time, but are not accurate because of that internal queue wait time as well.

While running the job, code may make additional calls to the instance APIs using AMB/REST/SOAP directly, that may not be via the ECC Queue. For example, IntegrationHub outputs simply reference a Flow Designer Context, and the Probe then needs to query that context in the instance to know what actual steps it is to execute.

The thread running the job **writes the result of running the probe to an XML file in one of the ECC Sender output folders in agent\work\monitors\ECCSender**. There are several folders depending on the priority or if it is sequential. These folders act as a send queue, and there are limits.

The probe will log to the MID Server's agent/logs/agent0.log.0 file as it runs. Adding Probe Parameters and MID Server parameters will cause additional debug to be written to the log. Each feature's probe is likely to have different probe parameters and levels of logging, and require more than just adding the mid.log.level parameter=debug to the mid server.

Agent log will write "Worker starting" and "Worker completed", and "Enqueuing:" when it writes the result to disk, where the sys_id in the thread name is the ecc_queue output record. "time:" is how long the probe ran for in the MID Server, which in this example would be how long approximately the REST message to the endpoint took:

```
02/14/23 18:38:37 (328) Worker-Expedited:MIDWorker-02aad4091b01e190d41b65fa234bcb18 Worker starting: RESTProbe source: https://a.b.com/x?x=z
02/14/23 18:38:37 (598) Worker-Expedited:MIDWorker-02aad4091b01e190d41b65fa234bcb18 Enqueuing: /<install_folder>/agent/work/monitors/ECCSender/output_1/ecc_queue.02aad4091b01e190d41b65fa234bcb18.xml
02/14/23 18:38:37 (599) Worker-Expedited:MIDWorker-02aad4091b01e190d41b65fa234bcb18 Worker completed: RESTProbe source: https://a.b.com/x?x=z time: 0:00:00.268
02/14/23 18:38:38 (204) ECCSender.1 Sending ecc_queue.02aad4091b01e190d41b65fa234bcb18.xml

```

# **5. The MID Server returns the result to the instance**

The ECCSender thread inserts an ecc queue input for each xml file, then deletes the XML file. Highest priority are sent first, with the oldest of those first, until all the folders are empty.

The SOAP Table API is used for the insert, just like any other inbound integration inserting into a table via a SOAP message, and will run in an API_INT semaphore. The instance Transaction Log will show it as:

```
/ecc_queue.do?redirectSupported=true&SOAP&displayvalue=all
```

The "ECC Queue - mark outputs processed" Business rule runs for each Input record inserted, which sets the Output record state to Processed.

[KB0743566 MID Server Max Threads, Worker Groups , Priority and Queues](https://hi.service-now.com/kb_view.do?sysparm_article=KB0743566) - Has more on ECC Sender folder, priority of sys_trigger jobs, and how many outputs are fetched at a time.

Agent log will write "ECCSender.1 Sending", where the sys_id in the temp filename is the ecc_queue output record:

```
02/14/23 18:38:38 (204) ECCSender.1 Sending ecc_queue.02aad4091b01e190d41b65fa234bcb18.xml

```

If there is a problem inserting the ecc_queue record, errors will be seen in the appnode localhost log for the API_INT SOAPProcessor thread for "/ecc_queue.do?SOAP", and mid server agent log ECCSender thread. Depending on the type of error, the mid server may retry several times, backing off the retry interval until giving up.

If the error is instance side, the XML file will be moved into agent\work\monitors\ECCSender\output_error. If the payload is larger than the MID Server permits (mid.eccq.max_payload_size), it is moved into agent\work\monitors\ECCSender\output_oversize. Those are not sent to the instance, and deleted after 30 days by [MID File Cleaner](https://hishowcase.service-now.com/kb?id=kb_article_view&sysparm_article=KB1207621).

Business rules will run for the insert, and they could error and break the insert transaction, causing status 500 to be returned. The MID Server will not know if it errored before or after insert, and assume the insert failed, which can lead to multiple inserts.

# **6. Sensors run in the instance**

Business rules run for each input record insert. They are usually synchronous, before or after input, as part of the API_INT semaphore SOAP transaction. One (or more) of these business rules will be what we call the "Sensor" for the job.

They run according to the Order field, and are skipped based on conditions, like any other business rule on record insert. Some will run condition checks to see if the input is for them, and if not then they leave the record as is, allowing the next BR in the order to have a go.

The following list groups the ecc_queue business rules by Package, helping see which act as the sensor for any particular job. The condition field can usually be used to easily see which jobs the sensor is for.

https://<instance name>.service-now.com/sys_script_list.do?sysparm_query=collection%3Decc_queue%5Eactive%3Dtrue%5EGROUPBYsys_package

[](https://support.servicenow.com/sys_attachment.do?sys_id=df9ed72d9375f510c2513f986cba1053)

Most sensor business rules pass on the work to a scheduled job by inserting a 'run once' sys_trigger record, that the Background Scheduler Worker threads will then pick up and run to do the actual sensor processing. For Discovery, this inherits the priority from the ECC Queue record. If the business rules spends too much time processing stuff as part of the SOAP insert then it risks blocking the API_INT semaphores. That's bad as there are only a few per app node, and there may be many MID Servers sharing those. It is the job of any specific sensor to deal with scheduler worker priority, and each feature/app may do it differently.

The specific sensor code will usually set the input to Processing status when it starts working on it, and error or processed when it ends. The sensor will usually populate the Error String field on Error. Each feature/app may do it differently in their sensors.

The payload field may end up in an attachment, which is an instance's SOAP table API's doing (see glide.soapprocessor.large_field_patch_max). It is the responsibility of each individual sensor to then deal with that. The attachment needs to be smaller than system property com.glide.attachment.max_get_size. Discovery aims to keep everything below 5MB but other features may not.

Don't always expect one input per output. Some features split large results into multiple input records. JDBCProbe for import set data sources splits the inputs into separate ecc_queue inputs for each 200 rows of data, only continuing with the transform once all inputs are received back to the ecc queue. This probe uses the output_s ECCSender folder, so the inputs arrive back at the instance sequentially. Discovery patterns can use multi-page inputs, and each data sub-set input is usually processed as it comes in, without waiting for the full set of data.

**There may not be a sensor for the input at all**. Those inputs remain in Ready state. e.g. RESTProbe outputs created by RESTMessageV2, that are executed synchronously, such that result/error handling is done by the same script creating the job, often won't need a sensor BR. Generally there should always be a sensor in order to at the very least do error handling, and set it to Processed, to avoid the false impression of a queue backlog.

The "Discovery - Sensors" BR will usually run for the input, even if it has nothing to do with discovery. This all goes back to when MID Server was part of Discovery and only used by Discovery. So long as the output parameters includes skip_sensor=true, then that's fine, and the discovery sensor know to skip it. Every non-Discovery job should include that, but many don't, including some OOTB features.  If the input doesn't have that parameter, the discovery sensor will try to process it, and may cause an Error. e.g. RESTProbe inputs without skip_sensor will get set as state=Error and Error string="No sensors defined". That parameter is in the payload, which may be huge, or even an attachment, and the discovery sensor has to process that to read the parameter, which in itself can take a while or use a lot of memory. When this sensor runs for non-Discovery jobs, you can tell because the app node logs will have "Get for non-existent record: discovery_status:..., Initializing" because the Agent Correlator field value isn't for one of these records.

The sensor will usually use Agent Correlator values to make sure the results end up back with the specific job/record/workflow/Discovery status that created the job. Orchestration values all start "rba." and Integrations Hub "ihub." for example.

# **Examples**

### **Example 1 - Heartbeat Probe**

sys_trigger job, BR sensor. slightly bad example in that sensor runs everything synchronously - doesn't offload the actually processing to a sys_trigger job.

- Initial script: Schedule [sys_trigger]: MID Server Monitor
- Sensor Business Rule: MID - Heartbeat

[](https://support.servicenow.com/sys_attachment.do?sys_id=9b9e972d9375f510c2513f986cba10c6)

### **Example 2 - Synchronous RESTMessagev2**

Unusual in that it executes synchronously in the instance, and waits for the response, literally sleeping and blocking the thread in the process.

- Initial script: Any custom script, calling RESTMessagev2.execute()
- Sensor Business Rule: None

In this case the initial thread sleeps, and regularly polls the ECC Queue. The stack trace of the thread looks like:

```
main,glide.scheduler.worker.4,4,<thread name - often a business rule or scheduled job name> (82899 ms)
java.lang.Thread.sleep(Native Method)
com.glide.ecc.ECCResponsePoller.poll(ECCResponsePoller.java:50)
com.glide.rest.outbound.ecc.ECCRESTResponse.fetchAndProcessEccResponse(ECCRESTResponse.java:232)
com.glide.rest.outbound.ecc.ECCRESTResponse.getBody(ECCRESTResponse.java:124)
```

For more information on this example, and why is is potentially rather bad, see:

[KB0727028 Why is State "Error" and "No sensors defined" in the ECC Queue for outbound REST/SOAP Message via MID Server?](https://hi.service-now.com/kb_view.do?sysparm_article=KB0727028) - Expands on the skip_sensor parameter.

[KB0694711 Outbound REST Web Services RESTMessageV2 and SOAPMessageV2 execute() vs executeAsync() Best Practices](https://hi.service-now.com/kb_view.do?sysparm_article=KB0694711)

[KB0716391 Best practices for RESTMessageV2 and SOAPMessageV2](https://hi.service-now.com/kb_view.do?sysparm_article=KB0716391)

[PRB1305586 RESTMessageV2/SOAPMessageV2 APIs allow running via MID Servers Synchronously, without a Sensor ECC business rule, causing blocked instance threads while sleeping, and Scheduler overload](https://hi.service-now.com/kb_view.do?sysparm_article=KB0714559)

[KB0749289 Synchronous Outbound Web Service Calls Timing Out After 30 seconds Following Upgrade](https://hi.service-now.com/kb_view.do?sysparm_article=KB0749289)

### 

[](https://support.servicenow.com/sys_attachment.do?sys_id=d39ed72d9375f510c2513f986cba1056)

### **Example 3 - Discovery Sensors**

- Initial script: ShazzamLaunch when starting Discovery, or triggered by the previous Discovery sensor. e.g. The Windows - Server pattern launched by the Windows - Classify sensor.
- Sensor Business Rule: Discovery - Sensors
- sys_trigger job: ASYNC: Discovery - MultiPage Sensors (Note: Paris now includes the name, source and sys_id of the ecc_queue input as well, to make it much easier to trace the thread)

For more information on this example, see:

[KB0718653 ECC Queue Processing and debugging, with "Discovery - Sensors" used as an example](https://hi.service-now.com/kb_view.do?sysparm_article=KB0718653) - Has details on how specifically Discovery sensors process to explain the Discovery example in more detail.

[](https://support.servicenow.com/sys_attachment.do?sys_id=839e972d9375f510c2513f986cba10c3)

### **Debugging**

The above should help you understand at what stage in the process you have a problem. If you know the 'where' you are halfway to solving it. The following KBs will help

[KB0718589 Why are my MID Server-related Jobs stuck and ECC Queue inputs still in Ready State?](https://hi.service-now.com/kb_view.do?sysparm_article=KB0718589) - Suggests possible causes of Sensor processing delay, and gives troubleshooting tips and solutions.

[KB0727132 - How to link an ECC Queue record back to a specific Feature or Job](https://hi.service-now.com/kb_view.do?sysparm_article=KB0727132) - Lists the Topic/Name/Source/Agent Correlator values used by many different features, and what the values mean.

## Related

- [[Mid Server]]
- [[Run Commands on Mid Servers]]
- [[How to import a CSV file from a Mid Server]]
- [[Installation]]
- [[IT Operations Management (ITOM)]]