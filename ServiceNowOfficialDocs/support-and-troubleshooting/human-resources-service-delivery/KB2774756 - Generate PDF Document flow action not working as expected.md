---
title: "\"Generate PDF Document\" flow action not working as expected "
aliases:
  - KB2774756
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2774756
kb_number: KB2774756
last_modified: 2026-02-12
---

## Issue

When using the OOB action Generate PDF Document in workflow studio, the expected result is to have a PDF generated from a template. The PDF is not generated, and the 'Generate Attachment Id' remains empty.

Even with valid parameters to the action with specific inputs, including TemplateId, TaskRecordId, Task Table, and PDFName.

![](/sys_attachment.do?sys_id=2ff9b0459703b65485e13bbe2153af31)

## Resolution

Based onr ["Using Document Templates: Custom use case" https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB2377258](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2377258)

1\. Create a copy of the 'Generate PDF Document' action in workflow studio. Make sure this is in the global scope.

2\. Replace the script in the copied action with the following code: (function execute(inputs, outputs) { outputs.generatedattachmentid = new sn\_doc.GenerateDocumentAPI().generateDocumentForTask(inputs.taskId, inputs.templateId, inputs.generatedPdfName); })(inputs, outputs);

3\. Test the modified action to verify if it generates the PDF and populates the 'Generate Attachment Id'. 4. Refer to the KB article 'Using Document Templates: Custom use case' (KB2377258) for additional guidance on custom implementations.  
  

![](/sys_attachment.do?sys_id=23f9b0459703b65485e13bbe2153af44)

The action can then be called from any other scoped flow.  You may need a  Application Restricted Caller Access (RCA) setup from your scope to global.

## Additional Information

["Using Document Templates: Custom use case" https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB2377258](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2377258)

  
[https://www.servicenow.com/community/developer-forum/using-document-templates-across-scopes-outside-of-hr/m-p/2955843](https://www.servicenow.com/community/developer-forum/using-document-templates-across-scopes-outside-of-hr/m-p/2955843)

  
[https://www.servicenow.com/community/developer-forum/generate-pdf-document-action-in-flow-designer/m-p/2701926/page/2](https://www.servicenow.com/community/developer-forum/generate-pdf-document-action-in-flow-designer/m-p/2701926/page/2)
