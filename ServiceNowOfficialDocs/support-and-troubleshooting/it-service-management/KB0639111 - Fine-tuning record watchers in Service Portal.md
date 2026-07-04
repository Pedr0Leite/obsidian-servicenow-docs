---
title: "Fine-tuning record watchers in Service Portal"
aliases:
  - KB0639111
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639111
kb_number: KB0639111
last_modified: 2024-12-09
---

## Fine-tuning record watchers in Service Portal

  

### Issue

There are two ways in which you can fine-tune a record watcher in Service Portal to reduce the number of calls a widget makes to the server. Understanding these methods will help avoid adding unnecessary overhead to the application server that comes from processing too many record watcher updates.

For further information regarding why this fine-tuning is important you can refer to these articles:

-   [KB0635134](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0635134 "KB0635134") - Resolving "Exhausted Default Semaphores" errors caused by Service Portal widgets having poorly defined record watcher (recordWatch) calls
-   [KB0634655](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0634655 "KB0634655") - Auto-refreshing Widgets leads to semaphore exhaustion

### Improve your filters

Having a good filter for a record watcher is critical to avoiding performance problems.

The filter should be passed as the third parameter in your call to

spUtil.recordWatch(Object $scope, String table, _String filter_, Function callback)

This filter accepts an encoded query as a string. You can use any of the JavaScript operators described in the product documentation topic [Operators available for filters and queries](https://docs.servicenow.com/csh?topicname=r_OpAvailableFiltersQueries.html&version=latest). This enables you to watch for changes to specific fields.

For example, if you have a widget to show all active P1 incidents, you need to take into consideration that P1 incidents are updated very frequently and that watching all of those updates could add overhead to your system. The record watcher might need to watch only for changes to the state of the P1 incident, for example. You can accomplish that in your filter as follows:

"priority=1^stateCHANGES^EQ"

You could also watch to see if the P1 state changed to resolved by using the _CHANGESTO_ operator instead:

"priority=1^stateCHANGESTO6^EQ".

### Choose when to refresh

Most of the performance issues related to record watchers in the portal happen because a widget makes too many calls to `spUtil.update()` or `server.update()` in a very short time. These calls are typically in response to the record watcher notifying the client that there is an update.

By default, if you do not pass in a callback to the record watcher, every update will result in a call to `server.update()` to refresh the widget data. That could cause a flood of calls to refresh the widget. Instead, define a callback function and use the information available from the record update event to determine whether the widget should refresh.

So, for example, take the same P1 widget and instead of watching only for changes to the state field, use a broader filter to watch all active P1s and then let the callback function determine whether to refresh the data.

var q = "priority=1^active=true^EQ";
spUtil.recordWatch($scope, "incident", q, function(event, data) {
   if (event.data && event.data.changes.includes("state")) { // only update if state was updated.
      spUtil.update($scope);
   }
});

In this example, a filter refines what is being watched and a callback function that determines whether to refresh the data. The callback function passes in event and data. Behind the scenes, this is merely an angularjs event handler. The data object contains information about the record that was updated. You can log that data variable to the console to see what is in it but perhaps the most useful property is “changes”. Data.changes contains an array of all fields that were changed in the update. You can use that information to check which fields have changed and determine whether it is necessary to update the data in the widget.

**Changes in Jakarta release:** 

In Jakarta, the data object is not defined in the record watcher callback and it is no longer a simple angularjs event handler. You can still use it in the same way, but the information about the record being updated has now been moved to the event object itself.

So, if you want to look into the changes made to a record you need to instead use event.data.changes to access the fields that have changed.

### Release

\-

### Resolution

\-
