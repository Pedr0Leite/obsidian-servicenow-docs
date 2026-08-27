---
title: "Convert KnowledgePage to PDF"
aliases:
  - Convert KnowledgePage to PDF
tags:
  - servicenow-dev-program
  - code-snippet
  - convert-knowledgepage-to-pdf
  - attachments
---

# Convert Knowledge Page HTML to PDF and attach it.
* Create PDF using GeneralPDF.
* Try it from a simple HTML conversion.
* It seems that the conversion fails if the HTML contains image files.
* See the Script Include GeneralPDF for details. 
* GeneralPDF is already in Script Include, but it may not exist in some environments

```javascript
var grKnow = new GlideRecord('kb_knowledge');
// Get a simple HTML KnowledgePage
if(grKnow.get('<KnowledgePage sys_id>') && grKnow.getValue('text')){
    // Create PDF Document.
    var pdfDoc = new GeneralPDF.Document(null, null, null, null, null, null);
    var document = new GeneralPDF(pdfDoc);
    document.startHTMLParser();
    document.addHTML(grKnow.getValue('text'));
    document.stopHTMLParser();
    // Create PDF Attachment.
    var att = new GeneralPDF.Attachment();
    att.setTableName(grKnow.getTableName());
    att.setTableId(grKnow.getValue('sys_id'));
    // Attached file name. 
    att.setName('TestPDF.pdf');
    att.setType('application/pdf');
    att.setBody(document.get());
    // Attachment creation
    GeneralPDF.attach(att);
}
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to Base64/README|Attachment to Base64]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Attachment to base64 in scope/README|Attachment to base64 in scope]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Base 64 to Attachment/README|Base 64 to Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/CSVParser/README|CSVParser]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Calculate attachment hash code/README|Calculate attachment hash code]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Attachments/Create Attachments/README|Create Attachments]]
