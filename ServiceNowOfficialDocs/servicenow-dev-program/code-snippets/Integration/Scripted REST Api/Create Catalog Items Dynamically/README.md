---
title: "Create Catalog Items Dynamically"
aliases:
  - Create Catalog Items Dynamically
tags:
  - servicenow-dev-program
  - code-snippet
  - create-catalog-items-dynamically
  - scripted-rest-api
---

# ServiceNow Catalog Builder API  
**Automate Catalog Item Creation with a Single REST Call**

---

## Overview

The **ServiceNow Catalog Builder API** is a custom **Scripted REST API** that dynamically creates Service Catalog Items in your instance — including variables and choices — from a simple JSON payload.  

This API eliminates the repetitive manual work of configuring Catalog Items one by one, and makes it possible to **automate catalog creation programmatically** or **integrate it with CI/CD pipelines, GitHub workflows, or external systems**.

---

## Key Features

Automatically create **Catalog Items** in `sc_cat_item`  
Dynamically generate **Variables** and **Choices**  
Supports **category mapping** and **item ownership**  
Extensible design for **flows, icons, and attachments**  
Developer-friendly — fully JSON-driven  

---

## Use Case

This API is perfect for:
- **Admin Automation:** Auto-build standard catalog forms during environment setup.  
- **RPA / CI Pipelines:** Integrate with DevOps or GitHub Actions to deploy catalog definitions.  
- **Dynamic Service Portals:** Allow external apps or portals to create items on demand.  

Example:  
A company wants to auto-create 10 new service catalog items from a GitHub configuration file.  
Using this API, they simply call one REST endpoint for each definition — no manual clicks needed.

---

## Scripted REST API Details

| Property | Value |
|-----------|--------|
| **Name** | Catalog Builder API |
| **API ID** | `x_demo.catalog_creator` |
| **Resource Path** | `/create` |
| **Method** | POST |
| **Authentication** | Basic Auth / OAuth |
| **Tables Used** | `sc_cat_item`, `item_option_new`, `question_choice` |

---

## Logic Flow

1. **Receive JSON input** with item name, category, and variables.  
2. **Create a new record** in `sc_cat_item`.  
3. **Loop through variables** and create them in `item_option_new`.  
4. If the variable type is `select_box`, create **choices** automatically.  
5. Return a JSON response with the new item’s `sys_id` and success message.  

---

## Example Input (POST Body)

```json
{
  "name": "Request New Laptop",
  "category": "Hardware",
  "short_description": "Laptop provisioning request form",
  "description": "Allows employees to request a new laptop with model and RAM options.",
  "owner": "admin",
  "variables": [
    {
      "name": "Laptop Model",
      "type": "select_box",
      "choices": "Dell,HP,Lenovo"
    },
    {
      "name": "RAM Size",
      "type": "select_box",
      "choices": "8GB,16GB,32GB"
    },
    {
      "name": "Business Justification",
      "type": "multi_line_text"
    }
  ]
}


## Example Output:
{
  "catalog_sys_id": "b2f6329cdb6d0010355b5fb4ca9619e2",
  "message": "Catalog item created successfully!"
}
After the API call:
A new Catalog Item appears under Maintain Items.
The item contains:
Short Description: Laptop provisioning form
Variables: Laptop Model, RAM Size, Business Justification
Choices: Auto-populated for select boxes
The item is active and ready to use in the catalog.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_definition_config|sys_ws_definition_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Scripted REST API/sys_ws_operation/sys_ws_operation_config|sys_ws_operation_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval APIs/README|Approval APIs]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/Approval on Behalf/README|Approval on Behalf]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CMDB API/README|CMDB API]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/Scripted REST Api/CURL Script to create incident via tableAPI/README|CURL Script to create incident via tableAPI]]
