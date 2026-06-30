---
title: Troubleshoot agentic evaluations
description: Find solutions to common evaluation errors, including run failures, data ingestion issues, and unexpected results.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/intelligent-experiences/troubleshoot-aia-eval.html
release: australia
topic_type: concept
last_updated: "2026-03-18"
reading_time_minutes: 3
breadcrumb: [Evaluate, Evaluate agentic AI assets, Now Assist AI agents, Enable AI experiences]
---

# Troubleshoot agentic evaluations

Find solutions to common evaluation errors, including run failures, data ingestion issues, and unexpected results.

When using agentic evaluations, you may see unexpected execution results or errors. The following discusses situations you could encounter and some of the reasons why those situations occur.

## Evaluation run failed

There are a few different reasons why an evaluation run may fail to execute properly.

-   **Agent version unavailable**

    Verify that the selected agent version still exists in [[ai-agent-studio|AI Agent Studio]]. The version does not have to be the one currently active, but deleted or archived versions can't be evaluated.

-   **User permissions**

    Confirm that your User record has the permissions required to execute evaluation runs in general and to use the specific AI asset. To check whether a certain user has access, you can perform an access test. See [[test-aia-access|Test user access to an AI agent]] and [[test-aw-access|Test user access to an agentic workflow]].

-   **Data format errors**

    Verify that the dataset conforms to the required format. Malformed records can cause the evaluation to fail. See [[ref-aia-eval|Data requirements for agentic evaluations]] for the supported data types.

-   **Metric and data mismatch**

    Confirm that all selected metrics have the required data inputs. Metrics that require ground truth will fail if the ground truth field is missing from the dataset.


## Agentic AI asset underperformance despite no issues found

If the evaluation found no issues, but the specific agentic AI asset is still not performing to acceptable standards, consider the following:

-   **Dataset coverage**

    The evaluation dataset may not include the types of inputs or scenarios that expose the agent's weaknesses. Review the dataset for any coverage gaps and add representative edge [[cases|cases]] to more closely align what is being evaluated with real-world scenarios.

-   **Metric selection**

    The selected metrics may not be measuring where the agentic AI asset is failing. Review whether additional or different metrics would better capture the performance gap. You can [[create-custom-metric|create custom metrics]] to evaluate other dimensions of the agentic AI asset responses or actions, such as length of response or whether a response meets certain formatting requirements.

-   **Scoring thresholds**

    The pass threshold for a metric may be set at a level that does not reflect your requirements. Review threshold settings in the metrics configuration to redefine success and failure.


## Optimization applied, but re-evaluation didn't improve

If the re-evaluation scores did not improve after [[aia-eval-apply-optimization|applying optimizations]], try the following:

-   Review trace details for the issues that were targeted. The optimization may have only alleviated surface-level symptoms without resolving the underlying root cause.
-   Check whether the optimization introduced a regression in a different metric. Score improvements in one area can sometimes degrade another, lowering the final scores.
-   If the optimization was applied to the list of steps of an agentic AI asset, verify that the updated list of steps was applied to the version you are evaluating.

## Data processing errors

If the data can't be processed because it doesn't meet data requirements, the evaluation can't execute properly. The following describes common causes of data processing errors:

-   **Incorrect file format**

    The accepted file formats are CSV and structured JSON. Other file formats can't be processed.

-   **Missing required fields**

    [[ai-datasets|Datasets]] must include the fields required by the selected metrics. Check for missing or misnamed columns. If you're using a ground truth, you must include it in the dataset.

-   **Encoding issues**

    Files must be UTF-8 encoded. Files with non-standard encoding may fail to be processed.

-   **File size**

    Very large files or datasets may time out during processing. If this occurs, reduce the dataset size or contact your Platform Administrator.

## Related

- [[test-aia-access|Test user access to an AI agent]]
- [[test-aw-access|Test user access to an agentic workflow]]
- [[ref-aia-eval|Reference for agentic evaluations]]
- [[create-custom-metric|Create a custom metric for evaluating agentic workflows]]
- [[aia-eval-apply-optimization|Apply optimizations to agentic AI assets and reevaluate]]
- [[ai-agent-studio|AI Agent Studio]]
- [[cases|Cases]]
- [[ai-datasets|Datasets]]
