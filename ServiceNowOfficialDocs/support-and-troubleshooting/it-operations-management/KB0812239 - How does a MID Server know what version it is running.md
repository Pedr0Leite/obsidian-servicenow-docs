---
title: "How does a MID Server know what version it is running?"
aliases:
  - KB0812239
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0812239
kb_number: KB0812239
last_modified: 2025-01-03
---

## How does a MID Server know what version it is running?

  

### Summary

When the MID Server decides it needs to upgrade itself, it compares the version it is currently running, with the version of the instance, or any pinned version set in the instance.

But how does it know what version it is currently running?

### Release

Any.

### Instructions

The MID Server uses a pair of files to know what instance version it is running. It just reads these files, and doesn't write to these files. They are simply overwritten each time the application or Java JRE/JVM is upgraded, with files copied from the upgrade ZIP files. The values are the files names from the upgrade zip files from the most recent upgrade, and include the buildstamp in the name.

#### \\agent\\package\\meta\\mid-core.meta.properties

Example contents:

#Thu, 02 Jan 2020 17:48:12 -0800  
package.filename=mid-core.orlando-12-11-2019\_\_patch0-01-02-2020\_01-02-2020\_1701.universal.universal.zip

Note: If this file is missing, then the MID Server record may have "fixed" as it's version.

#### \\agent\\package\\meta\\mid-jre.meta.properties

Example contents:

#Wed, 17 Apr 2019 11:51:08 -0700  
package.filename=mid-jre.london-06-27-2018\_\_patch8-04-17-2019\_04-17-2019\_1026.windows.x86-64.zip

The actual Java version will be different (e.g.1.8\_232), but that doesn't matter to the upgrade logic.
