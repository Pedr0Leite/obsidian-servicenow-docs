---
title: "oldValue returns empty value instead of the previous value for onChange client scripts"
aliases:
  - KB0711972
tags:
  - servicenow
  - support-kb
  - client-scripts
  - onChange
  - GlideForm
area: application-development
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0711972
kb_number: KB0711972
last_modified: 2024-01-28
---

## oldValue returns empty value instead of the previous value for onChange client scripts

  

### Issue

# Symptoms

* * *

When oldValue is used in onChange client scripts it always return empty value instead of the previous value. An example:

onChange client script is set to run on Short description field. When the client script triggered the oldValue is returning empty instead of what the user previously entered in the Short description field prior to saving the change.

# Release

* * *

All releases

# Cause

* * *

The change has not been saved yet so the previous value (oldValue) is always empty (assuming there's no value in the field prior to the change).

# Resolution

* * *

The field in which the onChange client script is executing against needs to have a value saved in the database first before oldValue can work to return the previous value saved.

Example of when it returns a value:

1) Short description is saved with a value of "ABC".

2) When onChange client script is executed oldValue would return "ABC".

Example of when it does not return any value:

1) "ABC" is entered into short description field but it's not saved.

2) When onChange client script is executed oldValue would return "" (empty value).

In either case, both are expected behaviors.

# Additional Information

* * *

[Different types of client scripts](https://docs.servicenow.com/csh?topicname=client-scripts.html&version=latest "Different types of client scripts")

## Related

- [[KB0697413 - In Client scripts, setvisible() or setDisplay() is not honored when used along with setmandatory()]]
- [[KB0696583 - Setting 'setSectionDisplay' function to 'false' does not hide the form section.]]
- [[KB0717382 - An empty or blank box appears inside List collector in Service Portal]]
