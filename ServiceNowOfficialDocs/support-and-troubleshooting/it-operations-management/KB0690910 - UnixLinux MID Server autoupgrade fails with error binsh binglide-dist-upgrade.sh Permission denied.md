---
title: "Unix/Linux MID Server autoupgrade fails with error \"/bin/sh: bin/glide-dist-upgrade.sh: Permission denied\"
aliases:
  - KB0690910
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0690910
kb_number: KB0690910
last_modified: 2024-04-07
---

## Unix/Linux MID Server autoupgrade fails with error "/bin/sh: bin/glide-dist-upgrade.sh: Permission denied"

  

### Issue

# Overview

* * *

The MID Server periodically checks if it is running the same version as the instance. The MID server automatically downloads and install updates in order to be in the same version as the instance.

The updates are downloaded to:

<mid\_server\_folder>/agent/package/incoming/

The upgrades are then extracted to:

/tmp/<generated\_random\_number>

Once the files are downloaded and extracted the upgrage begins by running "glide-dist-upgrade.sh"

# Error

* * *

The MID Server autoupgrade fails with error "glide-dist-upgrade.sh: Permission denied", full error as follows:

AutoUpgrade.3600 Stopping MID server. Bootstrapping upgrade.
Gobbling stderr: /bin/sh -c bin/glide-dist-upgrade.sh start Gobbled: /bin/sh: bin/glide-dist-upgrade.sh: Permission denied
AutoUpgrade.3600 Added marker \`/tmp/1528126003155-0\` to upgrade marker file.
AutoUpgrade.3600 SEVERE \*\*\* ERROR \*\*\* Upgrade failed.

# Troubleshooting

* * *

Confirm the file has execute permissions.

1.  Navigate to the "/tmp/<generated\_random\_number>/upgrade-wrapper/bin/" directory
2.  Run "ll" command to list files and permissions

Confirm the "/tmp" folder is not mounted as "noexec". When mounted with "noexe" option, it will not be possible to run ".sh" files from tmp even if the permissions are correct.

1.  Run "mount" command to view mounted filesystems and mount point configurations

# Solution

* * *

**Warning:** Contact the linux/unix admin of the system to perform the following. Example commands may be provided, however may differ from version to version

1.  Give execute permission to the "glide-dist-upgrade.sh" script file, if not already given
2.  Re-mount the /tmp folder without the "noexec" option. For example:
    -   sudo mount -o remount,exec /tmp
