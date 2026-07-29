---
title: "@mention functionality does not work for new records (not yet submitted)"
aliases:
  - KB0724958
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0724958
kb_number: KB0724958
last_modified: 2024-04-07
---

## @mention functionality does not work for new records (not yet submitted)

  

### Issue

# Symptoms

* * *

When creating a new record and trying to use the @mention functionality on a journal input type field such as comments or work notes it does not work. Nothing simply happens instead of the @mention popping up to allow the user to search which users to mention.

# Release

* * *

All releases

# Cause

* * *

This is expected behavior since @mention does not work for new records as journal input type fields on a new record form do not use UI16 activity stream. @mention will work correctly on existing records as long as the journal input type fields use UI16 activity stream.

# Resolution

* * *

Create the record first and then @mention will work correctly as expected.

Make sure to confirm that the journal input type fields are added to the UI16 activity stream.

[Activity formatter on a form](https://docs.servicenow.com/csh?topicname=c_ActivityFormatter.html&version=latest "Activity formatter on a form")

# Additional Information

* * *

[Activity stream mentions](https://docs.servicenow.com/csh?topicname=c_NavigationAndTheUserInterface.html&version=latest "Activity stream mentions")

@mention can also be disabled for specific tables by using the "live\_feed=false" attribute on the table's collection type dictionary.

[Dictionary attributes](https://docs.servicenow.com/csh?topicname=c_DictionaryAttributes.html&version=latest "Dictionary attributes")
