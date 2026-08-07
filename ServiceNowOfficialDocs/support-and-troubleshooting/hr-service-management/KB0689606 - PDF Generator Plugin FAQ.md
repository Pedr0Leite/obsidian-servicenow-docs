---
title: "PDF Generator Plugin FAQ"
aliases:
  - KB0689606
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0689606
kb_number: KB0689606
last_modified: 2025-04-23
---

## PDF Generator Plugin FAQ

  

### Issue

The HR Service Management application uses PDF generation to produce PDF documents from HTML templates for various HR based documents. The PDF generation functionality is in its own accessible plugin, and can be utilized with or without HRSM. We have built out additional  functionality for HR use cases, but there has been confusion about what the PDF generation plugin supports, what it doesn't support, and other technical specifics. The goal of this FAQ is to answer these questions and provide links to official documentation where appropriate.

Misunderstandings may come from assumptions about what functionality the PDF generator supports. Versions of the PDF generator using iText5 have limitations. If PDFs are not generating the way you would expect, verify which functionalities might not be supported yet. 

## PDF Functionality that is not Supported

The TinyMCE editor allows rich text creation that the PDF generator was not designed to support. TinyMCE is the standard editor for the ServiceNow platform, so it can not be simply updated to not allow certain HTML elements that PDF generation supports. Some of the more common questions we’ve seen involve expectations of the following non-supported HTML elements: 

-   Vertical alignment
-   Page breaks (workaround to add one manually using document.addNewPage()
-   Table-specific color (text color is supported)
-   Custom spacing between blocks of text or images
-   Custom column width in HTML tables
-   Custom column alignment in HTML tables
-   Custom border styling in HTML tables
-   CSS text manipulation ()including CSS based font tags)
-   Inline styling
-   Background images

iText 7 does support these HTML constructs and upgrading to it would allow the PDF generator to handle these. Creating enhancement requests for customers that wish to use them will provide us the information we need to properly prioritize potential enhancements.

## FAQ

-   Q: What page sizes can the PDF generator utilize?  
    -   A: Letter, Legal, and A4. A4 is the default if no size is passed in. Pagesize is the final parameter for the generalFormAPI.setDocument() API. 
-   Q: What version of iText does the PDF generator use?  
    -   A: Currently the PDF generator utilizes iTextPDF version 5.5.2

### Cause

There are two basic ways to allow generation PDFs in the HR application: 

-   Generating a PDF document from an HTML template
-   Generating a PDF from another PDF to automatically merge or add variables to it

This document covers the basics of each one as well as some technical details about script includes and other components that facilitate this functionality.

### Resolution

## Generating a PDF file from an HTML Document Template

### PDF Template Definition

HTML document templates can be created and updated from the "Document Templates" module in the HR Core application. A document template is comprised of the following components:

-   Header Image
-   Body (Text) 
-   Footer Image
-   Footer Text
-   Table (used for variable reference when generating a PDF document. 

The body text is defined and formatted with the TinyMCE editor and can merge or include user and table variables during generation. These variables can be selected and defined on the side of the editor. 

Please keep in mind that some of the HTML elements you can create using the editor are not supported by the PDF generator at this time. See the "PDF functionality that is not supported below" for more information on what is and is not supported.  
  

### Generating the Document

The most common use case is allowing an HR agent to generate a document from a case via UI action (A good OOB example is Employment Verification Letter.) This requires the following steps: 

-   Create a UI action on the table referenced in the Document Template
-   Code this UI action to call the document generation methods to generate the PDF

The first bullet point is straightforward, however there are a couple of ways to call the document generation functionality. With HR installed, you can use our wrapper method to generate the PDF by creating an instance of our helper class and calling the generate method:

// tableName: Name of the table that the Document Template is based on.  
// tableId: Sys ID of the record in the table to use for generation  
// targetTableName: Name of the table to attach the generated PDF  
// targetTableId: Sys ID of the record in the target table where the PDF will be attached

new GeneralHRForm(tableName, tableId, targetTableName, targetTableId).generate();  
  
1\. Create an instance of the GeneralFormAPI class

// fileName: Name of the PDF file that will be generated  
// targetTable: Name of the table to attach the PDF  
// targetTableSysID: Record to attach the PDF  
_new GeneralFormAPI(fileName, targetTable, targetTableSysId);_

_2\. Set the values saved in the Document Template class_

_// header: Header image for the PDF  
// footer: Footer image for the PDF  
// headerLocation: Is the header right, left, or center aligned  
// footerLocation: Is the footer right, left, or center aligned  
__GeneralFormAPI.SetDocument(header, footer, headerLocation, footerLocation);  
_

_3\. Call the createPDF method and pass in the body text defined in the document template_

_// body: body text defined in the template  
__GeneralFormAPI.createPDF(body);_

The PDF should be generated and attached to the record referenced in Step 1. 

## Generating a PDF from another PDF

In addition to generating PDFs from an HTML template, we also support generating a PDF based on a "fillable" PDF template. This template is implemented as a managed document using either a fillable PDF with mapped fields, or a standard PDF with an inline signature.

### Fillable PDFs

Fillable PDFs are a type of PDF where the fields are mapped to a data structure contained in the PDF itself. A fillable PDF can be uploaded as a managed document, parsed, and fields in the PDF structure can be mapped to record values in an HR table. The basic process for this:

-   Go to the Managed Documents module and create a managed document record. Be sure it's in published state before going to the next step.
-   Go to the  "Document Templates" module and create a PDF document template. Associate this new PDF template with the managed document by the Document Revision field. 
-   If the PDF is fillable, there will be a UI action to parse all document fields. This will show you all the fields in the PDF and allow you to map them to values in the table that the PDF Template is associated with.

When generating a PDF using a fillable PDF template, all PDF variables will be automatically mapped to values in the table. 

### Marking a Signature Area

In addition to allowing fillable fields, a "Signature area" can be defined while creating or modifying a PDF template as follows:

-   Click the "Mark Signatures" UI action while creating or modifying a PDF template
-   Click Add Field on the modal that opens
-   Drag and Drop an area to represent the signature area
-   Name the field and map it to an existing table field if desired

The following script includes are important for fillable PDF functionality and are included here for reference:

-   GeneralFormAPI: Contains methods for instantiating a template and generating a PDF  
    -   This is a global script include and part of the core PDF Generator plugin. Not HR specific

-   GeneralHRForm: HR specific script that wraps a lot of HR code and proxies the GeneralFormAPI.

-   GeneralPDFUtils: Collection of various PDF utility methods, some of the more important ones are:   
    -   getPDFFields - returns a collection of parsed fields on a fillable PDF
    -   mergeImageToPDF - used for merging a signature or image into the PDF document
    -   prefillPdf - automatically fills out a PDF with all mapped fields, used for preview functionality.

### Related Links

-   [HR Document Templates](https://docs.servicenow.com/csh?topicname=c_HRDocumentTemplates.html&version=latest "HR Document Templates")
-   [Add or Modify an HR PDF Document Template](https://docs.servicenow.com/csh?topicname=PDFTemplate.html&version=latest "Add or Modify an HR PDF Document Template")
-   [HR document templates](https://docs.servicenow.com/csh?topicname=c_HRDocumentTemplates.html&version=latest "HR document templates") for PDF generation support. Contains additional technical details on the scriptable PDF generation methods available. 
-   [iTextPDF documentation](https://developers.itextpdf.com/frequently-asked-developer-questions "iTextPDF documentation") for developers. This contains full documentation for the iTextPDF API and how its integrated.
