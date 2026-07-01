---
aliases:
  - "Using external LLMs with Now Assist"
tags:
  - now-assist
  - genai
  - llm
  - byok
  - generative-ai-controller
---

# Using external LLMs with Now Assist

[Eliza_0-1767991740879.png](https://www.servicenow.com/community/image/serverpage/image-id/495000i923213804D903B36/image-dimensions/737x199?v=v2)

When using Now Assist products, you may encounter a scenario where you wish to modify the large language model (LLM) providing generative AI capabilities. This guide details the options you have for adjusting the provider for both out-of-the-box (OOTB) and custom Now Assist skills and agents.

**Please note:** The selection of a provider and model is entirely dependent on your use case, and as such, cannot provide guidance on which provider to select. It is important to consider topics such as data sovereignty and handling, performance, and cost when evaluating candidates.

### **Article Contents**

1. Provider Connection Types
2. Feature support for provider connection types
3. How do I configure each provider connection type?
4. How do I configure my skills and AI Agents to use my chosen model?

# **Provider Connection Types**

A provider is considered to be the organization delivering the service. This includes Google, Microsoft Azure, AWS, and ServiceNow itself. Each provider offers a range of large language models (LLMs) to help complete actions, with each model having particular benefits and drawbacks.

The table below addresses the different provider types and the features that support them:

| Provider Connection Type |  | Definition | Supported Features |
| --- | --- | --- | --- |
| **ServiceNow Managed Connection**Note: This means you do not need to procure any licenses with third parties to gain access to these options | **NowLLM** | ServiceNow's LLM service. Find out more using our [model cards](https://www.servicenow.com/docs/csh?topicname=now-llm-model-updates.html&version=latest). | • OOTB Now Assist Skills
• Custom Skills
• AI Agents
• Custom AI Agents |
|  | **ServiceNow integrated model** | For users operating at least Yokohama Patch 6 or Zurich Patch 0 and above, a range of integrated model providers are available for use *without the need for additional licenses*.Administrators can choose from the following integrated model providers:
• Microsoft Azure Open AI
• Google Gemini
• AWS Anthropic ClaudeLearn more in our [model provider flexibility](https://www.servicenow.com/community/now-assist-articles/introducing-model-provider-flexibility-optimize-every-ai/ta-p/3306874) article. | • OOTB Now Assist Skills
• Custom Skills
• AI Agents
• Custom AI Agents |
| **Bring-your-own-key (BYOK) for ServiceNow integrated models** |  | This option enables Now Assist features to utilise your organisation's instance of Azure, Google AI Studio, or AWS Bedrock in lieu of the ServiceNow managed connection.You are required to bring your own connection credentials (such as API Key and endpoint), and ServiceNow will route Now Assist requests through your provider account rather than ServiceNow's managed infrastructure.The specific models available for selection using this method are each listed [here](https://www.servicenow.com/docs/csh?topicname=exploring-large-language-models.html&version=latest). | • OOTB Now Assist Skills
• Custom Skills
• AI Agents
• Custom AI Agents |
| **Bring-your-own-key (BYOK) for spokes** |  | We offer the option to connect to providers using our spokes. These spokes are several pre-built integrations for providers outside of our integrated providers. You are required to bring your own connection credentials (such as API Key and endpoint).The list of providers can be found in [product documentation](https://www.servicenow.com/docs/bundle/xanadu-intelligent-experiences/page/administer/generative-ai-controller/task/configure-generative-ai-controller.html). | • Limited OOTB Skills*
• Custom Skills |
| **Bring-your-own-LLM (BYOLLM)** |  | This refers to using a model or provider that ServiceNow does not support or certify.You are required to configure the connection yourself, and will need to provide credentials such as an API key and endpoint. The configuration process also includes some scripting in order to produce a transformer script, to translate the output from your provider into a ServiceNow recognized format. | • Limited OOTB Skills*
• Custom Skills |
- *Please refer to the section labelled "BYOK for spokes and BYOLLM for OOTB skills" in **How do I configure my skills and AI Agents to use my chosen model?***

# **Feature Support for Provider Connection Types**

Not all features within Now Assist are able to use all provider connection types. The table below maps the feature type to the supported provider connection types.

| Feature Type | Definition | Provider Connection Type Supported |
| --- | --- | --- |
| **OOTB Now Assist Skills** | ServiceNow shipped generative AI features. Managed in the Now Assist Admin console.**Examples:** incident/case summarization, knowledge article generation | • ServiceNow Managed Connection
• BYOK for ServiceNow integrated models
• BYOK for Spokes*
• BYOLLM* |
| **Custom skills** | User-developed skills, created within Now Assist Skill Kit. | • ServiceNow Managed Connection
• BYOK for ServiceNow integrated models
• BYOK for Spokes
• BYOLLM |
| **OOTB AI Agents** | ServiceNow shipped AI Agents. | • ServiceNow Managed Connection
• BYOK for ServiceNow integrated models |
| **Custom AI Agents** | User-developed AI Agents, created within AI Agent Studio. | • ServiceNow Managed Connection
• BYOK for ServiceNow integrated models |
- *Please refer to the section labelled "BYOK for spokes and BYOLLM for OOTB skills" in **How do I configure my skills and AI Agents to use my chosen model?***

# **How do I configure each provider connection type?**

### ***ServiceNow Managed Connection***

**No configuration required!** Connection to either NowLLM or any of the integrated models is automatic – they are all available for use as soon as a Now Assist-related plugin has been installed.

### ***BYOK for ServiceNow integrated models***

Please refer to the [support article](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2666298) that addresses how to input credentials for each integrated model provider.

We also have a video walkthrough for those looking to connect to Azure OpenAI:

[https://youtu.be/LxSst5zHpWM](https://youtu.be/LxSst5zHpWM)

### ***BYOK for Spokes***

We provide a number of spokes to external LLMs, including (as of December 2025):

- Azure OpenAI*
- OpenAI
- Aleph Alpha
- IBM's WatsonX
- Google's Vertex AI
- Google's Gemini AI Studio*
- AWS Bedrock*

**Important:** If you are to use **Google, Azure OpenAI, or AWS Bedrock**, we **strongly** recommend you instead follow the steps above for *BYOK for ServiceNow integrated model*.

To connect to a spoke, you need to procure your own license and provide ServiceNow with the key and any additional credentials that the API may need to verify the connection.

For providers that offer multiple LLMs, such as Amazon Bedrock and Vertex AI, please note that you are limited to usage of only one LLM at this time.

To see how to connect to one of our spokes, you can view the recording below:

[https://youtu.be/SwFEVRgX-Ec](https://youtu.be/SwFEVRgX-Ec)

### ***BYOLLM***

### **Washington DC, Xanadu, and Zurich patch 1-3 Instances**

Instances on at least the Washington DC release are able to use the [generic LLM connector](https://docs.servicenow.com/csh?version=latest&topicname=configure-a-generic-llm-connector.html) to connect to any external LLM not listed above, i.e. BYOLLM. This process requires a fair amount of technical acumen. To integrate with a non-spoke-supported LLM, you need:

- An API key from the provider
- Endpoint for the LLM
- Access to API documentation for that LLM to assist with writing the transformation script to translate the input and response into an acceptable format

An example demonstrating the process of connecting to an external LLM using the generic LLM connector can be seen in the video below:

[https://youtu.be/HxvpePrHwSY](https://youtu.be/HxvpePrHwSY)

### **Zurich Patch 4 (Now Assist Skill Kit plugin version 7.0.0)**

Configuration of BYOLLM can be performed by going to **Now Assist Skill Kit > Providers and Models**, and clicking on the **Add model** button. A guided setup will walk you through the process of connecting your custom model into ServiceNow.

[Eliza_3-1767999137441.png](https://www.servicenow.com/community/image/serverpage/image-id/495013i2D1EE6AEE21F1322/image-dimensions/684x373?v=v2)

# **How do I configure my skills and AI Agents to use my chosen model?**

### **OOTB Skills**

### ***ServiceNow Managed Connection***

You can adjust the provider for OOTB skills by first ensuring the provider is enabled within AI Control Tower, then navigating into **Now Assist Admin > Settings > Manage Model Provider**.

You can choose to modify the provider for all skills, a subset, or even on an individual skill by skill basis.

These steps are covered in detail in the video below (demo starts at 24:00):

[https://youtu.be/UdcAKjdWh7g](https://youtu.be/UdcAKjdWh7g)

### ***BYOK for integrated providers***

Once configured (refer to the section labelled "How do I configure each provider connection type?"), you need to then perform the following steps:

1. Navigate to Now Assist Admin Console.
2. Click on the tab named Settings, then Manage Integration.
3. For the provider you wish to use, ensure that BYOK has been selected, and click Save.
    
    [Eliza_2-1767999059864.png](https://www.servicenow.com/community/image/serverpage/image-id/495012iDFBE4ADDCB3B338C/image-dimensions/583x408?v=v2)
    

This means that all requests pointing to that provider will now be routed to your instance, rather than the ServiceNow managed (OEM) version.

Once this step is complete, you can then follow the same steps listed above under *ServiceNow Managed Connection*.

### ***BYOK for spokes and BYOLLM***

The process of connecting OOTB skills to BYOK for spokes and BYOLLM is conducted within Now Assist Skill Kit, by first cloning the skill, then creating a new prompt within that skill, which will allow for you to select a new provider. A walkthrough of this process is available below the table.

**Please note:** The BYOK for spokes/BYOLLM options are not available for OOTB skills.

To see which of your skills are eligible for this method, you can navigate to the `sn_nowassist_skill_config` table, and find the skills where `is_template = true`. The list of skills one can do this for as of December 2025/Zurich Patch 4 is as follows:

| Application | Skill Name |
| --- | --- |
| Custom App Record Summarization | Custom app record summarization |
| Flow Generation | Flow Generation with Images |
| GRC Common GenAI | Issue Summarization |
| GRC Shared GenAI | Risk Assessment Summarization |
| Now Assist for Accounts Payable Operations (APO) | Invoice data extraction |
|  | Invoice case summarization |
| Now Assist for Customer Service Management (CSM) | Case summarization |
|  | KB generation |
|  | Resolution notes generation |
| Now Assist for Employee Experience | Case summarization for approvals |
|  | Request summarization for approvals |
|  | Requested Item summarization for approvals |
| Now Assist for Enterprise Architecture (EA) | Business application insights |
| Now Assist for Field Service Management (FSM) | KB generation |
|  | Work Order Task Summarization |
| Now Assist for Financial Services Operations (FSO) | Claim summarization |
| Now Assist for FSC Common | Purchase order summarization |
|  | Supplier summarization |
| Now Assist for HR Service Delivery (HRSD) | KB generation |
|  | Persona Assistant |
|  | Case summarization |
| Now Assist for IT Service Management (ITSM) | Resolution notes generation |
|  | Change request risk explanation |
|  | KB generation |
|  | Incident summarization |
|  | Change request summarization |
| Now Assist for Legal Service Delivery | Legal Request summarization |
| Now Assist for OTSM | OT Incident resolution notes generation |
| Now Assist for OTSM | OT Incident summarization |
| Now Assist for RPA Hub | RPA bot generation |
| Now Assist for Security Incident Response (SIR) | Security Incident Quality Assessment |
|  | Security incident recommended actions |
|  | Generate content for shift handover |
|  | Resolution notes generation |
|  | Post incident analysis |
|  | Correlation insights generation |
|  | Security operations metrics analysis |
|  | Security incident summarization |
| Now Assist for Sourcing and Procurement Operations (SPO) | Sourcing request summarization |
|  | Sourcing request summarization |
|  | Purchase order summarization |
|  | Procurement case summarization |
|  | Purchase requisition summarization |
|  | Sourcing event summarization |
|  | Negotiation summarization |
|  | Purchase requisition summarization |
| Now Assist for Supplier Lifecycle Operations (SLO) | Supplier case summarization |
| Now Assist for Talent | Generate talking points |
| Now Assist for Telecommunications, Media and Technology (TMT) | Service Problem Case summarization |
|  | Customer Service Summary |

**Walkthrough of how to modify OOTB skills:**

[https://youtu.be/1YOabuUPaw8](https://youtu.be/1YOabuUPaw8)

### **OOTB and Custom AI Agents**

### ***ServiceNow Managed Connection***

You can adjust the provider for OOTB skills by first ensuring the provider is enabled within AI Control Tower, then navigating into **Now Assist Admin > Settings > Manage Model Provider**.

You can choose to modify the provider for all skills, a subset, or even on an individual skill by skill basis.

These steps are covered in detail in the video below (demo starts at 24:00):

[https://youtu.be/UdcAKjdWh7g](https://youtu.be/UdcAKjdWh7g)

### ***BYOK for ServiceNow integrated models***

Once configured (refer to the section labelled "How do I configure each provider connection type?"), you need to then perform the following steps:

1. Navigate to Now Assist Admin Console.
2. Click on the tab named Settings, then Manage Integration.
3. For the provider you wish to use, ensure that BYOK has been selected, and click Save.
    
    [Eliza_1-1767998989685.png](https://www.servicenow.com/community/image/serverpage/image-id/495011iC616F8A45125E6E0/image-dimensions/542x379?v=v2)
    

This means that all requests pointing to that provider will now be routed to your instance, rather than the ServiceNow managed (OEM) version.

Once this step is complete, you can then follow the same steps listed above under *ServiceNow Managed Connection*.

**Important:** *BYOK for Spokes and BYOLLM is currently not supported for both OOTB and custom AI Agents.*

### **Custom Skills**

When you are building your own custom generative AI functionality within Now Assist Skill Kit, you have the option of selecting both a provider, and a provider API (i.e. which model from the provider). This list is sourced from the records with `external=true` on the `sys_generative_ai_model_config` table.

[Eliza_0-1767998972924.png](https://www.servicenow.com/community/image/serverpage/image-id/495010iA5A91FA79504B2BF/image-dimensions/632x335?v=v2)

## Related

- [[Now Assist]]
- [[GenAI]]
- [[Build Custom AI Skills with Now Assist Skill Kit S]]
- [[Agentic Workflow & AI Agents]]