---
title: Create an observable from a case
description: New observables can be created from cases in Security Case Management.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/security-management/create-an-observable-from-a-case.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [IoCs and observables in cases, Case creation from security artifacts, Security Case Management, Threat Intelligence, Enterprise security case management applications, Security Operations]
---

# Create an observable from a case

New [[c_Observables|observables]] can be created from cases in [[case-mgmt|Security Case Management]].

## Before you begin

Role required: sn\_ti.case\_user

## Procedure

1.  Navigate to **All** &gt; **[[threat-intel-landing-page|Threat Intelligence]]** &gt; **Case Management** &gt; **All Cases**.

    The Security Cases list opens.

2.  Either open an existing case or click **New** to [[create-cases-in-case-mgmt|create a new case]].

3.  Click the **Case Artifacts** related link and click the **Observables** tab.

4.  Click **New** and enter the requested information.

    |Field|Description|
    |-----|-----------|
    |Value|\[Read only\] The case number.|
    |Observable type|Enter a descriptive name for the case.|
    |Observable type category|Select the type of case being investigated.|
    |Incident count|Select the importance of this case \(from Critical to Low\).|
    |Finding|\[Read only\] The date and time the case was last updated.|
    |Notes|A brief description of the case.|

5.  Click the **Additional Case Details** tab.

6.  Fill in the fields as appropriate.

    |Field|Description|
    |-----|-----------|
    |Created by|\[Read only\] The name of the user who created this case.|
    |State|The current state of the case. At case creation, the State defaults to Draft.|
    |Work notes list|Click the check box to display the work notes in the Additional Case Details section of the case record.|
    |Work Notes|If needed, type a work note for the case. If the **Work notes list** is selected, the work note appears in the Additional Case Details section of the case record.|

7.  Click **Submit**.

    As needed, you can click the **Case Artifacts** tab and [[add-records-to-cases|add artifacts to the case]].


**Parent Topic:**[[cases-in-threat|IoCs and observables in cases]]

**Related topics**  


[Create a case from IoCs or observables]()

[Add IoCs and observables to an existing case]()

[Run a [[indicator-sightings|sightings]] search on observables in a case]()

## Related

- [[create-cases-in-case-mgmt|Create cases in Security Case Management]]
- [[add-records-to-cases|Add artifacts to a case]]
- [[cases-in-threat|IoCs and observables in cases]]
- [[c_Observables|Observables]]
- [[case-mgmt|Security Case Management]]
- [[threat-intel-landing-page|Threat Intelligence]]
- [[indicator-sightings|Sightings]]
