---
title: Run a scheduled job to generate an application model for business applications
description: Execute a script to generate the application model for existing business applications. An application model is a structured representation of a business application's components and their relationships and interactions within your application landscape.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-portfolio-management/eaw-run-job-gen-model-id-ba.html
release: australia
topic_type: task
last_updated: "2026-02-25"
reading_time_minutes: 1
breadcrumb: [Working with an application portfolio, Working with Portfolio list view, Managing Enterprise Architecture Workspace, Enterprise Architecture Workspace, Enterprise Architecture]
---

# Run a scheduled job to generate an application model for business applications

Execute a script to generate the application model for existing business applications. An application model is a structured representation of a business application's components and their relationships and interactions within your application landscape.

## Before you begin

Role required: admin

## About this task

In [[ea-workspace|Enterprise Architecture Workspace]], the application model is denoted by **Model ID** field for a business application. This model is important for creating the application model life cycle for a business application. For existing business applications, you can run the **CSDM Product Model Assignment** script to generate the Model ID.

## Procedure

1.  Navigate to **All** &gt; ** System Definition ** &gt; ** Scheduled Jobs**.

2.  Find and open the  scheduled job **CSDM Product Model Assignment**.

3.  Select  ** Execute Now**.


## Result

After executing the script, the system automatically creates models IDs for the existing business applications for which the **Model ID** field is empty.

**Parent Topic:**[[eaw-work-with-application-portfolio|Working with an application portfolio]]

## Related

- [[eaw-work-with-application-portfolio|Working with an application portfolio]]
- [[ea-workspace|Enterprise Architecture Workspace]]
