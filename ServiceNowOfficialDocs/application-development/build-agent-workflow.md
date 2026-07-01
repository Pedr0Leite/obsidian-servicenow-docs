---
title: Build Agent workflow
description: The Build Agent workflow automates building applications, testing, and deploying update sets on the ServiceNow AI Platform. Build Agent streamlines development by handling code compilation, quality checks, and deployment steps without manual intervention.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/application-development/build-agent-workflow.html
release: australia
topic_type: concept
last_updated: "2026-04-30"
reading_time_minutes: 1
keywords: [Now Assist, AI Agents, generative AI, agentic AI]
breadcrumb: [Explore, Build Agent, Agentic development on the ServiceNow AI Platform, Building applications]
---

# Build Agent workflow

The Build Agent workflow automates [[build-applications|building applications]], testing, and deploying update sets on the ServiceNow AI Platform. [[build-agent|Build Agent]] streamlines development by handling code compilation, quality checks, and [[get-started-deployment|deployment]] steps without manual intervention.

A general workflow for using Build Agent in either [[servicenow-studio-landing|ServiceNow Studio]] or the [[servicenow-ide-landing|ServiceNow IDE]] is the following:

1.  Open ServiceNow Studio or the ServiceNow IDE to access the Build Agent panel in the workspace.
2.  Describe what to create or change in natural language.
3.  Let Build Agent parse requirements and propose the application and files to create or modify.
4.  Build Agent edits code or metadata or scaffolds a new application.
5.  Review proposed edits, diffs, and summaries, and approve or adjust before applying changes.
    1.  If you're [[using-servicenow-studio|using ServiceNow Studio]], look at the generated app details.
    2.  If you're using the ServiceNow IDE, inspect the code.
6.  Iterate until the desired metadata changes are complete. For more information, see [[build-agent-supported-metadata|Supported metadata in Build Agent]].
7.  Prompt Build Agent to create [[atf-landing-page|Automated Test Framework \(ATF\)]] [[tests-module|tests]], and then run them.
8.  Instruct Build Agent to build the application; verify results in the File Navigator or Metadata Explorer.
9.  Deploy the application. For more information, see [[build-agent-deployment|Deploying what you built with Build Agent]].

**Parent Topic:**[[exploring-build-agent|Exploring Build Agent]]

## Related

- [[build-agent-supported-metadata|Supported metadata in Build Agent]]
- [[build-agent-deployment|Deploying what you built with Build Agent]]
- [[exploring-build-agent|Exploring Build Agent]]
- [[build-applications|Building applications]]
- [[build-agent|Build Agent]]
- [[get-started-deployment|Deployment]]
- [[servicenow-studio-landing|ServiceNow Studio]]
- [[servicenow-ide-landing|ServiceNow IDE]]
- [[using-servicenow-studio|Using ServiceNow Studio]]
- [[atf-landing-page|Automated Test Framework \(ATF\)]]
- [[tests-module|Tests]]
