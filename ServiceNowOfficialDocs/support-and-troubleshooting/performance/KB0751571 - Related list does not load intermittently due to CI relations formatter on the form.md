---
title: "Related list does not load intermittently due to CI relations formatter on the form"
aliases:
  - KB0751571
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0751571
kb_number: KB0751571
last_modified: 2024-04-07
---

## Related list does not load intermittently due to CI relations formatter on the form

  

### Issue

# Symptoms

The related list does not load when the form is loaded on Internet Explorer 11

# Release

London, Madrid

# Cause

The issue happened due to the CI relations formatter configured in the form section. In large networks, a list of related CIs might be excessively long, which can slow performance when a CI form is rendered.

# Resolution

Please configure the below three properties as mentioned in the below document based on the organizational requirement and best practice (which would be the default values of these properties )

[CI relations formatter](https://docs.servicenow.com/csh?topicname=c_CIRelationsFormatterNG.html&version=latest "CI relations formatter")

# Additional Information

Also please note that it is good to use the new CI relations formatter and not the Legacy CI relations formatter.
