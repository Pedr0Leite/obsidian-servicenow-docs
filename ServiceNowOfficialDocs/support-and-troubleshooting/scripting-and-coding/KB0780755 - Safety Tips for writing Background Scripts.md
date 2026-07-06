---
title: "Safety Tips for writing Background Scripts"
aliases:
  - KB0780755
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0780755
kb_number: KB0780755
last_modified: 2026-04-20
---

## Safety Tips for writing Background Scripts

  

### Summary

The aim of this article is to increase knowledge in order to make doing changes safer, and spotting potentially problematic scripts easier but is all general information that would apply to any ServiceNow user doing scripting.

### Release

Any

### Instructions

## Table of Contents

-   [When might Technical Support write a script?](#mcetoc_1glp1cerl1vm)
    -   [Rule #1: Technical Support doesn't write code for customers](#mcetoc_1glp1cerl1vn)
    -   [If our bug broke customer's data, we should help clean it up](#mcetoc_1glp1cerl1vo)
    -   [Adding Debugging code, when we think may have a Problem](#mcetoc_1glp1cerl1vp)
    -   [Would writing a custom script be the most efficient solution?](#mcetoc_1glp1cerl1vq)
-   [The Trouble with .get() and .update()](#mcetoc_1glp1cerl1vr)
    -   [.get() may not actually get a record at all](#mcetoc_1glp1cerl1vs)
    -   [.get() may get more than 1 record](#mcetoc_1glp1cerl1vt)
    -   [.update() may actually insert a new record](#mcetoc_1glp1cerl1vu)
-   [Example: A custom Business Rule running on the insert of a CI Relationship record, to update a field of the Parent CI](#mcetoc_1glp1cerl1vv)
-   [Querying and using if and .next() instead](#mcetoc_1glp1cerl200)
    -   [Lessons learned:](#mcetoc_1glp1cerl201)
-   [Looping through records, using addEncodedQuery and while loop](#mcetoc_1glp1cerl202)
    -   [Bad example:](#mcetoc_1glp1cerl203)
    -   [Better example:](#mcetoc_1glp1cerl204)
-   [deleteRecord() and updateMultiple()/deleteMultiple(), and Cascade Delete](#mcetoc_1glp1cerl205)
-   [setWorkflow() and autoSysFields()](#mcetoc_1glp1cerl206)
    -   [setWorkflow(false);](#mcetoc_1glp1cerl207)
    -   [autoSysFields(false);](#mcetoc_1glp1cerl208)
-   ['false' means true](#mcetoc_1glp1cerl209)
-   [gs.log() and the Source parameter](#mcetoc_1glp1cerl20a)
-   [Thread dump and exact Timestamps](#mcetoc_1glp1cerl20b)
    -   [Example use case:](#mcetoc_1glp1cerl20c)
    -   [GlideLog.getStackTrace(new Packages.java.lang.Throwable())](#mcetoc_1glp1cerl20d)
-   [Run in the Correct Scope](#mcetoc_1glp1cerl20e)
-   [Run as a scheduled script, splitting the data sets, and limit()](#mcetoc_1glp1cerl20f)
    -   [Use .limit(n) to restrict the query to n records at a time, and then run the script several times.](#mcetoc_1glp1cerl20g)
    -   [Speed the job up by running multiple threads at once.](#mcetoc_1glp1cerl20h)
-   [Example of running a UI Action or Business Rule as a standalone script](#mcetoc_1glp1cerl20i)

## When might Technical Support write a script?

### Rule #1: Technical Support doesn't write code for customers

-   Technical Support doesn't write functional code for Customers. If there is a requirement to enhance, modify or change the existing designed behaviour of the out-of-box features, then that is a job for our Developers as part of a planned feature enhancement in which case it will then become supported code for all customers, or a Customer-specific Implementation perhaps with the involvement of a Partner or Professional Services, which would not be supported code.
-   Support won't customize an Out-of-the-box script for a customer unless it's a Problem workaround, and in that case, we will aim to make sure it is captured in an updated set, and clear instructions are given about reverting it after the fix release.
-   Support will try to identify if an issue with an out-of-box feature is caused by code in a custom script, but will not be responsible for fixing that custom script.
-   Support may correct custom scripts for customers if it is very simple, such as a logical or syntax error in a single line, and they will also aim to explain the best practices and why the customisation breaks things so that Customers know not to do it again.
-   For "how can I do something" questions, Support may give general steps or pseudo-code if we have a good solution idea, but will be clear that implementing the idea is the responsibility of the customer, perhaps with the help of an implementation Partner or Professional Services, who may actually have a better idea.
-   Support will also point out anything found that is not supported or recommended, that it is likely to break things after upgrades, or is going to need maintenance. Services can help with that work, which is normal once a customer takes ownership of our code or adds their own code alongside it.

### If our bug broke customer's data, we should help clean it up

Examples where a script may need writing by Technical Support for running on the Customer instance would be:

-   A Problem in Normalization Data Services caused loads of duplicate Model records to be created, requiring CIs to be pointed back to the original model, and the duplicate models to be deleted.
-   A Problem in CMDB Table-per-partition (TPP) Migration caused loads of duplicate CIs to be created after the upgrade, due to existing records not being seen by identification queries. Help would be required to identify and delete the duplicate CIs.
-   A Problem left loads of orphaned IP Address CI records with no parent Network Interface (NIC) record.
-   An undocumented Problem Fix added extra Model Category records, causing many unwanted Asset records to be created. Those would need unlinking from the CI, and the Assets deleted without causing the CI to be cascade deleted.

### Adding Debugging code, when we think may have a Problem

Examples would be:

-   Adding gs.log() statements for finding answers to questions such as:  
    -   Did we get to this line?
    -   What was a variable value at this point?
    -   Was it this update() that changed the value?
-   Commenting lines to see if we avoid the error, or get a different one.
-   Making corrections to see if we have identified the bug in the code

### Would writing a custom script be the most efficient solution?

-   How many records are involved?
-   Could it be fixed manually with a couple of hours of work instead?
-   Am I confident that I can write a script myself to do this?
-   Would Development or Support experts need to get involved?
-   Am I digging a hole for myself? See diagram:-

![Automation - writing a custom script](sys_attachment.do?sys_id=eb8058c2477cee1030fba325126d4396)

## The Trouble with .get() and .update()

[GlideRecord API](https://docs.servicenow.com/csh?topicname=c_GlideRecordAPI.html&version=latest "GlideRecord API"):

![The Trouble with .get() and .update()](sys_attachment.do?sys_id=ef8058c2477cee1030fba325126d4398)

![The Trouble with .get() and .update()](sys_attachment.do?sys_id=a78058c2477cee1030fba325126d43c6)

The scary things are:

### .get() may not actually get a record at all

If your script then uses values from that record in later code or queries, then you may be using 'null' (or 'undefined' or whatever non-sys\_id string value was used) rather than the value you assumed you had. 

### .get() may get more than 1 record

If your script assumes a single record is got, then you may end up doing something unexpected to records you were not intending to touch.

It is possible the whole table is returned, which also has app node memory implications.

### .update() may actually insert a new record

If the .get() didn't get a record, or if you dot-walk to a record via a broken reference, then the GlideRecord will still be initialized.

The common warning in the node logs for "Get for non-existent record: ...., initializing " shows this bad situation has occurred.

If your script carries on regardless, without checking and updating that gliderecord, an insert will happen.

## Example: A custom Business Rule running on the insert of a CI Relationship record, to update a field of the Parent CI

var parentGr = new GlideRecord('cmdb\_ci');  
parentGr**.get**(current.parent.sys\_id.toString());  
parentGr.u\_has\_relationship = true;  
parentGr**.update()**;

That has been written on the assumption that for a relationship record to exist, surely both the parent and child CI must already exit.

That assumption is false, because the cmdb\_rel\_ci record may have been inserted by the Discovery "Virtual Computer Check" Business Rule, which runs before the insert of the Parent Computer CI.

This will cause a premature Insert of the parent computer CI when .update() is called, with blank values in all the CI fields. When the 'real' insert happens, after all before insert business rules have been completed, it will fail due to the sys\_id already having been inserted.

This would be slightly better, by testing the .get() did return true.

var parentGr = new GlideRecord('cmdb\_ci');  
**if (parentGr.get**(current.parent.sys\_id.toString())) {  
  parentGr.u\_has\_relationship = true;  
  parentGr.update();  
}

But that's still not foolproof, as we may return more than one record. With a null value, it can return the whole table.

Note: The use of ".sys\_id.toString()" is also a good idea. JavaScript is supposed to be able to automatically type-cast between different object types but sometimes doesn't get it right. Doing the type conversions yourself is safer. .get() requires a string, and without this you are actually giving the method a GlideElement object of the reference field or sys\_id field.

## Querying and using if and .next() instead

This approach is even safer. We do a .query() instead of a .get(). We then use .next() to get the record. We can also use getRowCount() to check the record count is 1 before doing anything.

var parentGr = new GlideRecord('cmdb\_ci');  
parentGr.addQuery('sys\_id', current.parent.sys\_id.toString());  
parentGr.query();  
**if (parentGr.next() && parentGr.getRowCount()==1) {**  
  parentGr.u\_has\_relationship = true;  
  parentGr.update();  
}

### Lessons learned:

You may be using a broken reference value, or even a null if the previous code hasn't correctly set up the value first, so:

1.  Never use .get() without checking the result is True.
2.  It is a lot safer to use a query followed by if next.
3.  Count the records returned by the query

## Looping through records, using addEncodedQuery and while loop

Let's pretend we have a requirement to set all Computer class CIs as Retired if the most recent discovery date is longer ago than 3 months. These 8 records:

![Looping through records, using addEncodedQuery and while loop](/sys_attachment.do?sys_id=a78058c2477cee1030fba325126d43c2)

We could write this script to do it:

var gr = new GlideRecord('cmdb\_ci\_computer');
gr.query();
while (gr.next()) {
  if (gr.last\_discovered < '2019-04-19') {
  gr.hardware\_status = 'retired';
  gr.update();
  }  
}

### Bad example:

At least 7 things are badly wrong with that:

-   CMDB is an extended table. We are including all child tables of the Computer, including the Server, etc. in this query.
-   We are looping more records than necessary. We are holding in memory the GlideRecord object records we are not going to be updating.
-   We are updating records that may already be Retired, without first checking if they are already Retired
-   We are assuming last\_discovered has a value, but this would include all CIs without values too.
-   By the time we run this, 3 months ago may be a different date.
-   'gr' is not a safe variable name, especially when we have not wrapped this script in a function – see [KB0713029](https://hi.service-now.com/kb_view.do?sysparm_article=KB0713029) 
-   Powerpoint has messed up the apostrophes.

### Better example:

We can address all the above points by adding them to our list filter. Then use addEncodedQuery() with the same table/query string as the list, and you can safely loop through exactly the same records as the list. Not only the 8 records we are going to update will be in the GlideRecord object after the query(), making this quicker and use less memory.

var ciGr = new GlideRecord('cmdb\_ci\_computer');
ciGr.addEncodedQuery('last\_discovered<javascript:gs.beginningoflast3months()^hardware\_status!=retired^sys\_class\_name=cmdb\_ci\_computer^last\_discoveredisnotempty');  
cigr.query();  
while (cigr.next()) {  
   cigr.hardware\_status='retired';  
   cigr.update();  
}

## deleteRecord() and updateMultiple()/deleteMultiple(), and Cascade Delete

var ciGr = new GlideRecord('cmdb\_ci\_computer');  
ciGr.addEncodedQuery('<whatever>');  
ciGr.query();  
**while (ciGr.next()) {**  
  **ciGr.deleteRecord();**   // not .delete() as you might expect, given update() and insert()!  
}

Is equivalent to:

var ciGr = new GlideRecord('cmdb\_ci\_computer');  
ciGr.addEncodedQuery('<whatever>');  
**ciGr.deleteMultiple();  
**

**Note1:** .query() is not used with deleteMultiple(), or updateMultiple(), but don't forget to use .query(); when you do need to use it, or you still have the whole unfiltered table in your glideRecord object.

**Note2:** do not use deleteMultiple() or updateMultiple() inside a loop of the same GlideRecord with .next() iteration. Both deleteMultiple() and updateMultiple() are not designed to work with an iterating GlideRecord, and will cause **data loss or data corruption**.

var ciGr = new GlideRecord('cmdb\_ci\_computer');  
ciGr.addEncodedQuery('<whatever>');  
ciGr.query();  
**while (ciGr.next()) {**  
  **ciGr.deleteMultiple();**   // DON'T DO THIS!  
  **ciGr.updateMultiple();**   // DON'T DO THIS!  
}

Don't forget that both will cause a Cascade Delete, deleting all child records, and clearing reference values from other records. For a CI that may be all the NICs, Disks, Memory, Serial Numbers, and the linked Asset, plus all that's child records like Costs Lines, plus anything that references it like Affected CIs in Tasks like Incidents and Problems.

Cascade delete happens by looking for any other records that might reference the CI being deleted. Every field referencing the CMDB should have an Index. Deletes can be very slow if there is a missing index, with a huge proportion of the time could be spent checking a rarely used table that doesn't even have any relevant records. If the delete is slow, check for slow SELECT queries.

## setWorkflow() and autoSysFields()

Business rules and Engines will run for operations done in scripts, just like any other insert/update/delete.

Those could do unexpected things and very slow things.

e.g. CI-Asset Synchronisation will run, and so Assets and their parents/children will also be involved.

### setWorkflow(false);

Disables the running of business rules that might normally be triggered by subsequent actions.

Workflow Engine, and I believe all other engines, will not run. 

Also turns off auditing.

### autoSysFields(false);

Disables the update to the fields sys\_updated\_by, sys\_updated\_on, sys\_mod\_count, sys\_created\_by, and sys\_created\_on.

But just for the subsequent action! Just this script's next .update/delete.

#### Example:

var ciGr = new GlideRecord('cmdb\_ci\_computer');  
ciGr.addEncodedQuery('<whatever>');  
ciGr.query();  
while (ciGr.next()) {  
  **ciGr.setWorkflow(false);**  
  **ciGr.autoSysFields(false);**  
  ciGr.deleteRecord();  
}  
  
Notes:

-   Can't be used with deleteMultiple()
-   Will still cascade delete and run BRs for those extra updates/deletes.
-   Won't have any effect if sys\_class\_name is changed at the same time – see [KB0727652 What happens when you update an Extended Table record to change the Class?](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727652)

## 'false' means true

'false' is just a string value. type cast it to boolean and you get true, not false. Use the correct data types, and don't assume Javascript will end up with what you were expecting after automatically type casting.

-   .setWorkflow(false); turns OFF running engines on the next operation.
-   .setWorkflow('false'); **turns ON** running engines on the next operation.

At least 30 support cases, some quite serious, have been caused by this mistake, and that's just for setWorkflow().

## gs.log() and the Source parameter

gs.log() has a 2nd parameter for the 'source'.

while (ciGr.next()) {  
  gs.log('Deleting cmdb\_ci:' + ciGr.sys\_id, '**CS1234567'**);  
  ciGr.deleteRecord();  
}

/syslog\_list.do can then be filtered on source=CS1234567

For a scoped app, gs.log can't be used. gs.info(), gs.error(), gs.debug() can be used instead, but those don't have the 2nd parameter

## Thread dump and exact Timestamps

Adding gs.log() statements to several Sensors and Script Includes is often useful, but created times in syslog are only to 1 second, so the sequence is confused.

getTime() will return the milliseconds since 1970, so include that in you message:

gs.log(**'Now:' + new Date().getTime()** + 'Deleting CI: ' + ciGr.sys\_id, 'INT1234567');

I then export syslog to Excel, and sort by the timestamp.

You can extract the timestamp after "Now:" with this excel formula:  
\=MID(C2,FIND("Now:",C2)+4 ,13)

### Example use case:

Example of debugging MID Server Heartbeat. Log statements were added to the Sensor BR, and 5m scheduled job.

![](/sys_attachment.do?sys_id=e78058c2477cee1030fba325126d4394)

This ended up giving the proof that 2 app nodes must have system clocks that were out of sync. The input from the heartbeat probe arrives before it was sent, which is impossible if everything is using the same clock.

### GlideLog.getStackTrace(new Packages.java.lang.Throwable())

/threads.do will list the thread dump for all threads on the app node.

You can generate a similar thread dump for a thread as it runs on demand, and include it in a gs.log, from any script, such as Business Rule or Script include.

gs.log('Now:' + new Date().getTime() + 'Stack Trace:\\n '  
   + **GlideLog.getStackTrace(new Packages.java.lang.Throwable())**,   
   'INT1234567');

Great for answering questions like "What code is deleting the network adapters during a discovery run?"

A new Before Delete business rule for table cmdb\_ci network\_adapter can simply gs.log a stack trace.

Working back down the stack trace, you can see the .delete(), and the lines below that is what's doing the delete.

A script that works for scoped apps is also available in: [KB0683765 Troubleshooting tip - Debug business rule to print StackTrace](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0683765)

## Run in the Correct Scope

When running from the Scripts - Background page (/sys.scripts.do), you may have got into the habit of assuming it runs in Global scope, because that has always been the scope that had been selected by default.

This is often no longer true as new apps with scope names earlier in the alphabet get added, so be careful to switch the scope to Global, or the one you know you need to be running the script in.

![Run in the Correct Scope - Global Scope](/sys_attachment.do?sys_id=a78058c2477cee1030fba325126d43c8)

## Run as a scheduled script, splitting the data sets, and limit()

Data Fix scripts that Support writing for customers can run for a long time or timeout.

-   Run the script as a Scheduled Script (/sysauto\_script.do)
-   Run=On Demand, and Execute Now.
-   Scheduled to run later out-of-hours
-   Customers can run it themselves after we set it up, so Support doesn't need the added delay of a Normal Change in HI.

### Use .limit(n) to restrict the query to n records at a time, and then run the script several times.

var ciGr = new GlideRecord('cmdb\_ci\_computer');  
ciGr.addEncodedQuery('<whatever>');  
ciGr.limit(1000);  
ciGr.query();  
ciGr.deleteMultiple();

-   Only the first 1000 results of the query will be included.
-   Good for testing on a subset to then allow estimating total runtime
-   Good for confirming the script works!
-   to see if anything unexpected happened, check Rollback context, and deleted records as things may have been updated/cascade deleted in the process. e.g. linked Assets, Affected CIs on Changes etc.

### Speed the job up by running multiple threads at once.

-   The Database is a lot quicker than the App Node -> The bottleneck is the scheduler worker thread.
-   Often 4 or more CMDB update/delete scripts can be run in parallel before you start seeing database replication lag
-   e.g. set up 16 scheduled scripts. Run a few to begin with, and after reviewing database performance, start more.

Script 1 of 16

var ciGr = new GlideRecord('cmdb\_ci\_computer');  
ciGr.addQuery**('sys\_id',''STARTSWITH,'0');**  
ciGr.query();  
ciGr.deleteMultiple();

Script 16 of 16

var ciGr = new GlideRecord('cmdb\_ci\_computer');  
ciGr.addQuery**('sys\_id',''STARTSWITH,'f');**  
ciGr.query();  
ciGr.deleteMultiple(); 

## Example of running a UI Action or Business Rule as a standalone script

"Get MID thread dump" UI Action

var agent\_name = current.name.replace(/'/g, "\\\\'");  
var midmanage = new MIDServerManage();  
midmanage.threaddump(agent\_name);  
action.setRedirectURL(current);

-   'current' is a GlideRecord of the MID Server record, so ecc\_agent table, and whatever sys\_id this MID Server is.
-   If this had been a BR, current would be whatever record it was running for.
-   We don't care about the redirect line, which just tells the UI what to load next

We don't have 'current', so get() the record instead:

var midGr = new GlideRecord('ecc\_agent');  
if (midGr.get('d55a7c2fdb813300e1943ecf9d961964')) {  
  var agent\_name = midGr.name.replace(/'/g, "\\\\'");  
  var midmanage = new MIDServerManage();  
  midmanage.threaddump(agent\_name);  
}

And why not do it for all 'Up' MID Servers?

var midGr = new GlideRecord('ecc\_agent');  
midGr.addEncodedQuery('status=Up');  
midGr.query();  
while (midGr.next()) {  
  var agent\_name = midGr.name.replace(/'/g, "\\\\'");  
  var midmanage = new MIDServerManage();  
  midmanage.threaddump(agent\_name);  
} 

And then wrap it in a scheduled job...

![Example of running a UI Action or Business Rule as a standalone script](/sys_attachment.do?sys_id=a78058c2477cee1030fba325126d43c4)

We could come back to this MID server tomorrow and see from the wrapper log exactly what line of code each thread was running, every 10 minutes through the night.

That could identify what long-running threads were doing, what threads were running during High CPU/memory periods, and which lines of code or loops they were in.

### Related Links

What's the scripted equivalent of something like:

SELECT name, COUNT(name) AS NumOccurrences FROM cmdb GROUP BY name HAVING ( COUNT(name) > 1 ) ORDER BY NumOccurrences DESC;

Answer: [GlideAggregate](https://docs.servicenow.com/csh?topicname=c_GlideAggregateAPI.html&version=latest "GlideAggregate")

See [KB0744490](https://hi.service-now.com/kb_view.do?sysparm_article=KB0744490) - "Deleting duplicate records from any table" (login required).
