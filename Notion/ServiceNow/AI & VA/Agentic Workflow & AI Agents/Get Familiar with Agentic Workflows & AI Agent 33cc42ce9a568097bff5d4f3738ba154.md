---
aliases:
  - "Get Familiar with Agentic Workflows & AI Agent"
tags:
  - ai-agents
  - agentic-workflow
  - ai-agent-studio
  - now-assist-panel
  - ai-search
---

# Get Familiar with Agentic Workflows & AI Agent

Screenshot 2025-08-11 at 14.41.20.png

We used to design services. Now we’re designing the thinking *behind* them.

With ServiceNow’s **AI Agentic Workflows**, you're not just setting up automation, you’re training digital coworkers that can plan, reason, and get things done.

This ***hands-on guide is your quick and easy on-ramp to AI Agents***. In just a few steps, you’ll explore, activate, and test your first AI Agent, all with **zero coding required**. Whether you're new to the concept or ready to scale your impact, this lab will help you **get familiar with AI Agents fast and confidently**.

**PreRequisites**

1. **ServiceNow Instance**
2. **License**Now Assist License (Pro Plus/Enterprise Plus)
3. **Plugins**AI Agents store app installed.Make sure dependency apps and main "Now Assist for..." store apps are also installed and updated. Ensure to Install the required dependencies and the latest version is selected, and select “Load demo data” in order to have demo data pre-configured.If you are facing conflicts with plugin versions, repairing the following and related ones could solve the problem:

1. Flow designer (ServiceNow Product - 20 plugins)

2. Microsoft Azure OpenAI Generative AI Spoke (App id: sn_azure_openai)

3. Generative AI Controller (App id: sn_generative_ai)

4. Now Assist AI Agent (App id: sn_aia)

5. Now Assist for [Product Name] (Example: App id: sn_itsm_gen_ai)

6. Now Assist for Spokes (App id: sn_assist_spokes)

7. Now Assist for Platform (App id: sn_genai_platform)

8. Now Assist in AI Search (App id: sn_ais_assist)

9. Now Assist in Virtual Agent (App id: sn_nowassist_va)

10. Now Assist Platform Skills (App id: sn_nowassist_gs)

11. Now Assist for Creator (App id: sn_now_creator)

12. All the plugins and their dependent plugins which need update on your instance.

**Important**: *Make sure dependent plugins are on the latest version.*

1. **AI Search**Enable AI Search. Check status on “AI Search > AI Search Status”
2. **Now Assis Panel**For human agents to interact with the AI Agents, we also need to enable the Now Assist Panel. This will allow a human agent to interact with the AI Agent through a conversational interface, and is particularly important when the AI Agent has to ask clarifying questions or provide responses back to the human agent.

To turn on the Now Assist Panel:

In the navigation menu, go to Now Assist Admin > Experiences.

In Now Assist Experiences > Applications > Now Assist panel, go to the Summary widget. Select Turn on to enable the Now Assist Panel.

*Note that at least one Now Assist product plugin (ITSM, HRSD, CSM, SecOps, etc.) must be activated to turn on the Now Assist Panel.*

1. **Roles**Be sure your admin user is granted with the following roles: **sn_aia.admin, sn_nowassist_admin.nsa_admin**
2. **Data Quality**AI Agents use the context of your ticket and your searchable content to generate plans and actions. Ensure that your ticket data and knowledge base have the latest accurate information for the best results.

# **The GoalLab Summary: Exploring Out-of-the-Box AI Agents and Agentic Workflows**

In this lab, you'll get hands-on experience with ServiceNow’s out-of-the-box (OOTB) AI Agents and Agentic Workflows. The goal is to understand how some ootb AI Agents generate resolution plans, inspect their behavior, and become familiar with the tools available in the AI Agent Studio. You'll start by activating and exploring the default AI Agent setup, particularly the "Generate resolution plans" Agentic Workflow, then modify it to enhance its capabilities, specifically enabling the Agents to write logs in the system and automatically create a Change Request to track and resolve the issue. This exercise bridges the gap between AI reasoning and real-world action, showcasing how generative AI can be orchestrated within ServiceNow to drive intelligent automation.

**Considerations**

- Release:
    - **YP4** [glide-yokohama-12-18-2024__patch4-05-14-2025]
- Plugin versions:
    - Generative AI Controller [App id: sn_generative_ai]: Version: 10.0.8
    - Now Assist in AI Search [App id: sn_ais_assist]: Version: 11.0.14
    - Now Assist AI Agents [App id: sn_aia]: Version: 4.0.37
    - AI Agents Platform Usecase [App id: sn_aia_uc]: Version: 1.0.5
- Naming: The term '' replaced the original '' label used in the first release.
    
    *Agentic Workflow*
    
    *Use Case*
    
- Created on:
    
    11th August 2025
    
- Created by:
    
    Luis Estéfano
    

---

**Get familiar with ServiceNow AI Agentic Workflows**

Build AI Agents that plan, reason, and automate your workflows!

Enhance your team’s productivity with AI agents that orchestrate workflows, skills, and actions across your business. Learn how to activate prebuilt ServiceNow AI Agents and create custom agents tailored to your needs with minimal code.

Be sure the following are enabled:

- **AI Search**: Confirm that AI Search is enabled.

To confirm, navigate to AI Search > AI Search Status page.

- **Now Assist Panel**: Confirm that Now Assist Panel is enabled.

To do so, navigate to Now Assist Admin > Experiences. Then turn on the Panel.

**Exercices**

1. Exploring the Agentic Workflow

2. Exploring AI Agent

3. Test the Agentic Workflow and AI Agent

4. Duplicate an Agentic Workflow

5. Duplicate and Modify an AI Agent

6. Create an AI Agent

7. Deploying the AI Agent to the Now Assist Panel

8. Troubleshooting your AI Agent

---

**Exercise 1: Exploring the Agentic Workflow**

In this section, you'll explore out-of-the-box agentic workflows, referred to as Agentic Workflows in the latest release, break down their key components, and activate one of them.

1. To access the AI Agent Studio, in the navigation menu, go to: All > AI Agent Studio > Overview.
2. Scroll down to the Agentic Workflow sub-tab.
    
    *In the initial AI Agents releases, "Agentic Workflow" may be referred to as "Use Case".*
    
3. Select the “**Generate resolution plans**” agentic workflow. If necessary, sort the list by Name or click "View all" to display all available agentic workflows.
    
    [LuisEstefano_1-1755986288719.png](https://www.servicenow.com/community/image/serverpage/image-id/464943iA924D6989E2ADC45/image-size/large?v=v2&px=999)
    
    Another alternative is to go to "Create and manage" tab on the AI Agent Studio, in order to see all Agentic Workflows and AI Agents availables on the system.
    
    [LuisEstefano_2-1755986390784.png](https://www.servicenow.com/community/image/serverpage/image-id/464944iCB40DD8F4C9245B9/image-size/large?v=v2&px=999)
    
    SN Documentation:
    
    [Platform agentic workflows - **Generate resolution plans**](https://www.servicenow.com/docs/csh?topicname=platform-use-cases.html&version=latest)
    
4. Review the Agentic Workflow configuration. Notice that this Agentic Workflow is available out-of-box and is, therefore, set to a read-only protection policy (unable to be modified directly).
    
    [LuisEstefano_4-1755986654596.png](https://www.servicenow.com/community/image/serverpage/image-id/464946iD8409548058913D0/image-size/large?v=v2&px=999)
    
5. Under Describe the agentic workflow, examine the field values:
- Name: Business challenge that you want to solve.
- Description: Brief summary of what business problem your agentic workflow.
- Instructions: Guided actions to be followed by your AI agent.The Instructions field is designated as AI Instruction, meaning it is directly associated to the LLM input.
1. As you scroll, notice the Connect AI agents section. Here is where you map one or a team of AI Agents to execute the instructions of an agentic workflow. In this case, you see the following AI Agents connected to the "**Generate resolution plans**" *agentic workflow:*
    1. Record management AI agentPerform actions of fetch, create, update the record with the provided record details
    2. Next action recommendation AI agentThe Next best action recommender Agent is an AI agent designed to analyze and resolve tasks by following a specific progression of steps. It is responsible for fetching record details, similar records, and relevant knowledge articles to provide summaries or resolution steps as needed.
    3. Web research and recommendation AI agent**Familiarize yourself with the AI Agents by reviewing their descriptions and instructions to gain a clearer understanding of what to expect from each one.**
        
        This agent is designed to assist users in resolving issues by analyzing the problem and generating resolution steps using web search tools. It is intended for users who require assistance in troubleshooting and resolving technical or non-technical issues.
        
        [LuisEstefano_3-1755986551429.png](https://www.servicenow.com/community/image/serverpage/image-id/464945i0F827578BA611882/image-size/large?v=v2&px=999)
        
        The "**Generate resolution plans**" AI Agent is designed to resolve tasks by fetching record details, generating resolution summary steps, and updating comments or task work notes accordingly. It is intended for tasks that require analysis, solving, planning, or resolution, and can handle tasks with minimal or no details provided. Helps in resolving incidents, cases and tasks. Document all in a subtask for future reference.
        
        ---
        
2. The "Recommend AI agents" to add section leverages Now Assist to help you quickly find the right AI Agents to map to your agentic workflow. Make sure the Description and Instructions fields are well-defined.
3. Click Continue to review conditions for this agentic workflow to be automatically triggered.
4. From the Define trigger page, click Add Trigger to explore how to build a trigger.
    
    [LuisEstefano_5-1755986754092.png](https://www.servicenow.com/community/image/serverpage/image-id/464947iE931638358C23C32/image-size/large?v=v2&px=999)
    
5. Complete the fields as follows:
- Select trigger: Created or updated.
- Trigger name: <select any name>.
- Table: Incident.
    
    [LuisEstefano_0-1756033563858.png](https://www.servicenow.com/community/image/serverpage/image-id/464969iEF558EC351D6A157/image-size/large?v=v2&px=999)
    

As the Table field is defined, Conditions, Run as, and Objective Template fields automatically appear.

- To define when your AI Agent agentic workflow should run, you'll need to fill out two key fields:
    - Conditions: This field defines when the agentic workflow should trigger. For example, you can set it to run when a new record is created, or when a certain field, like Category, is set to a specific value, such as Password Reset.
    - Run as (sys_user): This field outlines whose permissions the AI Agent should use. It controls what the AI Agent is allowed to see or do as part of the agentic workflow. For example, select a role or persona that has access to modify incident records.For populating this field, there are two available options:
        - Use an existing table
        - Use a new custom script
- The Objective Template field tells the AI Agent what kind of situation should trigger the agentic workflow. It helps define the goal of the agentic workflow, such as solving a problem or answering a question.For example, ‘Help me resolve ${number}’ to let the Agent know it should guide the user through a solution.
1. Click Cancel for now. You’ll get to define a trigger in a later section of the lab.
2. Open the Select display page of the agentic workflow. Here is where you configure if this agentic workflow will be displayed on the Now Assist panel (NAP). It defaults to off.
    
    [LuisEstefano_6-1755987009295.png](https://www.servicenow.com/community/image/serverpage/image-id/464948i3D6601D964D897C9/image-size/large?v=v2&px=999)
    
3. Toggle the Display on and click the arrow next to it further define the user roles who can trigger this agentic workflow from the NAP.
4. In the User roles field, add now_assist_panel_user, then click Save and test.
    
    [LuisEstefano_7-1755987109480.png](https://www.servicenow.com/community/image/serverpage/image-id/464949iFD4078EB75CB4BD7/image-size/large?v=v2&px=999)
    

You've now activated your first agentic workflow! Before we test this agentic workflow, let's first explore the AI Agent associated with this agentic workflow: Next Best Action Agent.

---

**Exercise 2: Exploring AI Agent**

In this section, you'll explore the Next Best Action AI Agent.

1. Return to the **AI Agents Studio’s Overview** page.
2. Locate and open the “**Generate resolution plans**” ******agentic workflow.
3. From the **Describe and connect** tab. Scroll down to the **Connect AI agents** section.

Note that AI agents are mapped to a parent use card record - you can have many AI agents linked to a single agentic workflow.

1. Select the **Next Best Action Agent** AI agent record.
    
    [LuisEstefano_8-1755987314071.png](https://www.servicenow.com/community/image/serverpage/image-id/464950iEECDDBEF174F90C9/image-size/large?v=v2&px=999)
    
2. Under **Describe and instruct**, examine the field values:
- **Name**: Unique name for the AI Agent
- **Description**: Summarizes what the AI Agent can do
- **AI agent role**: The capabilities and responsibilities defined for your AI agent; it describes your AI agent performing its required actions.
- **Instructions**: Specific, task-oriented guidelines or commands that clearly delineate what the AI agent should do in each situation, complete with conditions, steps, or constraints.
1. Under the **Add tools and information** tab, you can add Tools to empower your AI Agent. Tools can come in many forms, including:
    - Catalog item
    - Conversational topic
    - Flow action
    - Now Assist skill
    - Record operation
    - Script
    - Search retrieval
    - Subflow
    - Web search

Regardless of which tool you use, the Inputs and Outputs can only be String. You may also leverage Now Assist to recommend tools with the **Suggested tools to add functionality**.

1. Under **Define availability**, activate the AI Agent by switching the **Status** toggle to 'on'.

---

**Exercise 3: Test the Agentic Workflow and AI Agent**

1. From the **Next Best Action Agent’s** **Define availability** section, click **Save and test.**

This action takes you to Testing page of the AI Agent Studio. You can also access this page by navigating to AI Agent Studio > Testing.

[LuisEstefano_1-1756033654774.png](https://www.servicenow.com/community/image/serverpage/image-id/464970i05C54BD034DE2DC1/image-size/large?v=v2&px=999)

1. In the **Test scenario** pane, select the following:
- **What to test**: Agentic Workflow (you can also test AI Agent by itself)
- **Agentic Workflow**: **Generate resolution plans**
- **Task**: Help me resolve Incident INC0009005.(Find an incident number on your instance by going "Service Desk > Incidents" on the left side menu).
    
    [LuisEstefano_2-1756033829961.png](https://www.servicenow.com/community/image/serverpage/image-id/464971i83F43A11D77C71CA/image-size/large?v=v2&px=999)
    
1. Click **Start Test**. The Agentic Workflow test begins, and you monitor the progress in the **Output** pane. The **AI agent decision logs** are recorded on the right-hand side of the panel. To view all log details, click the down-pointing arrows.You can export the decision logs report by clicking the Download logs button, on the top of the right side panel. There are also some options for the map, alowwing zoom in/out, download.
    
    [LuisEstefano_3-1756033951269.png](https://www.servicenow.com/community/image/serverpage/image-id/464972i9F111EB7439B7DCE/image-size/large?v=v2&px=999)
    
2. Verify, in the Now Assist panel, that the steps provided by the AI Agent are appropriate to resolve the Incident. **Review the incident to examine the output written by the AI Agent in the work notes activity. This reveals the Agent's thought process.** This shows the thought process of the Agent. Now, let's modify the agentic workflow to turn thought into action.
    
    [LuisEstefano_5-1756034291174.png](https://www.servicenow.com/community/image/serverpage/image-id/464974i9C620B42F1D6A3EE/image-size/large?v=v2&px=999)
    

---

**Exercise 4: Duplicate an Agentic Workflow**

Let's modify the agentic workflow and the AI Agent. We will also add a second AI Agent to the agentic workflow to perform more actions.

1. In the banner's top-right corner, verify that you are working in the Global application scope.*Check session and switch to Global application scope, if not yet already*The selected scope itself is not vital to this lab exercise, but goes to illustrate that the Duplicate function will duplicate the selected Agentic Workflow into the session's application scope. Be consistent with your application scope usage!
    
    [LuisEstefano_7-1756034436638.png](https://www.servicenow.com/community/image/serverpage/image-id/464976iD9E1648841B72DA8/image-size/large?v=v2&px=999)
    
2. Navigate to **AI Agent Studio >** **Create and manage**.
3. Under the **Agentic Workflows** pane, locate "**Generate resolution plans**" ****and click the **Duplicate** button.
    
    [LuisEstefano_8-1756034556505.png](https://www.servicenow.com/community/image/serverpage/image-id/464978i0268410A63F29B99/image-size/large?v=v2&px=999)
    
4. From the You are duplicating an agentic workflow dialog popup box, confirm by clicking **Duplicate**.Duplicate agentic workflow confirmation window.
    
    [LuisEstefano_9-1756034592690.png](https://www.servicenow.com/community/image/serverpage/image-id/464979i64C51F18426A1B7E/image-size/medium?v=v2&px=400)
    
5. You should now be in a new, duplicate agentic workflow called "**Generate resolution plans**" **(Copy)**. It is no longer read-only.
6. Let's update the agentic workflow with our desired changes. Rename the agentic workflow to a preferred name, then modify the field values as follows:
- **Name**: "<PREFIX> - Generate resolution plans".(It's helpful to add a prefix of your initials so that it's easier to find in the testing panel.)
- **Description**: Come up with a step-by-step plan for a given task like incidents, cases, or problems to resolve it. Create a change request based on it.
- **Instructions:** Add an additional step:
    - ***#### **5. Create change record with the generated resolution plan**Create a change request with the resolution plan generated by the "Nex action recommendation AI Agent (Copy)" AI Agent, by using the "Create Change record with Plan" AI Agent.***
        
        [LuisEstefano_22-1756076637973.png](https://www.servicenow.com/community/image/serverpage/image-id/465052i1A968F474B5516EE/image-size/large?v=v2&px=999)
        
        [LuisEstefano_21-1756076588171.png](https://www.servicenow.com/community/image/serverpage/image-id/465051i7321AEBBBB3B6538/image-size/large?v=v2&px=999)
        
1. At the bottom, click **Save and continue**.
2. From the Define Triggers page, click **Add Trigger**. We will create a Trigger for an AI Agent to run whenever an incident is created by you (admin).
3. Configure the trigger as the following:
- Select trigger: Created.
- Trigger name: Incident created by admin.
- Table: Incident.
- Conditions: Created | is | admin
- Run as: Caller [incident].
- Objective template: Help me resolve ${number}.

[LuisEstefano_14-1756035463925.png](https://www.servicenow.com/community/image/serverpage/image-id/464986i8F5766224749D789/image-size/large?v=v2&px=999)

1. Check the **Show Notifications** checkbox field, then click **Add**.
    
    [LuisEstefano_16-1753049140913.png](https://www.servicenow.com/community/image/serverpage/image-id/457158i51645824CAF49A05/image-size/medium?v=v2&px=400)
    
2. The new trigger you've created displays in the **Existing triggers** list. Click **Save and continue**.
3. From the **Select display** page, enable the agentic workflow by toggling on the **Display** field.
4. Click the down arrow, then add **now_assist_panel_user** in the **User roles** field.
    
    [LuisEstefano_15-1756035548550.png](https://www.servicenow.com/community/image/serverpage/image-id/464987iF02D5733BB10FA2C/image-size/large?v=v2&px=999)
    
5. When done, click **Save and test**. You are directed to the Testing page of the AI Agent Studio. Before testing this agentic workflow, we need to add another agent.

---

**Exercise 5: Duplicate and Modify an AI Agent**

Check to make sure that you are working in the same application scope as you had duplicated the Agentic Workflow into: **Global** application scope. We will modify an AI Agent to add a new Script tool and make other changes.

1. Return to the **Describe and connect** pane of your custom "".
    
    **Generate resolution plans**
    
2. Scroll to the **Connect AI agents** section and open the "" record.
    
    Next action recommendation AI agent
    
3. To the right of the **Exit** button, click the triple dot menu icon and select **Duplicate**.
    
    [LuisEstefano_0-1756073212195.png](https://www.servicenow.com/community/image/serverpage/image-id/465016i4B15CADB4675937A/image-size/large?v=v2&px=999)
    
4. In the popup dialog window, select **Duplicate**.
    
    [LuisEstefano_2-1756073390514.png](https://www.servicenow.com/community/image/serverpage/image-id/465019iC41C90013A1FE8BE/image-size/medium?v=v2&px=400)
    
5. You should have a new AI Agent with the "Nex action recommendation AI Agent (Copy)".
6. Scroll to the **Instruct the AI agent** section and review the **Instructions**. At the end of step 4th step, add a new step, and rename the "5. Finish" to "6. Finish":.Note the specificity of our step - we are noting the action to be done, the tool, and what objects are involved.
    
    **5. Output a message a message with a script with the Incident number**
    
    6. Finish.
    
    [LuisEstefano_3-1756073623265.png](https://www.servicenow.com/community/image/serverpage/image-id/465024i5EBE645F14EBE2F7/image-size/large?v=v2&px=999)
    
7. At the bottom, click **Save and continue**.
8. In the **Add tools and information** section, open the **Get similar Incidents** Flow actions tool.
    
    [LuisEstefano_4-1756073764511.png](https://www.servicenow.com/community/image/serverpage/image-id/465027i57B2B5C24A16B76C/image-size/large?v=v2&px=999)
    
9. Change the **Display output** to **Yes** and set the **Output transformation strategy** field to **Concise**.
    
    [LuisEstefano_5-1756073843040.png](https://www.servicenow.com/community/image/serverpage/image-id/465028i4A232F101E1B8854/image-size/large?v=v2&px=999)
    
    **IMPORTANT:** *As of Yokohama Patch 1, modifying a tool in a copied AI Agent also modifies the tool in the original agent. If you don't want this, manually duplicate the tool to modify it.*
    
10. Click **Save.** We should now expect similar incidents to appear when this tool is triggered.
11. Let's add a Script step to the Agent. From the **Add tools and information** page of your AI Agent, click **Add Tool** and select **Script**.
    
    [LuisEstefano_6-1756073975758.png](https://www.servicenow.com/community/image/serverpage/image-id/465029i0E209F64733CE2CC/image-size/large?v=v2&px=999)
    
12. Complete the Script form fields as follows:
- **Name**: Message Output.
- **Description**: Run a script that outputs a message that a plan has been approved for the given Incident number.
- Under **Script inputs**, click the **+ Add an input** button.
    - For **Input name**, enter **inc_number**.
    - For **Description**, enter **Incident number**.
        
        [LuisEstefano_7-1756074228060.png](https://www.servicenow.com/community/image/serverpage/image-id/465030i57266DFB07F6814D/image-size/large?v=v2&px=999)
        
- In the **Script** block, enter:

(function(inputs) {

gs.info("Plan approved for " + inputs.inc_number);

})(inputs);

---

[LuisEstefano_8-1756074264818.png](https://www.servicenow.com/community/image/serverpage/image-id/465034i79429A6133283232/image-size/large?v=v2&px=999)

- Set **Execution mode** to **Autonomous** (user will not be asked for permission), and set **Display Output** to **No** (the AI Agent will not communicate anything).
    
    [LuisEstefano_9-1756074300260.png](https://www.servicenow.com/community/image/serverpage/image-id/465035iF62DDE209CCDC239/image-size/large?v=v2&px=999)
    
1. Click **Add**.
2. At the bottom, click the **Save and continue** button.
3. In the **Define availability** section, click **Save and test**.

Before we test the AI Agent, let's add another agent that can create change requests.

---

**Exercise 6: Create an AI Agent**

Navigate to the AI Agent Studio’s **Create and manage** page. (If you are already in the AI Agent Studio, click the **Create and manage** tab).

1. Click the **AI Agents** sub-tab to display the list of available AI Agents.
2. On the right-hand side, click **New**.
    
    [LuisEstefano_11-1756074413741.png](https://www.servicenow.com/community/image/serverpage/image-id/465037i30D9DA6273BDFDE0/image-size/large?v=v2&px=999)
    
3. Complete the new AI Agent’s **Describe and instruct** fields as follows:
- **Name**: Create Change record with Plan.
- **Description**: This agent can create change records.
- **AI agent role**: You are an expert in creating change records.
- **Instructions**:

Create a change record with the generated plan from the "Nex action recommendation AI Agent (Copy)".

After record is successfully created, you are finished.

---

1. Click **Save and continue.**
2. Click **Add Tool**, then select **Record operation**.
    
    [LuisEstefano_12-1756074697547.png](https://www.servicenow.com/community/image/serverpage/image-id/465039i76E9AFCA96791EF4/image-size/large?v=v2&px=999)
    
3. Complete the **Add a record operation** form fields as follows:
- **Name**: Create Change Request record.
- **Description**: Create a change request record with the resolution plan.
- Under **Script inputs**, click the **+ Add an input** button to enter the following inputs:
    - **Input name**: change_title, **Description**: Summary of resolution plan.
    - **Input name**: res_plan, **Description**: Resolution plan created by "Nex action recommendation AI Agent (Copy)".Note the input descriptions used to describe what data is needed.

[LuisEstefano_13-1756074857378.png](https://www.servicenow.com/community/image/serverpage/image-id/465040i271B3019C581765E/image-size/large?v=v2&px=999)

- **Table**: Change Request
- Select operation: Create record
- Under **Field values**, click the **+ Add field value** button to enter the following values:
    - **Field**: Short description, **Value**: {{change_title}}
    - **Field**: Description, **Value**: {{res_plan}}
        
        [LuisEstefano_14-1756074981950.png](https://www.servicenow.com/community/image/serverpage/image-id/465041i514D28E4346C5AAC/image-size/large?v=v2&px=999)
        

Note the field values using double curly braces {{...}} to reference the data to be input into the fields. You can type the values or use the Tool input variable icon to fill in the fields.

- **Execution mode**: Supervised (will ask user for permission to create a change request)
- **Display output**: Yes (as we want confirmation)
- **Output transformation strategy**: Concise
    
    [LuisEstefano_15-1756075008807.png](https://www.servicenow.com/community/image/serverpage/image-id/465042iF2F40C29833D036B/image-size/large?v=v2&px=999)
    
1. Click **Add**.
2. At the bottom, click the **Save and Continue** button.
3. In the **Define availability** section, click **Save and test**.
4. We need to add this AI Agent to the (copy) agentic workflow previously created, on exercise five (5), and modify the agentic workflow’s instructions regarding our new AI Agent. Return to the list of agentic workflows and open your custom "Generate resolution plans" agentic workflow record.Double-check the second step was added to your duplicated Agentic Workflow per the previous exercise to account for this new agent.
5. From the **Connect AI agents** section, click **Add AI Agent**.
6. Search for and connect the  ****and AI Agents to your agentic workflow. When done, click **Add**.
    
    "Nex action recommendation AI Agent (Copy)"
    
    "**Create Change record with Plan"**
    
    [LuisEstefano_16-1756075306946.png](https://www.servicenow.com/community/image/serverpage/image-id/465043i06EC6892B09478FE/image-size/large?v=v2&px=999)
    
7. Remove the original
    
    "Nex action recommendation AI Agent".
    
8. Make sure your **Incident created by admin** trigger is set to Active, then click **Save and continue**.
9. Under **Define trigger**, make sure your **Incident created by admin** trigger is set to **Active**, then click **Save and continue**.
10. Proceed to the **Testing** page.
11. Test again your Agentic Workflow copy with incident INC0009005 (Pick one number from your instance) by checking the following steps occur:
    1. Record details displayed in the Output panel.
        
        [LuisEstefano_18-1756075940209.png](https://www.servicenow.com/community/image/serverpage/image-id/465048i800684E089605F44/image-size/medium?v=v2&px=400)
        
    2. A list of similar incidents is displayed in the **Output** panel.
    3. A **resolution plan** is generated and asks for user approval.
        
        [LuisEstefano_19-1756075971576.png](https://www.servicenow.com/community/image/serverpage/image-id/465049iA99553540A612822/image-size/medium?v=v2&px=400)
        
    4. A script is run and outputs a message regarding the Incident record. We can check this by checking the system logs and searching for the incident number (System Logs > System Log > All).
        
        [LuisEstefano_17-1756075908514.png](https://www.servicenow.com/community/image/serverpage/image-id/465047iF9EEEB0F4D69F91D/image-size/large?v=v2&px=999)
        
    5. A change request record is created. The AI Agent asked for approval to do so. Note in the testing panel the AI Agent switching over. Navigate to the Change Request table to confirm the record is created with the requested data.Change Request record created with the resolution plan:
        
        [LuisEstefano_23-1756076933141.png](https://www.servicenow.com/community/image/serverpage/image-id/465054iCEFDA0DA53819BF2/image-size/medium?v=v2&px=400)
        
        [LuisEstefano_24-1756076951199.png](https://www.servicenow.com/community/image/serverpage/image-id/465055i34C2205D3CFBE2B7/image-size/large?v=v2&px=999)
        
    6. Testing may run slowly, including processing responses you provide.

[LuisEstefano_25-1756077006700.png](https://www.servicenow.com/community/image/serverpage/image-id/465056i9DA13B2FEBA2B87D/image-size/large?v=v2&px=999)

---

**Exercise 7: Deploying the AI Agent to the Now Assist Panel**

Now, let's see the Agentic Workflow operate in the real world.

1. Navigate to Incident > Create New to generate a new incident record.
2. We want to create an Incident we know has existing similar incidents or a knowledge article. Note the caller should be admin (System Administrator) as this was a condition for the Agentic Workflow trigger. Fill out the form fields as follows:
    
    [LuisEstefano_26-1756077189915.png](https://www.servicenow.com/community/image/serverpage/image-id/465059i926645FE02329F15/image-size/medium?v=v2&px=400)
    
3. Click Submit.
4. Navigate to Workspaces > Service Operations Workspace.
5. On the banner's right side, notice the Now Assist panel has received a notification (recall you enabled notifications for the Agentic Workflow Trigger.)
    
    [LuisEstefano_37-1753049551160.png](https://www.servicenow.com/community/image/serverpage/image-id/457179i33C41A4B3E0C38CD/image-size/medium?v=v2&px=400)
    
6. Click the Now Assist icon to open the Now Assist panel and look into the notification to see the AI Agent run.
    
    [LuisEstefano_27-1756077252776.png](https://www.servicenow.com/community/image/serverpage/image-id/465060iC63059EA04B8B5F5/image-size/large?v=v2&px=999)
    
7. When asked, by the AI Agent, to proceed with creating a change record, enter Yes proceed.
    
    [LuisEstefano_28-1756077597619.png](https://www.servicenow.com/community/image/serverpage/image-id/465061i7FDEC3C0CBB8F097/image-size/large?v=v2&px=999)
    
    [LuisEstefano_29-1756077684649.png](https://www.servicenow.com/community/image/serverpage/image-id/465062i60568FC7B3FE618C/image-size/large?v=v2&px=999)
    
8. Once the change request is created, you can navigate in the Workspace to the list of Open or All changes to see the change record created.Optional: It is also possible to manually invoke your AI Agent by typing into the Now Assist Panel similar to the trigger's objective template.
9. Navigate to AI Agent Studio > Analytics to see the usage analytics of your AI Agents. Optionally, from the AI Agent Studio’s Overview page, click the View Analytics button to access the same Analytics dashboard.
    
    [LuisEstefano_30-1756077801938.png](https://www.servicenow.com/community/image/serverpage/image-id/465063iF3F072996F1C1A5D/image-size/large?v=v2&px=999)
    

---

**[Optional] Exercise 8: Troubleshooting your AI Agent**

You may occasionally get an error message when testing your AI Agents, "There are no agents available at the moment. Please try again later." Here are some things to check.

- Check that AI Search is enabled.
- Check that your Agentic Workflow and AI Agent(s) are active and connected.
- Check that your triggers are active.
- Check your AI Agent's "Proficiency". This determines what your AI Agent is able to do.
    1. To check your AI Agent's proficiency, add it as a column to the list of AI Agents in the Studio. Navigate to the **AI agents** sub-tab and click **View all** to open the list of available AI Agents.
    2. Click the **Update Personalized List** settings button.
        
        [LuisEstefano_42-1753049647682.png](https://www.servicenow.com/community/image/serverpage/image-id/457184i4CB978E2E6F1E6C7/image-size/medium?v=v2&px=400)
        
    3. Add the **Proficiency** column, then click **Apply**.You can then view and mouse over the Proficiency of your AI Agent. Make sure it's detailed and matches the intended goal and its ability to address the agentic workflow's Objective Template. The Proficiency is generated by the LLM and can't be modified.
        
        [LuisEstefano_31-1756077927881.png](https://www.servicenow.com/community/image/serverpage/image-id/465064i1B2104A2630599C8/image-size/large?v=v2&px=999)
        

---

**Conclusion**

In this lab, we covered the basics of AI Agent configuration on the ServiceNow platform:

- Tested a Agentic Workflow and AI Agent
- Duplicated and configured an Agentic Workflow
- Duplicated and configured an AI Agent
- Set up Trigger conditions
- Tested an Agentic Workflow in the Now Assist Panel

Ref: [Getting Started with ServiceNow Agentinc Workflow & AI Agents](https://www.servicenow.com/community/developer-articles/get-familiar-with-agentic-workflows-amp-ai-agent/ta-p/3326559)

## Related

- [[Agentic Workflow & AI Agents]]
- [[Agentic Workflow & AI Agents – Tips]]
- [[Best Practices for Creating AI Agent Workflows]]
- [[AI Agent tools – Getting the most out of your agen]]
- [[Introducing AI Agents and Quick Start Guide]]
- [[AI Agents & Agentic Workflows — Reference Compilat]]