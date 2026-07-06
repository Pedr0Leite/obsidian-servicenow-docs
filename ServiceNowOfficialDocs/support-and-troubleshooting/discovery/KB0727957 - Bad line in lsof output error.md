---
title: "Bad line in lsof output error"
aliases:
  - KB0727957
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727957
kb_number: KB0727957
last_modified: 2024-04-07
---

## Issue

Unix/Linux Application Dependency Mapping probe fails with error:

Bad line in lsof output

## Resolution

The following line of the LSOFParser breaks down the output into a string array containing each line of the output.

var lines = output.trim().split('\\n');

This line can be updated to filter out unwanted lines returned by "lsof -iTCP -n -P -F pcnfT" before the output is processed, replace <string\_to\_be\_removed> in the following with the string to be removed.

var lines = output.trim().split('\\n').filter(function(output){   
return ((-1 == output.indexOf("<string\_to\_be\_removed>")));   
});

**Note:** Modifying this script should only be a solution until the issue is resolved with the lsof command on the target host.

## Additional Information

-   [LSOFParser](https://docs.servicenow.com/csh?topicname=c_LSOFParserAPI.html&version=latest "LSOFParser")
