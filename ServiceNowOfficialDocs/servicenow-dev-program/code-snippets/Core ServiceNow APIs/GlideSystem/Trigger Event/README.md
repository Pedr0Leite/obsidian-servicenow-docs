---
title: "Trigger Event"
aliases:
  - Trigger Event
tags:
  - servicenow-dev-program
  - code-snippet
  - trigger-event
  - glidesystem
---

This shows the example of triggering the event using the gs.eventQueue() or gs.eventQueueScheduled()

eventQueue() - This method inserts an specified event in an event queue
 
 - Event name. Enclose the event name in quotes.
 - GlideRecord object, typically current but can be any GlideRecord object from the event's table.
 - Any value that resolves to a string. This is known as parm1 (Parameter 1). Can be a string, variable that resolves to a string, or method that resolves to a string.
 - Any value that resolves to a string. This is known as parm2 (Parameter 2). Can be a string, variable that resolves to a string, or method that resolves to a string.
 - (Optional) Name of the queue to manage the event.


eventQueueScheduled(String name, Object instance, String parm1, String parm2, Object expiration)

 - Event name. Enclose the event name in quotes.
 - GlideRecord object, typically current but can be any GlideRecord object from the event's table.
 - Any value that resolves to a string. This is known as parm1 (Parameter 1). Can be a string, variable that resolves to a string, or method that resolves to a string.
 - Any value that resolves to a string. This is known as parm2 (Parameter 2). Can be a string, variable that resolves to a string, or method that resolves to a string.
 - (Optional) GlideDateTime object or a date/time type element that specifies the date and time to process the event.

 Using eventQueue() we can specify our own event queue - which makes the event processing faster as we specify a dedictaed queue for the same. But if we are using the eventQueueScheduled this is not possible as we have to provide the time when the event should trigger.

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideSystem/Impersonate/README|Impersonate]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideSystem/Session/README|Session]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideSystem/Table/README|Table]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideSystem/User Display Name/README|User Display Name]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideSystem/User/README|User]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Core ServiceNow APIs/GlideSystem/date-time/README|date-time]]
