---
aliases:
  - "AI Agent tools – Getting the most out of your agen"
area: "AI & VA"
source: notion-export
tags:
  - ai-agents
  - agentic-workflow
  - ai-agent-tools
  - ai-search
  - flow-designer
---

# AI Agent tools – Getting the most out of your agentic workflows

# **AI Agent tools – Getting the most out of your agentic workflows**

Updated as of Yokohama Patch 1

AI Agent tools are essential to bringing your AI Agents from intelligence to action. See below for tips on how to optimize the usage of AI Agent tools. You can familiarize yourself with the tools available here: [https://www.servicenow.com/docs/bundle/yokohama-intelligent-experiences/page/administer/now-assist-a...](https://www.servicenow.com/docs/bundle/yokohama-intelligent-experiences/page/administer/now-assist-ai-agents/task/configure-next-best-action-agent.html)

### **General tool settings and tips**

- **Name** and **Description**: The AI Agent orchestrator will take these fields into account when determining whether and how to use the tool.
- **Input:** some tools such as Script or Record operation allow you to create an input variable, provide a description, and use it as a reference for your action.
- **Supervised/Autonomous:** You can determine whether to ask the user for permission to run the action.
- **Display Output:** This displays the output of the action to the end-user.
- **Output transformation strategy:** This determines the verbosity of the output. Some tools generate content, such as web search. An output strategy of “None” has no processing and output the raw output which may be JSON or technical jargon. This is preferable if outputting specific records or IDs. On the other end of the spectrum, an output strategy of “Verbose” will generate a longer, more eloquent answer.

All tools can currently only input and output String. For some tools such as Flow Action or Script, you may need to transform inputs and outputs to String for the tool to properly work. As a safety mechanism, you can set the system property: **sn_aia.continuous_tool_execution_limit** to set how many times maximum a given tool can run. Note that the number of tools (actions) run determine the number of assists consumed.

- ***NOTE**** - When you duplicate an AI Agent, the tools in the newly duplicated agent is still the tool in the original AI Agent! To make sure you don't affect the original Agent's tool, remove the tool and add a new tool. Take a screenshot or notes of the original tool if necessary so that you don't completely start from scratch.

### **Catalog Item**

Add a catalog item to your AI agent. Only conversational catalog items are available. See [here](https://www.servicenow.com/community/virtual-agent-nlu-articles/how-to-request-catalog-items-in-now-assist-in-virtual-agent/ta-p/2747811) for more information on conversational catalog items. For example, a holiday booking agent can ask if a user needs a travel visa, for which you may have a catalog item and can present to the end-user. This is what it looks like in AI Agents.

[](https://www.servicenow.com/community/image/serverpage/image-id/432273iE47B8903DD575678/image-size/medium?v=v2&px=400)

### **Conversational topic**

Add a Virtual Agent topic to your agent. Only LLM-based Virtual Agent topics (or topic blocks) that are active and published are available to use. Setup topics are not available. Select the topic from the tool drop-down to use.

### **Sub-flow/Flow Action**

Add a Sub-flow or Flow action from Workflow Studio to your AI Agent. The tool’s description should note what inputs and outputs the flow should expect. Note that the flow must have inputs and outputs as **String**, or else the AI Agent orchestrator (LLM) will not be able to process it.

Integration Hub spokes are now also AI Agents, see: [https://www.servicenow.com/docs/bundle/yokohama-integrate-applications/page/administer/integrationhu...](https://www.servicenow.com/docs/bundle/yokohama-integrate-applications/page/administer/integrationhub/reference/available-spk-ai-agents.html). The tools within the spoke AI Agents have been optimized for AI Agent processing. See below for an example of a *Microsoft Entra ID group manager spoke* AI Agent and its Flow Action tools.

[](https://www.servicenow.com/community/image/serverpage/image-id/432274i8B4C75D8DDDF450D/image-size/large?v=v2&px=999)

### **Now Assist skill**

Use an out-of-box or custom Now Assist skill created and published in Skill Kit to use with your AI Agent. The tool’s description should note what inputs and outputs the Skill should expect.

### **Record operation**

Use this tool if you want to create, look up, update, or delete records. To look up records, you need to select the table and the condition to display records. The condition builder is similar to Workflow Studio. Note that only String output type is available; records cards are not available. Select the “Verbose” output strategy for a better formatted list. See below for an example of looking up a list of purchase orders where the business owner is the end-user.

[](https://www.servicenow.com/community/image/serverpage/image-id/432272iAF64BE679C91B0C2/image-size/medium?v=v2&px=400)

To update records, you have to select the table and condition of which record(s) to update. Then select the field and value(s) to update. You can use **Inputs** to have the AI Agent ask the end-user which records to update and how. You can then use those inputs in the condition or field values via {{...}}. See the below example, which is an AI Agent updating the quantity of a purchase order line based on a user input of a purchase order line number. Note: Reference fields, or fields not on the table, are not supported.

[](https://www.servicenow.com/community/image/serverpage/image-id/432275i1F8C7FB9EAFE33D3/image-size/large?v=v2&px=999)

### **Script**

AI Agents can run scripts, and it can include inputs provided by the end-user or the AI Agent itself. See the below example, which outputs to System Logs a text string plus an Incident number from a previous step from the AI Agent. The input is called using ***inputs.inc_number.*** 

[](https://www.servicenow.com/community/image/serverpage/image-id/432276i4CDFF9EF6A4CE86D/image-size/medium?v=v2&px=400)

Result:

[](https://www.servicenow.com/community/image/serverpage/image-id/432277i2ADD975E309D1DA9/image-size/medium?v=v2&px=400)

### **Search Retrieval**

This uses AI Search/RAG to search for content such as knowledge articles. Select a Search profile, search sources, and fields (such as a KB Short description and Article body) to pass to the AI Agent. For search criteria, it is recommended you use “Hybrid”, which combines semantic and keyword search methods. Semantic indexed fields are based on the fields in your search source’s Indexed sources. If you run into issues, be sure that Now Assist in Search store app has been updated, AI Search is properly configured, search sources are indexed, and that the search profile has been published. Below is an example of search retrieval based on a KB article with citations.

[](https://www.servicenow.com/community/image/serverpage/image-id/432279iF322381845D3EA78/image-size/medium?v=v2&px=400)

### **Web Search**

There are two ways to perform a Web Search - “Search and scrape” or “AI Answers”. By using search and scrape, you are calling the search engine to return a list of related web links and a web scraping service to scrape those websites. The two options are Bing search or Google search. Then, it passes the scraped data to Now LLM to generate a response. By using AI answers, you are calling an LLM to generate an answer. The two options are Gemini or Perplexity. See this article for step-by-step instructions on how to set up Web Search: [https://www.servicenow.com/community/now-assist-articles/how-to-set-up-the-web-search-ai-agent-tool-...](https://www.servicenow.com/community/now-assist-articles/how-to-set-up-the-web-search-ai-agent-tool-using-google-gemini/ta-p/3227494). Remember to use the Output strategy to determine search result quality and length. Below is an example of a web search result (Output strategy set to "Verbose") with citations.

[](https://www.servicenow.com/community/image/serverpage/image-id/432278i5672AE288B2DA2F0/image-size/medium?v=v2&px=400)

## Related
- [[Introducing AI Agents and Quick Start Guide]]
- [[AI & VA]]
- [[Agentic Workflow & AI Agents – Tips]]

- [[Agentic Workflow & AI Agents]]
- [[Best Practices for Creating AI Agent Workflows]]
- [[Get Familiar with Agentic Workflows & AI Agent]]
- [[AI Search]]
- [[Now Assist in AI Search]]