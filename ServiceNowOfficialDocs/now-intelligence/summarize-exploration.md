---
title: Summarize an exploration
description: Use AI to generate a summary of an exploration. If you update the exploration, you can regenerate the summary.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/now-intelligence/summarize-exploration.html
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Use, AI Data Explorer, Now Assist in Platform Analytics, Platform Analytics]
tags:
  - now-intelligence
  - type-task
---

# Summarize an exploration

Use AI to generate a summary of an exploration. If you update the exploration, you can regenerate the summary.

## Before you begin

To access the AI summarization tool, the exploration summarization skill must be activated. For more information, see [[activate-now-ass-explorer|Activate AI Data Explorer skills]].

Role required: now\_assist\_explorer\_user. You need editing rights to the exploration.

Generate a summary by pressing the **Summarize** button in the exploration header.

\[Omitted image "nowass-summarize-button.png"\] Alt text: The Summarize button in AI Data Explorer.

AI generates a summary and places it beneath the goal.The **Summarize** button disappears.

\[Omitted image "nowass-expl-summary.png"\] Alt text: Summary of exploration of mental health-related HR cases, exposing Product Management as an area of special concern.

You can place your cursor in the generated summary and edit it, as described in [[write-text-exploration|Write or edit text in an exploration]].

If you change the exploration, you get a message in the summary header that changes have been made.

\[Omitted image "nowass-expl-refresh-summary-msg.png"\] Alt text: Message in the summary header to refresh the summary.

To refresh the summary, press the **Regenerate summary** button in the summary header. You are asked to confirm that you want to regenerate the summary. If you confirm, the summary now reflects the most recent changes, and the Refresh message is dismissed.

\[Omitted image "nowass-expl-regenerate-summary.png"\] Alt text: Regenerate button summary in the Summary header.

You can also delete a summary when you no longer need it. Press the **Delete** button in the summary header.

**Note:** The Regenerate and Delete summary actions are not available if the exploration summarization skill is deactivated or the exploration is made read-only.

**Parent Topic:**[[use-now-assist-explorer|Using AI Data Explorer]]

## Related

- [[activate-now-ass-explorer|Activate AI Data Explorer skills]]
- [[write-text-exploration|Write or edit text in an exploration]]
- [[use-now-assist-explorer|Using AI Data Explorer]]
