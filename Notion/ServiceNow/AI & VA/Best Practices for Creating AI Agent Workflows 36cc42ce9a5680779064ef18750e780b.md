---
aliases:
  - "Best Practices for Creating AI Agent Workflows"
tags:
  - ai-agents
  - agentic-workflow
  - prompt-engineering
  - react-loop
  - troubleshooting
---

# Best Practices for Creating AI Agent Workflows

https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2339651

### **Summary**

1. It is important to clearly describe and define the use case name and description as this is used for skill discovery based on the user’s utterance.

- Incorrect:

o Use case Name: License Processing

o Use case description: Software License Allocation is used to allocate a software license.

- Correct:

o Use case name: Software License Allocation

o Use case description: The Software License Allocation process involves verifying the details of the requesting user and checking the availability of the requested software license. If the user meets the eligibility criteria, the system proceeds with assigning the license, ensuring seamless access to the required software.

2. Write instructions in clear, grammatically correct English. Poor language quality can lead to misunderstandings or execution errors.

- Incorrect: "Run toolA and then show result, dont do confusions,"
- Correct: "Run Tool A to fetch the required data and then display the result to the user."

3. Structure your use case instructions using sections and subsections to create a logical workflow. This aids in understanding and navigating through the expected flow seamlessly.

- Incorrect: Get the user and license details. Allocate license if the user is eligible.
- Correct:

1. Fetch the details of the user who raised the incident.

2. Find out the details of the requested software license.

3. Verify if the user is eligible to get access to the requested software license.

3.a. If the user is eligible, then allocate the software license.

3.b. If the user is not eligible, then inform the user that they are not eligible.

4. Align instructions with similar terminology as used in the agent name/agent description such that the expected agent is chosen correctly.

- Context:

o Agent name: Notification Agent

o Agent description: This agent can send notifications to the provided list of users.

- Incorrect: Tell user that something went wrong. [This will confuse the orchestrator, and it might pick Communicator Agent rather than choosing the Notification Agent.]
- Correct: Send a notification to the user that something went wrong. [This will help the orchestrator understand that it should choose the Notification Agent]

5. Each instruction should contain only one actionable operation. This helps prevent misinterpretation and ensures that each step is independently executed without skipping any step.

- Incorrect: Check if the user is eligible for the requested software license and allocate it to them if they are eligible.
- Correct:

1. Verify the user’s eligibility to access the software license.

2. Based on whether the user is eligible or not, follow the below instructions:

2.a. If the user is eligible, then allocate it to them.

2.b. If the user is not eligible, then inform the user about the same.

6. Do not include internal system terms (e.g., short_term_memory, scratchpad, variables in xml tags) in the instructions. That will not add value to the instructions, rather it will confuse the agent.

- Incorrect: Get the user account lock status and store the information in your memory for processing it later.
- Correct:

1. Get the user account lock status.

2. If the user account is locked, unlock the user account. [Directly refer to the data, it will be available in the agent’s memory.]

- Incorrect: Store the user account status in variable <isActive>.
- Correct: If the user account is locked, unlock the user account.

7. When instructions involve communication with the end user, explicitly refer to them as “the user” rather than using ambiguous terms like ‘agent’, ‘entity talking to you’, etc.

- To show something to the user:

o Incorrect: Show the list of missing users to the agent.

o Correct: Show the list of missing users to the user.

- To ask something from the user:

o Incorrect: Find the record number.

o Correct: Ask the user for the record number.

8. Write the instructions to an agent in clear structural sequential steps.

- Incorrect agent instructions:

To check and allocate a software license, follow these steps:

Step 1: If there’s license id, then proceed to step 2.

If not provided, go to step 7.

[Issue in Step 1: The instruction doesn’t specify how to check for a license ID. Is it from memory? A user input? Needs clarity.]

Step 2: Follow the following steps: [This is unnecessary. Just write the actionable tasks]

If this is manager user, proceed to step 5.

If this is regular user, proceed to step 4.

If this is guest user, proceed to step 2.

[Issue in Step 2: Guest users will be stuck in a loop, endlessly going back to Step 2.]

Step 3: Guest user license allocation:

- Use appropriate tool to check if the user license can be allocated to a guest user.

[Issues in Step 3:]

[1: What is the "appropriate tool"? Not defined.]

[2: "check if the user license can be allocated" - What are the steps to check the eligibility criteria for license allocation?]

- If guest user can be allocated, tell user that you are assigning it to a guest user.
- Proceed to step 6.

Step 4: Manager user license allocation:

- If the manager is allowed to get a license, check if a license exists.
- If it does, assign it and let the user know.
- Otherwise, do something else.
- Move to Step 6.

[Issues in Step 4:]

[1: What does "allowed" mean? No criteria given.]

[2: "Do something else"—what exactly?]

Step 5: Regular User License Allocation:

- Check if the requested software license is there.
- If available, the user should get it.
- If not, then go to Step 6.

[Issues in Step 5:]

[1: "There"—where? Needs a database check or specific location.]

[2: "Should get it"—how? Missing the allocation method.]

Step 6: Handle Something (Unclear Purpose)

- If everything is fine, then move forward.
- If something went wrong, figure out what it is and fix it.

[Issues in Step 6:]

[1: "Handle something"—what exactly?]

[2: "Move forward"—to where? No direction provided.]

[3: How do you "figure out" what’s wrong? Missing troubleshooting steps.]

Step 7: If No License ID - If the user did not provide a license ID, then check if they need one. - If they need one, tell them to get it.

- If they don’t need one, then continue. [Issues in Step 7:] [1. How do we check if they "need one"? No method given.] [2: "Tell them to get it"—where/from whom? Missing clarity.] [3: What does "continue" mean? The process is left hanging.]
- Correct:

To verify the eligibility criteria and allocate a software license, follow the below instructions step-by-step:

Step 1: Verify if the License ID is available. If the License ID is missing, ask the user to provide it.

Step 2: Fetch the user details to determine the user type.

Step 3: If the user type is ‘manager’, then follow the below steps:

Step 3.1: Check if the requested software license is available.

Step 3.2: If available, allocate it to the user.

Step 3.2.1: Once the license is successfully allocated, inform the user about the same.

Step 3.3: If the licenses are not available, then inform the user the requested licenses are not available.

Step 4: If the user type is ‘regular employee’, then follow the below steps:

Step 4.1: Create a license allotment task for the user.

Step 4.2: Once the task is created, inform the user that the license allotment task has been created, and it is waiting for their manager’s approval. The license allocation will be processed based on their manager’s approval.

Step 5: If the user type is ‘guest’, then follow the below steps:

Step 5.1: Verify the roles of the guest user.

Step 5.2: Retrieve the list of roles who are eligible for the requested software license.

Step 5.3: Compare the guest user’s roles with the software license eligibility roles to determine if the guest user is eligible for the requested license.

Step 5.4: If the guest user is eligible for the requested license, then create a temporary license allocation task.

Step 5.4.1: Inform the user that the temporary license allocation task has been created for the guest user.

Step 5.5: If the guest user is not eligible for the requested license, then inform the user that the guest user is not qualified to access the requested software license due to missing roles.

9. Avoid redundant tools information in instructions. Do not add instructions like “You are given these tools” or “You are provided with the below tools”. The

tools and their descriptions mapped to the agent are already available to it. So, these instructions should not be restated in the instructions.

- Incorrect:

o You are provided with tool X, which has ABC functionality.

- Correct:

o Use tool X to extract data.

o Fetch the XYZ details.

10. Combining multiple actions in a single instruction can lead to skipping of few steps during execution. Each instruction must focus on a single actionable task.

- Incorrect: Summarize the record and show it to user, then update the record notes with the same data.
- Correct:

1. Summarize the record details.

2. Display the summarized record details to the user.

3. Update the record with the record summary.

11. Use unique inputs for tools across multiple agents in the team to prevent confusion.

- Incorrect: Naming both tool inputs as sys_id.

1. Agent 1:

o Name: Incident Analyzer Agent

o Tool name: Get incident details

§ Tool input name: sys_id

2. Agent 2:

o Name: User Analyzer

o Tool name: Get user details

§ Tool input name: sys_id

- Correct: Providing meaningful names to differentiate the different tool’s inputs.

1. Agent 1:

o Name: Incident Analyzer Agent

o Tool name: Get incident details

§ Tool input name: incident_sys_id

2. Agent 2:

o Name: User Analyzer

o Tool name: Get user details

§ Tool input name: user_sys_id

12. Unique names and clear descriptions for agents help the orchestrator pick the right agent for each task.

- Incorrect: Multiple agents in the team named "Analyzer" with similar descriptions.

1. Agent 1:

o Name: Data Analyzer Agent

o Description: This agent analyzes data.

2. Agent 2:

o Name: Content Analyzer Agent

o Description: This agent analyzes content.

- Correct:

1. Agent 1:

o Name: Data Analyzer Agent

o Description: Responsible for extracting and analyzing transaction data. Showing the results and taking feedback from the user.

2. Agent 2:

o Name: Log Analyzer Agent

o Description: Responsible for reviewing system logs and flagging anomalies and communicating them to the user.

13. Unique names and clear descriptions for tools help the agent pick the right tool for each task.

- Incorrect: Two tools whose purpose is different are named similarly and the description of the tools is also not clearly defined.

1. Agent 1: Incident Analyzer

o Tool name: Get user details

o Description: gets user details

2. Agent 2: User Analyzer

o Tool name: Get user details

o Description: gets user details

- Correct: The tool’s names and descriptions clearly depict the functionality of the tools.

1. Agent 1: Incident Analyzer

o Tool name: Get user status

o Description: Checks whether the user account is active or not.

2. Agent 2: User Analyzer

o Tool name: Get user details

o Description: Fetches user details like the name, department, manager, and other personal and team information.

14. Each operation (summarizing, gathering, concatenating data) should have its own dedicated instruction.

- Incorrect: Summarize and concatenate data before showing to the user.
- Correct:

1. Get similar incidents of the incident

2. Gather incident numbers from similar incidents.

3. Show the incident numbers to the user.

15. If a tool requires a particular input to be always present, ensure to mark it as mandatory if that feature is available in the tool (flow actions, subflow, etc). If not, mention it in the tool input description.

- Incorrect:

o Tool name: Get incident details

o Input name: incident_number

o Input description: incident number

- Correct:

o Tool name: Get incident details

o Input name: incident_number

o Input description: The unique identifier of the incident record. This is mandatory input. The incident number follows the pattern INCXXXXXX.

16. Always describe the inputs clearly while designing the tool to ensure a consistent pattern in execution of the tool.

- Incorrect:

o Input name: user_id

o Input description: The ID of the user.

- Correct:

o Input name: user_id

o Input description: The 32 characters alpha-numeric unique identifier of the user.

- Explanation: A user_id could be sys_id, full name, username, email_id, etc – it is important to clearly help the LLM understand what type of input should be chosen to run the tool.

17. Select an appropriate transformation strategy to process large outputs. For example, using an output transformation like "Summary for search results" helps filter and retain only relevant information, especially when using RAG as a tool.

- Incorrect: Directly pass the complete search results to the agent.
- Correct: Use output transformation: 'Summary for search results' to filter and pass only the contextual information needed for execution.
- Example: When fetching similar incidents, the RAG tool retrieves all incidents that are semantically like the search query. Applying the "Summary for search

results" transformation strategy ensures only the most relevant contextual information is selected and passed forward.

18. Be mindful that any tool output exceeding the model's token limit will be truncated. Ensure that tool code post-processing logic to process or summarize data appropriately to prevent data loss.

- Incorrect: Generating a large amount of data from the tool and passing it to the agent without considering the token limit.
- Correct: Fetching only necessary and meaningful data and summarizing it if needed.
- Example: Fetching all incidents assigned to a team may generate excessive data. The ideal approach is to retrieve all incidents, extract only the required attributes from the incident record, and summarize the data if necessary.

19. Use an actional statement to transfer the execution flow to another agent in the team without using the agent’s name or name of the tool mapped to the other agent.

- Incorrect: Call “Get incident details” from “Incident analyzer agent” with value incident_number as INCxxxxxx
- Correct:

1. Fetch incident details with the the retrieved incident number.

2. Fetch user details for the assigned user from the retrieved incident details.

20. For agent workflows that involve processing large datasets, generating structured content under specific constraints, or performing multi-step logic with deterministic outcomes, it is advisable to implement a dedicated Skill tool instead of relying on built-in tools like organize_general_knowledge or math.

o The built-in tools are designed to support lightweight, in-memory operations—offering temporary reasoning space to the agent without persisting output to memory or enabling inter-agent sharing. These tools are best suited for quick data structuring and basic reasoning tasks.

o For use cases where precise control over output (e.g., content, format, or structure) is necessary, custom Skill tools provide greater flexibility and reliability.

o Example 1: Next Best Action Agent: When generating plans, using a Skill tool ensures consistency in formatting, styling, and structure—something not easily achievable through the built-in tools where output cannot be explicitly guided or preserved.

o Example 2: Tasks like generating HTML responses, producing itemized lists with specific rules, or verifying large documents against detailed

criteria are better handled by Skill tools. Otherwise, the complexity of the instructions required in the agent may increase significantly, potentially leading to ambiguity or overlooked steps during execution.

o By using a custom Skill tool for such cases, you ensure the agent’s behavior is predictable, reusable, and maintainable.

### **Debugging**

1. Decision logs (right pane in Agent Playground) play a very crucial role in providing details on how our instructions in use case, agent and tool details are analyzed by LLM.

2. Every “Orchestrator” log is generated based on the instructions defined in the use case. This log describes the subtask(s) generated and the agents it delegates to.

3. Every <agent> log is generated based on the instructions defined in the agent.

4. Agent logs:

a. Thought describes what happened till now in the execution flow and what would be the next action to execute. The agent instructions are responsible for generating this Thought and controlling the flow of the agent. Refine your instructions accordingly.

b. Action Reasoning describes why the agent chose to run the tool and its inputs. If a wrong tool is chosen, then check your tool details like name, description, inputs, input descriptions.

c. Action Inputs depicts the data that is chosen to run the tool. This data is chosen from the memory of the agent. If an incorrect input is chosen, then refine the input description to align with the details of the input stored in the memory.

d. Output of the Action helps understand whether the tool run was successful or not and what output was returned from the tool.

5. All the data generated in the current conversation including tool execution outputs are stored in the memory (which gets persisted in the sn_aia_message table - `Message` column).

### **FAQs**

1. Skill is not discovered.

Ø Check if skill discovery is working on the instance, if not reach out to the respective team for further help.

Ø If skill discovery is working and the use case/agent is not being discovered, then check your use case name & description/agent name & description.

2. The execution ends immediately with “Sorry, there was a problem on my side trying to complete this request. Try asking again later.” error.

Ø First, navigate to the `sys_generative_ai_log` table and verify if the LLM calls are successful on your instance.

Ø If there is any error, then check Generative AI controller setup on your instance.

Ø If the Planner/ReAct LLM calls are successful, then it indicates that a suitable agent could not be picked for the given task. Check if the technical terms in the task align with the agent’s name, description, role, instructions, proficiency.

3. Incorrect agent is chosen during execution.

Ø Check the uniqueness of the agent’s name and descriptions of the agents in the team. If there are multiple agents in the team with overlapping context that might confuse the Orchestrator regarding which agent is most suitable for the task.

4. How to write instructions to reference the memory?

Ø No specific terms need to be used to refer to the agent’s memory. Directly write the instructions like `Show a message to the user about the extracted incident details.`

5. How to write instructions to hand over to another agent?

Ø Never mention the name of another agent or the name of a tool mapped to another agent to handover the flow of execution to another agent. This will confuse the current agent as it is not aware of the tools of other agents or the names of other agents in the team.

Ø Use an actionable statement explaining the task to achieve this.

Ø Example 1: Fetch the incident details (Here “Get incident details” is tool in some another agent).

Ø Example 2: Fetch user information with the assigned user from the details of the incident. (Here “Get user details” is a tool mapped to another agent)

6. How to write instructions to ask user / display something to user?

Ø The instruction should not contain anything related to the agent. Example: Ask agent to provide incident number. (This is incorrect)

Ø The statement should be addressed to the user. Example: Ask user to provide the incident number.

Ø To show something to user without seeking any input, address the user with terms like show/ display etc. Example: Inform user that incident details could not be fetched.

7. How to share memory across multiple agents?

Ø Do not use terms like store the value from the tool into <incident_details> or terms like ‘store in memory’. The agent cannot understand this as there is no concept of “saving something to memory” for an agent.

Ø Memory is internally maintained where all the tool outputs and information conveyed to the user is saved and that is and shared across all the agents.

Ø To refer to any data in the instructions, use actionable statements aligning to the terminology returned from the tool output, so that the context of the data being referred is clear to the agent.

Ø Example: Fetch user details with the assigned user from the retrieved incident details.

8. How to write instructions to end the agent execution?

Ø Do not use statements like “end the conversation” / “stop execution” / “end the flow” / “terminate the execution”.

Ø No specific instructions are required for this. Once the action items given are fulfilled by the agent as per the instructions it will come to completion.

### **Related Links**

For more details on **"Advanced AI Agent Instructions Guide: ServiceNow Edition"**, please refer to the below community article,

[https://www.servicenow.com/community/now-assist-articles/advanced-ai-agent-instructions-guide-servicenow-edition/ta-p/3346578](https://www.servicenow.com/community/now-assist-articles/advanced-ai-agent-instructions-guide-servicenow-edition/ta-p/3346578)

## Related

- [[Agentic Workflow & AI Agents]]
- [[Get Familiar with Agentic Workflows & AI Agent]]
- [[AI Agent tools – Getting the most out of your agen]]
- [[Agentic Workflow & AI Agents – Tips]]
- [[AI Agents & Agentic Workflows — Reference Compilat]]