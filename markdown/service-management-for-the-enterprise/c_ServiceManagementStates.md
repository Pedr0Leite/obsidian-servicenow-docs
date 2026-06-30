---
title: Service management states
description: From creation until closure, SM application requests for work \(for example, work orders and facilities requests\), and their respective tasks follow a life cycle tracked by the State field in Field Service Management and Facilities Service Management.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/service-management-for-the-enterprise/c\_ServiceManagementStates.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Service Management]
---

# Service management states

From creation until closure, SM application requests for work \(for example, work orders and [[c_FacilitiesRequests|facilities requests]]\), and their respective tasks follow a life cycle tracked by the **State** field in Field Service Management and [[FacilitiesLandingPage|Facilities Service Management]].

The life cycle is controlled through business rules and UI actions that are updated by the system automatically.

**Note:** The **State** field on the record is always read-only.

-   **[[c_StateFlowCustomization|State flow customization]]**  
State flows control the sequence in which records transition between states in Service Management applications.
-   **[[t_StateFlowExample|State flow example]]**  
Your business processes might require work order tasks to be accepted automatically when dispatched to an agent.
-   **[[c_ImpDsblStFl|Implications of disabling SM state flows]]**  
State flows are used by SM applications to control how a work order or request automatically transitions from one state to the next. When state flows are disabled, various aspects of the ServiceNow system are also changed, as described here.

**Parent Topic:**[[c_ServiceManagement|Service Management]]

**Related topics**  


[bundle-fsm.t_CustomizeAStateFlow]

## Related

- [[c_StateFlowCustomization|State flow customization]]
- [[t_StateFlowExample|State flow example]]
- [[c_ImpDsblStFl|Implications of disabling SM state flows]]
- [[c_ServiceManagement|Service Management]]
- [[c_FacilitiesRequests|Facilities requests]]
- [[FacilitiesLandingPage|Facilities Service Management]]
