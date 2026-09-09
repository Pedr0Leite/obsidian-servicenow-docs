Custom metrics for agentic auto-evaluation

A developer quick reference for workflows and AI agents

Contents

[1\. What this guide covers](#sec_1_what_this_guide_covers)

[2\. Before you start](#sec_2_before_you_start)

[3\. The process at a glance](#sec_3_the_process_at_a_glance)

[4\. Step 1—Create the metric](#sec_4_step_1_create_the_metric)

[5\. Step 2—See what your script receives](#sec_5_step_2_see_what_your_script_receives)

[6\. Step 3—Read the execution object](#sec_6_step_3_read_the_execution_object)

[7\. Step 4—Choose how the metric decides](#sec_7_step_4_choose_how_the_metric_decides)

[8\. Step 5—Write a rule-based metric](#sec_8_step_5_write_a_rule_based_metric)

[9\. Step 6—Write a model-based metric](#sec_9_step_6_write_a_model_based_metric)

[10\. Step 7—Supply an expected result, if you need one](#sec_10_step_7_supply_an_expected_result_if_you_need_one)

[11\. Step 8—Format the output and define labels](#sec_11_step_8_format_the_output_and_define_labels)

[12\. Step 9—Publish and run](#sec_12_step_9_publish_and_run)

[13\. Troubleshooting](#sec_13_troubleshooting)

[14\. Limits worth knowing](#sec_14_limits_worth_knowing)

[15\. A suggested order of work](#sec_15_a_suggested_order_of_work)

[For more information](#sec_for_more_information)

# 1\. What this guide covers

Agentic Evaluations let you test an AI agent or agentic workflow at scale: the platform samples records from a table you nominate, runs your agent against each one, and scores the result. The built-in metrics need no setup. This guide covers the next step—writing a custom metric when the built-ins do not measure what your business actually cares about.

The hard part is not the scripting. It is knowing what your script receives. This guide answers that first, then builds up to a working metric.

There are three ways a custom metric can decide a score: scripted rules, a script comparing against an expected answer you supply per record, or a judge skill called from the script. Section 7 sets out which to reach for. The rest of the process is the same whichever you choose.

| In scope                                                                                    | Not in scope                                                                            |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Non-conversational evaluation—an agent or workflow running against a record or an objective | Conversational Assistant Evaluation, where the tool simulates a back-and-forth end user |
| Custom metrics you write and publish yourself                                               | Skill-level evaluation in Now Assist Skill Kit, which has its own ground truth model    |
| Rule-based and model-based judging                                                          | Fine-tuning or training a model                                                         |

# 2\. Before you start

Three prerequisites, and the second is the one people miss.

| You need                                                   | Why                                                                                               | How to confirm                                                     |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| The admin role                                             | Required to create metrics and to call a skill from a script                                      | Check your roles                                                   |
| At least one completed execution of your agent or workflow | It supplies the execution plan sys_id you will test against. Without it you cannot see your input | Open the sn_aia_execution_plan list and sort by created descending |
| Your agent or workflow published and working               | A metric tells you nothing about an asset that never ran                                          | Run it once by hand                                                |

You do not need to build a dataset table, and you do not need to create a hundred test records. The dataset configuration points a filter at records that already exist.

# 3\. The process at a glance

| Step | What you do                                                                                   | Where                                                 |
| ---- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| 1    | Create the metric and give it a name                                                          | AI Skill Kit, Agentic Evaluations, Evaluation metrics |
| 2    | Set a test value, then run a test to see what your script receives                            | Script Editor                                         |
| 3    | Read the execution object and note the exact agent, tool and input names                      | Run test result panel                                 |
| 4    | Choose rule-based or model-based judging                                                      | A design decision, not a setting                      |
| 5    | Write the comparison and assign scores                                                        | Script Editor                                         |
| 6    | Map a dataset field to the expected_response input, only if the expectation cannot be derived | Evaluation run, Configure data                        |
| 7    | Format the output to the metric output template and define score labels                       | Script Editor                                         |
| 8    | Publish, then select the metric in an evaluation run                                          | Evaluation metrics, then Evaluations                  |

# 4\. Step 1—Create the metric

Navigate to All, AI Skill Kit, Agentic Evaluations, then the Evaluation metrics tab, and select Create metric.

1. General information—name and short description. You can skip straight to the Script Editor from here.
2. Metric details, optional - document how the metric works and what it outputs. This is what the next person reads.
3. Metric inputs, optional - the execution plan sys_id is included by default. Add more inputs with the plus icon.
4. Finish setup to open the Script Editor.

Each metric input has a datatype, name, description, test value and a mandatory flag. The name matters: whatever you type becomes the key you read in the script. An input named expected_response is read as currentInputs.expected_response.

# 5\. Step 2—See what your script receives

This is the step that will save you hours. Do not write code yet.

## The test value expects an execution plan sys_id

The executionplansysid input is described only as a specific input used to check if your script is working. In practice it expects one thing: a 32-character sys_id of a record in sn_aia_execution_plan. Copy one from a completed run of your agent.

This input matters more than it looks. It is what the parser tool keys off, so a wrong or empty test value gives you an empty context and a script with nothing to work on.

## Run the test before changing anything

Leave the prefilled template exactly as it is, set the test value, and select Run test. The result panel lets you review the response and the request of both the overall execution and the parser tool and keeps a run test history.

The parser tool response is your input. That is the object your metric works on, rendered for you, with no code written. Read it before you write a line.

# 6\. Step 3—Read the execution object

| What you might assume                                  | What is actually true                                                                                                                                                 |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| currentInputs holds the record and the execution trail | currentInputs holds ids only. It is a bag of sys_ids and any inputs you declared                                                                                      |
| You must call an API to fetch the execution            | The parser tool already fetched and parsed it into context. Read context instead—it avoids a cross-scope call, which is the most common cause of a first test failing |
| The context key is tool.output                         | The prefilled template uses context\['AgenticExecutionParserTool.output'\]. Trust the template                                                                        |
| The parser value is an object                          | It may arrive as a string. Test with typeof and parse it if needed                                                                                                    |

## What you get, and what you write

Run test returns the parser tool response as JSON, and your script receives that same JSON as an object—parserToolOutput in the prefilled template. Everything after that is yours to write. The platform hands you the parsed execution; traversing it, finding the agent, tool or value you care about, and comparing it are all scripted by the developer.

Copy the agent name, tool name and input keys from what the test actually returned. Retyping them from a form label is the most common reason a first metric scores zero on a run that went fine.

## Unwrap it defensively

The value is an envelope of payload and status. Three things about it catch people out, and each one costs a run:

- The status reads success, not completed. Testing for the wrong word sends your script down the failure branch on a perfectly good execution.
- The value may arrive inside an output property rather than as the envelope itself. Handle both: take raw.output if it is there, otherwise take raw.
- If the key is missing, reading a property of it throws—and a metric that throws returns no response at all, which looks like nothing ran. Guard before you dereference.

## What the payload contains

Four top-level keys, and the two agent lists are not the same thing.

| Path                                                  | What it holds                                                                                     |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| payload.executionInputs.utterance                     | The objective the run was given. For a dataset-driven run this contains the record it ran against |
| payload.executionInputs.agenticWorkflow               | The name of the workflow that ran                                                                 |
| payload.executionInputs.instructions                  | The workflow base plan                                                                            |
| payload.executionInputs.agents                        | The agents as configured, with their instructions and the tools available to them                 |
| payload.executionOutputs.agents                       | What actually happened. One entry per agent, in execution order                                   |
| payload.executionOutputs.agents\[\].name and .subTask | The agent, and the subtask it was given                                                           |
| payload.executionOutputs.agents\[\].tools             | The tool calls that agent made                                                                    |
| ...tools\[\].name, .inputs, .output                   | The tool called, what it was called with, and what it returned                                    |
| payload.executionMessages                             | The conversation, each entry with a role, a message and an order                                  |
| payload.executionPlanDetails                          | runType, state, conversationId and the built-in tool names                                        |

executionInputs.agents is configuration—what the agent could have done. executionOutputs.agents is history—what it did. Comparing the two is how you tell a wrong tool choice from a tool that was never available.

One thing is not there: workflow variables. Values held in workflow memory are not exposed, so a metric cannot read them by name. Read the tool output or the agent message where the value surfaced instead. This is the single most common wrong assumption when writing a first metric.

# 7\. Step 4—Choose how the metric decides

Three approaches, and the plumbing is identical for all of them. What differs is where the correct answer comes from.

| Approach                                | Where the expected value comes from                                                                                           | Best for                                                                          |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Scripted rules                          | The execution itself, or a rule written into the script—a pattern match, a count of steps, a tool that should never be called | Anything checkable without a person deciding. Start here                          |
| Scripted against a supplied expectation | A value you author per record and map into the expected_response input                                                        | A correct answer only a person can decide, but which can then be compared exactly |
| Model-based judging                     | A judge skill called from your script decides and returns a score                                                             | Quality judgements that cannot be reduced to a comparison                         |

The first two are the same mechanism: your script compares and assigns the score. They differ only in where the expected value comes from. The third hands the decision to a model.

|                | Scripted, either kind                                    | Model-based                                                                   |
| -------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------- |
| How it decides | Your script compares values and assigns the score        | Your script sends the evidence to a judge skill and uses the score it returns |
| Cost           | None beyond the run                                      | One model call per record, so it scales with dataset size                     |
| Repeatability  | Deterministic. The same execution always scores the same | Probabilistic. Expect some variance between runs                              |
| Debuggability  | You can always say why it scored what it scored          | You depend on the judge explaining itself                                     |

Prefer a scripted rule whenever the question has a checkable answer. Reach for a judge only when correctness genuinely cannot be expressed as a comparison.

# 8\. Step 5—Write a rule-based metric

The pattern is always the same four moves: read the parser output, walk the trail, compare, and emit a score per thing you checked.

## Walk the trail

var agents = (payload.executionOutputs && payload.executionOutputs.agents) || \[\];

for (var a = 0; a < agents.length; a++) {

var tools = agents\[a\].tools || \[\];

for (var t = 0; t < tools.length; t++) {

var tool = tools\[t\];

// tool.name, tool.inputs, tool.output, agents\[a\].name, agents\[a\].subTask

}

}

Two details from real output. A tool output is sometimes a string and sometimes an object, so normalise it before you search it. And output shown to the user arrives as a FALLBACK tool whose inputs carry mode and prompt—if you are checking what the agent told somebody, that prompt is where the text is, not in a tool output.

## Derive the expectation instead of hard-coding it

A metric that hard-codes a record number only works for one row. Read the record out of the objective instead, and the same metric works for any dataset size:

var utterance = (payload.executionInputs && payload.executionInputs.utterance) || '';

var match = utterance.match(/INC\[0-9\]+/);

var expected = match ? match\[0\] : null;

Then assert that the tool was called with that value. This is the single most useful habit in custom metrics: most expectations that look like they need an authored expected result are derivable from the input row.

## Compare defensively

Trim and lowercase both sides before comparing names. The out-of-box tool metric compares raw strings with no normalising, so a difference in case or a stray space reads as a failure. Your own metric does not have to repeat that.

# 9\. Step 6—Write a model-based metric

When correctness is a judgement, call a skill from inside the metric and let a model score it.

## The call

var request = { executionRequests: \[{ payload: inputsPayload, capabilityId: CAPABILITY_ID, meta: { skillConfigId: SKILL_CONFIG_ID } }\], mode: 'sync' };

var out = sn_one_extend.OneExtendUtil.execute(request);

var raw = out\['capabilities'\]\[CAPABILITY_ID\]\['response'\];

var verdict = JSON.parse(raw).model_output;

## What to send the judge

Send the evidence, not the whole trail. A judge given everything scores vaguely. Build a small payload containing the objective, the specific output you are judging, and the criterion in plain language.

| Do                                                                                          | Do not                                               |
| ------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Ask for a single number on a stated scale, plus a one-line justification                    | Ask an open question and hope for a parseable answer |
| State the criterion explicitly in the prompt                                                | Assume the model knows your quality bar              |
| Wrap the parse in a try, and score it as an error if the judge returns something unexpected | Let a parse failure throw and fail the whole run     |
| Send the objective plus the one output being judged                                         | Send the entire execution trail                      |

Set the status field on your indicator to error rather than completed when the judge fails, so a bad model call is visible as a bad model call and not as a genuine low score.

# 10\. Step 7—Supply an expected result, if you need one

An expected result is a correct answer you author by hand for one specific record, so the metric can compare against it. Before you commit to it, be clear about when it is genuinely required.

| Question you are asking                                                                              | Needs an expected result?                       |
| ---------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Was the right tool called, with the record this run was about?                                       | No. Use OOB metric.                             |
| Did the agent finish within an acceptable number of steps?                                           | No. Use OOB metric.                             |
| Was a tool called that should never be called?                                                       | No. Use OOB metric.                             |
| Should this specific incident have been categorised as Network, VPN, and routed to the network team? | Yes. That is a human judgement about one record |

## Map a dataset field to a metric input

The expected answer lives in a field on the records you are evaluating, and you map that field to a metric input when you create the evaluation run. The platform pairs them for you, per record. There is no separate table to build, no key to derive, and nothing to look up.

1. On the metric, add an input named expected_response with a datatype of String.
2. Put the expected answer on the source records—either in a field that already exists, or in a new field you add to the table.
3. Create the evaluation run and select your custom metric among the metrics to run.
4. In Configure data, select your input data and give context. A section for mapping dataset fields to evaluation metric inputs then appears.
5. Map expected_response to the field holding your expected answer.
6. Your script reads currentInputs.expected_response and gets the value for the record being evaluated, already paired.

The mapping section only appears once a custom metric with inputs is selected, which is why it is easy to miss on a first pass.

| What you put in the field                         | When to choose it                                                                                        |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| The expected JSON, inline                         | The default. The whole expectation sits on the record it applies to, visible to anyone reviewing a score |
| A sys_id pointing at a record that holds the JSON | The expectation is larger than the field can hold, or the same expectation is reused across many records |

Check the length of the field you map. A short string field will truncate a JSON block without complaint, and a truncated expectation fails to parse. If in doubt, map a sys_id and hold the JSON somewhere with room for it.

## Reading it in the script

var expected = currentInputs.expected_response;

if (typeof expected == 'string') expected = JSON.parse(expected);

To support both storage choices with one script, test whether the value looks like a sys_id before parsing it as JSON:

var ref = String(currentInputs.expected_response || '').trim();

var expected = null;

if (/^\[0-9a-f\]{32}\$/.test(ref)) {

var gr = new GlideRecord('your_expected_result_table');

if (gr.get(ref)) expected = JSON.parse(gr.getValue('your_json_field'));

} else if (ref) {

expected = JSON.parse(ref);

}

Guard the parse. If the input is empty or is not valid JSON, score the record as an error rather than a failure—a missing or malformed expectation is a data problem, not a badly behaving agent.

## A workable JSON shape

One field can carry every expectation for that record, so put them all in one place. There is no platform-defined schema: your metric is the only thing that reads it. A shape along these lines works well:

| Field                     | Type             | Purpose                                                                                                                                                                               |
| ------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| record                    | String           | The record this expectation describes, for example an incident number. Not needed to find the expectation, but worth carrying as a sanity check that it was paired with the right row |
| expected_category         | String           | An expected field value on the record after the run                                                                                                                                   |
| expected_assignment_group | String           | Another expected field value                                                                                                                                                          |
| expected_tool_calls       | Array of objects | Each with a tool name, an agent name, and optionally the input values you expect to see                                                                                               |
| notes                     | String           | Why this is the right answer. Invaluable when someone disputes a score six months later                                                                                               |

Carrying the record identifier costs nothing and lets the metric assert that the expectation it received matches the execution it is scoring. If they disagree, that is worth reporting as an error.

# 11\. Step 8—Format the output and define labels

Two things here decide whether your results are readable, and both are easy to get wrong.

## Match the output template

In the Script Editor, select Metric output template to see the code the results display expects, and copy it as your starting point rather than writing the return shape from memory. Verify your output matches it before publishing.

| Field                                | What it is for                                                                                       |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| indicatorResponse                    | The array of scores. This is what aggregates into the run summary                                    |
| indicatorResponse\[\].value          | Your justification, in plain language. This is what a person reads when they ask why a record failed |
| indicatorResponse\[\].score          | The number. Keep the scale small and defined                                                         |
| indicatorResponse\[\].additionalInfo | Optional context per tool or agent, such as the names involved and the actual values seen            |
| indicatorResponse\[\].status         | completed or error. Use error for a metric that could not evaluate, not for a low score              |
| generated_response                   | Your working evidence, not scored. Put here what a person needs in order to debug a failure          |

The whole object is returned as a string. Wrap it with JSON.stringify inside a response property.

# 12\. Step 9—Publish and run

1. Select Publish metric. Until you do, the metric is not available to an evaluation run.
2. Go to Agentic Evaluations and create an evaluation.
3. Configure the dataset—choose the table, add filters, set the number of records, and write the Task template that tells the agent what to do with each record.
4. Select your metric alongside the built-in ones. Run the built-ins too: they give you a baseline.
5. If your metric declares inputs, map them to dataset fields in the section that appears once the metric is selected. See section 10.
6. Run it on one record first, then five, then the full set. Fix the metric on cheap runs, not expensive ones.
7. Read the failures before trusting the percentages. A metric that scores everything zero is usually a name mismatch, not a broken agent.

Do not aim for a perfect score. A dataset where everything passes is telling you the dataset is too easy, not that the agent is ready.

# 13\. Troubleshooting

| Symptom                                                       | Most likely cause                                                                                                                                                                                          |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No response at all, not even an error                         | The script threw before it returned. Reading a property of a missing object is the usual cause. Wrap the whole body in a try and return the caught error as an indicator with a status of error            |
| The script reports the parser tool failed on a good execution | The status is being compared against the wrong word. It reads success, not completed                                                                                                                       |
| The parser output is empty or undefined                       | The test value is missing or is not a valid execution plan sys_id. Check the key name too—log Object.keys(context)                                                                                         |
| A payload key you expected is not there                       | Workflow variables are not exposed. Read the tool output or agent message where the value surfaced                                                                                                         |
| A security exception on the first test run                    | The script is reaching across scopes. Read the execution from context instead of calling the API                                                                                                           |
| Every record scores zero                                      | A name mismatch. Compare your expected names against what the test actually returned, character for character                                                                                              |
| The metric is not selectable in a run                         | It has not been published                                                                                                                                                                                  |
| expected_response is empty in the script                      | The input was never mapped to a dataset field, the mapped field is empty on that record, or the name in the script does not match the name on the form. Score the record as an error rather than a failure |
| The mapping section never appeared                            | It only shows once a custom metric that declares inputs is selected for the run                                                                                                                            |
| A parse error on the expected result                          | The mapped field holds something other than valid JSON, it was truncated by a short field, or it holds a sys_id and the script is parsing it as JSON. Test for a sys_id first                              |
| Scores vary between runs on the same data                     | Expected for model-based judging. If it matters, make the metric rule-based                                                                                                                                |

# 14\. Limits worth knowing

Constraints to plan around rather than discover late.

| Limit                                           | What it means for you                                                                                                                                                          |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| An expected result is one per record            | It lives in a field on the records you evaluate, so scaling the dataset scales the authoring, unless the expectation is derivable from the input row                           |
| The expected result schema is yours alone       | Nothing validates it. A typo in a field name fails silently as a wrong score, so validate the shape in the script and report a bad expectation as an error                     |
| Workflow variables are not in the parser output | You can only assert on tool inputs, tool outputs and messages. If a value never surfaces in one of those, no metric can see it—surface it deliberately if you need to score it |
| Scores are AI-generated and probabilistic       | Human review remains essential for sensitive outputs. Auto-evaluation tells you where to look. It does not certify that an agent is safe                                       |

Prefer the documented surface where you can: the metric output template, the run test panel, and the parser tool output. Treat the rest as something to re-verify when you upgrade.

# 15\. A suggested order of work

| Do this                                                                          | Expected result needed | Why in this order                                                                  |
| -------------------------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------- |
| Run the built-in metrics against existing execution logs                         | None                   | Signal today, nothing to author. Establishes a baseline and shakes out the harness |
| Read the failures                                                                | None                   | Tells you which custom metric is actually worth writing                            |
| Write one rule-based custom metric for what the built-ins missed                 | None                   | Learn the contract, the output shape and the labels cheaply                        |
| Scale the dataset                                                                | None                   | Now the percentages are trustworthy enough for a go-live conversation              |
| Add a model-based metric, if quality judgement is what you are missing           | None                   | Makes a model call per record, so add it once you know it earns its place          |
| Supply expected results, only if correctness still cannot be expressed as a rule | One per record         | By now you know exactly which comparison justifies the authoring cost              |
| Re-run on a cadence and on every change to the agent                             | As above               | This is where the value actually is                                                |

Most teams get what they need without ever authoring an expected result. The real cost was never the scripting—it is deciding, case by case, what correct means for your business. That is also the part that makes the resulting numbers worth trusting.

# For more information

| Page                                     | Link                                                                                                  |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Create a custom metric                   | servicenow.com/docs/r/zurich/intelligent-experiences/create-custom-metric.html                        |
| Agentic evaluation parser tool           | servicenow.com/docs/r/yokohama/intelligent-experiences/eval-parser-tool.html                          |
| Agentic evaluation run results           | servicenow.com/docs/r/zurich/intelligent-experiences/aia-eval-metrics.html                            |
| Evaluate agentic workflows and AI agents | servicenow.com/docs/r/intelligent-experiences/execute-aia-eval.html                                   |
| Call a custom skill from a script        | servicenow.com/docs/r/intelligent-experiences/now-assist-skill-kit/call-custom-skill-from-script.html |