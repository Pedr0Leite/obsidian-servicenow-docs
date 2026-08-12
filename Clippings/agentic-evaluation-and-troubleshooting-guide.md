---
title: "Agentic Evaluation and Troubleshooting Guide"
source: "https://www.servicenow.com/community/servicenow-otto-articles/agentic-evaluation-and-troubleshooting-guide/ta-p/3495111"
author:
  - "[[Brad Tilton]]"
  - "[[Peinadov]]"
published: 2026-03-02
created: 2026-08-12
description: "Agentic Evaluation and Troubleshooting Guide Table of Contents Navigate to Automated Evaluation Configure Evaluation Settings Name and Select"
tags:
  - "clippings"
---
### Guide Link

[sn.works/AIAgentE2EGuide](https://sn.works/AIAgentE2EGuide)

### We Value Your Feedback!

Have any suggestions or topics you'd like to see in the future? Let us know!

## Overview

Agentic evaluations provide a systematic approach to testing and monitoring the performance of your AI agents and agentic workflows. This feature allows you to evaluate your agents against custom datasets, measure key performance metrics, and compare results across different benchmarks. By running automated evaluations, you can ensure your AI agents consistently meet quality standards and identify areas for improvement.

Once evaluations are complete, you can analyze results through both overview dashboards and detailed breakdowns. The platform enables you to export reports, clone evaluations for comparative analysis, and track improvements across iterations. This structured evaluation framework ensures your AI agents deliver reliable and consistent outcomes in production environments.

This guide is part 3 in a series of articles describing how to enable Agentic workflows in your instance. If you would like to navigate to the other articles, please follow the links below.

## Navigate to Automated Evaluation

## Configure Evaluation Settings

### Name and Select Workflow

1. Enter a descriptive name for your evaluation in the name field
2. Add a description that explains the purpose of this evaluation
3. Use the drop-down search field to select the agentic workflow you want to evaluate
4. Click the Continue button in the lower-right corner to proceed to the next step
![MariaGabriela_1-1772219788533.png](https://www.servicenow.com/community/image/serverpage/image-id/504048i6AAF9F31D3FFC2B3/image-size/large?v=v2&px=999 "MariaGabriela_1-1772219788533.png")

### Select Evaluation Metrics

1. Review the available evaluation metrics on the "evaluation metrics" page
2. Select the specific metrics you want to measure during the evaluation
3. Click Continue to move to the dataset configuration
![MariaGabriela_2-1772219795751.png](https://www.servicenow.com/community/image/serverpage/image-id/504049iC8305BDF38AC1DC8/image-size/large?v=v2&px=999 "MariaGabriela_2-1772219795751.png")

## Create and Configure Dataset

### Set Up Dataset Parameters

1. Enter a name for your new dataset
2. Provide a clear description of the dataset purpose
3. Select "By running agentic workflow and using the generated execution logs" as the dataset creation method
4. Choose the table from which to run evaluations (for example, "Incidents")
5. Enter the maximum number of records to include in the evaluation
6. Add any desired filters to narrow the dataset scope

Important Note

The agentic evaluation consumes 1 assist per record processed during evaluation.

![MariaGabriela_3-1772219810456.png](https://www.servicenow.com/community/image/serverpage/image-id/504050i4CDD70CF0A3FE509/image-size/large?v=v2&px=999 "MariaGabriela_3-1772219810456.png")

### Add Workflow Instructions

1. Navigate to the "Add instructions" section
2. Enter your instruction using dynamic field references (for example, "Investigate {{incident.number}}")
3. Use the pill picker on the right side to select the correct table field
4. Click Continue to proceed to the review stage
![MariaGabriela_4-1772219827539.png](https://www.servicenow.com/community/image/serverpage/image-id/504051i701EBA840DE4D11C/image-size/large?v=v2&px=999 "MariaGabriela_4-1772219827539.png")

## Review and Launch Evaluation

### Review Configuration Summary

1. Examine all configuration details on the "Review summary" page
2. Verify that the workflow, metrics, dataset, and instructions are correctly configured
3. Click "Start evaluation" in the lower-right corner when ready to begin

Processing Time Note

The execution log generation process may take some time to complete depending on the dataset size.

![MariaGabriela_5-1772219840451.png](https://www.servicenow.com/community/image/serverpage/image-id/504052iD367E3A50DD86A60/image-size/large?v=v2&px=999 "MariaGabriela_5-1772219840451.png")

### Monitor Evaluation Progress

1. Wait for the execution log generation to complete
2. Verify that the "Start Evaluation" button becomes available
3. Click the button to initiate the evaluation run

Evaluation Duration Note

The evaluation process may take a considerable amount of time depending on the number of records.

![MariaGabriela_6-1772219851136.png](https://www.servicenow.com/community/image/serverpage/image-id/504053i0E4335F08DD803F3/image-size/large?v=v2&px=999 "MariaGabriela_6-1772219851136.png")

## Review Evaluation Results

### Analyze Performance Data

1. Access the Overview tab to view high-level performance metrics
2. Switch to the Detailed Results tab for granular analysis of individual evaluations
3. Review specific execution details and metric scores for each evaluated record

![MariaGabriela_7-1772219871229.png](https://www.servicenow.com/community/image/serverpage/image-id/504054i26E1AB310AF5A863/image-size/large?v=v2&px=999 "MariaGabriela_7-1772219871229.png")  
![MariaGabriela_8-1772219875143.png](https://www.servicenow.com/community/image/serverpage/image-id/504055i80B0A197E1279D08/image-size/large?v=v2&px=999 "MariaGabriela_8-1772219875143.png")  

### Access Documentation

For comprehensive information on agentic evaluations, visit the ServiceNow documentation at: [https://www.servicenow.com/docs/r/intelligent-experiences/execute-aia-eval.html](https://www.servicenow.com/docs/r/intelligent-experiences/execute-aia-eval.html)

## Troubleshooting

### Verify Prerequisites and Permissions

1. Confirm that all configuration steps have been completed in sequence
2. Verify that you have the appropriate entitlements to use Now Assist AI Agents
3. Check that AI Search has been enabled in your instance
4. Ensure the Now Assist Panel is turned on and accessible

### Update Required Components

1. Navigate to the store apps section and verify all apps are updated to the latest version
2. Sync the plugins manager page to retrieve the most recent plugin versions
3. Repair plugins after updating to ensure changes and fixes take effect properly

### Check System Properties and Roles

1. Verify that the system property `sn_ais_assist.dpr_ingestion_completed` is set to true
2. Confirm your user account has the necessary roles for agent access
3. Ensure the agent configuration allows the expected roles for user access and data access

### Additional Troubleshooting Steps

1. Log out of your ServiceNow instance and log back in after making configuration changes
2. Clear browser cache if interface elements are not displaying correctly
3. Contact Now Support by logging a case if issues persist after completing all troubleshooting steps

## More Training & Reference Material

ServiceNow University

[Now Assist AI Agents Deep Dive](https://learning.servicenow.com/lxp/en/now-platform/now-assist-ai-agents?id=learning_path_prev&path_id=072bbda947606694db63fb25126d4332)

Contains Essentials course and hands-on labs.

Now Assist Community

[Now Assist in AI Agents – Resource Guide](https://www.servicenow.com/community/now-assist-articles/now-assist-in-ai-agents-resource-guide-updated-december-25/ta-p/3450997)

Community articles, FAQ/troubleshooting, prompting guide, and advanced features.

More? Use AI Agents for employee self-service

[Activating self-service AI Agents for a great employee experience](https://www.servicenow.com/community/now-assist-articles/activating-self-service-ai-agents-for-a-great-employee/ta-p/3518614)

Documentation

Version history

Last update:

04-01-2026 02:12 PM

Updated by:

[Victor Chen](https://www.servicenow.com/community/user/viewprofilepage/user-id/119101)

Contributors