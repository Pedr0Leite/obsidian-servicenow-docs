---
title: "Find MRVS Total"
aliases:
  - Find MRVS Total
tags:
  - servicenow-dev-program
  - code-snippet
  - find-mrvs-total
  - business-rules
---

# Server-Side MRVS Total Calculator
This ServiceNow Business Rule automatically calculates the sum of a numeric field from all rows within a Multi-Row Variable Set (MRVS) after a catalog item has been submitted.
It populates a separate variable with the calculated total, making the value easily accessible for flows, reports, and integrations without needing to parse the MRVS JSON every time. This script is designed to run on the back-end, ensuring the total is accurate and persistent.

## How to Implement
Follow these steps to configure the Business Rule in your instance.

### 1. Prerequisites
Before creating the rule, make sure you have the following variables on your Catalog Item:

- A Multi-Row Variable Set (e.g., named item_details).
- A variable inside the MRVS that will contain a number (e.g., named quoted_price).
- A single variable outside the MRVS to store the final sum (e.g., a Single Line Text variable named total_estimate).

### 2. Business Rule Configuration
Create a new Business Rule with the following settings:
- Name: A descriptive name like Calculate MRVS Total on RITM.
- Table: Requested Item [sc_req_item].
- Advanced: Check this box to reveal the script field.
- When to run:
  - When: Before
  - Insert: true
  - Update: true

Copy and paste the script from `mrvs_total_sum.js` into the Script field within the Advanced tab of your Business Rule.

Before saving, you must update the three configuration variables at the top of the script to match your specific setup. 
You will need to set the following:
- `VARIABLE_NAME_TO_POPULATE_WITH_SUM` to the internal name of your total variable
- `MRVS_INTERNAL_NAME` to the internal name of your Multi-Row Variable Set
- `MRVS_VARIABLE_NAME_TO_SUM` to the internal name of the numeric variable inside the MRVS that you want to sum.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/ATF Duplicate Execution Order/README|ATF Duplicate Execution Order]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Abort Parent Incident Closure When Child is Open/README|Abort Parent Incident Closure When Child is Open]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add HR task for HR case/README|Add HR task for HR case]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add itil role to ootb user query to also see inactive users/README|Add itil role to ootb user query to also see inactive users]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add notes on tag addition or removal/README|Add notes on tag addition or removal]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Business Rules/Add or remove a tag from the ticket whenever the comments are updated/README|Add or remove a tag from the ticket whenever the comments are updated]]
