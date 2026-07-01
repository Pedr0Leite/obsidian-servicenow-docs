---
aliases:
  - "Now Assist for CSM - Resolution Notes Generation"
tags:
  - now-assist
  - genai
  - csm
  - summarization
  - case-management
---

# Now Assist for CSM - Resolution Notes Generation

Resolution Notes Generation is a Now Assist skill that creates a clear, concise summary of how a case was resolved. Using case fields, user activity, related tasks, and conversation transcripts, the skill drafts notes that reflect the full context of the resolution. This reduces documentation effort, improves consistency across agents, and provides better reporting, customer perception and audit visibility.

[now-assist-csm-rn-generation.png](https://www.servicenow.com/community/image/serverpage/image-id/461038i5C4AD59445CA91F8/image-size/large/is-moderation-mode/true?v=v2&px=999)

# **Key Capabilities**

- **Generate Draft Notes on Case Resolution**
    
    The skill becomes available when a case is in a resolved or closed state, enabling agents to generate a draft summary that captures resolution steps.
    
- **Contextual Awareness**
    
    The generated draft reflects information from fields like resolution code, timeline activity, live chat, email, and task records, ensuring the summary is relevant and complete.
    
- **Editable Preview for Human in the Loop Oversight**
    
    Agents can review and edit the generated content before saving it, keeping them in control of what’s documented.
    
- **Configurable Triggers and Permissions**
    
    Admins can determine when the feature appears, for which users, and under what case conditions (e.g., based on case type or priority).
    

[resolutionnotes.png](https://www.servicenow.com/community/image/serverpage/image-id/461040i4F9C98D786E7242E/image-size/large/is-moderation-mode/true?v=v2&px=999)

# **Implementation**

Prerequisites:

- Requires Now Assist for CSM plugin
- AI Search and Now Assist Panel must be enabled
- Knowledge Management and Case Management must be configured

[**Configure Resolution notes generation in CSM**](https://www.servicenow.com/docs/csh?topicname=configure-resolution-notes-generation-in-now-assist_0.html&version=latest)

[**Use Resolution notes generation in CSM**](https://www.servicenow.com/docs/csh?topicname=now-assist-csm-generate-resolution.html&version=latest)

[**Customize Resolution notes generation in CSM (same steps as Case Summarization)**](http://need%20your%20help%20escalating%20a%20defect%20%20%20for%20nask/NAA%20new%20admin%20experience%20%20%20JT%20and%20I%20found%20it,%20input%20table%20is%20not%20getting%20synced%20between%20NAA%20and%20NASK,%20this%20was%20reported%20a%20couple%20of%20weeks%20ago%20from%20us%20%20%20and%20now%20she%20is%20telling%20me%20that%20%20the%20platform%20team%20targeted%20DEF0766184%20to%20March%20release%20%20%20totally%20unacceptable%20%20%20the%20workaround%20is%20going%20to%20the%20varset%20and%20doing%20a%20bunch%20of%20changes%20in%20the%20source%20tables,%20its%20a%20mess%20%20%20and%20some%20of%20it%20may%20not%20be%20available%20to%20non-maint)

# **Key Best Practices**

- Make sure the case is fully updated (tasks closed, resolution code set) before using the generation triggers
- Encourage agents to make quick tuning before submitting
- Monitor agent feedback to adjust usage patterns or train agents on reviewing multiple outputs
- [Customizing Resolution Notes visibility and UI](https://www.servicenow.com/community/now-assist-articles/now-assist-for-csm-handling-custom-scenarios-around-now-assist/ta-p/3018803)
- Workaround for Now Assist Context Menu to be added on extended Case table (e.g: Case Types) so skill can be triggered:
    1. Add Skill ID Attribute:
        - In the sys_dictionary table, find the entry where table = <extended table> and type = "Collection”.
        - Add a new attribute named wwna_skill_id with the value found
    2. Create a Quick Action for Extended Table
        - In the wwna_quick_actions (Search for "Now Assist Context Menu Quick Actions") table, locate the record for Resolution Notes in CSM
        - Create a new record with table = <extended table> and ensure all other fields match this record.
    3. Add a New NACM Var Set in the Skill Config
        - In the sn_nowassist_skill_config table, navigate to the Resolution Notes Generation skill config record.
        - Create a new Skill Config Var Set with config type = "NACM Config Params".
        - WWNA Component ID = <extended table>
        - Table = <extended table>
        - Default Action = the quick action created in step 2
        - Ensure all other fields match the previous OOTB record

# **Formal Learning**

[Now Learning: Now Assist for CSM Essentials Path](https://learning.servicenow.com/lxp/en/customer-service-management/now-assist-for-customer-service-management-csm?id=learning_path_prev&path_id=30bec1bf8765fdd4f40fc95d0ebb356f)

SNU's Now Assist Acceleration Bundle: [Summarization & Generation](https://learning.servicenow.com/lxp/en/pages/learning-course?id=learning_course&course_id=1b8b355fc36e2254e5533b877d0131be&group_id=9c05965fc3a66254e5533b877d01314e&child_id=0de5fd64c3f22694e5533b877d0131fd&spa=1)

# **Measured Success and Outcomes**

| **Outcome** | **How It Helps Customer Service Teams** | **Success Metric** |
| --- | --- | --- |
| Reduced documentation time | Speeds up post-resolution work by drafting notes that agents can refine | Avg. time to complete case notes |
| Improved consistency | Ensures case records have complete, professional summaries regardless of agent | % of cases with resolution notes entered |
| Enhanced agent productivity | Reduces fatigue and burnout by removing repetitive writing tasks | Hours saved per week per agent |
| Better internal visibility | Helps team leads and other agents understand what actions were taken for similar cases | ASAT for internal users (agent survey) |
| Higher data quality | Structured, standardized notes support reporting, root cause analysis, and downstream workflows | % of resolution notes reused in similar cases |

---

# **Frequently Asked Questions**

### **Where does Resolution Notes Generation work?**

It is available in the **CSM Configurable Workspace or Now Assist Panel**, triggered on cases in a resolved or closed state.

### **Can agents modify the generated notes?**

Yes. Agents are presented with a preview before saving the content, and they can freely modify or rewrite any part.

### **What inputs are used to generate the notes?**

The skill uses available structured and unstructured case data, including resolution code, task outcomes, agent timeline entries, live chat transcripts, and emails.

### **Can I customize the input? Is it compatible with custom case types?**

While the skill is installed OOTB, admins can influence results by adjusting what fields are required or prominently displayed. Admins need to leverage Now Assist Skill Kit to change the output and duplicate the skill is Now Assist Admin console.

### **Can I customize the content structure or tone?**

Agents can use NACM (Now Assist Context Menu) to iterate and fine tune such as tone or length

### **Does this replace the agent’s voice in the case?**

No. The skill is designed to assist, not override. It provides a starting point to help agents document clearly and consistently, saving time while keeping their final approval.

## Related

- [[Now Assist]]
- [[Now Assist for ITSM Handling Customization Scenari]]
- [[Now Assist case Summaization in custom tables]]
- [[Introducing Custom Record Summarization Now Assist]]
- [[AI Search]]