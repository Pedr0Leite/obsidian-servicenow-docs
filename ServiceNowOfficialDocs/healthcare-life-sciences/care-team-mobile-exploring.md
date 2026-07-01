---
title: Exploring Care Team Mobile
description: Discover how to use the Care Team Mobile application to create requests for care team support departments from the convenience of your mobile device.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/healthcare-life-sciences/care-team-mobile-exploring.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Care Team Mobile, Healthcare Operations, Healthcare and Life Sciences]
tags:
  - healthcare-life-sciences
  - type-concept
---

# Exploring Care Team Mobile

Discover how to use the [[care-team-mobile-landing|Care Team Mobile]] application to create requests for care team support departments from the convenience of your mobile device.

## Care Team Mobile overview

The Care Team Mobile application is designed to streamline the reporting and tracking of operational issues for care team members. Care Team Mobile enhances efficiency by enabling care team members to report and track the status of any case directly from their smart phones or tablets. This application saves time on operational work management that they can then redirect to patient care.

Care Team Mobile includes the following features:

-   Asset tag scanning enables you to scan tags on medical equipment and be redirected to the asset's record, where they can view its history, status, and associated requests.
-   Browse locations to view healthcare location information and create support requests for specific locations as needed.
-   Secure mobile access through identity management solutions supports both hospital-provided and personal devices.

Care Team Mobile requires [[hcls-cto-app|Healthcare Operations Core]] and can be used with the following Care Team Operations plugins:

-   [[hcls-cto-it-app|Care Team Operations for Healthcare IT]]
-   [[care-team-operations-for-biomed|Care Team Operations for Biomed]]
-   [[cto-facilities-landing|Care Team Operations for Facilities]]
-   [[cto-evs-landing|Care Team Operations for Environmental Services]]

## Care Team Mobile users

|User|Description|
|----|-----------|
|Registered Nurse|Registered nurses are responsible for providing and coordinating patient care, administering medications and treatments, and collaborating with other healthcare professionals to develop and implement care plans. They use Care Team Mobile to create and track support requests for ancillary departments.|
|Nurse assistant|Nurse assistants provide basic care to patients in healthcare facilities, assisting with daily living, monitoring patient health, and providing vital support to nurses and medical staff. They use Care Team Mobile to create and track support requests for ancillary departments.|
|Unit Secretary|Unit secretaries provide administrative support to nursing units and facilitate communication between staff, patients, and families while maintaining patient records. They use Care Team Mobile to create and track support requests for ancillary departments.|

## Care Team Mobile workflow

\[Omitted image "cto-mobile-workflow.png"\] Alt text: An example workflow for Care Team Mobile wherein a care team member requests a linen change and a support agent fulfills it.

1.  An administrator installs Care Team Mobile on the care team's mobile devices alongside all relevant Care Team Operations applications.
2.  A nurse notices that a room needs a linen change and creates a request for the Environmental Services department using Care Team Mobile with the Care Team for Environmental Services plugin installed.
3.  A support agent from the Environmental Services department receives the request and proceeds to change the linens in the room. The support agent then marks the request as Complete using FSM Mobile or CSM/FSM Configurable Workspace.
4.  The nurse who created the request receives an alert that the linen change request was fulfilled and then accepts the solution.

## Care Team Mobile benefits

|Benefit|Feature|Users|
|-------|-------|-----|
|Create support requests based on installed [[healthcare-operations-overview|Healthcare Operations]] case types directly from your mobile device.|[[cto-mobile-create-requests|Create support requests using Care Team Mobile]]|Nurse, Nurse Assistant, Unit Secretary|
|Scan tags on medical equipment and be redirected to the asset's record, where you can view its history, status, and associated cases.|[[cto-mobile-asset-scan|Asset Scan in Care Team Mobile]]|Nurse, Nurse Assistant, Unit Secretary|
|View requests for specific locations, such as patient rooms or supply closets, and access relevant details and preconfigured workflows for reporting issues like sanitation requests or facility repairs.|[[cto-mobile-browse-locations|Browse locations in Care Team Mobile]]|Nurse, Nurse Assistant, Unit Secretary|

## What to explore next

To learn more about configuring and using Care Team Mobile, see:

-   [[care-team-mobile-configuring|Configure Care Team Mobile]]
-   [Create support requests using Care Team Mobile](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/healthcare-life-sciences/cto-mobile-create-requests.md)

## Related

- [[cto-mobile-create-requests|Create support requests using Care Team Mobile]]
- [[cto-mobile-asset-scan|Asset Scan in Care Team Mobile]]
- [[cto-mobile-browse-locations|Browse locations in Care Team Mobile]]
- [[care-team-mobile-configuring|Configure Care Team Mobile]]
- [[care-team-mobile-landing|Care Team Mobile]]
- [[hcls-cto-app|Healthcare Operations Core]]
- [[hcls-cto-it-app|Care Team Operations for Healthcare IT]]
- [[care-team-operations-for-biomed|Care Team Operations for Biomed]]
- [[cto-facilities-landing|Care Team Operations for Facilities]]
- [[cto-evs-landing|Care Team Operations for Environmental Services]]
- [[healthcare-operations-overview|Healthcare Operations]]
