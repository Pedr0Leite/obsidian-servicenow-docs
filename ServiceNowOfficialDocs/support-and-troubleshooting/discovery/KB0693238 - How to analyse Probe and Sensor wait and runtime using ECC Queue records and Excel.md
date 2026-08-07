---
title: "How to analyse Probe and Sensor wait and runtime using ECC Queue records and Excel"
aliases:
  - KB0693238
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0693238
kb_number: KB0693238
last_modified: 2026-04-09
---

## How to analyse Probe and Sensor wait and runtime using ECC Queue records and Excel

  

### Issue

Sometimes it is necessary to analyse a long running discovery schedule to work out where all the time goes. Or it may be useful to know which sensor jobs are particularly long running and risk blocking the instance's scheduler workers. This is a simple low-tech way of analysing Discovery probe and sensor processing time and backlog.  Look at Outputs for Probe MID Server wait and run times, and Inputs for instance sensor wait and run times.

This is based on the assumption that for ecc\_queue outputs:

-   Created - The time that the Probe is added to the ECC Queue
-   Processed - The time when the MID Server picked up the job. If the MID Server is busy, , this could be some time after Created. This doesn't necessarily mean when the MID Server started to execute the probe, as it may be held in an internal queue for a while.
-   Updated - The time the Input is returned to the ECC Queue.  That might have been queued as a temporary file in the ECCSender folder for some time after the probe finished executing, before being retirned to the instance.

This is based on the assumption that for ecc\_queue inputs:

-   Created - The time that the MID Server had finished running the probe and returned the input containing the result data to the instance ECC Queue
-   Processed - The time when the Discovery Sensor job started running for that input. If there is a scheduler worker backlog in the instance, this could be some time after Created.
-   Updated - The time the sensor processing had finished. This could be the same second as Processing, or some minutes or even hours later.

### Release

Any

### Resolution

1.  Open the ECC Queue table. **Discovery - ECC Queue**
2.  Ensure the following columns are in your list view, and **Personalize List View** to add them if necessary
    -   Created
    -   Updated
    -   Processed
    -   Name (probe name or command)
    -   and perhaps others such as Source (Target IP), State (Error/Processed), Topic (Probe type), Agent (MID)
3.  **Filter the table** down to a manageable number of records. 
    -   Start by showing only **Queue=Input** records. Or just Output ones.
    -   Perhaps filter for a **Created time** around the time you are interested in
    -   or where **Agent Correlator=<_sys\_id of your discovery\_status record for a particular schedule run_\>**
    -   or **Topic=SNMP** or some other kind of Discovery probe
4.  **Export the list as Excel** format. 
5.  Open in Excel and add 2 new columns - 'wait time' and 'run time' - and set the Cell Format as "Time". This will show the value in hours:minutes:seconds e.g. 00:00:02 is 2 seconds.
6.  Add a formula to subtract pairs of dates in the first data row of those new columns:
    -   Wait time: **\=<Processed value> - <Created value>**
    -   Run time: **\= <Updated value> - <Processed value>**
7.  Copy those formulae down all rows.
8.  You could then analyse the data in various ways:
    -   **Sort the sheet on the Run Time column** to identify the longest running sensors
    -   Sort on Wait Time to see the **longest time a sensor job had to wait before starting** when there was a free Scheduler Worker in which to execute it.
    -   Apply **Conditional Formatting** colours for a 'heat map'.
9.  You should have ended up with something like this, which is from a normal discovery of a few servers on a healthy instance:

![](sys_attachment.do?sys_id=8fd2bf4b938c4f14f538fb2d6cba103e)

Notes:

I used Microsoft Excel for this example, but other spreadsheet applications could be used, as the preadsheet features mentioned are common to all.

There may be some weird values seen in the calculations, perhaps if there were errors processing the sensor, which in itself tells you something.

This works well for Discovery and Service Mapping. For other features using MID Servers via the ECC Queue, not all sensors update the ecc\_queue input records and timestamps in the same way, and some may not even have sensons.
