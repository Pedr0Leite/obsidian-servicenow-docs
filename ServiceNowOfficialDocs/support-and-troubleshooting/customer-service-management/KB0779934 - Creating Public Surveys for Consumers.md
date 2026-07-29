---
title: "Creating Public Surveys for Consumers"
aliases:
  - KB0779934
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0779934
kb_number: KB0779934
last_modified: 2025-09-08
---

## Creating Public Surveys for Consumers

  

In CSM, there are two types of consumer tables:

-   csm\_consumer\_user: this table is extended from sys\_user and stores the registered consumer records.
-   csm\_consumer: this table is NOT extended from sys\_user table and stores the unregistered consumers.

The **Consumer** field on the Case table references the csm\_consumer table, which enables agents to create cases for unregistered users too.

In the B2C use case, there are times when you want to send surveys to your consumers to get feedback on the type of the service they received once their cases are closed or resolved.

Non-public surveys in ServiceNow have a known limitation where the trigger condition’s **User** field can only be set to a table or a reference table that references the sys\_user table. Due to this limitation, survey records do not get created for the records in the csm\_consumer table because the csm\_consumer table does not extend from sys\_user and consumers do not have any access to the instance.

There are two options for sending surveys to non-registered consumers: public surveys and non-public surveys. These options are discussed below. 

**_Option 1: Public Surveys_**

Make your survey accessible to the public by clicking the **Enable Public Access** UI action, which makes the survey available to users who are not logged in to the instance. This option generates a static URL that can be sent from a Flow Designer or email notification based on the conditions that trigger the survey. The static URL can be appended with the following two parameters which link the survey to the Case record that triggered the email.

-   sysparm\_trigger\_table: the Case Table (sn\_customerservice\_case)
-   sysparm\_trigger\_id: the sysId of the record that triggered the flow/email notification. 

These parameters populate the **Trigger Id** reference field with the correct data on the survey instance which can then be used for reporting or analysis purpose.

**Note:** Set the **Allow survey link from email to open in service portal view (applies only for surveys)** property value to false to disable survey records from opening in Service Portal.

**_Option 2: Non-public Surveys_**

If you do not want to make the survey public, then the consumer must be registered and assigned the appropriate roles (sn\_customerservice.consumer). Before your trigger point for the survey in the business rule, do the following:

1.  Copy the record from the csm\_consumer table to the csm\_consumer\_user table.
2.  Add the corresponding reference to this new record back on the csm\_consumer table’s **User** field to use the existing trigger condition.

Example:

function onAfter(){  
  var consumer = new GlideRecord('csm\_consumer');  
  consumer.get(current.consumer);  
  var gr = new GlideRecord("csm\_consumer\_user");  
  gr.initialize();  
  if(gs.nil(consumer.getValue('user'))){  
    gr.first\_name = consumer.first\_name;  
    gr.last\_name = consumer.last\_name;  
    gr.email = consumer.email;  
    gr.user\_name = consumer.email;  
    var user = gr.insert();  
    consumer.user = user;  
    consumer.update();  
  }  
            
  (new sn\_assessment\_core.AssessmentCreation()).conditionTrigger(current, 'a491d4f1c311220071d07bfaa2d3ae85');  
  
 }

**Note:** Because the csm\_consumer\_user table is an extension of the sys\_user table, it is recommended that you do not overload it with user data that will be used only once. In such cases, set up a scheduled job to clear out these records that were created just for the surveys.
