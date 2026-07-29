---
title: "E-Signature/Document Template FAQ"
aliases:
  - KB0966931
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0966931
kb_number: KB0966931
last_modified: 2025-09-22
---

## E-Signature/Document Template FAQ

  

This article addresses the most frequently asked questions related to E-Signature and Document Templates. Jump to a specific question by clicking on it in the list below to learn more, and view the [Additional Information](#mcetoc_1hhkhd6jo8v) section at the bottom of this page to learn more.

## Frequently asked questions

-   [What are the various E-signature applications available with HR Service Delivery?](#mcetoc_1hhkhd6jo8h)
-   [How do I generate documents in HR Service Delivery?](#mcetoc_1hhkhd6jo8i)
-   [How can I use E-signature outside of HR?](#mcetoc_1hhkhd6jo8j)
-   [I e-signed, but the signature doesn't appear in the document. Why?](#mcetoc_1hhkhd6jo8k)
-   [How do I solve HTML to PDF conversion issues?](#mcetoc_1hhkhd6jo8l)
-   [Can I use different documents for the same HR case?](#mcetoc_1hhkhd6jo8m)
-   [Can generalPdfUtils.prefillPdf() be used to generate an editable PDF? If not, how can I generate an editable PDF?](#mcetoc_1hhkhd6jo8n)
-   [Why is a fillable PDF not editable for the user?](#mcetoc_1hhkhd6jo8o)
-   [Why can a user edit fields on the fillable PDF of HR PDF Template on an E-signature task, yet after signing and submission, only the signature is updated and not the edited fields?](#mcetoc_1hhkhd6jo8p)
-   [I have an issue with the old "sign document" task type. What should I do?](#mcetoc_1hhkhd6jo8q)
-   [Can you confirm whether "Automatically Create Draft Document" (HR Service Case Option) works with Document templates (not HR Documents)?](#mcetoc_1hhkhd6jo8r)
-   [Can you confirm whether "Preview document" works with Document Templates of type PDF on the new HR Agent workspace (configurable)? We already know they work with HTML documents.](#mcetoc_1hhkhd6jo8s)
-   [Are Document Templates \[sn\_doc\] going to replace HR Document Templates, as HR Document Templates offer limited functionality and will not be updated in the future?](#mcetoc_1hhkhd6jo8t)
-   [How to increase the size of an e-signature on the generated PDF?](#mcetoc_1hhkhd6jo8u)
-   [Additional information](#mcetoc_1hhkhd6jo8v)

### What are the various E-signature applications available with HR Service Delivery?

-   [HR e-signature](https://www.servicenow.com/docs/bundle/yokohama-employee-service-management/page/product/human-resources/concept/hr-e-signature.html "Sign electronic documents from any desktop or mobile device with e-signature. E-signature is a scoped application that enables users to sign managed documents, knowledge articles, or HR document templates with their typed or drawn e-signature, their credentials, or as an acknowledgment.")
-   [HR document templates](https://www.servicenow.com/docs/bundle/yokohama-employee-service-management/page/product/human-resources/concept/c_HRDocumentTemplates.html "HR Document Templates are used to create and modify reuseable HR documents.")
-   [Document Templates](https://www.servicenow.com/docs/bundle/yokohama-employee-service-management/page/product/human-resources/concept/document-templates-overview.html "With the ServiceNow Document Templates application, you can create HTML and PDF document templates to generate standard letters or documents. You can automate and simplify the process of filling, signing, and reviewing a document online.")

See [E-signature applications of HR Service Delivery](https://www.servicenow.com/docs/csh?topicname=hr-esigning-app.html&version=latest "E-signature applications of HR Service Delivery") for more details.

### How do I generate documents in HR Service Delivery?

You can generate documents in HR Service Delivery in 3 ways: **Automatic**, M**anual**, and **Signatures collected**. Each of these options is outlined below.

#### Automatic

If the "Automatically Create Draft Document" case option on the HR service is set, when a case is created with that HR service and its state is changed to Work in Progress or Ready, a task gets automatically generated for the employee with the document available for signing. In the case of the new Document Template, the case option is "Automatically Initiate Document Tasks".

#### Manual

The HR agent clicks "Preview Document" on the case to preview and generate the document. The agent can also click "Sign Document" to sign the document.  Once the document is generated it gets attached to the case. If the employee is also required to sign the document, the agent can either email the document to the employee or the agent can create an e-signature task and assign it to the employee (you can insert multiple signatures in the HR document template (both HTML and PDF). 

#### Signatures collected

Documents like offer letters can require multiple signatures. When all signatures are collected, the document is automatically generated. This can be achieved through either Service activities in HR Service OR the new Document Template by specifying participants and order.

### How can I use E-signature outside of HR?

Review the following example of creating an E-signature on an incident task:

1.   Create the e-sign template on the incident task table. Select the following:
    -   Document type - Managed Document
    -   E-signature type - Signature
2.  Configure the Incident task form and add the 'E-Signature Template' field
3.  Configure the Incident Related Lists and add the 'E-signature history'. Fill in the template field with the template created previously
4.  Assign a group and a user to the task.
5.  Impersonate the user and open the task.
6.  Move the task to 'Work in progress'

The 'Sign document' UI action will now appear for the user to sign the document.

To retrieve this signature log, navigate to System Logs > Signature Images (signature\_image table).  Also, you can view the E-signature history in the related list

Note: make sure the user has access to KB as KB is the document used in the E-Signature template

### I e-signed, but the signature doesn't appear in the document. Why?

You can only embed the signature through HR Document Template (document type = HR document template in E-signature template). If you e-sign a managed document or knowledge article (document type = managed document/knowledge article in E-signature template), the signature will not appear within the document itself. However, the signature will be saved to the E-signature history.  
  

### How do I solve HTML to PDF conversion issues?

You may encounter issues related to formatting, padding, margins, fonts, etc. as there are some issues/limitations using itext5 for the conversion. To solve this, turn on system property **sn\_hr\_core.itext7.pdf\_conversion** to use itext7 instead of itext5.

For new customers in Paris, this property is true by default. 

For customers upgrading to Paris or later, they can create this system property and set it to true.

Also, see [KB1633478](/kb?id=kb_article_view&sys_kb_id=b51b4954472c8690f93138ce536d4365) on this.

**Note:** Images might turn out distorted using itext7. If this happens, customers are advised to adjust the images in the html template.

### Can I use different documents for the same HR case?

We do not currently support using different documents for the same HR case.  
  

### Can generalPdfUtils.prefillPdf() be used to generate an editable PDF? If not, how can I generate an editable PDF?

generalPdfUtils.prefillPdf() does not output an editable PDF; however, the Platform provides an API PDFGenerationAPI that outputs an editable PDF.

#### Sample Code:

var fieldMap = new Object();  
fieldMap\["Address"\] = "PO Box 344";  
fieldMap\["City"\] = "Jerome";  
fieldMap\["State"\] = "AZ";  
fieldMap\["Zip"\] = "86331";  
var flatten = new Object();  
flatten\["FlattenType"\] = "donot\_flatten";  
var v = new sn\_pdfgeneratorutils.PDFGenerationAPI;  
var result = v.fillDocumentFieldsAndFlatten(fieldMap, "c53d9b87eb930110ec17bed05952286e", "incident", "57af7aec73d423002728660c4cf6a71c",  
"pdfName",flatten);  
gs.info(JSON.stringify(result));

Please refer to the [PDFGenerationAPI API - Scoped, Global](https://docs.servicenow.com/csh?topicname=PDFGenerationAPIBothAPI.html&version=latest) product documentation for more information.

### Why is a fillable PDF not editable for the user?

HR PDF templates do not support the filling of any information on the PDF document except the signature. Customers can use PDF template mapping to auto-populate fields from the table. See the first note in the below documentation page:

[Configure an HR PDF document template](https://docs.servicenow.com/bundle/washingtondc-employee-service-management/page/product/human-resources/task/PDFTemplate.html)

If you wish to use fillable PDF for filling other fields apart from signature, you will need to use Document Templates. Steps for this can be found in the KB article [KB0998546](/kb?id=kb_article_view&sysparm_article=KB0998546).  
  

### Why can a user edit fields on the fillable PDF of an HR PDF template on an E-signature task, yet after signing and submission, only the signature is updated and not the edited fields?

Being able to edit fillable PDFs along with signature and save is a new feature in Document Template and not part of HR Document Template.  
For HR pdf templates, the line ref in the [Configure an HR PDF document template](https://docs.servicenow.com/bundle/washingtondc-employee-service-management/page/product/human-resources/task/PDFTemplate.html) product documentation "Fillable PDFs presented to an employee does not save any data populated by the employee (except for signatures). Fillable PDFs are only used for mapping fields to a table" applies.

### I have an issue with the old "sign document" task type. What should I do?

Customers should be using the new e-signature task type. Refer to the [Migrate existing HR task templates and open HR tasks to e-signature](https://docs.servicenow.com/bundle/washingtondc-employee-service-management/page/product/human-resources/task/migrate-existing-tasks-to-scoped-e-signature.html) product documentation for more information.

### Can you confirm whether "Automatically Create Draft Document" (HR Service Case Option) works with Document templates (not HR Documents)?

"Automatically Create Draft Document" is only for HR document template, "Automatically Initiate Document Tasks" is for document template

### Can you confirm whether "Preview document" works with Document Templates of type PDF on the new HR Agent workspace (configurable)? We already know they work with HTML documents.

Starting with v4.0.0 of Agent Workspace for HR Case Management (available for Yokohama release), "Preview Document" works with Document Templates of both types - PDF and HTML - on the new HR Agent Workspace (Configurable).

### Are Document Templates \[sn\_doc\] going to replace HR Document Templates, as HR Document Templates offer limited functionality and will not be updated in the future?

Yes, starting with the Yokohama release, [HR Document Templates](https://www.servicenow.com/docs/csh?topicname=c_HRDocumentTemplates.html&version=latest "HR Document Templates") is being prepared for future deprecation. It will be hidden and no longer activated on new instances but will continue to be supported.

Use [Document Templates](https://www.servicenow.com/docs/csh?topicname=document-templates-overview.html&version=latest "With the ServiceNow Document Templates application, you can create HTML and PDF document templates to generate standard letters or documents. You can automate and simplify the process of filling, signing, and reviewing a document online.") \[sn\_doc\] instead, as it provides the latest experience for this functionality. For migration guidelines, see [Migrating from HR Document Templates to Document Templates](https://www.servicenow.com/docs/csh?topicname=migration-hrdt-dt.html&version=latest "Review these guidelines to successfully migrate from HR Document Templates to Document Templates. Document Templates provides the latest experience of HR Document Templates functionality with additional features and capabilities.").

### How to increase the size of an e-signature on the generated PDF?

The signature size on the generated PDF can be increased by updating the method \_get\_signature() in OOB Script Include GeneralHRForm. See [KB1590161](/kb?id=kb_article_view&sysparm_article=KB1590161) for more details. 

## Additional information

#### Product Documentation:

-   [HR Document Templates](https://docs.servicenow.com/csh?topicname=c_HRDocumentTemplates.html&version=latest)
-   [HR E-signature](https://docs.servicenow.com/csh?topicname=hr-e-signature.html&version=latest)
-   [Document Templates](https://docs.servicenow.com/csh?topicname=document-templates-overview.html&version=latest)
    -   Applicable outside of HR. It is capable of attracting participants. It has its own flow, and document tasks are generated for each signer/filler/reviewer based on configuration. New document templates will not work with all tasks by default. It must be adopted, and the flow must be triggered based on the business use case.
-   [E-Signature](https://docs.servicenow.com/csh?topicname=e-signature.html&version=latest)
    -   A scoped application that enables users to sign managed documents or knowledge articles with their typed or drawn e-signature, credentials, or as an acknowledgment. This can be used outside of HR.

A helpful video about Advanced Forms Management can be found on ServiceNow Community at [Advanced Forms Management in HR Service Delivery](https://www.servicenow.com/community/hrsd-articles/advanced-forms-management-in-hr-service-delivery/ta-p/2309758).
