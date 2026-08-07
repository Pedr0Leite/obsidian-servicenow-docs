---
title: "Expected Transfer Order Line Task Behaviour When Field Service Management (FSM) Is Enabled"
aliases:
  - KB3013065
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3013065
kb_number: KB3013065
last_modified: 2026-05-12
---

## Issue

When Field Service Management (FSM) is installed, the Transfer Order Line (TOL) workflow dynamically determines      the fulfilment path at runtime based on stockroom and location configuration. As a result, task generation and state transitions may vary and can appear inconsistent, but this behaviour is expected and by design.

## Resolution

-   After closing Request for Fulfilment, FSM evaluates whether physical shipping is required.
-   If the stockroom and destination location are effectively the same, shipment is not needed. In this case:
    -   Shipment‑related tasks (Prepare for Shipment and Ship) are skipped
    -   The workflow proceeds directly through Receive and Deliver
        
        If the stockroom and destination location are different, shipment is required. In this case:
        
        -   Prepare for Shipment and Receive tasks may be generated simultaneously
        -   Closing Prepare for Shipment temporarily moves Receive to _Closed Skipped_ while Ship becomes active
        -   After Ship is completed, Receive is reopened and must be completed before Deliver is generated

This temporary skip and reopen of the Receive task allows FSM to support both shipping and non‑shipping fulfilment paths within the same out‑of‑box workflow.
