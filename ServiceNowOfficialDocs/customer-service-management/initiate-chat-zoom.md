---
title: Initiate Zoom meetings from chats
description: Resolve issues faster by initiating a Zoom meeting directly from a customer chat using the Chat Zoom Connector application.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/initiate-chat-zoom.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Using Chat Zoom Connector, Customer communication, Use, Customer Service Management]
---

# Initiate Zoom meetings from chats

Resolve issues faster by initiating a Zoom meeting directly from a customer chat using the [[chat-zoom-connector|Chat Zoom Connector]] application.

## Before you begin

Ensure that an administrator has installed and set up the Chat Zoom Connector application. For more information, see [[config-chat-zoom-connector|Configure Chat Zoom Connector]].

Role required: agent\_workspace\_user

## About this task

You can use a Zoom meeting to host a screen-sharing or video conference. You can also record the meeting and save the recordings.

## Procedure

1.  Navigate to **Agent Workspace**.

2.  Accept and respond to a chat from your agent inbox.

3.  Ask questions and find out more about the issue.

4.  To start a Zoom session with a customer, click the quick actions icon \(\[Omitted image "quick-actions.png"\] Alt text: Quick Actions icon\), and then select **/zoom**.

    **Tip:** You can also enter `/zoom` in the text field of the chat.

5.  Click the send icon \(\[Omitted image "send.png"\] Alt text: Send icon.\).

    A message announcing that the Zoom meeting has started and one containing the meeting URL are posted in the chat window for both agent and customer. If the session was initiated through the Private Chat tab, the session's URL isn't shared with the customer.

6.  Click the URL to host the Zoom meeting and request the customer to click the URL too.

    As a host of the meeting, you can admit participants by sharing the meeting URL with them. The number of participants you can admit depends on your Zoom account settings.

    The meeting topic is set to the number of the associated chat interaction record. The meeting description is set to the short description of the associated chat interaction record. If the short description of the associated chat interaction record is empty, the meeting description is shown as a dash \(-\).

7.  Record the meeting.

    For more information, see the [Zoom Help Center](https://support.zoom.us/hc/en-us).


## Result

An interaction record of type **Zoom** is generated for the meeting that captures the Notify conference call details for this Zoom session. A Notify administrator or agent manager can access the conference call details associated with the Zoom meeting from the interaction record.

**Note:** The conference call number is a value automatically generated in the **Channel Metadata Record** field on the Interaction form. For more information, see [[view-details-chat-zoom|View details for Zoom meetings initiated from chats]].

The recording URL of the Zoom meeting is added to the [[csm-config-ws-activity-stream|activity stream]] of the interaction record.

## Related

- [[config-chat-zoom-connector|Configure Chat Zoom Connector]]
- [[view-details-chat-zoom|View details for Zoom meetings initiated from chats]]
- [[chat-zoom-connector|Chat Zoom Connector]]
- [[csm-config-ws-activity-stream|Activity stream]]
