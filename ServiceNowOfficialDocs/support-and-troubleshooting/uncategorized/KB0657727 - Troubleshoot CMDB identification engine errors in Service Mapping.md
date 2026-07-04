---
title: "Troubleshoot CMDB identification engine errors in Service Mapping"
aliases:
  - KB0657727
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657727
kb_number: KB0657727
last_modified: 2026-03-06
---

## Troubleshoot CMDB identification engine errors in Service Mapping

  

### Issue

Troubleshoot common CMDB identification engine errors encountered during Service Mapping and Discovery, including unexpected record creation, duplicate Configuration Items (CIs), duplicate entry points, and dependency issues.

### Release

All supported releases

### Resolution

#### **A new record was unexpectedly created, or an expected record was not created** 

To investigate unexpected record creation or missing records:

1.  Go to **Service Mapping** > **Properties** and enable verbose mode for the identification engine. Without verbose mode, only errors appear in the system log.
2.  Go to **System Logs** and filter messages containing "identification\_engine", "Output=", or "Input=".
3.  Open the input message in a JSON editor. The input shows the CI and relationship provided to the identification engine.
4.  Locate the corresponding output for the input. Input and output entries typically appear close together in the logs with the same number of items and relations. If there are multiple input/output records, match them by className (type) or sysid.
5.  Review the output to determine the result:  
    -   If the CI exists in the database, identificationAttempts - attemptResult shows MATCHED and the operation is NO\_CHANGE. The output also shows the attributes used to match.
    -   If there is no match, the operation is INSERT. The number of attempts corresponds to the number of identification rules and their criteria.

#### **Duplicate CIs appear in the database**

CIs that appear to be duplicates may actually be distinct records due to dependency rules. For example, Tomcat WARs may be defined identically but reside on different servers, making them separate CIs.

To determine whether CIs are true duplicates:

1.  Go to the identification rule for the CI type.
2.  Review the criterion attributes.
3.  Open the CIs that appear to be duplicates.
4.  Compare the dependency relationships. CIs may appear identical based on the identification rule criteria but have dependencies with different CIs, making them distinct records.

#### **CI does not meet identification or dependency criteria**

CI may fail identification if it does not meet the identification rule criteria or the dependency criteria. For example, an Apache CI may exist in the database without the expected dependency on a Linux server.

To troubleshoot these issues:

1.  Enable verbose logging mode for the identification engine (see the first scenario in this article, steps 1–2).
2.  Filter system logs using the "identification\_engine" prefix and compare all input/output records using a JSON editor.
3.  Go to **Identification/Reconciliation** > **Identification Logs** to review descriptive errors and the associated input/output data.
4.  Go to **Identification/Reconciliation** > **Metadata Editor** to review or modify the identification rules.

To test changes using the REST API:

1.  Open the REST API Explorer.
2.  Select the **Identify CI (Post)** endpoint under Identification and Reconciliation.
3.  On the **Request** tab, select **Raw Body** and paste the corrected input payload.
4.  Select **Send** and review the response.

#### **Common errors in the output payload**

The following errors may appear in the identification engine output payload:

-   **Missing identification rules** — The output indicates that an identification rule is missing for the CI type.
-   **Missing attributes** — The output indicates missing matching attributes or a required attribute. This can occur when a field is defined as mandatory but the pattern does not populate a value for it. The glide.required.attribute.enabled property controls whether the identification engine enforces mandatory attributes. This property is set to true by default. Setting it to false causes the identification engine to skip mandatory attribute validation. This error also appears in the Discovery logs.
-   **Duplicate** — The output indicates duplicate CIs. See the duplicate CIs scenario for troubleshooting steps. 

#### **Common dependency issues**

The following dependency issues can affect CI identification:

-   Incorrect definition of hosting or containment rules
-   No dependencies present in the payload, resulting in a "Missing Dependency" error
-   Multiple dependencies present in the payload

For dependency troubleshooting, follow the steps in the CI identification criteria scenario.
