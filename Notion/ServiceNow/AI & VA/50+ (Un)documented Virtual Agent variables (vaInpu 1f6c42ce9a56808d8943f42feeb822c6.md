---
aliases:
  - "50+ (Un)documented Virtual Agent variables (vaInpu"
tags:
  - virtual-agent
  - vaInputs
  - vaVars
  - vaContext
  - vaSystem
  - scripting
---

# 50+ (Un)documented Virtual Agent variables (vaInputs, vaVars, vaContext, vaSystem)

Hi there,

If you are an admin or Virtual Agent admin, you can use variables to customize the behavior of Virtual Agent Topics. On the ServiceNow [Docs](https://docs.servicenow.com/csh?topicname=virtual-agent-scripts.html&version=latest) only a few of these variables are described. You might already have come across some of these while exploring the out-of-the-box Virtual Agent Topics or the Community, though there are lots more!

I'll sum up, which variables and undocumented variables I've come across so far. You will also see some of these used in the Virtual Agent Topic Block articles and share downloads which I'm publishing.

*Note: Some of these undocumented variables are very useful, though some might also be unsupported!*

**User input variables (vaInputs)**

| vaInputs.user | Provides the display value of the logged-in user's User record. It is possible to apply dotwalking, like "vaInputs.user.first_name".*Example output: "mark.roethof"* |
| --- | --- |

**Script variables (vaVars)**

| vaVars._interaction_record_sysid | Provides the Sys ID of the Interaction which is created automatically and associated with the chat.*Example output: "3127a4802f90a050b0c2d5ea2799b690"* |
| --- | --- |
| vaVars._liveagent_disabled_msg | Same as vaVars._liveagent_handoff_error_msg. Provides the error message which is shown when there are no agent available.*Example output: "There are no agents available at the moment. Please try again later.*" |
| vaVars._liveagent_handoff_error_msg | Same as vaVars._liveagent_disabled_msg. Provides the error message which is shown when there are no agent available.*Example output: "There are no agents available at the moment. Please try again later.*" |
| vaVars._setup_anything_else_topic | Provides the Topic name of the Anything else topic as mentioned in the "Virtual Agent > General Settings > Setup Topics".*Example output: "Anything Else Topic."* |
| vaVars._setup_closing_topic | Provides the Topic name of the Closing topic as mentioned in the "Virtual Agent > General Settings > Setup Topics".*Example output: "Closing conversation."* |
| vaVars._setup_error_topic | Provides the Topic name of the Error topic as mentioned in the "Virtual Agent > General Settings > Setup Topics".*Example output: "Error Handling Topic."* |
| vaVars._setup_explore_help_topic | Provides the Topic name of the Explore help topic as mentioned in the "Virtual Agent > General Settings > Setup Topics".*Example output: "Virtual Agent Capabilities."* |
| vaVars._setup_fallback_topic | Provides the Topic name of the Fallback topic as mentioned in the "Virtual Agent > General Settings > Setup Topics".*Example output: "Fallback Topic."* |
| vaVars._setup_survey_topic | Provides the Topic name of the Survey topic as mentioned in the "Virtual Agent > General Settings > Setup Topics".*Example output: "Virtual Agent Feedback."* |
| vaVars._setup_welcome_topic | Provides the Topic name of the Greeting topic as mentioned in the "Virtual Agent > General Settings > Setup Topics".*Example output: "Dynamic Greeting Topic."* |
| vaVars._topic_choice_list_msg | Provides the value of System Property "com.glide.cs.topic_choice_list_message". My advice would be to NOT alter the value of this System Property when working on a Multi-language instance. Update the Message of the corresponding UI Message instead.*Example output: "I want to be sure I got this right. What item best describes what you want to do?"* |
| vaVars._topic_current | Same as vaVars._topic_results. Provides details of the current Topic the conversation is in, in JSON format. Details like the Sys ID of the current Topic, Sys ID of the Conversation Task, name of the current Topic.*Example output: "{"sys_id":"5e85248c2f50a050b0c2d5ea2799b6b4", "task":"f327e4802f90a050b0c2d5ea2799b63d", "entities":null, "modelId":null, "name":"Test Topic", "prediction":null, "title":"Test Topic", "type":"normal", "utterance":"test topic"}"* |
| vaVars._topic_not_found_msg | Provides the value of System Property "com.glide.cs.no_topic_found_message". My advice would be to NOT alter the value of this System Property when working on a Multi-language instance. Update the Message of the corresponding UI Message instead.*Example output: "Please try giving me your request in a different way. I'm currently better at understanding short sentences."* |
| vaVars._topic_postchat_user_id | Provides the display value of the logged-in user's User record. Unlike the vaInputs.user, it is NOT possible to apply dotwalking.*Example output: "mark.roethof"* |
| vaVars._topic_results | Same as vaVars._topic_current. Provides details of the current Topic the conversation is in, in JSON format. Details like the Sys ID of the current Topic, Sys ID of the Conversation Task, name of the current Topic.*Example output: "{"sys_id":"5e85248c2f50a050b0c2d5ea2799b6b4", "task":"f327e4802f90a050b0c2d5ea2799b63d", "entities":null, "modelId":null, "name":"Test Topic", "prediction":null, "title":"Test Topic", "type":"normal", "utterance":"test topic"}"* |
| vaVars._topic_sorry_msg | Provides the value of System Property "com.glide.cs.no_topic_sorry_message". My advice would be to NOT alter the value of this System Property when working on a Multi-language instance. Update the Message of the corresponding UI Message instead.*Example output: "I am sorry but I didn't understand your request."* |
| vaVars._topic_sth_else_option | Provides the value of System Property "com.glide.cs.want_something_else_option". My advice would be to NOT alter the value of this System Property when working on a Multi-language instance. Update the Message of the corresponding UI Message instead.*Example output: "I want something else"* |
| vaVars._topic_strategy | No clue yet.Found this Script variable within one of the out-of-the-box Topics, which proves a value of "sure". |
| vaVars._topic_wrong_msg | Provides the value of System Property "com.glide.cs.wrong_topic_message". My advice would be to NOT alter the value of this System Property when working on a Multi-language instance. Update the Message of the corresponding UI Message instead.*Example output: "No problem, let's try again. Select one that matches what you want to do."* |
| vaVars.global_client_mode | No clue yet.Found this Script variable within one of the out-of-the-box Topics, which proves a value of "NORMAL". |

**Context variables (vaContext)**

| vaContext.deviceTimeZone | Same as vaContext.getDeviceTimeZone(). Provides the timezone from the Device on which the logged-in user is working. So the timezone from the laptop or mobile phone for example. This is NOT the timezone value of the logged-in user's User record.*Example output: "Europe/Amsterdam"* |
| --- | --- |
| vaContext.deviceType | Provides the type of Device on which the logged-in user is working.*Example output: "mweb", "ios", "android"* |
| vaContext.getDeviceTimeZone() | Same as vaContext.deviceTimeZone. Provides the timezone from the Device on which the logged-in user is working. So the timezone from the laptop or mobile phone for example. This is NOT the timezone value of the logged-in user's User record.*Example output: "Europe/Amsterdam"* |
| vaContext.getRequesterLang() | Provides the value of the Language field of the logged-in user's User record.*Example output: "en"* |
| vaContext.portal | Provides the Portal suffix. This Context variables only works instantly when using Service Portal Agent Chat Configuration. If using legacy methods (like embedding the Service Portal widget to the header or footer), this would only work when adding sysparm_portal to the URL.*Example output: "sp"* |

Below variables can be found in one of more out-of-the-box Topics. Unfortunately, so far I did not get these variables mentioned working.

vaContext.case_sys_id

vaContext.case_number

vaContext.task_number

vaContext.task_tablename

vaContext.parent_case_sys_id

vaContext.providerAppId

vaContext.providerUserId

vaContext.providerUserName

vaContext.task_sys_id

**System Variables (vaSystem)**

| vaSystem.attachRecordToConversation() | From the Docs: "This method attaches ServiceNow records that are updated or created during a Virtual Agent conversation to the Related Tasks list in a Virtual Agent interaction record."*Example usage: "vaSystem.attachRecordToConversation('incident', 'f327e4802f90a050b0c2d5ea2788b63d')"* |
| --- | --- |
| vaSystem.attachToRecord() | From the Docs: "This method attaches an uploaded image to a ServiceNow record."*Example usage: "vaSystem.attachToRecord(vaInputs.file_picker.getValue(), 'incident', 'f327e4802f90a050b0c2d5ea2788b63d')"* |
| vaSystem.connectToAgent() | From the Docs: "This method connects the customer to a live agent." |
| vaSystem.getClosingMessage() | Same as vaSystem.sendSeparatorMessage(). Provides the value of System Property "com.glide.cs.general.closing_message". My advice would be to NOT alter the value of this System Property when working on a Multi-language instance. Update the Message of the corresponding UI Message instead.*Example output: "Thank you for using our support chat."* |
| vaSystem.getConversationId() | Provides the Sys ID of the Conversation record which is created automatically.*Example output: "32dbbc9a2f1ce850b0c2d5ea2799b68d"* |
| vaSystem.getGreetingMessage() | Same as vaSystem.sendSystemMessage(). Provides the message of UI Message with key "Hi, I'm your Virtual Agent. Let me know how I can help you today.".*Example output: "Hi, I'm your Virtual Agent. Let me know how I can help you today."* |
| vaSystem.getSearchText() | From the Docs: "This method returns the last utterance typed by the user and is used to find the current topic."*Example output: "My mouse isn't working anymore."* |
| vaSystem.getSurveyVerificationMessage() | Provides the value of System Property "com.glide.cs.general.chat_survey_verification_message". My advice would be to NOT alter the value of this System Property when working on a Multi-language instance. Update the Message of the corresponding UI Message instead.*Example output: "Is the summary accurate?"* |
| vaSystem.getTopicSelectionMessage() | Provides the message of UI Message with key "What's your issue or request? Or take a look at what I can help with.".*Example output: "What's your issue or request? Or take a look at what I can help with."* |
| vaSystem.getTranscript() | Provides the contents of the full current conversation up to that point.*Example output: "[07:30] Virtual Agent: G'day Mark.[07:30] Virtual Agent: Let me know how I can help you today. What's your issue or request? Or take a look at what I can help with.[07:30] Virtual Agent: Show Me Everything[07:30] Mark Roethof (SysAdmin): Test Topic[07:30] Virtual Agent: Test Topic"* |
| vaSystem.getTranslation() | Provides the value of the matching Translated Text record corresponding the Language given. The first parameter concerns the GlideRecord object, the second parameter concerns the Fieldname value, the third parameter concerns the Language value for the translation to retrieve, the fourth parameter concerns the Field of the GlideRecord object which needs to be translated against the Translated Tekst.*Example usage: "vaSystem.getTranslation(gr, 'question', 'nl', gr.question)"* |
| vaSystem.isAllowTranscriptDownload() | Provides a boolean value which corresponds with the value of checkbox Allow Transcript Download on the Chat Setup record.Example output: "true" or "false" |
| vaSystem.isLiveAgentAvailable() | From the Docs: "This method checks whether a live agent is available to receive a conversation (transferred from the bot)."*Example output: "true" or "false"* |
| vaSystem.sendSeparatorMessage() | Same as vaSystem.getClosingMessage(). Provides the value of System Property "com.glide.cs.general.closing_message". My advice would be to NOT alter the value of this System Property when working on a Multi-language instance. Update the Message of the corresponding UI Message instead.*Example output: "Thank you for using our support chat."* |
| vaSystem.sendSystemMessage() | Same as vaSystem.getGreetingMessage(). Provides the message of UI Message with key "Hi, I'm your Virtual Agent. Let me know how I can help you today.".*Example output: "Hi, I'm your Virtual Agent. Let me know how I can help you today."* |
| vaSystem.sendTopicPickerControl() | This Script variables provides the logged-in user with a list of available Topics. Usage of this Script variable is required if willing to work with utterances.*Example usage: "var greetingMessage = vaSystem.getTopicSelectionMessage();vaSystem.sendTopicPickerControl(greetingMessage);"* |
| vaSystem.switchTopic() | Can be used to switch to another Topic. After completion of the Topic switched to, the conversation returns to the Topic switched from.*Example usage: "vaSystem.switchTopic('Topic Name to Switch to');"* |
| vaSystem.topicDiscovery() | Can be used to discover and switch to another Topic. After completion of the Topic switched to, the conversation returns to the Topic switched from.*Example usage: "vaVars.global_search_text = 'Topic Name to Switch to';vaSystem.topicDiscovery();"*  |

Below variables can be found in one or more out-of-the-box Topics. Unfortunately, so far I did not get these variables mentioned working.

vaSystem._topic_current

vaSystem.endConversation()

vaSystem.portal

## Related

- [[VA - Basic Arch and ACLs]]
- [[Migrating Virtual Agent and NLU between instances]]
- [[Knowledge graph enhancing Virtual Agent search]]
- [[Theming for Now Assist in Virtual Agent enhanced c]]
- [[Now Assist in AI Search]]