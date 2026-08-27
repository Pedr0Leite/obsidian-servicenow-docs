---
title: "Server error \"Command Not Found\"
aliases:
  - KB0727949
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0727949
kb_number: KB0727949
last_modified: 2024-04-07
---

## Issue

Following error found when running a command on a server. This error could happen when running a discovery (via probes and patterns), orchestration activity, or any integration. 

**command not found**

## Resolution

The following are possible solutions and should resolve the issue in most environments. However, the steps may differ depending on environment configuration or company practices. Therefore, the best solution is to contact the admin for the target server in order to configure the target server accordingly.

**A. Add the command directory path to the user's configuration.**

1.  Log into target server.
2.  Navigate to $HOME:
    1.  cd $HOME
3.  With a text editor(vi, vim, etc) add the following line to either ".profile" or ".bashrc":
    1.  export PATH="$PATH:<command\_directory>"

**Note:** ".bashrc" will be used by the bash shell, whereas ".profile" will be read by many shells in the absence of their own shell configuration files.

Next, run the "source .bashrc", or "source .profile", command to load the new configuration.

**B. Change user default shell to a shell which will allow the user to run the commands.**

**C. Update orchestration, probe, or pattern command to include full path or full command in order to be able to execute the command from the default shell.**

**Finally, confirm the logged in user can run the command:** 

1.  Log into target server, or source the new configuration as explained in the previous steps.
2.  Run "which <command\_name>" and confirm the path is found, empty output means that the command was not found.
3.  Run the command and confirm proper output (which will depend on the command), and that there are no permission errors or any other errors.
