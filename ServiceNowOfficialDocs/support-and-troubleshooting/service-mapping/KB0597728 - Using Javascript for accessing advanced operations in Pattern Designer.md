---
title: "Using Javascript for accessing advanced operations in Pattern Designer"
aliases:
  - KB0597728
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0597728
kb_number: KB0597728
last_modified: 2024-09-03
---

## Using Javascript for accessing advanced operations in Pattern Designer

  

### Issue

Using Javascript for accessing advanced operations in Pattern Designer | Optional 

Overview

* * *

This article is relevant for the Geneva and later releases.

You can [create or customize patterns](https://docs.servicenow.com/csh?topicname=c_MappingPatternsCustomization.html&version=latest "create or customize patterns") using Pattern Designer. The Pattern Designer user interface allows you to use only predefined operations. However, you can also use Javascript to use advanced operations that are not part of the Pattern Designer UI. Insert Javascript to access predefined context (CTX) objects to run commands, retrieve attributes values, or set attribute values. This feature is available for the Set variable and Transform table operations.

<table class="noteTable" align="left"><tbody><tr><td style="text-align: center;"><img title="Note" src="/Note_25x.pngx" alt="" align="baseline" border="" hspace="" vspace=""></td><td style="text-align: left;"><strong>Note</strong>:&nbsp;<span style="text-align: start;">Use Javascript in Pattern Designer&nbsp;only if you are an advanced user with programming experience</span>.</td></tr></tbody></table>

Execution context methods

* * *

There are several execution methods of the CTX objects in Pattern Designer:

-   **getCommandManager():** This method returns a Command Manager object (see details on this object below).
-   **getAttribute(name):** This method uses the attribute name as its input and returns its value. If the attribute is scalar, it returns an object of String type. If it is a table, it returns a Java object of the List type <Map<String,String>. Each object in the List is a row in the table. Each row is Map<String,String>, where the key is the column name and the value is the field value.
-   **setAttribute(name, Object):**This method sets an attribute in the context. The first argument is the attribute name. The second can be a String, in case of scalar attribute, or Java object of type List<Map<String,String>>, in case of table attribute.
-   **CommandManager.shellCommand:** This method executes a command on a target host. On UNIX machines or network devices, this command is using SSH. On Windows machines, it runs commands using the 'cmd'.
    
    Arguments:
    
    -   Command: string containing the command to be executed
    -   superUser: Boolean argument defining if the command needs to be executed with elevated rights like sudo
    -   executionMode: put null here
    -   commandParams: put null here
    -   executionContext: put CTX here

Procedure

* * *

1.  Create a new pattern or select an existing [pattern to customize](https://docs.servicenow.com/csh?topicname=c_MappingPatternsCustomization.html&version=latest "pattern to customize") as described in the product documentation.
2.  Navigate to the **Identification section** or **Connection section**.
3.  Add a new step or select a step you want to customize.
4.  Select **Set Variable** from the **Operation** list.
5.  In the **Value** field, type EVAL(javascript:), and then click the **Edit Text** button.  
      
    ![](sys_attachment.do?sys_id=6d8c24aedb42b450e515c223059619f2)
6.  In the Edit Text window, enter your Javascript code.  
    For example, enter eval(javascript: CTX.getCommandManager().shellCommand("hostname", false, null, null, CTX);) to execute the hostname comment on the target host.
7.  Click **OK**.  
    The Javascript is displayed in the **Value** field. 
8.  Enter the relevant entry that in the **Parameter** field.  
    The parameter displays the value that is retrieved as a result of running the Javascript.
9.  Click **Save**.
