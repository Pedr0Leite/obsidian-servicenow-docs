---
title: "Appointment Booking is not working on Order Guides."
aliases:
  - KB0714468
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714468
kb_number: KB0714468
last_modified: 2024-10-12
---

## Issue

Appointment Booking is not working on Order Guides.

## Resolution

This is by Design.

Appointment Booking uses the '_sn\_appointment\_variable\_set_' Variable Set.

This Variable Set uses the '**appointmentBooking\_SelectMacro**' UI Macro to book the appointment.

This UI Macro is designed to work only on Catalog Items. This is not designed to work on Order Guides.

There is an Enhancement Request FTASK39904 to extend the support for Order Guide.
