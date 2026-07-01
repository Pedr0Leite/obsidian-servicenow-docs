---
aliases:
  - "VA - Basic Arch and ACLs"
area: "AI & VA"
source: notion-export
tags:
  - now-assist
  - virtual-agent
  - acl
  - architecture
  - security
---

# VA - Basic Arch  and ACLs

### **Summary**

### **Plugin - Glide Virtual Agent**

[Untitled](VA%20-%20Basic%20Arch%20and%20ACLs/Untitled%201cec42ce9a5680fea539e91357bf57ae.csv)

Virtual Agent Conversations are stored in 2 different tables.

- **sys_cs_message:** holds every chat message, irrespective of the conversation ID number.
- **sys_cs_conversation:** holds the conversation ID number and has a related list of Conversation Messages which will store the individual messages.

**Read Access to:**

The sys_cs_message and sys_cs_conversation tables are provided to users with the following roles - interaction_agent/interaction_admin, admin & virtual_agent_admin. You can find these ACLs in your instance.

- /nav_to.do?uri=sys_security_acl.do?sys_id=eb0be6cfc30713009cbbdccdf3d3ae00
- /nav_to.do?uri=sys_security_acl.do?sys_id=13a8f31c1bfbc010f2a8dc61ab4bcb82
- /nav_to.do?uri=sys_security_acl.do?sys_id=c1d8447cdb2c0010a445fd441d96191e
- /nav_to.do?uri=sys_security_acl.do?sys_id=6134bfb3b70123007d70702e7e11a911
- /nav_to.do?uri=sys_security_acl.do?sys_id=1aa8ffd81bfbc010f2a8dc61ab4bcbd8

**Write Access to:**

sys_cs_message & sys_cs_conversation tables are only provided to 'maint' users (ServiceNow Personnel). You can find these ACLs below in your instance.

- /nav_to.do?uri=sys_security_acl.do?sys_id=aba8f31c1bfbc010f2a8dc61ab4bcb88
- /nav_to.do?uri=sys_security_acl.do?sys_id=92a8ffd81bfbc010f2a8dc61ab4bcbdf

### **Related Links**

**Conversation** `(sys_cs_conversation)` stores a record for each conversation.

**Topic** `(sys_cb_topic)` contains the records for each of the topics in the instance.

**Topic** `(sys_cs_topic)` stores a particular run time of the topic in sys_cb_topic with a user.

**Conversation Task** `(sys_cs_conversation_task)` has an entry for every conversation task.

**Product Documentation to refer to:**

- [**Virtual Agent conversation settings**](https://docs.servicenow.com/csh?topicname=va-conversation-settings.html&version=latest)
- [**Customer Service Virtual Agent conversations**](https://docs.servicenow.com/csh?topicname=csm-virtual-agent-chatbot.html&version=latest)
- [**ITSM Virtual Agent conversations**](https://docs.servicenow.com/csh?topicname=itsm-virtual-agent-topics.html&version=latest)
- [**Get help using virtual agent conversations**](https://docs.servicenow.com/csh?topicname=csm-virtual-agent-conversation.html&version=latest)
- [**Install Virtual Agent integrations for enterprise messaging apps (Slack, Microsoft Teams, and Workplace by Facebook)**](https://docs.servicenow.com/csh?topicname=install-va-integrations.html&version=latest)

**Community Links to refer to:**

- [**Virtual agent chat history**](https://community.servicenow.com/community?id=community_question&sys_id=4785c220db05334014d6fb2439961950)
- [**Virtual Agent - Changing the bot appearance**](https://community.servicenow.com/community?id=community_article&sys_id=8bbd6a92dbd8ffc42be0a851ca9619c0)
- [**Virtual Agent feedback and conversation history**](https://community.servicenow.com/community?id=community_question&sys_id=4c396703db11c89813b5fb24399619ea)
- [**Is there a way to extract all Virtual Agent conversations/nodes easily?**](https://community.servicenow.com/community?id=community_question&sys_id=49354caedbbfab84a39a0b55ca961904)

However, if the OOB system topics have been customized, and the VA plugin is not working after the upgrade, please follow the below steps to repair the plugin:

1. Click on **Repair the plugin**
2. Create a new update set and make it current
3. Open the sys_upgrade_history_log record for the plugin repair
4. Go through the **Skipped Changes to Review** list and open each record
5. For each record, open the **Resolve Conflicts** button
6. If you don’t see any differences you want to keep, click the **Revert to Base Version** button
    - Repeat this for all skipped changes
7. Complete the update set

## Related
- [[Knowledge graph enhancing Virtual Agent search]]
- [[Now Assist in AI Search]]
- [[Now Assist Panel (NAP) Troubleshooting Guide Commo]]

- [[Now Assist]]
- [[VA - Basic Arch and ACLs – Untitled]]
- [[Now Assist Q&A using Dynamic Translation]]
- [[Theming for Now Assist in Virtual Agent enhanced c]]
- [[Migrating Virtual Agent and NLU between instances]]
- [[Security & ACL]]