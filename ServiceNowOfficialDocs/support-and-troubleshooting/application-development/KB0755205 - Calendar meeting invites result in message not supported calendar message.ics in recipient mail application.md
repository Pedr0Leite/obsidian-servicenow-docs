---
title: "Calendar meeting invites result in message \"not supported calendar message.ics\" in recipient mail application"
aliases:
  - KB0755205
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755205
kb_number: KB0755205
last_modified: 2024-04-30
---

## Issue

## Overview

ServiceNow supports basic calendar invitations by the use of notifications set to 'Meeting Invite' type. The notification template in this case contains specially formatted text which conforms to the [iCalendar specification](https://icalendar.org/RFC-Specifications/iCalendar-RFC-5545/ "iCalendar specification"). The base system templates only use a small subset of the available iCalendar attributes.

When ServiceNow generates an invitation, it uses the data in the calendar template, inserts data from referenced fields and produces the email data representing that calendar invite.

See ServiceNow documentation [here](https://docs.servicenow.com/csh?topicname=t_CRiCalendarInvCustomTables.html&version=latest "here").

If any values in the calendar notification template produce an out-of-specification iCalendar invitation, the message  "not supported calendar message.ics" may appear in Outlook. Other mail applications may display a different message.

## ICalendar Specification

A notification template associated to a notification of type "Meeting Invitation" MUST conform do the iCalendar specification. If it does not, there is a lower chance a receiving email client will be able to interpret it.

An example of an iCalendar invite sent in the email data is given on the [iCalendar site,](https://icalendar.org/ "iCalendar site") In general, it looks like this:

BEGIN:VCALENDAR
<lots of stuff between the start and end, from the specification>
END:VCALENDAR

### ICalendar Extensions

iCalendar specification allows third parties to define their own headers in a calendar invite. For example, Microsoft defines a number of their own headers understood by Microsoft products (like Outlook or Exchange). Headers of this type are free to be ignored by other vendor's products, as their products are unaware of the data and its meaning.

These values, too, must conform to that vendor's specification for that header. If the value is out-of-range or does not in some way conform to the third-party vendor's specification, it is possible the iCalendar invitation cannot be interpreted by the email recipient's email application. Some third-party headers may not publish and support their extensions for general public reliance. While you are free to add any valid header into one of these templates in your implementation, you are responsible to ensure the correct values are supplied to cause the desired effect in the vendor's email software.

### Third-Party Compatibility Issues

Sometimes a meeting invite will be interpreted by one product (e.g., Gmail) but not another product (e.g., Outlook). This may be because

a) A product may be written to be stricter in what it accepts and rejects the smallest non-compliance. Another product may be less strict and ignore non-compliant data, but still accept the invitation.

b) When vendor-specific headers are used, that vendor's product may reject invalid data, while a non-vendor product ignores that vendor's headers because it knows nothing about them, and thus accepts the overall invitation.

c) Microsoft provides a few articles for Outlook/Exchange issues in particular

-   [this article](https://support.microsoft.com/en-nz/help/2643084/outlook-receives-a-message-that-has-an-attachment-that-is-named-not-su "this article") and which may provide additional help in certain very specific circumstances with lotus notes
-   [this article](https://support.microsoft.com/en-us/help/4456241/you-receive-a-meeting-request-that-has-not-supported-calendar-message "this article") relating to RRULE and RDATE iCalendar headers if used. (These are not used in the base system's meeting invites.)

## Debugging a Calendar Issue

The most likely explanation is that the iCalendar data produced by the calendar invite somehow does not conform to the specification (RFC-5545)

By opening the "not supported calendar.ics" file from the receipient in a text editor application and reviewing its content, you will be looking at the calendar invite raw data generated from the instance.

You can review the legal values for each of the provided headers of the invite

### Field Substitutions in iCalendar data

Sometimes a calendar invite will use a field substitution to assign a record's value into the iCalendar header value. This can cause a subtle bug as follows.

Remember that the iCalendar specification (or a vendor's specification in the case of extensions) governs what values are acceptable for a given header. For example, the "Priority" header is defined [here](https://icalendar.org/iCalendar-RFC-5545/3-8-1-9-priority.html "here") in the iCalendar specification

"This priority is specified as an integer in the range 0 to 9. A value of 0 specifies an undefined priority. A value of 1 is the highest priority. A value of 2 is the second highest priority. Subsequent numbers specify a decreasing ordinal priority. A value of 9 is the lowest priority.

When the meeting invite template shows a field substitution value, the data produced must be valid for that iCalendar specified value. For example, if this field substitution:

PRIORITY: ${priority}

produces this in the iCalendar sent to the recipient:

PRIORITY: 3 - Medium

then the value does not conform to the iCalendar specification for legal values for "Priority". Depending on the receiving email application's level of strict interpretation, it may not accept this as a valid meeting invite.

Every line in an iCalendar specification is similarly defined.

### iCalendar Validator

The iCalendar web site also provides a [validator page](https://icalendar.org/validator.html "validator page"), so you can paste the generated email data to ensure it conforms to the specification. If you identify any data that does not conform to the specification, update the meeting invite template with the correctly formatted data. Be sure any data submitted to this third party site does not violate your company's data handling policies.
