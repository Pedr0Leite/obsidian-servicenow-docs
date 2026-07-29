---
title: "How to configure Appointment Booking for custom table from portal"
aliases:
  - KB0868565
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0868565
kb_number: KB0868565
last_modified: 2024-05-16
---

## How to configure Appointment Booking for custom table from portal

  

**Appointment Booking from portal** 

Install Appointment Booking plugin (ID : com.snc.appointment\_booking)

**Step#1: Catalog Item**

Appointment booking is supported for task extended tables. A task record has to be created before any appointment record. Task records will be created by the record producers.

You can use any Record Producer of your choice / create a new record producer. (Refer: Catalog Information -> Catalog item).

Make sure you use proper variables for generating task record.

Note that we use this catalog item in our Step#3 while creating Appointment Booking Service Configuration.

In order to get Appointment Booking widget inside the catalog item, add **“sn\_appointment\_variable\_set”** as a variable set.

**Step#2: (Create Appointment Booking Configuration)**

Navigate to Appointment Booking  ->  Appointment Booking Configuration

Click on NEW button and create the following Configuration

_(I’m using CHANGE REQUEST Table in this example)_

![Appointment Booking Configuration](sys_attachment.do?sys_id=27e2e55fdbcde010fa192183ca9619e9 "Appointment Booking Configuration")

"Availability Method" represents the method with which the slots are determined. 

This has 2 choices. They are :

1\. Number of appointments per slot

2\. Scripted (Make sure the scripted method returns JSON in this format)

```
{
  "success": true,
  "data": [
    {
      "start_date": "2020-12-17 13:00:00",
      "end_date": "2020-12-17 15:00:00",
      "start_date_display": "13:00",
      "end_date_display": "15:00",
      "start_dateUTC": "2020-12-17 21:00:00",
      "end_dateUTC": "2020-12-17 23:00:00",
      "available": false
    },
    {
      "start_date": "2020-12-17 15:00:00",
      "end_date": "2020-12-17 17:00:00",
      "start_date_display": "15:00",
      "end_date_display": "17:00",
      "start_dateUTC": "2020-12-17 23:00:00",
      "end_dateUTC": "2020-12-18 01:00:00",
      "available": true
    },
  ],
  "hasMore": false,
  "noApptAvailable": false,
  "timeZone": "America/Los_Angeles",
  "timeZoneDisplayValue": "America/Los_Angeles",
  "errorCode": "",
  "msgType": "success"
}
```

**Step#3: (Create Appointment Booking Service Configuration)**

From the above Configuration, Click on New Button.

And fill in the form with something like shown below:

Note that Catalog item mentioned in step#1 is filled here.

![Appointment Booking Service Configuration](sys_attachment.do?sys_id=79d3a513db012410fa192183ca961972 "Appointment Booking Service Configuration")

**Step#4: Create a Variable for User contact field**

Notice in Step#3 we are setting “Requested by” as “User Contact". This signifies about who requested appointment.

This variable can change as per the task table.

For change request, setup the fields as:

**Type**: Reference

**Catalog Item** : (Given in #3 – changeRequestCatalog)

**Mandatory**: True

**Active**: True

**Question**: Requested by

**Name**: requested\_by

**Reference**: User \[sys\_user\]

**User reference qualifier** : simple

This can change to ‘caller\_id’ for incident table, ‘caller’ for wm\_order table etc., This varies based on the business requirement. Also, please not that only sys\_user reference columns are supported for this.

**Step#5: Navigate to record producer and click on Tryout/Preview item**

![Catalog Preview](sys_attachment.do?sys_id=00d21eab1b6c301017d162c4bd4bcb96 "Catalog Preview")

Upon submitting, a new change request record will be created.

In order to get a new record in ‘Appointment booking (sn\_apptmnt\_booking\_appointment\_booking)' table, a script needs to be added in a before business rule, on the insert of task table listed in the record producer.

Here, it will be a before business rule on insert of change request table. This script should contain code for creating a new Appointment record.

For example, we can use the below script, which only creates appointment record, shall customize the code based on the requirement, with additional availability checks.

```
    var sn_appointment = current.variables.sn_appointment;
    var helper = new sn_apptmnt_booking.AppointmentBooking_Factory().getWrapperType(sn_apptmnt_booking.AppointmentBookingConstants.APPOINTMENT_BOOKING_IMPL);
    var sn_appointmentJSON = JSON.parse(sn_appointment);
    // creating an appointment <br>
    var appointmentId = helper.submitAppointmentFromPortal(sn_appointment, current, sn_appointmentJSON.config.opened_for, sn_appointmentJSON.config.location, current.short_description);
```

Also, we can use flow designer instead of business rules. For further reference, check ‘Create Appointment’ business rule on ‘wm\_order’ table.

On successful addition of Business rule / flow, appointment record will be created.

![Appointment Bookings](sys_attachment.do?sys_id=fe15a157db012410fa192183ca9619b8 "Appointment Bookings")
