---
title: "IT Asset Management Content Request Process"
aliases:
  - KB0790305
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790305
kb_number: KB0790305
last_modified: 2026-02-26
---

## Text

The IT Asset Management Content Services Team manages and supports content requests from ITAM customers. The ITAM Content Team will review content requests and deliver them through the regular weekly content updates.

Examples of content requests include but are not limited to the addition of or update to Publishers, Products, Publisher Part Numbers, Discovery Maps and Lifecycle Dates. While customers have the ability to add Custom Data (Publishers, Products, etc.) to their instance, it is recommended that customers leverage out-of-box content for ITAM use cases. If a customer were to create custom data that has since been delivered through the Content Service, references should be updated to the out-of-the-box content, and custom data should be deleted.

Content Requests fall into two categories:

1.  **New Content**: Customers need content that isn't available in the Content Library, such as new publishers, products, publisher part numbers, lifecycle information, and normalization rules to transition from publisher normalized and partially normalized discovery models to fully normalized ones.
    -   New Content can be requested by submitting a Catalog Request with details of their request through the NowSupport Portal
        -   Attach the information on the new content required via the appropriate template (SAM template or HAM template). This is a mandatory requirement for our internal automation processes.
        -   However, for any Normalization request, please attach an XML extract of Non-Normalized/concerned (Match not found, Publisher/manufacturer normalized and Partial normalized) records from the cmdb\_sam\_sw\_discovery\_model table (for SAM) or cmdb\_hardware\_product\_model (for HAM). (Please do NOT extract the full table, and only extract the concerned non-normalized records).
    -   Post closure of the CR (Catalog Request), if any questions arise for customers on the fulfilled CR, a Case ticket can be filed   giving the reference of the CR#
    -   CRs do not involve the Support organization and hence do not follow the workflow process of Case requests
2.  **Content Correction**: Customers require previously delivered content to be corrected, such as publisher part numbers, lifecycle information, fully normalized discovery models, etc.
    -   Content update is requested by filing a Case with ServiceNow Customer Support with details of their request through the NowSupport Portal.

Content requests undergo a research and development process. Based on the volume of content requested/to be researched, and the current queue of customer requests with the content team, this process can span several content update cycles. Customers will be updated and can track the progress of their requests through the Case provided in Hi.  Customers will be notified when the content has been created, and in what content release cycle it will be included.  Customers can also view the latest Content Library statistics on the [Normalization and Content Service Dashboard](https://docs.servicenow.com/bundle/tokyo-it-asset-management/page/product/software-asset-management2/concept/sam-normalization-dash.html "Normalization and Content Service Dashboard").

Content is researched and evaluated for reliability or verifiability before it is created. In cases where such information is not available to the manufacturers or in the public domain, such content will not be created by the content team. Alternatively, customers can provide proof of the software with documents such as purchase orders, etc. (where it can be shared with ServiceNow) and the content team will evaluate it and if found sufficient and verifiable will uptake that content.

Content created is also treated in a generic manner that can be applicable to all customers. If any customer requirement is to define/redefine the content towards specifics of requesting customers, and if that may not be suitable for the wider customer base using this data, such data may not be added to the content library. This content would need to be handled locally as custom data by the requesting customer.  

Content Updates are shipped on a weekly basis and follow its own release cycle. Data curated and validated generally takes between 7 to 10 days to reach the central instance and be available for customer download.

To request **new** IT Asset Management Content:

\* _Federal customers should follow a separate process mentioned below._ 

All users and partner users belonging to your company can access this service catalog and create Content Requests. 

-   Login to ServiceNow's Now Support Portal.
-   Navigate to: Automation Store > Service Catalog > Search and pick catalog item: Asset Management Content Request.

![](/sys_attachment.do?sys_id=dc4d0c5393b7ea9c7c79b36d6cba10ec)

-   The Catalog Item form will automatically populate:
    -   Catalog Request number (CR)
    -   Requested By
    -   Company

![](/sys_attachment.do?sys_id=584d0c5393b7ea9c7c79b36d6cba10f0)

-   You will need to enter the following:
    -   **Title:** Summary of your request.
    -   **Description:** details of your content request.
    -   **Selected Instance:** Which instance you are requesting the content for?
    -   **Watch List:** Add individuals within your organization to view the progress of this request.
    -   **Content Category:** Software Asset Management (SAM) or Hardware Asset Management (HAM) content.
    -   **Attachment:** Attach an Excel sheet with the needed information about the content requested.

**NOTE:** You can use "Create Case" UI Action if you have further inquiries regarding the delivered content.

**IMPORTANT**: For Federal/GCC customers:

Federal/GCC customers, please follow the steps below to complete a new content request:

-   Create **HIWAVE** case
-   Case Type = “Service Request” – I have a service request that is not available in the Automation Store”
-   Subject = “Federal Customer – New Content Request for Software Asset Management”
-   Select Instance(s) Impacted
-   Describe the issue = “I am a Federal customer and would like to add new content that is not currently in the Content Library”
-   Attach information containing new content. You may choose to upload content in the format specified in these [SAM content templates](/kb?id=kb_article_view&sysparm_article=KB2499223) or [HAM content templates](/kb?id=kb_article_view&sysparm_article=KB2499232). 
-   Attach information that helps verify content (redacted Purchase Orders/Quotes)

To view your current Content Requests:

-   Login to ServiceNow's Now Support Portal.
-   Navigate to: Automation Store > Service Catalog > My Content Requests.
-   **Requests in an 'Awaiting Info' state**: Any Content Catalog Request directed to the customer for additional information, and stays in the same status for more than 15 calendar days (i.e., without any information or updates) shall be closed by the Content Team. If the customer has the sought-out information in the future time, a new request can be created with such information for the Content Team to review and process.
-   **Requests without standard format**: We will request the customer to share the template in the standard format and we will move the CR to an 'Awaiting Info' state.  
     

**NOTE:** There is a default filter applied that only shows active requests. If you'd like to see all your requests (including closed ones), you'll need to adjust the filter.
