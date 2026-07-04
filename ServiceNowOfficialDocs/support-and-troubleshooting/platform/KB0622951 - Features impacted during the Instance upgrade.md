---
title: "Features impacted during the Instance  upgrade"
aliases:
  - KB0622951
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0622951
kb_number: KB0622951
last_modified: 2025-07-07
---

## Issue

Users can, on occasion, experience minor functional issues arising from accessing functionality touched by many plugins. User-facing functional issues are usually transitory and can often be resolved with a simple browser refresh.

However, while an upgrade is running, the system cannot be guaranteed to run every business process perfectly, especially those that run continuously. For that reason, some features run less or not at all during the instance upgrade. This article describes some of those features, especially platform features on which many applications rely.

This article also highlights a few frequently asked about features; it is not an exhaustive list.

This article provides a general guideline for what is expected to run and not run during the instance upgrade and is for informational purposes only. This article should not be taken as definitive doctrine and is certainly not the final authority on this subject. This article does not account for:

-   all functionality potentially affected during the entire upgrade process
-   customizations made to base version functionality
-   third party integrations

This article may not include recent product changes.The Now Platform performs upgrades without instance downtime or hard-down service interruption. Users are able to interact with the service and often are unaware that an upgrade is taking place.

## Resolution

#### Connect

-   Connect runs during the database upgrade

#### Discovery

-   During the instance upgrade, the Discovery events are not processed in order to not change the CMDB while it is being upgraded
-   After the upgrade is complete, the Discovery events are processed and catch up

#### Event Management (em\_event)

-   Event management is sometimes confused with Platform Events (For more information, see the Platform Events section below.)
-   Event management runs during the instance upgrade

#### Legacy Chat

-   Legacy Chat runs during the database upgrade

#### MID Server

-   The MID servers run during instance upgrade (heartbeat, etc.). However, since discovery schedules are not running, they are not given additional work to do and only complete the jobs they already have
-   After the instance upgrade is complete, the MID servers start to upgrade to match the current version running on the Instance. They power-cycle as they upgrade, and discovery schedules are not processed while that is happening. Under normal circumstances, the MID server upgrade completes in a few minutes

#### Platform Events (sysevent) and Email

-   Platform events are sometimes confused with Event Management (For more information, see the Event Management section above.)
-   The event processor runs during the instance upgrade, however, only email related events are processed
-   Email generation for outbound notifications and inbound email processing are both fired from events in the event queue
-   Scheduled Jobs interact with email servers and are writing/reading sys\_email records
-   Any other email generation mechanism is dependent on the process or business logic that uses it. That process would therefore need to be running during the database upgrade to see the email created by that process. For example, scheduled reports are not emailed during the database upgrade because the scheduled reports are not "upgrade safe" and therefore do not run
-   For the other events, the state is marked as “encore\_ready,” which indicates that they have been preprocessed
-   The reason we do not process non important events during upgrade is that event processors continuously use many different features of the platform, unlike end users. An event processor is much more likely to process one or more events incorrectly during brief periods of metadata inconsistency than end user transactions are. We want to reduce the risk whereby (for example) an event triggers a script action that may be invoking logic that is being changed by the upgrade
-   After the upgrade is completed and the system resumes normal operations, the event delegator moves the events to the “resumed” state. The event processor then completes the processing of these resumed events and on successful completion marks them as “processed”

#### Scheduled Jobs (sys\_trigger)

-   Only “Upgrade safe” scheduled jobs are processed during the instance upgrade
-   Do not change the upgrade\_safe flag on any record to upgrade\_safe=true
-   All custom sys\_triggers **must** be marked upgrade\_safe=false
-   After the instance upgrade is complete, upgrade unsafe jobs are processed and catch up

#### Text Indexing

-   Text Indexing does not run during the instance upgrade
-   After the instance upgrade is complete, Text Indexing is processed and catches up

#### Workflows and SLA

Workflow, as an Engine, runs during the instance upgrade. However, the Timer workflows and the SLA Percentage Timer workflows are scheduled jobs in sys\_trigger and they do not run during an upgrade window as they are not "upgrade safe."

-   User transaction thread workflows execute during the database upgrade
-   After the instance upgrade completes, the Timer workflow and SLA Percentage Timer workflow scheduled jobs are processed and catch up
