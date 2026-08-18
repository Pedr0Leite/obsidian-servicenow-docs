---
title: "Now Assist record summarization — the OOB Summarize button (nowassist_record_summarize)"
tags: [servicenow, now-assist, gen-ai, ui-macro, summarization]
product: Now Assist
artifact: sys_ui_macro
---

# Now Assist record summarization — the OOB "Summarize" button

How the out-of-box **Summarize** button on a back-office (Core UI) case form is
actually wired. Captured from the platform on 2026-08-11; the macro source is
reproduced verbatim below.

> [!important] The method is `TaskSummarize`, not `TaskSummarization`
> There is no `TaskSummarization` anywhere. The server-side entry point the OOB
> button uses is the **`TaskSummarize`** script include. Searching for
> `TaskSummarization` returns nothing because the artifact does not exist under
> that name.

## The artifact

| | |
|---|---|
| Table | `sys_ui_macro` |
| Name | `nowassist_record_summarize` |
| Type | Jelly UI macro (Core UI / back-office form, not UIB) |

## Server-side entry point

The macro's first `g2:evaluate` block is the whole server-side story:

```javascript
var uxcLogger = new UXCGenAILogger();
if (!current.isNewRecord()){
    var taskSummarize = new TaskSummarize();
    var summarizedConfigs = taskSummarize.fetchConfigs(jelly.jvar_table, jelly.jvar_form_sys_id);
} else {
    uxcLogger.debug("Skipping config retrieval for unsaved record as SysId is not available");
}
```

- **`new TaskSummarize().fetchConfigs(tableName, sysId)`** returns a **JSON
  string** of configuration, not a summary. It is parsed with `JSON.parse` and
  the macro renders nothing unless `config && config.fields` is truthy.
- It is skipped entirely on an unsaved record (`current.isNewRecord()`), because
  there is no sys_id to summarize.
- **`UXCGenAILogger`** is the logging class used throughout (`.debug()`,
  `.error()`).

### What this does *not* tell us

`fetchConfigs` fetches **configuration only**. The macro never calls a
summarization API server-side — the actual generation happens client-side via
`GenAIRecordSummary` (below). Whether `TaskSummarize` exposes a method that
returns a summary directly is **not visible from this macro and remains
unverified**.

## Client-side entry point

The summary itself is produced by a client class loaded from
`scripts/gen_ai_summary_functions.js`:

```javascript
var genAICard = new GenAIRecordSummary(
    "$[jvar_table]",
    "$[jvar_table_label]",
    "$[jvar_form_sys_id]",
    "$[jvar_configs]",
    toolbar,
    "$[jvar_uxc_labels._stringified]",
    "$[gs.getUserID()]"
);

angular.element(document).scope().$on('record.updated', genAICard._onRecordUpdated.bind(genAICard));

if(genAICard.config $[AMP]$[AMP] genAICard.config.proActiveTrigger) {
    genAICard.getSummary();
}
```

- **`genAICard.getSummary()`** is the call that generates the summary.
- **`config.proActiveTrigger`** makes it fire automatically on form load rather
  than waiting for the button. That flag comes out of `fetchConfigs`.
- Re-summarization on save is wired through the Angular `record.updated` event.
- The card is Angular/Core-UI bound (`angular.element(document).scope()`), so
  **this path is not reusable from a Workspace/UIB or a server script.**

## Other details worth keeping

- `$[AMP]$[AMP]` is the Jelly-escaped `&&`. It appears in both evaluate blocks
  and in the inline script.
- Label overrides are supported: `configs.summaryCardLabelsOverride` keys are
  matched against a fixed label map and passed through
  `GlideStringUtil.escapeHTML(value)`.
- Two label variants exist throughout — plain and `...Nacm` (e.g.
  `defaultHeader` / `defaultHeaderNacm`), so the card has a second presentation
  mode.
- HR tables are special-cased for label casing:
  `jelly.jvar_table.indexOf('hr_') !== -1 || jelly.jvar_table.indexOf('sn_hr') !== -1`
  keeps the table label cased, everything else lowercases it.
- The macro checks for an active `agentic_sidebar` UI macro and only inlines
  `ai-agent-stepper.xml` when that is **absent**.
- TinyMCE toolbar is resolved by major version (4, 5, 6/7/8+) from
  `glide.ui.html.editor.*` properties — relevant if the summary is edited before
  posting to work notes.

## Calling summarization from a script — what to use instead

The OOB button is **not** a scripting API. For invoking a skill from server-side
script the documented route is `sn_one_extend.OneExtendUtil.execute(request)` —
see [[call-custom-skill-from-script]] in the official docs
(`ServiceNowOfficialDocs/intelligent-experiences/now-assist-skill-kit/call-custom-skill-from-script.md`),
which takes `executionRequests[].payload` with `tableName` / `sysId`, a
`capabilityId` and `meta.skillConfigId`, and `mode: 'sync'`.

A working example of that pattern against a real summarization skill is
`_getStaleCaseSum(caseNumber)` in [[Proactive Customer Case Communicator]],
which uses `sn_one_extend.OneExtendUtil.executeSecure` with the
[[stale-case-summarization-skill-notes|Stale Case Summarization]] skill.

## Full macro source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<j:jelly
    xmlns:j="jelly:core"
    xmlns:g="glide"
    xmlns:g2="null"
    xmlns:j2="null" trim="true">
    <g:inline template="uxc-version.xml" />
    <g2:evaluate var="jvar_configs" jelly="true" object="true">
        var uxcLogger = new UXCGenAILogger();
        if (!current.isNewRecord()){
            var taskSummarize = new TaskSummarize();
            var summarizedConfigs = taskSummarize.fetchConfigs(jelly.jvar_table, jelly.jvar_form_sys_id);
        } else {
            uxcLogger.debug("Skipping config retrieval for unsaved record as SysId is not available");
        }
        if (summarizedConfigs) {
            var config;
            try {
                config = JSON.parse(summarizedConfigs);
            } catch(e) {
                err = gs.getMessage("Failed to parse configuration for UI macro nowassist_record_summarize: Invalid JSON structure with error : {0}", e);
                uxcLogger.error(err);
            }

            if (config $[AMP]$[AMP] config.fields) {
                summarizedConfigs;
            } else {
                null;
            }
        } else {
            null;
        }
    </g2:evaluate>
    <j2:if test="$[jvar_configs != null]">
            <g2:evaluate var="jvar_uxc_labels" jelly="true" object="true">
                var tableLower = jelly.jvar_table.indexOf('hr_') !== -1 || jelly.jvar_table.indexOf('sn_hr') !== -1 ? jelly.jvar_table_label : jelly.jvar_table_label.toLowerCase();
                var labels = {
                    actionButton: gs.getMessage('Summarize'),
                    copyNotification: gs.getMessage('{0} summary copied to clipboard.', jelly.jvar_table_label),
                    copyErrorNotification: gs.getMessage('There was an error copying {0} summary', tableLower),
                    defaultHeader: gs.getMessage('{0} summarized by Now Assist', jelly.jvar_table_label),
                    defaultHeaderNacm: gs.getMessage('Now Assist {0} summary', tableLower),
                    disclaimer: gs.getMessage('Be sure to check the AI-generated summary for accuracy.'),
                    disclaimerNacm: gs.getMessage('Check AI-generated content for accuracy.'),
                    initialHeader: gs.getMessage('{0} summary by Now Assist', jelly.jvar_table_label),
                    initialHeaderNacm: gs.getMessage('Now Assist can summarize this {0}', tableLower),
                    loadingHeader: gs.getMessage('Now Assist is summarizing your {0}...', tableLower),
                    loadingHeaderNacm: gs.getMessage('Summarizing this {0}...', tableLower),
                    popoverContent: gs.getMessage('AI summarized this using the record details. Check it for accuracy.'),
                    regeneratingMessage: gs.getMessage('Summarizing {0}...', tableLower),
                    shareDescriptionMessage: gs.getMessage('Be sure to check the AI-generated summary for accuracy and make any needed edits before saving. You\'ll still have access to the original {0} summary by Now Assist.', tableLower)
                };
                var configs = JSON.parse(jelly.jvar_configs);
                if (configs.summaryCardLabelsOverride) {
                    var overrides = Object.entries(configs.summaryCardLabelsOverride);

                    for (var i = 0; i &lt; overrides.length; i++) {
                        var key = overrides[i][0];
                        var value = gs.getMessage(overrides[i][1]);
                        if (labels.hasOwnProperty(key)) {
                            labels[key] = GlideStringUtil.escapeHTML(value);
                        }
                    }
                }
                labels._stringified = JSON.stringify(labels);
                labels;
            </g2:evaluate>
    </j2:if>
    <g2:evaluate var="agenticSidebarEnabled">
            var gr = new GlideRecord("sys_ui_macro");
            gr.addQuery("name", "agentic_sidebar");
            gr.addQuery("active", true);
            gr.query();
            gr.hasNext();
    </g2:evaluate>
    <g:if test="${!agenticSidebarEnabled}">
        <g:inline template="ai-agent-stepper.xml"/>
    </g:if>
    <j2:if test="$[jvar_configs != null]">
    <g:if_polaris>
        <g:then>
            <g:requires name="/styles/com.sn.uxc.gen.ai/polaris.css" params="${jvar_uxc_cache_version}" />
        </g:then>
        <g:else>
            <g:requires name="/styles/com.sn.uxc.gen.ai/doctype.css" params="${jvar_uxc_cache_version}" />
        </g:else>
    </g:if_polaris>
    <g:messages>Summarize
        Thanks for your feedback!
        Summary posted to {0}
        summary by {0}
        {0} summarized by {1}
        AI summarized this using the record details. Check it for accuracy
        Now Assist is summarizing your
        Share
        Refresh
        Retry
        Copy
        Save to {0}
        Share to {0}
        Helpful
        Not helpful
        Collapse card
        Expand card
        View more
        View less
        There was an error summarizing your
        Updated {0}
        {0} summary copied to clipboard
        Thank you for submitting feedback
        Be sure to check the AI-generated summary for accuracy and make any needed edits before posting into {0}. You'll still have access to the original case summary by {1}.
        There's not enough {0} activity for AI to summarize yet. You'll see the option to summarize after more activity is added.
        Summary is successfully posted to {0}
        Summary cannot be empty</g:messages>
    <div class="row">
        <div class="col-xs-12" id="gen-ai-summarize-card" style="display:none;">
            <div class="form-group">
                <div class="col-xs-12 col-md-1_5 col-lg-2 control-label" aria-hidden="true"/>
                <div class="col-xs-10 col-md-9 col-lg-8 form-field input_controls">
                    <div id="gen-ai-summaryWrapper" class="summarize-wrapper -collapsed">
                        <div class="summarize-container col-sm-12">
                            <div class="summarize-header">
                                <div id="gen-ai-summaryCardTitle" class="summarize-header-title">
                                    <span id="gen-ai-summary-card-title">$[jvar_uxc_labels.initialHeader]</span>
                                    <span class="icon-info" tabindex="0" aria-label="$[jvar_uxc_labels.popoverContent]" title="$[jvar_uxc_labels.popoverContent]" />
                                </div>
                                <span id="gen-ai-summaryProgressTitle" class="summarize-header-progress">
                                    <span id="gen-ai-summary-loadingIcon" class="icon-loading" aria-hidden="true"/>
                                    <span>$[jvar_uxc_labels.loadingHeader]</span>
                                </span>
                                <div class="summarize-header-actions">
                                    <button id="gen-ai-summarizeButton" class="btn btn-default btn-sm -summary" type="button" title="$[jvar_uxc_labels.actionButton]" aria-label="$[jvar_uxc_labels.initialHeader]">$[jvar_uxc_labels.actionButton]</button>
                                    <button id="gen-ai-summary-postToWorknotesButton" class="btn btn-default btn-sm -worknotes" type="button" title="${gs.getMessage('Share')}" aria-label="${gs.getMessage('Share')}">${gs.getMessage('Share to Worknotes')}</button>
                                    <button id="gen-ai-summary-card-collapseButton" class="btn btn-icon icon-chevron-up btn-sm" type="button" title="${gs.getMessage('Collapse')}" aria-label="${gs.getMessage('Collapse')}" />
                                </div>
                            </div>
                            <div id="gen-ai-summarySection" class="summarize-body">
                                <div id="gen-ai-summaryText" class="summary-content" role="region" aria-label="Summary" aria-live="assertive">${gs.getMessage('This is the summary text.')}</div>
                                <button id="gen-ai-summary-viewMoreButton" class="btn btn-link btn-sm" type="button" >${gs.getMessage('View more')}</button>
                            </div>
                            <div id="gen-ai-summaryErrorSection" class="summarize-error">
                                <span class="icon-alert-triangle" aria-hidden="true" />
                                <span id="gen-ai-summaryErrorText" />
                            </div>
                            <footer id="gen-ai-footerSection" class="summarize-footer">
                                <div class="summarize-footer-actions">
                                    <button id="gen-ai-summary-thumbsUpButton" class="btn btn-icon btn-sm icon-like" type="button" disabled="disabled" title="${gs.getMessage('Helpful')}" aria-label="${gs.getMessage('Helpful')}" />
                                    <button id="gen-ai-summary-thumbsDownButton" class="btn btn-icon btn-sm icon-like -dislike" type="button" disabled="disabled" title="${gs.getMessage('Not helpful')}" aria-label="${gs.getMessage('Not helpful')}" />
                                    <button id="gen-ai-summary-copyTextButton" class="btn btn-icon btn-sm icon-copy" type="button" disabled="disabled" title="${gs.getMessage('Copy')}" aria-label="${gs.getMessage('Copy')}" />
                                    <button id="gen-ai-summary-refreshButton" class="btn btn-icon btn-sm icon-refresh" type="button" title="${gs.getMessage('Refresh')}" aria-label="${gs.getMessage('Refresh')}" />
                                    <span id="gen-ai-summary-refreshProgressTitle" class="summarize-refresh-progress">
                                        <span id="gen-ai-summary-loadingIcon" class="icon-loading" aria-hidden="true"/>
                                        <span>$[jvar_uxc_labels.regeneratingMessage]</span>
                                    </span>
                                </div>
                                <div id="gen-ai-summary-timestampSection" class="summarize-footer-timestamp" tabindex="0"/>
                            </footer>
                            <div id="gen-ai-disclaimerSection" class="summarize-disclaimer-section">
                                <div id="gen-ai-summary-disclaimer" class="summary-disclaimer"/>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-xs-2 col-md-1_5 col-lg-2 form-field-addons" aria-hidden="true"/></div>
        </div>
    </div>
    <g:inline template="tinymce_setup.xml" />
    <g:requires name="scripts/gen_ai_summary_functions.js" params="${jvar_uxc_cache_version}" />
    <script type="text/javascript">
        function initGenAISummaryCard() {
            var tinymceVersion = window.tinymce?.majorVersion;

            var toolbar;
            switch (tinymceVersion) {
                case '4':
                    toolbar = [
                        "$[gs.getProperty('glide.ui.html.editor.v4.toolbar.line1')]".replace(/,/g, ' '),
                        "$[gs.getProperty('glide.ui.html.editor.v4.toolbar.line2')]".replace(/,/g, ' ')
                    ];
                    break;
                case '5':
                    toolbar = "$[gs.getProperty('glide.ui.html.editor.v5.toolbar')]";
                    break;
                case '6':
                case '7':
                case '8':
                default:
                    toolbar = "$[gs.getProperty('glide.ui.html.editor.toolbar')]";
                    break;
            }

            var genAICard = new GenAIRecordSummary(
                "$[jvar_table]",
                "$[jvar_table_label]",
                "$[jvar_form_sys_id]",
                "$[jvar_configs]",
                toolbar,
                "$[jvar_uxc_labels._stringified]",
                "$[gs.getUserID()]"
            );

            // Listen to record updated event
            angular.element(document).scope().$on('record.updated', genAICard._onRecordUpdated.bind(genAICard));

            if(genAICard.config $[AMP]$[AMP] genAICard.config.proActiveTrigger) {
                genAICard.getSummary();
            }

        }
        if (document.getElementById('gen-ai-summarize-card')) {
            initGenAISummaryCard();
        } else {
            document.addEventListener('DOMContentLoaded', initGenAISummaryCard);
        }
    </script>
    </j2:if>
</j:jelly>
```

## Provenance

Macro source supplied by the user from a live instance on 2026-08-11. The
analysis above is read off that source; nothing here is from vendor
documentation. As of capture, `TaskSummarize`, `GenAIRecordSummary`,
`UXCGenAILogger` and `nowassist_record_summarize` had **no matches anywhere else
in this vault** — these are the first notes on them.
