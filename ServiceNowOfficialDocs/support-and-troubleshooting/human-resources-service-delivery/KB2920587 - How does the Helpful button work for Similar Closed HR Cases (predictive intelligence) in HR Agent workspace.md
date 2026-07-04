---
title: "How does the \"Helpful\" button work for \"Similar Closed HR Cases\" (predictive intelligence) in HR Agent workspace"
aliases:
  - KB2920587
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2920587
kb_number: KB2920587
last_modified: 2026-03-27
---

## How does the "Helpful" button work for "Similar Closed HR Cases" (predictive intelligence) in HR Agent workspace

  

### Summary

After enabling “Similar Closed HR Cases” similarity solution (Predictive Intelligence) in HR Agent Workspace, we can see recommended similar closed HR case cards when clicking the “Agent Assist” button.

  
In these cards, there is an option under the top-right three-dot menu called “Helpful.” 

**How this-"helpful" feature works. Specifically, does selecting “Helpful” send the HR case mentioned in the recommended card to ServiceNow to improve their algorithms?**

The 'Helpful' is just to mark the relevant document as 'Helpful'. It's not used to improve the recommendation or any algorithm. It's an agent assist action and can be found on all cards that agent assist shows if it's enabled and not just for cards that are shown by the ML solution.

  
The results are stored in 'cxs\_rel\_doc\_detail' table for the records where it has been selected as helpful or not helpful.

### Release

Yokohama
