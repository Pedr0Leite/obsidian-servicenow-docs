---
aliases:
  - "Creating Custom MS Teams Cards"
area: "Integrations"
source: notion-export
tags:
  - teams-integration
  - flow-designer
  - script-include
  - integrations
  - adaptive-cards
---

# Creating Custom MS Teams Cards

## The Requirement

Today we were presented the challenge of:

*"We want an MS Teams notification sent to every member of an assignment group whenever a new incident is assigned to that group"*

I will probably write a separate post about the investigation 
into that but during the investigation into it I discovered something I 
thought was really cool.

## Sending a MS Team message from a script

ServiceNow has an API for firing teams messages that can be called form a custom flow action, business rule, wherever you like!

The
 Script include is called MSTeamsOutboundMessages but unfortunately its 
locked down. But looking into some other scipts I found 
that MSTeamsOutboundMessages().sendDirectMessage() takes three 
arguments:

- sys_id of the user who should receive the teams message
- the string "adaptiveCard"
- a JSON which is what tells teams what to display. The JSON is part
of "Adaptive Cards" which you can read all about
here https://adaptivecards.io/. There is even a GUI designer for
creating cards found here https://adaptivecards.io/designer/

Create the Flow in the "Microsoft Integrations - Core" Scope

Here is an example:

```jsx
var inc_number = "INC007"
var send_to = '00004934db486850e2bd49a239961949'
var priority = "P1"
var SD = "Short Description"
var record_id = "000024e1be38d906da0a798bd4bcbe9"

var card =
{
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "size": "Large",
            "weight": "Bolder",
            "text": "Incident has been assinged to your queue.\n ",
            "wrap": true
        },
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": priority + " " + inc_number,
            "wrap": true
        },
        {
            "type": "TextBlock",
            "text": SD,
            "wrap": true
        },
        {
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.OpenUrl",
                    "title": "View Ticket details",
                    "url": "https://xxxx.service-now.com/nav_to.do?uri=%2Fincident.do%3Fsys_id%3D" + record_id
                }
            ]
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3"
}

var outBoundMessage = new MSTeamsOutboundMessages();
var response = outBoundMessage.sendDirectMessage(send_to, MSTeamsConstants.OUTBOUND_MESSAGE_TYPE.ADAPTIVE_CARD, card2);
```

We can create a card that looks like

[](https://www.servicenow.com/community/image/serverpage/image-id/139785iD4393F56B9A33D95/image-size/large?v=v2&px=999)

## Doing something useful with that information

### Now we know how to send cards we can create a custom Flow ActionInputs

[](https://www.servicenow.com/community/image/serverpage/image-id/139793i8418F99417114711/image-size/large?v=v2&px=999)

Then we add a scripted step

[](https://www.servicenow.com/community/image/serverpage/image-id/139799iAB16F57B2A22ED80/image-size/large?v=v2&px=999)

We need to add our input values

[](https://www.servicenow.com/community/image/serverpage/image-id/139783i14E224C14D4BC180/image-size/large?v=v2&px=999)

And our script

```jsx
(function execute(inputs, outputs) {
var card =
{
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "TextBlock",
            "size": "Large",
            "weight": "Bolder",
            "text": "Incident has been assigned to your queue.\n ",
            "wrap": true
        },
        {
            "type": "TextBlock",
            "size": "Medium",
            "weight": "Bolder",
            "text": inputs.number + " \n " + inputs.priority,
            "wrap": true
        },
        {
            "type": "TextBlock",
            "text": inputs.short_description,
            "wrap": true
        },
        {
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.OpenUrl",
                    "title": "View Ticket details",
                    "url": "https://xxxxx.service-now.com/nav_to.do?uri=%2Fincident.do%3Fsys_id%3D" + inputs.record_id
                }
            ]
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3"
}

var outBoundMessage = new MSTeamsOutboundMessages();
var response = outBoundMessage.sendDirectMessage(inputs.user_id, MSTeamsConstants.OUTBOUND_MESSAGE_TYPE.ADAPTIVE_CARD, card);

})(inputs, outputs);

```

Then we can test using

[](https://www.servicenow.com/community/image/serverpage/image-id/139797i4C4FDE631F54B8DE/image-size/large?v=v2&px=999)

[](https://www.servicenow.com/community/image/serverpage/image-id/139791i75948FDEDCF90CCB/image-size/large?v=v2&px=999)

An providing the the user in the "send to id" field has their account linked to MS Teams they should get a card

[](https://www.servicenow.com/community/image/serverpage/image-id/139795iA56216F190DD3BAC/image-size/large?v=v2&px=999)

- [Flow Designer](https://www.servicenow.com/community/now-platform-articles/tkb-p/now-platform-kb/label-name/flow%20designer?labels=flow+designer)

```jsx
//Last part of the code
var outBoundMessage = new MSTeamsOutboundMessages();
var response = outBoundMessage.sendDirectMessage(inputs.caller, MSTeamsConstants.OUTBOUND_MESSAGE_TYPE.ADAPTIVE_CARD, card)
```

## Related
- [[Integrate your self-configured bot with single Mic]]
- [[ServiceNow – Integrations]]

- [[Teams Integration]]
- [[Conversational integration with Microsoft Teams -]]
- [[Flow Designer]]
- [[UI macro to add “Start Conversation” to field]]