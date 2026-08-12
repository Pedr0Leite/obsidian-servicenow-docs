---
title: "Agentic Evaluations FAQ"
source: "https://www.servicenow.com/community/servicenow-otto-articles/agentic-evaluations-faq/ta-p/3429085"
author:
  - "[[Ashley Snyder]]"
published: 2025-12-12
created: 2026-08-12
description: "️ 12-minute read Table of Contents General Questions Getting Started Understanding Evaluation Metrics Running Evaluations Understanding Evaluation"
tags:
  - "clippings"
---
**️ 12-minute read**

## General Questions

**Q: What is Agentic Evaluations?**

**A:** Agentic Evaluations is an automated quality validation capability that helps you assess AI agent and agentic workflow performance before production deployment. Think of it as your pre-flight checklist for agentic workflows.

Agentic Evaluations uses LLM-based judges to evaluate your agent's execution logs and assess quality, similar to how an experienced ServiceNow administrator would review agent behavior. Rather than just checking final outputs, the evaluation examines the complete sequence of decisions and actions: every tool selection, every parameter passed, every step in the workflow. The judge evaluates whether your agent achieved the right outcome, even when the path varies between executions.

Each evaluation produces a score to help you understand your agent's performance.

**Key Terms**

**Execution logs:** Complete record of an AI agent's actions when completing a task, including every tool selection, parameter, and decision made

**LLM-based judge:** An AI model that evaluates agent performance by analyzing execution logs—similar to how an experienced administrator would review agent behavior

**Agentic workflow:** A multi-step business process where AI agents make context-aware decisions, choose tools, and orchestrate actions to accomplish tasks

**Q: What metrics does Agentic Evaluations provide?**

**A:** The framework provides three core evaluation metrics:

**1\. Overall Task Completeness**

Validates actual completion, confirms that workflows genuinely accomplished their assigned tasks, not just that agents reported success. This metric analyzes your agent's execution record, from the initial user request through each tool invocation to the final outcome, to verify real business outcomes were achieved.

For example, if you have an incident resolution workflow, this metric evaluates: Did the agent correctly categorize the incident, retrieve the relevant knowledge article, apply the fix, and update the incident record? It's your workflow-level view confirming that the multi-step orchestration achieved the intended business outcome.

**2\. Tool Calling Correctness**

Validates parameter accuracy and completeness, confirms that agents correctly construct tool calls with accurate parameters, proper formatting, and all required fields. Even when the agent picks the right tool, this metric ensures the inputs will lead to successful execution.

For example, if your agent calls "Update Incident Record," this metric checks: Is the incident sys\_id present and properly formatted? Are required fields like priority and state included? Are the values valid according to your ServiceNow instance configuration? This granular validation ensures that tool selection translates into successful tool execution.

**3\. Tool Choice Accuracy**

Validates optimal tool selection, confirms that at each decision point in the workflow, your agent selected the most appropriate tool for the task at hand. The judge analyzes the context, available tools, and task requirements to verify intelligent decision-making throughout the execution.

For example, when resolving a service request, did the agent correctly choose the "Get Knowledge Article" tool when it needed information, or did it mistakenly try to update a record before gathering necessary details? This validates decision-making quality before choices cascade into downstream issues.

**Q: Why do I need Agentic Evaluations? Can't I just use traditional testing?**

**A:** Traditional testing methods work well for deterministic workflows, where the same input consistently produces the same output. But AI agents are different. They're flexible and adaptive, making context-aware decisions with variable outputs. This means they require a new approach to quality validation.

When your workflow uses AI agents to interpret user intent, choose the right tools, and orchestrate multi-step processes, you need more than unit tests. You need AI-powered agentic evaluation that can validate tool selection, parameter accuracy, and genuine task completion, not just predetermined execution paths.

**Q: Where does Agentic Evaluations fit in my development process?**

**A:** Agentic evaluations serves as your quality gate between development and production:

1. **Plan and Build (AI Agent Studio):** Create your agents, configure their tools and instructions, define workflows
2. **Manual Testing (AI Agent Studio):** Run test conversations to validate basic behavior, refine agent responses through iterartive testing
3. **Automated Evaluation (Agentic Evaluations):** Measure task completion rates, tool calling accuracy, and overall quality at scale with automated judge-based evaluation across scaled execution logs
4. **Deploy:** Promote production-ready agents to live environments and make them available to end users
5. **Monitor (AI Agents Analytics):** Track ongoing production performance, measure user satisfaction, identify areas for continuous improvement

Think of Agentic Evaluations as your pre-flight checklist: After building and manually testing your agent, use automated evaluation to validate it works correctly across diverse scenarios before deployment. Once deployed, AI Agent Analytics helps you monitor ongoing performance and identify opportunities for refinement.

**Q: What types of agents and workflows can I evaluate?**

**A:** Agentic Evaluations works with any agentic workflow built in ServiceNow's AI Agent Studio, including:

**Common use cases:**

- Issue resolution agents (ITSM, HR Service Delivery, Customer Service)
- Case creation and management workflows
- Multi-agent workflows where agents collaborate
- Custom workflows leveraging IntegrationHub and external tools

**What can be evaluated:**

- Agents using out-of-the-box ServiceNow tools
- Agents using custom tools you've built
- Single-agent workflows
- Standalone AI agents
- Multi-agent orchestration scenarios
- Workflows involving external system integrations

If your agent runs in AI Agent Studio and generates execution logs, you can evaluate it with Agentic Evaluations.

**Q: Should I evaluate standalone agents or complete agentic workflows?**

**A:** Use both approaches at different stages:

**Evaluate standalone agents when:**

- You're building an agent and want to validate it works correctly before adding it to a workflow
- A complete workflow isn't performing well and you need to identify which specific agent is causing issues
- You've updated an agent and want to verify your changes improved performance
- You're creating an agent that will be reused across multiple workflows

**Evaluate agentic workflows when:**

- You need to confirm multiple agents work together correctly to achieve a business outcome
- You're preparing for production deployment and need end-to-end validation
- Success depends on agents passing information correctly between steps
- You want to validate the entire process, not just individual components

Think of standalone agents like unit evaluation and agentic workflow evaluation like end-to-end evaluation, you need both to build confidence in your AI agents, but they serve different purposes in your quality validation process.

**Q: Does Agentic Evaluations guarantee my agent is production-ready?**

**A:** No, and that's by design. Agentic Evaluations is a powerful decision-support tool, not a replacement for human judgment.

**What the tool provides:**

- AI-generated performance scores (probabilistic, not deterministic)
- Visibility into agent behavior patterns
- Data-driven insights for improvement
- Scalable testing across many scenarios

**What still requires human review:**

- Final deployment decisions based on your organization's risk tolerance
- Validation that agent behavior aligns with business expectations
- Assessment of context that automated systems can't fully capture
- Compliance with industry-specific regulations and standards

Think of it like this: Agentic Evaluations tells you *how* your agent performs. You decide *whether* that performance meets your needs.

**Q: How is Agentic Evaluation different from Auto-Evaluation for Now Assist Skills?**

**A:** They evaluate different things:

**Auto-Evaluation for Now Assist Skills** evaluates individual AI capabilities in isolation, like whether a summarization or classification skill produces quality outputs. It answers: "Does this specific AI skill work well?"

**Agentic Evaluation** evaluates complete individual agents or agentic workflows where agents make decisions, choose tools, and accomplish multi-step tasks. It answers: "Can this agent successfully complete real-world workflows from start to finish?"

**When to use each:**

- Use **Auto-Evaluation** when evaluating individual AI skills or capabilities
- Use **Agentic Evaluation** when evaluating complete agent workflows built in AI Agent Studio

**Q: Does evaluation consume assists?**

**A:** Yes. Running evaluations uses AI services to generate scores, which consumes assists. Consider this when:

- Planning large-scale evaluations
- Evaluating frequently during development
- Budgeting for AI usage in your organization

---

## Getting Started

**Q: I'm new to Agentic Evaluations. Where should I start?**

**A:** Start here:

1. **Pick a workflow or agent you know well**: Choose one you've already built and tested manually. This helps you evaluate the quality of the evaluation insights themselves.
2. **Start small**: Begin with 10-20 execution logs to understand how evaluation works before scaling up.
3. **Use all three metrics**: Select Overall Task Completeness, Tool Calling Correctness, and Tool Choice Accuracy to get a comprehensive view.
4. **Review the detailed results**: Don't just look at the scores, drill down into individual executions to understand what the evaluation is telling you.
5. **Iterate**: Make improvements based on the recommendations, then re-evaluate to see if performance improved.

The most important thing is to start. You'll learn more from running one evaluation than from reading about it.

**Q: Should I run Agentic evaluations in production or a sub-production environment?**

**A:** We strongly recommend running evaluations in sub-production environments (test, staging, development) rather than production. Evaluating in sub-production enables you to iterate quickly without impacting live users, experiment safely with agent configurations, and identify issues before they affect production operations.

Use sub-production for active development and pre-deployment validation, running frequent evaluations with controlled test scenarios. Once your agent is deployed, you can periodically evaluate production execution logs to monitor ongoing quality. Consider running these evaluations in a test environment using exported production data, rather than generating new test executions in production. The key principle: test in sub-production, validate with production data, deploy with confidence.

**Q: How can I create a dataset for evaluation?**

**A:** Datasets used in Agentic Evaluations are comprised of execution logs records. Execution logs capture the complete record of an AI agent's actions when completing a task. They include:

- What the agent was asked to do
- Which tools the agent chose to use
- How the agent invoked those tools
- The sequence of steps the agent took
- The final outcome

These logs provide the raw material for evaluation. There are three ways to create an evaluation dataset:

**1\. Use existing execution logs**

Leverage logs from agents that have already run in your environment. This is recommended for agents with existing usage history and is ideal when you want to evaluate real-world performance with actual user interactions, conduct post-deployment analysis, or assess production readiness. Best for production readiness assessments, regression testing, and analyzing real-world performance.

**2\. Generate new execution logs in AI Agent Studio**

Run the agent workflow in AI Agent Studio to create fresh test data with full control over test scenarios. This works well when you need precise control over test cases, are in active development, want to validate specific workflow configurations before deployment, or need to test edge cases.

**3\. Run an agentic workflow to generate execution logs**

Automatically generate execution logs at scale directly within Agentic Evaluations. An LLM acts as a conversational partner with your agent, autonomously driving workflow execution across multiple records. This eliminates the bottleneck of waiting for real users or manually creating test cases one at a time, allowing you to evaluate 50-100+ scenarios quickly. Best for pre-deployment validation at scale, testing across diverse data variations, and rapid iteration cycles.

**Q: How many samples do I need for evaluation?**

**A:** Start with enough data for meaningful insights:

- **10-50 samples**: Initial evaluation and debugging
- **100-300 samples**: Production rollout readiness

Start small to validate your approach, then expand as you gain confidence.

---

## Running Evaluations

**Q: When should I run Agentic Evaluations?**

**A:** Run evaluations at strategic points in your agent development and deployment lifecycle:

**After collecting sufficient data:** Evaluation runs are measured against logs of agentic workflow activity on your instance. Ensure you have enough execution logs to make meaningful assessments, at minimum 10-20 logs for initial testing, 50-100 for pre-deployment validation.

**When you make significant changes:** Run evaluations after updates to your agentic workflow to track the efficacy of the new version. This includes changes to:

- Agent instructions or system prompts
- Tool definitions or configurations
- Workflow logic or structure
- Model or parameter settings

**During development cycles:**

- After each major iteration to validate improvements
- Before promoting changes from development to test environments
- As part of your testing process before deployment

**Post-deployment:**

- Periodically (weekly, monthly, or quarterly) to monitor ongoing quality
- When investigating production issues or user feedback
- To establish baseline metrics for future comparisons

**Pro tip:** Establish a regular evaluation cadence based on your development velocity. Active development may require daily or weekly evaluations, while stable production agents might only need monthly quality checks.

**Q: How long does an evaluation take?**

**A:** Most evaluations complete in minutes. When evaluating against 100+ records, evaluations can take 10-30 minutes to complete. Real-time progress tracking shows you exactly how far along the evaluation is, helping you plan your next iteration, grab coffee while waiting, or start reviewing partial results as they become available.

**Q: Can I modify an evaluation after starting it?**

**A:** No. Once you click " **Start evaluation**," the configuration is locked. This ensures evaluation integrity and reproducibility. If you need to make changes, you can:

- Clone the evaluation run
- Make your modifications
- Start a new evaluation

**Q: Can I stop or abort a running evaluation?**

**A:** Yes, click the "Abort evaluation" button. Note that partial results won't be saved - you'll need to start a new evaluation run.

---

## Understanding Evaluation Metrics

**Q: Which AI model(s) do you use as the judge model?**

**A:** Agentic Evaluations uses ServiceNow's Large Language Model (Now LLM) as the judge model to evaluate your agent's performance. This is an AI-powered evaluation system (often called "LLM-as-a-judge") that analyzes your agent's execution logs and scores them against the evaluation metrics you've selected.

**How the Now LLM judge evaluates:**

The Now LLM judge examines each execution log and evaluates (based on metric selection):

- **Overall task completeness:** Did the agent complete its intended task?
- **Tool choice accuracy:** Were appropriate tools selected?
- **Tool calling correctness:** Were tools called correctly with valid parameters?

The judge model considers multiple factors when scoring:

- The agent's defined objectives and instructions
- Tool definitions and expected usage patterns
- The execution trace showing what the agent actually did
- Conversation logs and related records for context

The judge model understands ServiceNow workflows, tools, and terminology, providing consistent evaluation criteria across hundreds of records within an evaluation dataset. However, automated scores are probabilistic, not deterministic, which is why your human review is essential for final deployment decisions.

**Q: How are percentages calculated?**

**A:** For each metric, the percentage is calculated only for records or tools that were successfully evaluated. Evaluation errors are excluded from the calculation.

For example, if 10 records were evaluated but 2 had evaluation errors, the perecentage for Overall Task Completeness would be based on the 8 records that were successfully evaluated, not all 10.

This ensures that technical issues during evaluation don't artificially lower your agent's performance scores. You can see which records had evaluation errors in the detailed results view.

**Q: What do the rating thresholds mean (Excellent, Good, Moderate, Poor)?**

**A:** The default thresholds are:

- **Excellent**: 90-100%
- **Good**: 70-89%
- **Moderate**: 50-69%
- **Poor**: 0-49%

These thresholds are **customizable**. Click "Customize metric thresholds" to define your own quality standards based on your organization's risk tolerance and use case requirements.

**Q: Why would I customize metric thresholds?**

**A:** Different use cases have different quality requirements. Customizing thresholds helps you align evaluation results with your specific business needs and risk tolerance.

**Common scenarios:**

- **High-risk scenarios** (compliance-sensitive workflows) might require 95%+ for "Excellent" to ensure maximum accuracy and reliability
- **Lower-risk scenarios** (internal documentation, categorization, routine tasks) might accept 80%+ as "Excellent" since minor errors have limited impact
- **Customer-facing applications** typically need higher thresholds than internal tools due to reputation and user experience concerns
- **Pilot or experimental agents** might use lower thresholds initially, then raise them as the agent matures

Adjust thresholds to match your specific context—there's no one-size-fits-all standard.

---

## Understanding Evaluation Results

**Q: How do I read my evaluation results?**

**A:** After running an evaluation, you'll see AI-powered scoring with clear deployment guidance. Each metric receives a rating like "Good," "Excellent," or "Deploy with caution," giving you visibility into your agentic workflow or agent's readiness.

For example:

- **Good**: Most tasks completed successfully, but some performance inconsistencies suggest areas for improvement
- **Excellent**: The agent consistently selects the best tools for each task
- **Moderate**: A significant portion of tool inputs had correctness issues

Each metric includes:

- **A clear rating badge**: Good, Excellent, Moderate, etc.
- **Specific percentages**: Showing how execution logs performed across your dataset
- **Result explanations**: Describing what the evaluation observed—which steps succeeded, which failed, and common patterns
- **Recommended actions**: Providing specific guidance on what to investigate (e.g., "Investigate recurring failures, identify root causes, and refine tool execution logic")

You can drill down into individual execution logs to see the complete workflow: exactly which tools the agent invoked, what parameters were passed to each tool, which steps succeeded or failed, and how the workflow progressed from start to finish. This visibility helps you identify patterns across multiple executions rather than debugging individual cases.

**Q: What does "human review required" mean?**

**A:** While Agentic Evaluations provides sophisticated automated scoring, the results are AI-generated and probabilistic. Human review ensures that:

- Evaluation scores align with business expectations
- Agent behavior is appropriate for your specific use case
- Results meet organizational quality standards and risk tolerance
- Deployment decisions consider the context that automated systems can't fully assess

**Q: How do I interpret the "task completion distribution" chart?**

**A:** This circular chart visualizes how your execution logs performed across the Overall Task Completeness metric:

- **Purple segment**: Successful executions – tasks completed as intended
- **Coral/Orange segment**: Partially successful executions – some objectives achieved but not all
- **Cyan/Blue segment**: Unsuccessful executions – tasks failed to complete

The center shows the total number of records evaluated. This gives you a quick visual understanding of overall performance patterns at a glance.

**Q: What do I see when I drill down into an individual evaluation result?**

**A:** When you click on an individual evaluation result, you'll see detailed information about that specific execution:

- **Record details**: Links to the execution log, conversation log, and related records so you can review the full context
- **Execution status**: Whether the workflow completed successfully, terminated early, or had errors
- **Evaluation details**: The score assigned for each metric along with a detailed explanation of why that score was given
- **Tool evaluation**: Expandable sections showing which agents used which tools, the parameters passed, and whether tools were used correctly
- **Exclusion option**: Ability to exclude this record from evaluation results if it's not representative or has data quality issues

This drill-down view helps you understand exactly what happened during execution and why the evaluation scored it the way it did.

**Q: Why would I exclude a record from evaluation results?**

**A:** You might exclude records if:

- The execution lo isn't representative of real-world usage
- There were system issues during execution (not agent issues)
- The execution log has data quality problems
- The scenario is an edge case you don't need to optimize for

Excluding records recalculates the metrics without those data points.

**Q: How do I know if my agent is ready to deploy?**

**A:** Consider these factors:

1. **Metrics meet thresholds**: Scores are in your desired range (typically "Good" or "Excellent")
2. **Consistent performance**: Individual records show stable, predictable behavior
3. **Representative evaluation**: Your dataset covers real-world scenarios the agent will encounter
4. **Stakeholder approval**: Subject matter experts validate that agent behavior is appropriate
5. **Risk assessment**: Your organization's risk tolerance aligns with observed performance

Even with perfect scores, remember: human review is required for final deployment decisions.

**Q: What should I do after running an evaluation?**

**A:** Your next steps depend on your evaluation results:

**If results meet your deployment criteria (typically "Good" or "Excellent" ratings):**

1. **Document your results** - Export the evaluation report for compliance and stakeholder approval
2. **Get stakeholder sign-off** - Share results with product owners, compliance teams, or management as needed
3. **Deploy to production** - Promote your agent from test to production environments
4. **Set up monitoring** - Use AI Agent Analytics in AI Control Tower to track ongoing performance

**If results show issues ("Moderate" or "Poor" ratings), follow this iteration process:**

Follow the iteration process described in the "How do I iterate and improve based on evaluation results?" to diagnose root causes, make targeted improvements, and re-evaluate.

**Q: My evaluation scores are low. How do I troubleshoot and improve them?**

**A:** When evaluation results show issues, follow this systematic improvement process:

**1\. Analyze patterns by metric**

Drill into individual failed records to identify common issues. Different metrics indicate different problems:

**Low Overall Task Completeness** suggests:

- **Unclear agent instructions**: Review your agent's instructions and ensure they clearly define the expected outcome
- **Missing or incorrect tools**: Verify your agent has access to all the tools it needs to complete tasks
- **Tool description issues**: Check that your tool descriptions accurately explain what each tool does and when to use it
- **Workflow logic problems**: Review your workflow structure to ensure steps are in the right order

**Low Tool Calling Correctness** suggests:

- **Missing required parameters**: Your agent isn't providing all required fields when calling tools
- **Incorrect parameter formats**: Parameters are in the wrong format (e.g., string instead of number)
- **Invalid values**: The agent is using values that don't match your instance configuration

**Low Tool Choice Accuracy** suggests:

- **Ambiguous tool descriptions**: Make your tool descriptions more specific about when each tool should be used
- **Too many similar tools**: Consider consolidating tools that serve similar purposes
- **Insufficient context**: Ensure your agent has enough information to make informed decisions

**2\. Diagnose root causes**

Look for patterns across multiple failed executions rather than fixing individual cases. Determine what's causing the issues you observed:

- **Agent configuration**: Are instructions clear and complete?
- **Tool definitions**: Are tool descriptions accurate and helpful?
- **Workflow design**: Are there missing steps or logic gaps?
- **Dataset quality**: Are test cases representative and valid?

**3\. Make targeted improvements**

Address the root causes you identified:

- Refine agent instructions and system prompts
- Improve tool descriptions and examples
- Update workflow structure
- Add error handling and fallback logic

**4\. Re-evaluate with comparable data**

After making improvements, you need fresh execution logs that reflect your updated agent. Clone your original evaluation configuration, then generate new execution logs using one of these methods:

- **Manual testing in AI Agent Studio**: Run your improved agent against the same types of test scenarios
- **Run an agentic workflow to generate execution logs**: Use the same record filters and selection criteria as your original evaluation to ensure comparable test coverage

This gives you a fair before/after comparison using the same test methodology against your improved agent.

**5\. Iterate until ready**

Repeat this cycle until metrics meet your deployment criteria. Most customers iterate 2-4 times before achieving deployment-ready scores.

**Q: What if my evaluation results seem inconsistent or unexpected?**

**A:** If evaluation scores don't align with your expectations, consider these possibilities:

**The evaluation may be correct:**

- Remember that automated scores are AI-generated and probabilistic, not deterministic
- The evaluation might be catching issues you missed during manual testing
- Review individual execution details to understand the judge's reasoning

**Check your test data quality:**

- Are execution logs representative of real-world usage?
- Do test cases cover the scenarios you actually care about?
- Are there system errors or data quality issues affecting results?

**Verify your expectations:**

- Are your quality thresholds aligned with your actual requirements?
- Review the "Customize metric thresholds" to adjust what "Good" means for your use case
- Compare automated scores with human review of the same executions

**Review specific discrepancies:**

- Drill down into results that seem wrong
- Check if the judge is evaluating based on criteria you didn't anticipate
- Look for patterns in where expectations and results diverge

If you consistently find scores don't match manual review, this may indicate your agent instructions, tool descriptions, or quality thresholds need refinement. Human review remains essential for validating automated scores align with business expectations.

---

## Working with Agentic Evaluations

**Q: How do I share evaluation results with stakeholders?**

**A:** Click the " **Export as report** " button to generate comprehensive documentation, including:

- Executive summary with key metrics
- Detailed breakdown of all evaluation results
- Individual record analysis
- Recommendations based on performance

This report can be shared with compliance teams, management, or included in deployment documentation.

**Q: How do I compare evaluations and track improvement over time?**

**A:** You can compare evaluations to measure progress and validate improvements:

**Viewing all evaluations:**

From the Evaluations home page, you can view all your evaluation runs and compare:

- How performance improved after making changes
- Different agent versions or configurations
- Performance across different datasets or time periods

**Using Clone for fair comparisons:**

The "Clone" feature copies all settings from an existing evaluation (agent, dataset filters, evaluation metrics) so you can:

- Re-evaluate after making improvements using the same test data
- Track progress with consistent methodology
- Create objective before/after comparisons

**Clone vs. creating new:**

- **Clone**: Use when you want to measure improvement on the same agent with the same configuration. Perfect for iteration cycles.
- **Create new**: Use when evaluating a different agent or testing a completely different scenario.

**Pro tip:** For the best comparison, clone your baseline evaluation and re-run it after each change. This ensures you're measuring improvement fairly with identical test conditions.

Version history

Last update:

12-15-2025 07:58 AM

Updated by:

[Ashley Snyder](https://www.servicenow.com/community/user/viewprofilepage/user-id/329530)

Contributors