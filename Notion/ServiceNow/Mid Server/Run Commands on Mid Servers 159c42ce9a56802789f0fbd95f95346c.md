---
aliases:
  - "Run Commands on Mid Servers"
area: "Mid Server"
source: notion-export
tags:
  - mid-server
  - ecc-queue
  - shell-commands
---

# Run Commands on Mid Servers

# Command Line Execution with ServiceNow MID Servers

![](https://john-james-andersen.com/wp-content/uploads/Shell1.png)

A little known fact about ServiceNow and MID Servers is that 
ServiceNow can be configured such that it can execute shell commands on a
 computer that hosts a MID Server.  Of course, it will only execute 
commands that it has rights to execute as the user running the MID 
Server process, but this can be very handy with command line 
integrations.

In order to have a MID Server execute a shell command, simply create a
 record on the ECC Queue that has the following information:

> Agent: YOUR MID SERVER
> 
> 
> **Topic**: Command
> 
> **Name (optional):** THE COMMAND YOU WISH TO EXECUTE
> 
> **Queue**: Output
> 
> **Payload (optional)**: An XML document defining a command to execute.
> 

There are two ways to do this: the name method and the payload 
method.  With the “Name” method, you place your command in the “Name” 
field fo the ECC Queue record in the format that you normally would on a
 Shell prompt.  With the “Payload” method, you encapsulate the command 
in an XML document for the MID Server to process.

The advantage of the “Name” method is that it is easy to enter and 
very readable.  The advantage of the “Payload” method is that you may 
need longer command strings than the name field can support (eg. 120 
characters).  The Payload field can handle a much larger command.

# The Name Method

The following record will execute a directory listing with the “-l” option for the working directory of the MID Server:

![](https://john-james-andersen.com/wp-content/uploads/shell2.png)

Once this executes, a corresponding Input record will be generated:

![](https://john-james-andersen.com/wp-content/uploads/shell3.png)

If you open that record and read the Payload field, you will find the results to me “ls -l” query:

| <?xml version="1.0" encoding="UTF-8"?><results probe_time="2165">
  <result command="ls -l">
    <stdout>total 52
drwxr-xr-x 2 john john 4096 Mar 28 11:11 bin
drwxr-xr-x 2 john john 4096 Mar  6 11:25 conf
-rwxr-xr-x 1 john john 5715 Mar 28 11:11 config.xml
drwxr-xr-x 2 john john 4096 Mar  6 11:25 etc
drwxr-xr-x 2 john john 4096 Mar  6 11:32 extlib
drwxr-xr-x 8 john john 4096 Mar  6 11:25 jre6
drwxr-xr-x 2 john john 4096 Mar  6 11:25 lib
drwxr-xr-x 2 john john 4096 Mar  6 11:33 logs
drwxr-xr-x 2 john john 4096 Mar  6 11:25 properties
-rwxr-xr-x 1 john john   16 Jan 16 14:38 start.sh
-rwxr-xr-x 1 john john   15 Jan 16 14:38 stop.sh
drwxr-xr-x 4 john john 4096 Mar  6 11:33 work</stdout>
    <stderr/>
  </result>
  <parameters>
    <parameter name="topic" value="Command"/>
    <parameter name="queue" value="output"/>
    <parameter name="error" value=""/>
    <parameter name="from_sys_id" value=""/>
    <parameter name="sys_id" value="bc7e5b29508520006d4913147419ba01"/>
    <parameter name="state" value="ready"/>
    <parameter name="from_host" value=""/>
    <parameter name="agent" value="mid.server.DEB1"/>
    <parameter name="processed" value=""/>
    <parameter name="ecc_queue" value="bc7e5b29508520006d4913147419ba01"/>
    <parameter name="response_to" value=""/>
    <parameter name="source" value=""/>
    <parameter name="sequence" value="1365a5ab1950000001"/>
    <parameter name="name" value="ls -l"/>
    <parameter name="table_name" value="ecc_queue"/>
    <parameter name="agent_correlator" value=""/>
  </parameters></results> |
| --- |

# The “Payload” Method

The payload method will yield the same results as the “Name” method, 
but the difference is in the creation of the initial output ecc queue 
record.

Instead of placing the command in the “Name” field of the ECC Queue 
record we make up a small XML Document and place it in the Payload 
field.

In this example, we want to see what files within the MID Server installation have changed today:

find /home/john/mid/deb1 -type f -mtime -1 -exec ls -al {} \;

To do this using the Payload method, we create an ECC Queue record that looks like:

![](https://john-james-andersen.com/wp-content/uploads/Shell4.png)

The payload as shown in the screenshot is:

| <parameters>
  <parameter name="name" value="find /home/john/mid/deb1 -type f -mtime -1 -exec ls -al {} \;"/></parameters> |
| --- |

The resulting record will be in the same format as using the Name method, so I won’t display it here.

## Related

- [[Mid Server]]
- [[Installation]]
- [[How to import a CSV file from a Mid Server]]
- [[How the ECC Queue table records get processed from]]