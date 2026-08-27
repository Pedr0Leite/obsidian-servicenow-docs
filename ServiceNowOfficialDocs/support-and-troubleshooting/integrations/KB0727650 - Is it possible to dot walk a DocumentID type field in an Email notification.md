---
title: "Is it possible to dot walk a DocumentID type field in an Email notification ?"
aliases:
  - KB0727650
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727650
kb_number: KB0727650
last_modified: 2024-04-07
---

## Is it possible to dot walk a DocumentID type field in an Email notification ?

  

### Issue

Is it possible to dot walk a DocumentID type field in an Email notification ? 

Problem

How to reference a Document ID type field that is associated with a linked table in the body of any notification when the linked table is not known.

  
Resolution

The Document ID field references any record on any table, therefore you need to check what is the associated table.

-   Go to Dictionary
-   Search for the DocumentID field: "document\_id" in the columns
    -   Verify which table name this is associated with. For example table \[sysapproval\_approver\], the source field contains the table name it is associated with. 
    -   It is the Document ID record that contains the source table.

 ![](sys_attachment.do?sys_id=0b1ae8e2db42b450e515c22305961933)

![](sys_attachment.do?sys_id=cb1ae8e2db42b450e515c22305961938) 

-   For example,  open up a sample record in the \[sysapproval\_approver\] and show the XML source view

<table><tbody><tr><td><span style="background-color: #d1d1d1;">&lt;document_id&gt;41cdb152db252200a6a2b31be0b8f527&lt;/document_id&gt;</span><br><span style="background-color: #d1d1d1;">&lt;source_table&gt;change_request&lt;/source_table&gt;</span></td></tr></tbody></table>

 The source table is \[change\_request\]

Therefore the "DOT WALK" notation with that document ID will pull in all fields related to the change\_request table and other linked fields.

<table class="noteTable" align="left"><tbody><tr><td class="c3"><img class="c2" title="Note" src="/Note_25x.pngx" align="bottom" border="border" hspace="" vspace=""></td><td class="c4"><strong>Note</strong>:&nbsp;The actual name of the source table&nbsp;is not shown in the dictionary entry.</td></tr></tbody></table>
