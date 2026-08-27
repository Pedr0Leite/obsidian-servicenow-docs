---
title: "What does \"No message handler for this message\" error mean?"
aliases:
  - KB0694128
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0694128
kb_number: KB0694128
last_modified: 2024-04-07
---

## What does "No message handler for this message" error mean?

  

### Issue

# Symptoms

* * *

You may see this error in the ECC Queue or other features that use the MID Server to run a job.

**No message handler for this message.**

# Cause

* * *

Translated into English that error actually means:

**The ECC Queue output record for a MID Server job specifies a bad value for the 'Topic' field, which the MID Server has no idea how to run.**

A possible cause of that is that you have an **empty Topic value**. 

If you have a Topic value, **the case may be wrong**. e.g. "**c**ommand" instead of correct "**C**ommand".

# Resolution

* * *

If this is because a custom Discovery Probe is being run, and that Probe definition doesn't have a value for 'ECC queue topic', then fixing or deactivating that probe would solve this.

There will be other causes, and in that case identify what code causes the ECC Queue job to be created in the first place.
