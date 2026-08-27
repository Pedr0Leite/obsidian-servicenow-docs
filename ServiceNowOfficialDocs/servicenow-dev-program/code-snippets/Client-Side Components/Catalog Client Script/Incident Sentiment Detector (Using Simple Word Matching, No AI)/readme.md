---
title: "Incident Sentiment Detector (Using Simple Word Matching, No AI)"
aliases:
  - Incident Sentiment Detector (Using Simple Word Matching, No AI)
tags:
  - servicenow-dev-program
  - code-snippet
  - incident-sentiment-detector-using-simple-word-matching-no-ai
  - catalog-client-script
---

Incident Sentiment Detector (No AI, Pure JavaScript)

A lightweight ServiceNow utility that detects sentiment (Positive / Negative / Neutral) of an Incident’s short description or comments using simple keyword matching — no AI APIs or external libraries required.

Useful for support teams to auto-tag sentiment and analyze user frustration or satisfaction trends without expensive integrations.

🚀 Features

✅ Detects sentiment directly inside ServiceNow ✅ Works without external APIs or ML models ✅ Instant classification on form update ✅ Adds detected sentiment to a custom field (u_sentiment) ✅ Simple to extend — just add more positive/negative keywords

🧩 Architecture Overview

The solution consists of two main scripts:

Component Type Purpose SentimentAnalyzer Script Include Processes text and returns sentiment Client Script (onChange) Client Script Calls SentimentAnalyzer via GlideAjax on short description change 🧱 Setup Instructions 1️⃣ Create Custom Field

Create a new field on the Incident table:

Name: u_sentiment

Type: Choice

Choices: Positive, Neutral, Negative

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Label For Attachment/README|Add Label For Attachment]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Add Rows in MRVS/README|Add Rows in MRVS]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto Save Draft Feature/README|Auto Save Draft Feature]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Auto-populate field from URL/README|Auto-populate field from URL]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autofilling the request details from previous request/Readme|Autofilling the request details from previous request]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/Catalog Client Script/Autopopulate Department/README|Autopopulate Department]]
