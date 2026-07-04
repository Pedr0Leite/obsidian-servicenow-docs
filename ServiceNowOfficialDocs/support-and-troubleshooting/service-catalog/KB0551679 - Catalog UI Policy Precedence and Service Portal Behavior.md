---
title: "Catalog UI Policy Precedence and Service Portal Behavior"
aliases:
  - KB0551679
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551679
kb_number: KB0551679
last_modified: 2026-04-09
---

## Catalog UI Policy Precedence and Service Portal Behavior

  

### Issue

## 1\. Catalog UI Policy Overview

Catalog UI Policies apply to either:

-   A specific Catalog Item, or
-   Any Catalog Item that uses a specific Variable Set

A UI Policy may reference only those variables defined on the associated Catalog Item or Variable Set. UI Policies can modify variable properties, such as visibility, mandatory status, and read-only status, using UI Policy Actions or Client Scripts.

## 2\. UI Policy Execution Order and Precedence

Multiple UI Policies may apply to a single Catalog Item, including policies inherited from Variable Sets. When multiple policies affect the same variable, the final behavior is determined by execution order and policy type.

### 2.1 Order Field

Each UI Policy includes an Order field. Policies with lower numeric values run first; policies with higher values run later. The last policy to run determines the final state of the affected variables.

### 2.2 Catalog Item vs. Variable Set Precedence

Execution precedence between policy types is fixed:

-   Variable Set UI Policies run first
-   Catalog Item UI Policies run second

As a result, Catalog Item UI Policies always take precedence over Variable Set UI Policies, regardless of the Order field.

### 2.3 Exception: System Property Override

If the system property glide.sc.ui\_policiy.variable\_set\_run\_first is set to false, the execution order is reversed:

-   Catalog Item UI Policies run first
-   Variable Set UI Policies run second and therefore take precedence

### 2.4 Conflict Resolution

Conflicts between a Catalog Item UI Policy and a Variable Set UI Policy cannot be resolved by adjusting the Order field. The Order field only affects policies of the same type.

## 3\. Common Symptoms of UI Policy Conflicts

Administrators may observe the following behaviors:

-   A variable displays an unexpected value
-   A variable property (visibility, read-only, mandatory) does not match the intended configuration

These symptoms typically occur because the last executed UI Policy determines the final outcome.

**This is an example illustrating how UI policy works in Service Portal \-**  UI Policies Not Triggering After Save in Service Portal

When using the sp-variable-editor widget, Catalog UI Policies and Catalog Client Scripts may not re-run after clicking the Save button. This section describes the issue, reproduction steps, and a supported workaround.

After saving variable data in the Service Portal using the sp-variable-editor widget, UI Policies and Client Scripts do not automatically re-evaluate. As a result, variable visibility or other properties may not reflect the expected UI Policy logic until the page is refreshed.

## 1\. Steps to Reproduce

1.  Create a Service Portal page and add the sp-variable-editor widget.
2.  Create a Catalog Item with two variables (e.g., a Yes/No select box and a text field).
3.  Configure a Catalog UI Policy that hides the second variable unless the first variable is set to "Yes".
4.  Test the Catalog Item; the UI Policy behaves as expected.
5.  Open the RITM in the Service Portal using the sp-variable-editor widget.
6.  Click Save.
7.  UI Policies no longer run; the second variable becomes visible regardless of the first variable's value.
8.  Refresh the page; UI Policies function correctly again.

## 2\. Cause

The Save action in the sp-variable-editor widget does not trigger a UI Policy re-evaluation event. As a result, UI Policies and Client Scripts do not execute after saving variable data.

## 3\. Workaround

To ensure UI Policies re-run after saving:

1.  Open the Form widget (`sp_widget.do?sys_id=fd1f4ec347730200ba13a5554ee490c0`).
2.  Create a new Widget Dependency.
3.  Add a JS Include under the dependency.
4.  Create a new UI Script and paste the contents of the provided workaround file (`workaround2-kp3.js.txt`).
5.  Clone the sp-variable-editor widget.
6.  Add the new widget dependency to the cloned widget.
7.  In the cloned widget's Client Controller, add the following line after line 40:  
    $rootScope.$emit("sp.form.record.updated");
8.  This event triggers a re-evaluation of the UI Policy after the Save action.

### Release

All the versions included

### Resolution

To ensure the correct UI Policy behavior:

-   Review all Catalog Item and Variable Set UI Policies that apply to the item
-   Confirm that the policy intended to take precedence executes last
-   Adjust the system property if a different precedence model is required
