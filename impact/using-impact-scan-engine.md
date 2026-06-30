---
title: Running on-demand scans
description: You can initiate some scan types on-demand to run whenever they are required.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/impact/using-impact-scan-engine.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Run your first scan, Configure the Impact Store Application, Configuring Impact, Impact]
---

# Running on-demand scans

You can initiate some scan types on-demand to run whenever they are required.

You can initiate the following scan types on-demand.

<table id="table_jxp_zlk_hhc"><thead><tr><th>

Scan type

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Application scans

</td><td>

Scan in-development applications to identify definition findings before publishing to the application repository. Application scans give insight into health scores, the number of findings, and the total [[impact-landing-page|impact]] of findings within your custom applications. **Note:** View application health scores in the Application Health dashboard by navigating to **ALL &gt; Impact &gt; [[platform-health-idi|Platform Health]] &gt; Application Health**. Health scores are calculated based on finding severity, count, and policy impact.

</td></tr><tr><td>

Limited definition scans 

</td><td>

Scan your instance against a single specified definition or definition suite.

</td></tr><tr><td>

Update set scans 

</td><td>

Scan open update sets for findings to get insights into what you are importing and exporting across your environments. 

</td></tr><tr><td>

Instance scans 

</td><td>

Scan your ServiceNow instance for findings. These scans return the findings and store them in the Opens Findings table.  **Note:** Only users with the Scan Engine Admin role can initiate instance scans.

</td></tr></tbody>
</table>Scheduled instance scans can be executed immediately using the **Execute Now** action, but they cannot bypass their configured schedule settings. Real-time scans run automatically during record saves and cannot be manually triggered.

**Note:** The Scan Engine integrates with certain development tools, such as App Engine Studio, ServiceNow Studio, and script editors. It scans business rules, script `includes`, UI scripts, client scripts, ACLs, record producers, and other script-containing records in real-time as they are saved.

Scans are initiated in different ways. They run using the Scan Engine properties you configured.

For more information, see [[configure-scan-engine-properties|Configure Scan Engine properties]] and [[additional-scan-engine-properties|Configure definition properties]].

-   **[[initiating-on-demand-scans-scan-engine|Initiate application scans]]**  
Scan applications to identify definition findings before publishing to the application repository. Application scans give insight into health scores, the number of findings, and the total impact of findings within your custom applications. 
-   **[[initiate-update-set-scans|Initiate update set scans]]**  
You can scan open update sets for findings to get insights into what you are importing and exporting across your environments. 
-   **[[initiate-instance-scans|Initiate instance scans]]**  
You can scan your ServiceNow instance for findings.
-   **[[initiate-limited-def-scans|Initiate limited definition scans]]**  
You can scan individual definitions or suites of definitions on-demand.

**Parent Topic:**[[run-scan-engine|Run your first scan with the Scan Engine]]

**Related topics**  


[[scan-engine-parallel-processing|Full and delta instance scans]]

[[initiate-manage-scan-engine|Initiate and manage scans]]

## Related

- [[configure-scan-engine-properties|Configure Scan Engine properties]]
- [[additional-scan-engine-properties|Configure definition properties]]
- [[initiating-on-demand-scans-scan-engine|Initiate application scans]]
- [[initiate-update-set-scans|Initiate update set scans]]
- [[initiate-instance-scans|Initiate instance scans]]
- [[initiate-limited-def-scans|Initiate limited definition scans]]
- [[run-scan-engine|Run your first scan with the Scan Engine]]
- [[scan-engine-parallel-processing|Full and delta instance scans]]
- [[initiate-manage-scan-engine|Initiate and manage scans]]
- [[impact-landing-page|Impact]]
- [[platform-health-idi|Platform Health]]
