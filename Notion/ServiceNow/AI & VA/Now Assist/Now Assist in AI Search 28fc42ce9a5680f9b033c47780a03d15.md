---
aliases:
  - "Now Assist in AI Search"
area: "AI & VA"
source: notion-export
tags:
  - now-assist
  - ai-search
  - genai
  - rag
  - virtual-agent
---

# Now Assist in AI Search

1. **What is Now Assist in AI Search?**
    - Now Assist in AI Search is the next evolution of Search from ServiceNow and enables users to find answers quickly. Now Assist in AI Search responds to user questions with an actionable *Q&A - Now Assist for Search Genius Results* card, along with the most relevant search results in a list.

[VictorChen_2-1723661090245.jpg](https://www.servicenow.com/community/image/serverpage/image-id/379381i312838AA40368EAC/image-size/large?v=v2&px=999)

1. **What is the main value of Now Assist in AI Search?**
    - Customer-specific answers from trusted Knowledge Base and Service Catalog sources, without a need to train or fine-tune a model.
2. **Explain Now Assist in AI Search as if I were a 5th grader**
    - Imagine asking for guidance on a problem and getting a concise list of immediately actionable steps to follow instead of a list of documents to study - this is what Now Assist for Search does, by providing actionable answers and resolutions, in addition to the most relevant classic AI Search results that users expect.
3. **What is innovative about Now Assist in AI Search?**
    - AI Search in 2020 moved us closer to consumer-grade search with Machine Learning (ML) relevancy and a refined user experience. Now Assist for Search delivers on the promise of “answers instead of links” using what is known as a retrieval augmented generation search architecture and supports our human-centered approach to developing trustworthy AI.
4. **How does Now Assist in AI Search work?**
    - Now Assist in AI Search uses a [Retrieval-Augmented Generation (RAG)](https://www.servicenow.com/community/ai-intelligence-articles/under-the-hood-now-assist-for-search/ta-p/2642915). When a user asks a question, it uses AI Search on the back end to  relevant articles from the customer’s data, then  the user’s query with context from the content of the top knowledge article and provides this as input to the LLM. Other relevant AI Search results are provided with the response.
        
        retrieve
        
        augments
        
5. **Where can Now Assist in AI Search be used?**
    - Now Assist in AI Search provides actionable answers to questions via *Q&A - Now Assist for Search Genius Results* cards in Global Search (Next Experience), Service Portal, Employee Center and/or Virtual Agent.
6. **Why Now Assist in AI Search?**
    - Now Assist in AI Search delivers on self-service with answers, along with search results
    - AI Search integration with ServiceNow security models provides content access restrictions
    - Customer has control over relevancy using AIS Admin tuning / improvement rules
    - Reduces the risk of hallucination by grounding of responses in customers’ content with citations
    - Use of customer KB articles allows the LLM to return intelligent answers without new AI model training
7. **What are the risks and limitations?**
    - All LLMs are known to have a risk of producing Hallucinations.
    - Attachments are not currently supported.
8. **What models are supported?**
    - A preconfigured Now LLM model is used to power Now Assist for Search.
    - No other models are supported.
9. **What is the platform compatibility:**
    - Vancouver Patch 2+
10. **What are the Licensing & Packaging dependencies?**
    - Now Assist for CSM, ITSM, HRSD, or other Pro Plus or Enterprise Plus packages

---

**Getting started**

1. **How do admins get started with Now Assist for Search?**
    - The instance must be on **Vancouver Patch 2+**.
    - AI Search must be activated and ready for use (go to **All > AI Search Status**).
    - The Now Assist for Search plugin is automatically installed when either of the **Now Assist for CSM**, **ITSM**, **HR, etc.** packages are installed, along with all dependencies being up to date.
    - Admins can verify that Now Assist for Search is installed by navigating to **All > Now Assist Admin > Features**, then in the workflow list, select **Platform**, and verify that the Search card displays, and that **Q&A - Now Assist for Search** appears in the **All Search skills** listing.
    - With the store app is installed, search administrators can navigate to the new *Now Assist in AI Search setup* page to configure genius results for search profiles.

[VictorChen_0-1723661002562.jpg](https://www.servicenow.com/community/image/serverpage/image-id/379379iD432D5E3C15FAB56/image-size/large?v=v2&px=999)

**Post-implementation FAQs**

1. **As an admin, how can I easily figure out some search queries to see how it works?**
    - Get an understanding of the instance's knowledge base contents by logging into the instance, going to **All > kb_knowledge.list** to browse and view a few KB articles. Try to find some articles that contain detailed instructions with *how to* steps for users to follow - the short description might include clues with verbs such as *activate, apply, add*…
    - Make a note of which sampled articles include content that contains at least one descriptive solution to a relevant issue, then try search for help on the specific task.
    - **IF** there is a relevant KB article **AND** the article has a well-articulated solution to the specific question being asked by the user, then the probability is high that a *Q&A - Now Assist for Search Genius Results* card will be generated.
    - **IF NOT**, then the user will simply see the list of most relevant remaining articles to review.
2. **Why am I getting an answer?**
    - KB article is published
    - User has permission to view the KB article
    - User's session language is English.
    - The [genius result configuration](https://docs.servicenow.com/bundle/vancouver-platform-administration/page/administer/ai-search/concept/configuring-gen-ai-powered-srch.html#title_enable-qna-nas-gr-global-search) is enabled for that experience,
    - The article is included in the Knowledge table [encoded query string](https://docs.servicenow.com/bundle/vancouver-platform-administration/page/administer/ai-search/concept/configuring-gen-ai-powered-srch.html#title_restrict-kbs-sent-llm-gai-pwr-srch) results. (**Note**: This feature was removed in Washington DC Patch 5+, and another way to filter results for Genius Results is targeted in November '24.)
    - The search phrase matches the regex [configured query condition](https://docs.servicenow.com/bundle/vancouver-platform-administration/page/administer/ai-search/concept/configuring-gen-ai-powered-srch.html#title_define-query-conds-gai-pwr-srch).
3. **Why am I getting a bad answer?**
    - All LLMs are known to have a risk of producing Hallucinations.
    - Customers are encouraged to participate in AI data sharing so that our models can be improved to reduce the chance of hallucinations.
    - Users can provide feedback using the "Was this suggestion helpful?" feedback mechanism on the result card.
4. **Why am I getting no answer?**
    - Genius result card may not be configured correctly
    - Article does not provide an obvious solution to the question
5. **What can I do in AI Search to more consistently get great answers with Now Assist for Search?**
    - Spend some time optimizing the instance's AI Search content and configuration for [search results relevancy](https://www.servicenow.com/community/ai-intelligence-articles/content-creation-for-relevancy-in-ai-search/ta-p/2307968), since this is the engine that searches for the most relevant articles related to the query that the Now LLM will evaluate to determine whether it should generate an answer from the contextually relevant content.
    - Most companies tend to have their own internal jargon and acronyms. Configuring synonyms and stop word dictionaries for AI Search can help.
    - In some cases, creating result improvement rules and boosting documents will help to give the more trusted articles a higher score.
    - Test all your configuration changes with *AI Search Preview*. You can see scores, which stop-words have been removed, and which synonyms and results improvement rules are at work.
    - Optimize your Knowledge Base, making sure that KB article short descriptions (title) is clear. Check that knowledge base articles are up to date and accurate. **See this [Knowledge Management + AI Search best practices](https://www.servicenow.com/community/knowledge-managers/kmug-ai-search-and-knowledge-management-best-practices/ba-p/2694499) article for more information**.
    - In the Xanadu+ release, you can boost results by geography or organization: [AI Search personalization enhancements in Xanadu...](https://www.servicenow.com/community/intelligence-ml-articles/ai-search-personalization-enhances-in-xanadu-release-boost/ta-p/3054786)
    - After trying all this, if you are still not seeing improvements, you may want to check your scripts and/or EVAM.
6. **Can I change the Genius Result Card?**
    - This would be considered a customization and is not recommended.
7. **I'm getting different search results between portal and the Virtual Agent. Why is that?**
    - Check to see that the search profile used by the Portal is the same as the one used by the Virtual Agent. The Portal's search profile can be found via its Search Application in the Portal record. The Virtual Agent's search profile can be found via the Virtual Agent's Search Application. In the Washington Patch 3 release, admins can also find the Now Assist in Virtual Agent's search profile in the setup page: "Information sources".

**External Content FAQ for Now Assist in AI Search (as of Washington DC)**

1. What external content search sources are currently (and will be) supported?
    - As of the Yokohama release, SharePoint, Confluence, and Google Drive are supported.
2. Does the SharePoint federated search for Now Assist in AI Search use the same connector available for core AI Search?
    - It uses the same connector in the background, but it no longer requires Employee Center Pro. The configuration is also simpler.
3. What are the requirements to use SharePoint federated search?
    - A Pro Plus/Enterprise Plus Now Assist SKU
    - Now Assist in AI Search plugin
    - IntegrationHub Enterprise
    - SharePoint admin access (via Azure)
4. Does the SharePoint federated search use IHub transactions?
    - No. However, it consumes assists. (1 assist per genius result).
5. How does SharePoint federated search work?
    - AI Search sends a query to both AI Search and SharePoint Search (built by Microsoft). The returned SharePoint result is based on the user's authentication/permissions. SharePoint results do not go through the entire AI Search RAG pipeline, only through Now LLM for Genius Result generation.
6. Does SharePoint federated search support “multi-source” generation (like KBs)?
    - No.
7. What file types are supported?
    - TXT, PDF, DOC, HTML
8. How do I configure the SharePoint connection?
    - See documentation here: [https://docs.servicenow.com/bundle/xanadu-platform-administration/page/administer/ai-search/concept/...](https://docs.servicenow.com/bundle/xanadu-platform-administration/page/administer/ai-search/concept/external-content-qna.html)
9. What languages are supported?
    - All platform languages are supported.
10. Do results improvement rules apply to External Content Q&A?
    - No.

[VictorChen_1-1723661036027.jpg](https://www.servicenow.com/community/image/serverpage/image-id/379380i3F99EF5ACBC22EF4/image-size/large?v=v2&px=999)

## Related
- [[Now Assist Q&A using Dynamic Translation]]
- [[Knowledge graph enhancing Virtual Agent search]]
- [[Now Assist Panel (NAP) Troubleshooting Guide Commo]]

- [[Now Assist]]
- [[AI Search]]
- [[AI Search – Considerations for Designing, Maintaining, and Sca]]
- [[AI Search Synonyms]]
- [[GenAI]]
- [[VA - Basic Arch and ACLs]]