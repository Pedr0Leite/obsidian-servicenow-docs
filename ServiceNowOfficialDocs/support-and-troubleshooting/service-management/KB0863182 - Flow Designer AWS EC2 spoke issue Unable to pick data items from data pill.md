---
title: "Flow Designer: AWS EC2 spoke issue: Unable to pick data items from data pill"
aliases:
  - KB0863182
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0863182
kb_number: KB0863182
last_modified: 2024-04-08
---

## Flow Designer: AWS EC2 spoke issue: Unable to pick data items from data pill

  

### Issue

# Amazon EC2 spoke

Integrate ServiceNow instance with Amazon Elastic Compute Cloud (EC2). Manage Amazon instances, Amazon Machine Images (AMIs), Key Pairs, and Tags from your ServiceNow instance.  

[Amazon EC2 Spoke](https://docs.servicenow.com/csh?topicname=amazon-ec2-spoke.html&version=latest "Amazon EC2 Spoke")

From this KB perspective , Amazon EC2 spoke use the Action "List Instances" to list the instances for a region and then using the Action "Stop Instances" , to stop the relevant instances by providing the "Instance ID" as an input to stop instance action

Trying to pull the value of the Instance ID variable from the output variables of "List Instances" action in flow designer but the variable "Instance ID" from the Data Picker in flow designer towards the right is grayed out. In fact the whole array and its all fields are grayed out and doesn't allow us to pull the instance id as inputs to stop instance action

**Sample Flow:**

![](/sys_attachment.do?sys_id=7f1af0cddbc034d016d2a345ca961991)

  

**List Action data pill structure for Ec2 spoke:**

![](/sys_attachment.do?sys_id=7b1af0cddbc034d016d2a345ca961994)

### Release

Paris

### Cause

We could get the results from list of instances action in the flow in the below format

Reservation Set - {  
"reservation\_set" : \[ {  
"imageId" : "ami-02354e95b39ca8dec",  
"instanceId" : "i-0cedd3f1defebd299",  
"instanceState" : {  
"name" : "stopped"  
},  
"instanceType" : "t2.micro",  
"ipAddress" : null,  
"monitoring" : {  
"state" : "disabled"  
},

From the results of list instance action , the instance id is present in Reservation set --> reservation set array as stated above. The instance id from list instance data pill in the right under flow designer, we could see the instance id object exists under Reservation set object 

Hierarchy of the list instance action design is Reservation set object --> Reservation set object  Array --> Reservation set object  --> Instance id , image id etc

The list instance action data pill in flow designer has Reservation set object followed by reservation set array, again an object and then the instance id object. The input for instance id under stop instances action is expecting an array object but the instance id in list instance data pill design is under Reservation set normal object and hence we cannot pull the instance id from list instance action data pill as an input to the stop instance action

### Resolution

In the list instances result , we have "Reservation Sets"(type object) => "Reservation Set(Type Array)" => "Instance ID". "Reservation set" is type of array. If we need to use "Instance ID" as an input to stop action from the results of list action , use " For loop" and place the stop action inside the for loop. 

Here is the screenshot 

![](/sys_attachment.do?sys_id=f31af0cddbc034d016d2a345ca961993)

This will read the instance id from the "For loop" results and stop the instances accordingly.
