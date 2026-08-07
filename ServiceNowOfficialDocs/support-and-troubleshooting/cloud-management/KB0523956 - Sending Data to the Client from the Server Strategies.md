---
title: "Sending Data to the Client from the Server | Strategies"
aliases:
  - KB0523956
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0523956
kb_number: KB0523956
last_modified: 2025-06-16
---

## Issue

Client side scripts have access, through the g\_form.getValue() method to the value of all fields on a form.  For some client side scripting, access to data that is not on the form is necessary.

### Detailed Explanation

There are a number of strategies for getting data from the client side to the server:

-   Add a field to the form and then hide the field
-   Use a g\_form.getReference() method call
-   Use a Display Business Rule
-   Use a Script Include

 Which strategy is best?  Well...it depends.

### Steps to Implement

**Adding/Hiding a Field**

A classic strategy is to add a field to a form and then hide it.  This strategy allows access to data without making a round-trip server call after a form loads.  Only fields from the form's table or from records related to the table can be added.  The drawback to this strategy is that  form load times increase if a form is heavily loaded with hidden fields.  On slow networks, users will see the entire form as it loads, including hidden fields.  After the form load is complete, the onLoad(), on Change() (depending on the script), and onLoad UI Policies execute.  As the client side scripts execute, the fields start to disappear from the form in full view of the person awaiting the form load.  The disappearing form fields and long load times can lead to a poor user experience. 

![](/HiddenField2.jpgx "Hiding a field with a UI Policy")

The UI Policy Action hides the Locked out field on the Incident form.  Although the user can't see the field, the field and its value are available for scripting.

**g\_form.getReference()**

The g\_form.getReference() method allows a scripter to request data from the server after a form loads.  Unlike the previous strategy, this strategy has no impact on form load times.  There is, however, a performance penalty due to the time it takes the request to go to the server and bring data back to the client.  The performance penalty is mitigatable by making the method call asynchronous through the use of a callback function.  (See Knowledge article https://support.servicenow.com/kb\_view.do?sysparm\_article=KB0523744&sysparm\_nameofstack=&sysparm\_kb\_search\_table=).  Scripters can request fields and values from the form's related tables.

![](/getRefClientScript.jpgx "A g_form.getReference() Client Script retrieving caller's locked out state")

This onChange Client Script retrieves an Incident's Caller's record from the database and takes action based on the value of the locked\_out property of the returned callerRec object.  Any time the value of the Caller field on the form changes the script logic is executed again.  
  

**Display Business Rules**

Display Business Rules use the g\_scratchpad object to pass data from the server to the client when a form loads.  Display Rules execute before control of a form is given to a user. 

The g\_scratchpad object has no properties when instantiated;  display Business Rules must populate the g\_scratchpad object wtih property/value pairs:

-   Fields from the requested record that are not on the form
-   Fields from related records
-   Fields from any record in the db
-   Hardcoded values

In this Display Business Rule the current record's caller's locked\_out field and its value are passed in the g\_scratchpad object as the lockedOut property:

![](/DisplayBR.jpgx "Display Business Rule passing a caller's locked_out state in the g_scratchpad object")

Any client side script can use the g\_scratchpad object's properties and values:

![](/ClientScriptScratchpad.jpgx "Using the g_scratchpad object in a Client Script")

Display Business Rules only execute when a form loads so if the data to be passed is dependent on a field on the form, you may or may not be able to use this strategy.  For example, for a new Incident, the Caller field has no value.  In this case no data related to the Caller record could be passed.

**Script Include**

Client Callable Script Includes that extend the AbstractAjaxProcessor class can be called at any time from any client side script.  Although extending a class is the choice with the most work for the scripter, it allows access to the full server side API for gathering information to return to the client.  In this example we are passing a single value, either true or false, but any number of values could be passed back through the use of a JSON object or a character delimited string.  Script Includes execute asynchronously to insure a good user experience.

The Script Include to return the locked\_out field's value using a passed in sys\_id identifying a User record:

![](/AJAXScriptInclude.jpgx "A Scripti Include to return a caller's locked_out field value")

 A Client Script that calls the Script Include and processes the returned value:

![](/ClientSideScriptInclude.jpgx "Client Script calling a Script Include and processing returned value")

## Resolution

Strategies to Remember

Strategy 1:  Adding a field to a form and hiding it:

\+ Easy to do  
\- Field must be from the form's table or a related table  
\- Can impact form load time and therefore the user experience  
\- Users may see field before UI Policy or Client Script hides it

Strategy 2:  g\_form.getReference()

\+ When executed asynchronously has minimal impact on the user experience  
\- When used synchronously negatively impacts the user experience  
\- Can only reference fields from a form's related tables

Strategy 3:  Display Business Rule

\+ Executed on form load and before control given to user (minimal load time impact, good user experience)  
\+ g\_scratchpad objects populated on the server side and can be from any table's fields or hardcoded  
\+ Has full access to the DB and server side API  
\- Can't always know in advance what record's data to pass (ie - a related field telling which record to use to populate g\_scratchpad has no value)  
\- Only executes on form load so cannot respond when form field values change

Strategy 4:  Script Include

\+ Callable from any script at any time  
\+ Executes asynchronously  
\+ Has full access to the DB and server side API  
\- More work for the scripter
