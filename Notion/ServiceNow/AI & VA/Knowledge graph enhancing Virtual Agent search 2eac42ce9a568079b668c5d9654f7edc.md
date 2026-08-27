---
aliases:
  - "Knowledge graph enhancing Virtual Agent search"
area: "AI & VA"
source: notion-export
tags:
  - virtual-agent
  - knowledge-graph
  - ai-search
  - now-assist
  - nlq
---

# Knowledge graph enhancing Virtual Agent search

# **Introduction**

A well-structured knowledge base is without a doubt one of the most powerful tools an organization can use to meet this expectation. By making relevant information easily accessible, a strong knowledge base empowers users to find solutions on their own—without needing to contact support teams. This not only improves the user experience, but also significantly reduces the volume of incoming tickets and repetitive questions handled by service teams.

However even the best knoweldge bases can fall short if users struggle to find the right information. Especially in large global organisations this challenge is amplified. Policies will be different for each country, business unit and departments. A simple query, for example on a leavve policy, might therefore be challenging to find an asnwer to if there are high volumes of leave policy articles.

With AI search we can boost geographical content and I have often relied on this excellent guide from [@Shamus Mulhall](https://www.servicenow.com/community/user/viewprofilepage/user-id/451610) for boosting local content to users – [Result Improvement Rules for Global Companies](https://www.servicenow.com/community/intelligence-ml-articles/result-improvement-rules-for-global-companies/ta-p/2472571)

Howver this is only part of the answer, the search tool deosn’t intuitively undrstand what is the best answer to the employee. This is the challenge we have addressed with the May release of our Now Assist for Search in Virtual Agent where we can enhance search queries with knowledge graph.

# **Overview**

This article is a result of a deep dive I have taken into the Knowledge Graph capabilities together with my colleague **Thomas Geering**. I will walk through what a Knowledge Graph is used in Servicenow and highlight three key capabilites where knowledge graph can provide a benefit for your employees through the virtual agent.

- Q&A search enhancement
- Slot filling in conversational catalog
- Employee Q&A to Knowledge Graph

I will provide examples of the functionality, how to activate the feature and highlight configuratoin options.

### **Knowledge Graph**

[Screenshot 2025-06-13 at 15.09.48.png](https://www.servicenow.com/community/image/serverpage/image-id/448606i9DEA9E355F554E25/image-size/small?v=v2&px=200)

The

[knowledge graph](https://www.servicenow.com/docs/bundle/yokohama-intelligent-experiences/page/administer/knowledge-graph/concept/knowledge-graph-landing.html)

uses structured and unstructured data within the ServiceNow database making it accessible through natural language queries (NLQ). NLQ is particularly important in the world of generative AI as AI bots and Agentic Workflows will use NLQ to look up information. Customers can utilise the OOTB knowledge graphs or configure their own using the

[knowledge graph designer](https://www.servicenow.com/docs/bundle/yokohama-intelligent-experiences/page/administer/knowledge-graph/concept/exploring-knowledge-graph.html)

. These graphs are the underpinning enabler of the features highlighted in this article. Although this article focuses on the capabilities enhancing the Virtual Agent knowledge Graph also have other uses, most notably as a source of data for

[Agentic Workflows](https://www.servicenow.com/community/now-assist-articles/ai-agent-tools-getting-the-most-out-of-your-agentic-workflows/ta-p/3227648)

.

### **Q&A Search Enhancement**

[Screenshot 2025-06-13 at 13.23.21.png](https://www.servicenow.com/community/image/serverpage/image-id/448601i76AB2CDD6AA91F9B/image-size/medium?v=v2&px=400)

Normally during a search the articles are ranked according to weight. The weight is given based on relevance on the keywords used and semantic significance of the wording. Result improvement rules as described above can further provide user specific weighting to the article however this requires extra maintenance of the articles. This is especially challenging for global organisations and we often see this challenge being prevalent in HR Knowledge bases where policies, for example leave policies, will be different for each legislation. With Q&A Search enhancement key information is included in the search analysis performed by the LLM.

In the example you can see two users asking the same question: *What is the max amount of time I can take off for PTO?*. Since the location information is included with the query the LLM will *understand* that Storm (based in Sweden) is interested in the Swedish article and Emily (based in US) is interested in the US article. The only additional consideration in this case is that the articles are clearly defined for the country the apply to which anyhow is best practice when writing articles.

### *Activation and configuration*

This feature uses the **Now_user_graph** by default which includes information about the user’s Company, Department, Assets, Location and Manager.

Especially the location is useful for the knowledge graph. To activate the Q&A Search Enhancement you can set the *sn_vad_genai.now_assist.search.user_knowledge_graph.enabled* sys property to *true*. It is possible to configure the input given to the LLM and change the knowledge graph from the *sn_kg_context_config* table. However this requires changes to code so proceed with caution.

### **Slot filling in conversational catalogue**

[Screenshot 2025-06-13 at 13.51.25.png](https://www.servicenow.com/community/image/serverpage/image-id/448605iCCB43CEFB09A2320/image-size/medium?v=v2&px=400)

The conversational catalogue was one of the earliest capabilities introduced with Now Assist. In short it allows Now Assist to read available offerings from the service catalogue and help a user fill them out through a conversation. An example of this may be a user needing a new laptop and instead of opening the “request a laptop” form on the employee centre they can ask the virtual agent to help them request a laptop the virtual agent will then guide them through the questions on the form.

In some cases the forms contain questions where there already is a known answer. this could be a question about which department the user is in or their address for shipping. Although this could be added to the form by a query this is additional code and may create additional maintenance. With slot filling from the knowledge graph we can allow the Virtual Agent to query the knowledge graph for answers to questions on the users behalf.

In this example Emily is getting help from the VA to request an employee travel visa. Some of the information is added directly from the ask such as the country travelling to and the start date – however the Country of Birth is a required field to be added to the visa – here we have activated the OOTB HRSD knowledge graph that contains this specific data and the VA can fill it out for her. Naturally it asks for her confirmation before proceeding.

### *Activation and configuration*

This feature uses a knowledge graph assigned to the virtual agent through the assistant configuration. Before configuring start by setting the syst property *sn_vad_genai.knowledge_graph.enabled* to true and you can configure the number of slots filled with the property

*sn_vad_genai.max.knowledge_graph.slots*. After this you can go to assistants in conversational interfaces and add your knowledge graph of choice to the Virtual Agent on your portal.

### **Employee Q&A to Knowledge Graph**

Sometimes employees ask questions for information that is stored directly in the ServiceNow database. This might be which asset ID their computer has, what their employee number is or even information about colleagues or managers. With employee Q&A the Virtual Agent can check the knowledge graph directly for an answer. In the example below you can see example queries such as asset questions and questions about employees even by asking for “the manager of my manager” the knowledge graph can understand that it needs to look up the manager relation user to user twice to get the answer.

[Screenshot 2025-06-13 at 16.25.12.png](https://www.servicenow.com/community/image/serverpage/image-id/448607i9FE9797882F0AC7C/image-size/large?v=v2&px=999)

### *Activation and configuration*

This feature uses the *Now_user_graph_nlq* Graph by default as seen in the screenshot above. To activate set the *sn_ais_assist.enable_knowledge_graph_nlq* sys property to *true* and in the *sn_ais_assist.kgnlq_schema_name* sys property you can define which knowledge graph you want the feature to utilise.

# **Conclusion**

All three capabilities are great ways to enhance the responses to employees through the virtual agent. There is a clear benefit in simplified administration and faster time to value by using knowledge graphs as a source of information to employees. I would encourage customers to combine these features with other capabilities such as result improvement rules for the optimal outcome.
## Related
- [[Now Assist Q&A using Dynamic Translation]]
- [[Now Assist]]
- [[Introducing AI Agents and Quick Start Guide]]

- [[AI Search]]
- [[Now Assist in AI Search]]
- [[VA - Basic Arch and ACLs]]
- [[Agentic Workflow & AI Agents]]
- [[50+ (Un)documented Virtual Agent variables (vaInpu]]

