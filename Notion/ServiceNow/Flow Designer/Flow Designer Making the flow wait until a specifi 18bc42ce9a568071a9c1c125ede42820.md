---
aliases:
  - "Flow Designer Making the flow wait until a specifi"
tags:
  - flow-designer
  - wait-condition
  - catalog-variable
  - automation
---

# Flow Designer : Making the flow wait until a specific date time based on a catalog variable

Recently I was working on a requirement to make the flow wait 
until a specific date/time is reached and then trigger the next action. I
 initially thought it would be an easy configuration but couldn't find 
how because out of the box there are two conditions -

- Wait for a condition
- Wait for a duration

But they didn't have any straightforward option and I was trying to not get into scripts to do this.

Here is what worked for me -

Used the wait-for-duration activity, changed the duration type to 
relative duration, and then used 1 second after the variable value to 
make the flow until the specified time and then triggered the next 
action.

[](https://www.servicenow.com/community/image/serverpage/image-id/352639i6B50C275B0F5BB87/image-size/large?v=v2&px=999)

Thought I would create this as an article so they can utilize it in 
case someone is looking for it. If this has helped you, please like the 
post!

## Related

- [[Flow Designer]]
- [[How to nudge a flow]]
- [[What is “Presumed Interrupted” state]]
- [[sn_fd FlowAPI nudgeFlow does not work if completed]]