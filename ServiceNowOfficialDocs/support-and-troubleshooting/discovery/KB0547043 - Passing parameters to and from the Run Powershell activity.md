---
title: "Passing parameters to and from the Run Powershell activity"
aliases:
  - KB0547043
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0547043
kb_number: KB0547043
last_modified: 2025-04-09
---

## Passing parameters to and from the Run Powershell activity

  

### Issue

In some cases you may need to:

-   Run a PowerShell script on the MID Server, or have the MID Server to run the script on a remote machine. 
-   Pass parameters to the PS script. 
-   Take the parameters that are passed to the PS script from the scratchpad, or even being computed from some input variables to the workflow. 

All these cases are discussed in this article with two simple workflow examples.

### Release

All

### Resolution

### Implement Workflow 1 - Setting parameters from the activity

1.  Go to **Orchestration > MID Server Properties** and make sure that the option **MID Server** contains the name of a valid MID Server.
2.  Create a new workflow and name it, for example, "Test PowerShell 1".
3.  Add a **Run Powershell** activity between **Start** and **End** (connect both **Success** and **Failure** outputs) with the next values:   
    -   Name: Test PS
    -   Hostname: (Machine where the command has to be run, localhost is ok for testing.)
    -   Command: `Write-Host "Updating user $user_name with id $user_id"`
    -   PowerShell script variables: `{"user_id": "1234", "user_name": "foo"}`
    -   Sensor script:
        
        doProcessResponse();
        **function** doProcessResponse() {
            workflow.scratchpad.midoutput = activity.output;
        }
        
4.  Add a **Run Script** activity between **Test PS** and **End** with the next values:  
    1.  Name: **Print scratchpad**
    2.  Script:  
        
        workflow.info("The MID Server returned: {0}", workflow.scratchpad.midoutput);
        
        Your Workflow should look like the following:
        
        Begin ==> Test PS ==> Print scratchpad ==> End
        

### Implement Workflow 2 - Setting parameters from values in the scratchpad

1.  Go to **Orchestration > MID Server Properties** and make sure that the option **MID Server** contains the name of a valid MID Server.
2.  Create a new workflow, name it, for example, "Test PowerShell 2".
3.  Add a **Run Script** activity between **Start** and **End** with the next values:  
    -   Name: Put values in Scratchpad
    -   Script:
        
        workflow.scratchpad.user\_id = "1234";  
        workflow.scratchpad.user\_name = "foo";
        
        **Note**: We are populating the scratchpad with some variables. You can compute these scratchpad variables based on values taken from workflow input variables, requested item variables, etc.
4.  Add a **Run Powershell** activity between **Put values in Scratchpad** and **End** (connect both **Success** and **Failure** outputs) with the next values:  
    -   Name: Test PS
    -   Hostname: (machine where the comand has to be run, localhost is ok for testing).
    -   Command: `Write-Host "Updating user $user_name with id $user_id"`
    -   PowerShell script variables: `{"encrypted:user_id": "${workflow.scratchpad.user_id}", "user_name": "${workflow.scratchpad.user_name}"}`
    -   Sensor script:
        
        doProcessResponse();  
        **function** doProcessResponse() {  
          workflow.scratchpad.midoutput = activity.output;  
        }
        
5.  Add a **Run Script** activity between **Test PS** and **End** with the next values:  
    -   Name: Print scratchpad
    -   Script: `workflow.info("The MID Server returned: {0}", workflow.scratchpad.midoutput);`  
        Your Workflow should look like:  
        
        Begin ==> Put values in Scrachpad ==> Test PS ==> Print scratchpad ==> End
        

### Run the Workflow

Now you can run this workflow from the Workflow Editor by clicking the green **\[->\]** on the title bar. 

You can also assign this workflow to a Catalog Item and make it run upon **Item order**.

### Check results

Once your Workflow has run, check how it worked by going to **Workflow > All Contexts**, and searching for your workflow there.

Select **Test PowerShell 1** (sort the list by date from newest to oldest and find your workflow at the top of the list).

Access the context and go to the related list **Workflow Log**. 

Observe there the entry with the message, _The MID Server returned: Updating user foo with id 1234_. 

Observe also the scratchpad in this context (you might need to add the scratchpad field to the form). 

-   The scratchpad for the first workflow would be: `{"midoutput":"Updating user foo with id 1234"}` 
-   The scratchpad for the second workflow would be: `{"midoutput":"Updating user foo with id 1234","user_id":"1234","user_name":"foo"}`

### Passing parameters to the PS script

In order to pass variables to the PS script you have to add a JSON formatted object containing your variables to the **PowerShell script variables** field of the **Run Powershell** activity. 

In the example we have used:

{
  "user\_id": "1234", 
  "user\_name": "foo"
}

You could pass other kinds of data, such as numbers, booleans, and other complex objects.

It is possible to have these parameters passed encrypted to the MID Server. For that, just pre-ped each variable name with **encrypted**:. In our example, we would encrypt the **user\_id** parameter with:

{
  "encrypted:user\_id": "1234", 
  "user\_name": "foo"
}

That results in the next parameters in the payload of the probe are sent to the MID Server:

**<parameter** name="powershell\_user\_id" value="QOtbi3Ftvks="/>
**<parameter** name="powershell\_param\_user\_name" value="foo"/>

### Taking values from the scratchpad

In order to take anything from the scratchpad you just need to use _Javascript expansion_:

${workflow.scratchpad.a\_variable}

You can use JS expansion in **String** activity fields. In this case, we can write our **PowerShell script variables** field like:

{
  "encrypted:user\_id": "${workflow.scratchpad.user\_id}", 
  "user\_name": "${workflow.scratchpad.user\_name}"
}
