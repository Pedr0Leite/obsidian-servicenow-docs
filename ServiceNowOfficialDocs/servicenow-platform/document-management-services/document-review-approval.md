---
title: Document approval and publish process
description: A reviewer approves or rejects the document. A document can have multiple reviewers. During the approval process, the approver approves or rejects the document. A document goes through the approval process after the review process. A document is published after the review and approval process.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/servicenow-platform/document-management-services/document-review-approval.html
release: australia
product: Document Management Services
classification: document-management-services
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Use, Document Management, Document Services, Manage content capabilities, Extend ServiceNow AI Platform capabilities]
tags:
  - servicenow-platform
  - documents
  - storage
  - dms
  - attachments
  - type-concept
---

# Document approval and publish process

A reviewer approves or rejects the document. A document can have multiple reviewers. During the approval process, the approver approves or rejects the document. A document goes through the approval process after the [[c_ReviewProcess|review process]]. A document is published after the review and approval process.

A document can have a reviewer or multiple reviewers and no approvers and vice versa. You must have the platform\_document\_management\_admin or admin role to create approval and review rules.

Users who can create documents have the option to do the following:

-   Add approvers and reviewers to a document​.
-   Initiate the approval and review workflow​ for a document version.
-   Publish the approved version.
-   See the activity stream of the approval and review workflow.

All approvers and reviewers have read access to the documents that they’re approving.

## Document approval revision rule

The [[r_ApprovalProcess|document approval]] and revision rule is created based on the conditions defined in the condition builder to determine which documents use the approval rule. After the approval rule is saved, reviewers and approvers are added if the conditions in the Condition field are met.

**Note:** Document reviewer and approver directly added from the document record aren’t added to the Document approval and revision rule.

## Document review

If the reviewer rejects the document, the author and owner are notified and the review is canceled. The author, owner, and reviewer should discuss what changes must be made to the document. If the reviewer approves the document, the author and owner are notified that the review was successful, and the document can move to the approval stage. If multiple reviewers are assigned to a document, the first reviewer to act dictates what happens to the document. For example, there are two reviewers, A and B.

If reviewer A acts first and rejects the document, the review process stops and the revision state is set to Canceled. Reviewer B receives a notification [[email|email]] stating that the review was rejected and the status is changed to No Longer Required. If reviewer A acts first and approves the document, the review process stops and the document can move to the approval stage. Reviewer B's status is changed to No Longer Required.

## Document approval

After the document has been reviewed, submit the document for approval. If the document doesn’t have an approver, the approval process is omitted.

If the final approver approves the document, the author and the owner are notified. After the final approval is successful, the document stage changes to Ready for Publishing in the [[document-mgt-versions|Document versions]] list.

If there are [[c_MultipleApprovers|multiple approvers]], the approval process works in sequence, and multiple approvers can be assigned to a single sequence. For example:

-   Sequence 1: Approvers A and B
-   Sequence 2: Approvers C and D
-   Sequence 3: Approver E

The sequences take place in ascending chronological order, approvers A and B receive the approval request first \(approvers C, D, and E aren’t part of the process yet\). Similar to the review process, the first approver to act within a sequence dictates what happens to the document. If approver A acts first and rejects the document, the approval process stops and the state is set to Canceled. Approver B's status is changed to No Longer Required. If approver A acts first and approves the document, the process stops and approver B's status is changed to No Longer Required. The document then moves to approval sequence 2. After at least one approver in each sequence approves the document, the author and the owner are notified that the document has been approved.

## Publish a document

After a document has been created and edited, the revision can be submitted for draft review and final approval. After final approval, the document can be published.

If the approval and publishing process is repeated, the published revision is retired when the new revision is published. Any workflows running against previous revisions are canceled when the document is published.

-   **[Create a document approval revision rule](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/document-management-services/create-doc-approval-rev-rule.md)**  
[[create-doc-approval-rev-rule|Create a document approval revision rule]] for the document review and approval process.
-   **[Add a reviewer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/document-management-services/add-a-reviewer.md)**  
Add a single or multiple reviewers to the document approval and review rule for document review.
-   **[Add an approver](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/document-management-services/add-an-approver.md)**  
Add a single or multiple approvers to the document approval and review rule for document approval.
-   **[Send a document version for review and approval](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/document-management-services/send-document-for-review.md)**  
[[send-document-for-review|Send a document version for review and approval]] before publishing the document.
-   **[Approve or reject a document version](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/document-management-services/approve-document.md)**  
[[approve-document|Approve or reject a document version]] after the review process is complete.
-   **[Approve or reject a document version through email](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/document-management-services/approve-reject-document-email.md)**  
Approve or reject a document version request directly from your email.
-   **[Publish a document](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/document-management-services/publish-a-document.md)**  
[[publish-a-document|Publish a document]] revision that has been approved.

**Parent Topic:**[Using Document Management](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/servicenow-platform/document-management-services/using-document-management.md)

## Related

- [[c_ReviewProcess|Review process]]
- [[r_ApprovalProcess|Document approval]]
- [[email|Email]]
- [[document-mgt-versions|Document versions]]
- [[c_MultipleApprovers|Multiple approvers]]
- [[create-doc-approval-rev-rule|Create a document approval revision rule]]
- [[send-document-for-review|Send a document version for review and approval]]
- [[approve-document|Approve or reject a document version]]
- [[publish-a-document|Publish a document]]
