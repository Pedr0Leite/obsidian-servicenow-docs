---
aliases:
  - "Now Assist Skill Kit - Knowledge Article Categoriz"
area: "AI & VA"
source: notion-export
tags:
  - now-assist
  - skill-kit
  - genai
  - knowledge-management
  - flow-designer
---

# Now Assist Skill Kit - Knowledge Article Categorization

**Overview**

Now Assist Skill Kit (NASK) allows you to create new generative AI skills using the generic Now LLM or your own LLM.  NASK has been designed to easily manage and integrate new skills into the ServiceNow platform via a UI Action and soon into the Now Assist Panel. With NASK you define the input data, leverage tools to process the data, activate the new skill, and deploy it to the platform (see below).

[johlee_0-1730236671212.png](https://www.servicenow.com/community/image/serverpage/image-id/398167iC6F1E010C43B9753/image-dimensions/707x348/is-moderation-mode/true?v=v2)

**Using NASK to Automatically Categorize KCS KB Articles**

A key challenge in building and maintaining an effective Knowledge Base for diverse self-service use cases is achieving accurate content categorization and tagging. Properly tagging articles based on their content and aligning them with a broader taxonomy enables users to quickly find relevant information, improving the self-service experience and lightening the load on support teams. Moreover, well-organized content prepares your organization for future AI-driven use cases, such as use cases relying on Retrieval Augmented Generation and advanced search patterns, unlocking greater value from your knowledge assets.

Given this challenge, Large Language Models (LLMs) are highly effective at interpreting unstructured text and extracting meaning. We can harness this capability by using NASK to process unstructured [Knowledge Centered Service](https://docs.servicenow.com/bundle/xanadu-servicenow-platform/page/product/knowledge-management/concept/knowledge-centred-configuration.html) (KCS) KB article data and allowing the Now LLM to intelligently categorize the content by selecting from predefined categories within our Knowledge Base…effectively automating the categorization of KCS KB articles at massive scale (see high level flow below).

[johlee_1-1730236712620.png](https://www.servicenow.com/community/image/serverpage/image-id/398168i12618BE0D5A03467/image-dimensions/745x420/is-moderation-mode/true?v=v2)

**Below is what the finished product looks like:** 

 **1.** The UI action calls the custom NASK skill.

 **2.** Now LLM predicts category given KCS KB article text.

  **3.** If Now LLM output matches existing category, update the category field. If no category match can be made, do not update category field.

[johlee_2-1730236777391.png](https://www.servicenow.com/community/image/serverpage/image-id/398169iB744B990463AA3EE/image-dimensions/717x190/is-moderation-mode/true?v=v2)

**You will need the following to implement this use case in your instance:**

- Purchase any Now Assist SKU or request a Now Assist evaluation instance from your ServiceNow Account team.
- Upgrade the instance to the latest version of Xanadu and install any of the Now Assist plugins.
- Configure Now Assist Skill Kit by following the steps in our [documentation.](https://docs.servicenow.com/bundle/xanadu-intelligent-experiences/page/administer/now-assist-skill-kit/concept/now-assist-skill-kit-landing.html)
- To use Now Assist Skill Kit you will need to grant yourself **sn_skill_builder.admin** role.
- Since we will be analyzing surveys the **kb_knowledge** and **kb_category** tables will need to be populated with KCS articles and corresponding article text.

**Lab Flow:**

There are nine phases to build a custom skill with NASK that automatically categorizes KCS KB articles.

1. **Phase 1 –** Review knowledge base and gather which categories we want the Now LLM to use to categorize KCS KB article text.
2. **Phase 2 –** Identify and review a specific KCS KB article that we can use as a test record for the custom skill.
3. **Phase 3 –** Using data from **Phase 1**, build a Subflow that automatically gathers the categories we want the Now LLM to use.
4. **Phase 4 –** Build the custom skill using NASK.
5. **Phase 5 –** Testing the custom skill.
6. **Phase 6 –** Deploying the custom skill
7. **Phase 7 –** Activating the custom skill
8. **Phase 8 –** See custom skill in action, on a single KCS KB article
9. **Phase 9 –** See custom skill in action, on a list of KCS KB article

**Phase 1: Review knowledge base and gather categories for use in NASK**

First, we need to identify, review, and collect information about 1) the knowledge base and 2) the categories contained in this knowledge base for NASK use. The purpose is to capture a finite list of categories that the Now LLM can choose from given the text of a KCS knowledge base article.

1. Type **kb_category.list** into the filter navigator.

2. Identify and review which knowledge base you intend to use. For this demonstration I will use: **Knowledge Base: IT** in the Parent ID column.

[johlee_54-1730237110998.png](https://www.servicenow.com/community/image/serverpage/image-id/398181iA0E324115F229C47/image-dimensions/713x275/is-moderation-mode/true?v=v2)

3. Identify which knowledge base you intend to use in the Parent ID column. For this demonstration I will use: **Knowledge Base: IT**.

4. Next, right click on the **Knowledge Base IT** field of a record and click **Show Matching**.

[johlee_55-1730237110999.png](https://www.servicenow.com/community/image/serverpage/image-id/398183iA4DCC653AA27F067/image-dimensions/763x164/is-moderation-mode/true?v=v2)

5. Make note of the Parent ID (which should be a combination of characters and numbers) after clicking **Show Matching.** Using the lab example, the Parent ID for **Knowledge Base: IT** is **a7e8a78bff0221009b20ffffffffff17**. Store this ID for use later.

[johlee_56-1730237111000.png](https://www.servicenow.com/community/image/serverpage/image-id/398182iBEE6C224DECD5F2C/image-dimensions/722x228/is-moderation-mode/true?v=v2)

6. We also need to add the categories for another knowledge base. To do this, I go to the list of kb_category and repeat the above steps. For this lab, click **Show Matching** once more and note the Parent ID for **Knowledge Category: Operating Systems**: **9d4737cbff0221009b20ffffffffff33**. Store this ID for use later.

[johlee_57-1730237111000.png](https://www.servicenow.com/community/image/serverpage/image-id/398184i557256A7AFE4DBCA/image-dimensions/757x89/is-moderation-mode/true?v=v2)

**Phase 2: Identify and review KCS knowledge article for use in NASK** 

1. Type **kb_knowledge.list** into the filter navigator.

2. Filter the list of knowledge articles so that class is KCS Article.

[johlee_58-1730237111001.png](https://www.servicenow.com/community/image/serverpage/image-id/398185i1D817E1CC5EE0D7D/image-dimensions/715x156/is-moderation-mode/true?v=v2)

3. Identify KCS knowledge article(s) you intend to use as test records for NASK.  The ideal candidate record should have Knowledge base as a required field. Additionally, Category should be (empty) or incorrect, and detailed text descriptions in the following fields:

**Short description**, **Issue**, **Environment**, **Cause**, and **Resolution**.

If you don’t have a KCS knowledge article to use, you can use the following example (which we will use in this lab):

```
Knowledge base:IT
Category:(empty)
Short Description:How do I set the correct date and time on my Mac?
Environment:Mac
Cause:The date or time might need to be set again, or it might be using custom format.
Resolution:

Check Date & Time preferences
1. Choose Apple menu > System Preferences, then click Date & Time.
2. In the Date & Time pane, make sure that “Set date and time automatically” is selected and your Mac is connected to the Internet. Your Mac can then get the current date and time from the network time server selected in the adjacent menu.

To make changes, click the lock to open, then enter your administrator password. If you do not have elevated access, contact IT for assistance.

If you don't have an internet connection, or you want to set the date and time manually, deselect “Set date and time automatically.” You can then click today’s date on the calendar, drag the clock’s hands to the correct time, or use the fields above the calendar and clock to enter the date and time. Then click Save.
```

4. Note down the number of the KCS knowledge article you are using. For this demonstration, we are using **KB0050013.** Store this number for use later.

[johlee_59-1730237111001.png](https://www.servicenow.com/community/image/serverpage/image-id/398186i24CC42F512D17302/image-dimensions/699x362/is-moderation-mode/true?v=v2)

**Phase 3: Build a Subflow to collect relevant Knowledge Base categories**

1. Navigate to **All > Flow Designer**. Click **New > Subflow**.

[johlee_60-1730237111002.png](https://www.servicenow.com/community/image/serverpage/image-id/398187iE82AE271C0F69046/image-dimensions/192x293/is-moderation-mode/true?v=v2)

2. If you have Now Assist for Creator installed, you have the option to build your Subflow with Now Assist. For today, however, we will build it ourselves. Click the **Build on your own** tab.

3. Name your Subflow: Get IT Knowledge Base Categories. Set the Application to: Global. Click, **Build subflow**.

[johlee_61-1730237810226.png](https://www.servicenow.com/community/image/serverpage/image-id/398188iBA457E32717022E5/image-dimensions/707x365/is-moderation-mode/true?v=v2)

4. Click Select to create the inputs & outputs of your Subflow. Click the plus icon next to **Outputs**.

[johlee_62-1730237858961.png](https://www.servicenow.com/community/image/serverpage/image-id/398189i69F9562F73935087/image-dimensions/645x244/is-moderation-mode/true?v=v2)

5. Set the label of your output as **Compiled IT KB Categories**, then click **Done**.

[johlee_63-1730237889207.png](https://www.servicenow.com/community/image/serverpage/image-id/398190iDB0A79409BC41F8D/image-dimensions/705x362/is-moderation-mode/true?v=v2)

6. Open the More Actions menu in the upper right corner of the screen as denoted by the three dots (…), then click **Flow Variables**.

[johlee_64-1730237889207.png](https://www.servicenow.com/community/image/serverpage/image-id/398191i774677631E201482/image-dimensions/305x280/is-moderation-mode/true?v=v2)

7. Click the plus icon to add a new flow variable. Set the label to **Compiled IT KB Categories** as a string, then click **Save**.

[johlee_65-1730237889208.png](https://www.servicenow.com/community/image/serverpage/image-id/398192i2D16A880164F4FF6/image-dimensions/736x378/is-moderation-mode/true?v=v2)

8. Click **Add an Action, Flow Logic, or Subflow.** Select **Action**, then type **Look up records** in the search bar. Click on **ServiceNow Core**, then finally click on the **Look Up Records** action.

[johlee_66-1730237889208.png](https://www.servicenow.com/community/image/serverpage/image-id/398194iD6F959E769C41F05/image-dimensions/600x249/is-moderation-mode/true?v=v2)

9. Populate the action as seen below, then click **Done** (we are populating with the Parent ID’s we collected in phase 2):

- **Table**: Knowledge Category [kb_category]
- **Conditions**: Parent ID is **a7e8a78bff0221009b20ffffffffff17** OR Parent ID is **9d4737cbff0221009b20ffffffffff33**.

[johlee_67-1730237889209.png](https://www.servicenow.com/community/image/serverpage/image-id/398193iA0A3FEC094A9E6FE/image-dimensions/710x283/is-moderation-mode/true?v=v2)

10. Click on **Flow Logic**, then select **For Each**. 

[johlee_68-1730237889209.png](https://www.servicenow.com/community/image/serverpage/image-id/398195i0FD7DD385FE9A933/image-dimensions/668x276/is-moderation-mode/true?v=v2)

11. Drag and drop the **kb_category Records** data pill into the Items field, then click **Done**.

[johlee_69-1730237889210.png](https://www.servicenow.com/community/image/serverpage/image-id/398197i549C3332777C65F6/image-dimensions/717x357/is-moderation-mode/true?v=v2)

12. Click the small plus icon under the For Each loop and select **Flow Logic** again. This time, click **Set Flow Variables**.

[johlee_70-1730237889211.png](https://www.servicenow.com/community/image/serverpage/image-id/398196i506F7CADFF810D35/image-dimensions/534x194/is-moderation-mode/true?v=v2)

13. Click the plus icon, then set the flow variable to Compiled IT KB Categories. Click the script icon next to the text box that appears to make a script field appear. Copy and paste the below code into the area:

```jsx
var result = fd_data.flow_var.compiled_it_kb_categories

+ fd_data._2__for_each.item.label

+ "\n";

return result;
```

[johlee_71-1730238144882.png](https://www.servicenow.com/community/image/serverpage/image-id/398198i8AE726D0D3BEAEF0/image-dimensions/692x337/is-moderation-mode/true?v=v2)

14. Click **Done**.

15. Next, add another Flow Logic item, and click **Assign Subflow Outputs**

[johlee_72-1730238193896.png](https://www.servicenow.com/community/image/serverpage/image-id/398199iBDCBE3F751B5F5AA/image-dimensions/676x341/is-moderation-mode/true?v=v2)

16. Set the Subflow output variable to be Compiled IT KB Categories. Drag and drop the flow variable with the same name into the data field. Click **Done**.

[johlee_73-1730238212639.png](https://www.servicenow.com/community/image/serverpage/image-id/398201iE1FBAB26D41D6523/image-dimensions/739x373/is-moderation-mode/true?v=v2)

17. Click **Save**, then **Run Test**. In the module that appears, click **Run Test** again.

[johlee_74-1730238212640.png](https://www.servicenow.com/community/image/serverpage/image-id/398200iD2C19D07E5D19BCD/image-dimensions/531x273/is-moderation-mode/true?v=v2)

18. Click on the **Assign Subflow Outputs** box to review the action that took place. Click on the Runtime Value to see the list of IT Knowledge Base Categories that were returned. 

[johlee_75-1730238212641.png](https://www.servicenow.com/community/image/serverpage/image-id/398202i85A0F8B7311EAC6A/image-dimensions/730x368/is-moderation-mode/true?v=v2)

19. Once you validate the categories returned by the Subflow test, return to your Subflow by clicking its name in the tabs at the top. Click **Publish** in the top right of the screen. If you get a message stating that this is associated to 0 flows, please ignore it and publish it anyway.

Congratulations!

![:party_popper:](https://www.servicenow.com/community/s/html/@07C9E2A98E52617ED4037524D1BEE458/emoticons/1f389.png)

![:party_popper:](https://www.servicenow.com/community/s/html/@07C9E2A98E52617ED4037524D1BEE458/emoticons/1f389.png)

We now have all the input data we need to run this custom skill.

**Phase 4: Build the custom skill**

1. Navigate to **All > Now Assist Skill Kit > Home** from the filter navigator.

2. Click **Create new skill**.

[johlee_77-1730238405689.png](https://www.servicenow.com/community/image/serverpage/image-id/398204i0C677881B108CEDF/image-dimensions/656x440/is-moderation-mode/true?v=v2)

3. Name the skill IT KCS Knowledge Categorizer. In this lab, we will be using the Now LLM service to complete our task, so ensure the Default provider and Provider API values are both set to Now LLM Generic. Click **Create new skill**.

[johlee_78-1730238430256.png](https://www.servicenow.com/community/image/serverpage/image-id/398205i096581B2CCE1964D/image-dimensions/692x439/is-moderation-mode/true?v=v2)

4. Add a new skill input by clicking the plus icon next to it. This is where we add the reference to a knowledge article to use within the prompt. 

[johlee_79-1730238480701.png](https://www.servicenow.com/community/image/serverpage/image-id/398206i4BEC22D6FCC33955/image-dimensions/447x225/is-moderation-mode/true?v=v2)

5. Populate the skill input form with (screenshot below):

**Datatype:** Record

**Table name:** kb_knowledge

**Name:** Knowledge

**Choose test record:** KB0050014 (the number of the knowledge article we took note of in phase 2).

Once complete, click **Add skill input**.

[johlee_80-1730238480702.png](https://www.servicenow.com/community/image/serverpage/image-id/398207i8B8ED8038F397F4F/image-dimensions/512x364/is-moderation-mode/true?v=v2)

6. Next to Tools, click the plus icon. 

[johlee_81-1730238480703.png](https://www.servicenow.com/community/image/serverpage/image-id/398208i587B5129D89F01CC/image-dimensions/353x243/is-moderation-mode/true?v=v2)

7. Populate the form as seen below. Note the lack of spaces in the Name, and the resource is the name of our published Subflow, i.e., Get It Knowledge Base Categories. 

[johlee_82-1730238480704.png](https://www.servicenow.com/community/image/serverpage/image-id/398210iD917EB138F2D9241/image-dimensions/721x364/is-moderation-mode/true?v=v2)

8. [Optional] Click the Pencil Icon   next to the prompt name to rename the prompt. We are renaming it to Knowledge Categorizer here. Click **Save changes**.

[johlee_83-1730238480704.png](https://www.servicenow.com/community/image/serverpage/image-id/398209i19C85C290444A19F/image-dimensions/24x21/is-moderation-mode/true?v=v2)

[johlee_84-1730238480705.png](https://www.servicenow.com/community/image/serverpage/image-id/398211i57AB0C71B6C7DB84/image-dimensions/763x385/is-moderation-mode/true?v=v2)

9. In the prompt field, remove the template text and replace it with the following:

```
You are tasked with classifying input text into one of the following categories:

Each category represents a distinct type of content. Based on the content of the input text,
identify which category best describes it. Ensure that the categorization is based on clear
patterns or keywords in the text that match the defining characteristics of each category.

Instructions:
Review the input text. Choose the category that best matches the content. If the input text
could fit into more than one category, choose the most appropriate one based on the primary
theme.

Example Inputs:
Input: "Title: Can't login to my windows laptop."
Category: Windows

Input: "Issue: Zoom keeps crashing when I start a meeting"
Category: Zoom

Now, classify the following Knowledge Base Article:

Title:
Issue:
Environment:
Cause:
Resolution:

Return only the category. No other text.
```

10. Click in the prompt field after the string “...one of the following categories:”. Click on **Insert inputs**, GetITKnowledgeBaseCategories **>** Compiled IT KB Categories. 

[johlee_85-1730238480707.png](https://www.servicenow.com/community/image/serverpage/image-id/398212iE37751083540713F/image-dimensions/741x374/is-moderation-mode/true?v=v2)

11. Repeat the above insert inputs process to add the corresponding text fields to the following fields defined in the prompt:

```
Title:
Issue:
Environment:
Cause:
Resolution:
```

**Note:** because we are using KCS Knowledge Articles, when inserting inputs, ensure you select KCS Article **>** short description and so on.

[johlee_86-1730238827183.png](https://www.servicenow.com/community/image/serverpage/image-id/398213iA15B13FAB1AF279D/image-dimensions/739x373/is-moderation-mode/true?v=v2)

12. The completed process prompt should look like the screenshot below. Notice that the Knowledge Base article **Short Description** field is inserted into the **Title** section:

```
You are tasked with classifying input text into one of the following categories:
{{GetITKnowledgeBaseCategories.compiled_it_kb_categories}}

Each category represents a distinct type of content. Based on the content of the input text,
identify which category best describes it. Ensure that the categorization is based on clear
patterns or keywords in the text that match the defining characteristics of each category.

Instructions:
Review the input text. Choose the category that best matches the content. If the input text
could fit into more than one category, choose the most appropriate one based on the primary
theme.

Example Inputs:
Input: "Title: Can't login to my windows laptop."
Category: Windows

Input: "Issue: Zoom keeps crashing when I start a meeting"
Category: Zoom

Now, classify the following Knowledge Base Article:

Title:{{knowledge.ref_kb_template_kcs_article.short_description}}
Issue:{{knowledge.ref_kb_template_kcs_article.kb_issue}}
Environment:{{knowledge.ref_kb_template_kcs_article.kb_environment}}
Cause:{{knowledge.ref_kb_template_kcs_article.kb_cause}}
Resolution:{{knowledge.ref_kb_template_kcs_article.kb_resolution}}

Return only the category. No other text.
```

13. Click **save.**

# **Phase 5: Testing the custom skill**

1. Scroll down to the Test prompt section. Click **Run tests**.

[johlee_87-1730238827184.png](https://www.servicenow.com/community/image/serverpage/image-id/398214i73BEB83FBEE0FC79/image-dimensions/515x201/is-moderation-mode/true?v=v2)

2. Verify that the LLM's output is correct. If you desire, you can iterate upon the provided prompt. However, for our purposes, the skill correctly categorizes the KCS Knowledge article accurately.  

[johlee_88-1730238827185.png](https://www.servicenow.com/community/image/serverpage/image-id/398215iCE16634C4A2F3474/image-dimensions/732x370/is-moderation-mode/true?v=v2)

3. To verify if information from your skill inputs is being brought in correctly, click on the tab named **Grounded prompt**. You will see the input that was delivered to the LLM, including the categories and knowledge article text.

[johlee_89-1730238827186.png](https://www.servicenow.com/community/image/serverpage/image-id/398217i0168D02F556CCF5F/image-dimensions/722x285/is-moderation-mode/true?v=v2)

4. Once content with the output of your skill, click **Finalize prompt**.

5. Once content with the output of your skill, click **Finalize prompt**.

[johlee_91-1730239244390.png](https://www.servicenow.com/community/image/serverpage/image-id/398220iDFAAE3E51241A349/image-dimensions/463x177/is-moderation-mode/true?v=v2)

# 

# **Phase 6: Deploy the custom skill**

1. Click on **Skill settings** at the top of the page. 

[johlee_92-1730239266978.png](https://www.servicenow.com/community/image/serverpage/image-id/398222i18B62FCA286BC677/image-dimensions/677x342/is-moderation-mode/true?v=v2)

2. Click on the option named **Deployment Settings**.

3. Underneath the workflow header, set the value to **Other**, if not already selected.

4. Tick the option marked **UI Action** and set the table to **Knowledge** (to do so, type in **kb_knowledge** and scroll down until you find it.) 

[johlee_93-1730239266979.png](https://www.servicenow.com/community/image/serverpage/image-id/398223iDAA04BEEDA60C304/image-dimensions/725x366/is-moderation-mode/true?v=v2)

5. Click **Create UI Action**, then **Link to UI Action** once it appears. 

[johlee_94-1730239266980.png](https://www.servicenow.com/community/image/serverpage/image-id/398221iDBC7396C16BB8123/image-dimensions/243x193/is-moderation-mode/true?v=v2)

6. A new window containing your UI Action will appear. Change the value in the **Name** field to **IT KCS Knowledge Categorizer**.

[johlee_95-1730239266980.png](https://www.servicenow.com/community/image/serverpage/image-id/398225iF4BB282A46E8D18B/image-dimensions/533x309/is-moderation-mode/true?v=v2)

7. Additionally, check both the **Form button** and **List banner buttons** to have the **UI action** show up in both a form (i.e., a specific KCS KB article record) and list (i.e., a list of KCS KB article records).

[johlee_96-1730239266981.png](https://www.servicenow.com/community/image/serverpage/image-id/398224i8A7EDE1EDACF9D54/image-dimensions/616x380/is-moderation-mode/true?v=v2)

8. In the script field, replace everything from the try statement and below with the code provided below.

[johlee_97-1730239266981.png](https://www.servicenow.com/community/image/serverpage/image-id/398226i1693CB9D27193D75/image-dimensions/691x452/is-moderation-mode/true?v=v2)

```jsx
try {

    // Capture the original category

    var originalCategoryGR = new GlideRecord('kb_category');

    originalCategoryGR.get(current.kb_category);  // Fetch the current category record

    var originalCategory = originalCategoryGR.getValue('label');  // Store the original category label

    // Execute the request and get the skill's response

    var output = sn_one_extend.OneExtendUtil.execute(request)['capabilities'][request.executionRequests[0].capabilityId]['response'];

    // Parse the model output to extract category-related information

    var modelOutput = JSON.parse(output).model_output;

    // Populate the category field using the output of the model

    var categorySysId = getCategorySysIdFromModelOutput(modelOutput); // custom function to resolve category from output

    if (categorySysId) {

        current.kb_category = categorySysId;  // Set the category to the resolved sys_id

        current.update();  // Save the changes to the KB article

        // Inform the user of the original category and the updated category with the record number

        gs.addInfoMessage("The category of record " + current.getValue('number') + " has been updated from '" + originalCategory + "' to '" + modelOutput + "'. Please review the update for accuracy.");

    } else {

        gs.addErrorMessage('No matching category found for the model output for record ' + current.getValue('number') + '. Please review the output or adjust manually.');

    }

} catch(e) {

    gs.error(e);

    gs.addErrorMessage('Something went wrong while executing the skill for record ' + current.getValue('number') + '. Please try again.');

}

// Custom function to get the sys_id of the category from the model output

function getCategorySysIdFromModelOutput(modelOutput) {

    // Assuming the model output contains the name or label of the category

    var categoryName = modelOutput.trim();  // Adjust based on actual model output structure, trim to remove extra spaces

    // Query the KB Category table (kb_category) to get the sys_id of the matching category

    var kbCategoryGR = new GlideRecord('kb_category');

    kbCategoryGR.addQuery('label', categoryName);

    kbCategoryGR.query();

    if (kbCategoryGR.next()) {

        return kbCategoryGR.getValue('sys_id');

    } else {

        return null; // Return null if no match is found

    }

}
```

9. Click **Update** to save the record.

10. Return to your skill within Now Assist Skill Kit.

11. In the module that opens, tick the box containing your finalized prompt, then click **Publish**.

# **Phase 7: Activate the custom skill**

1. Navigate to Now Assist Admin from within the filter navigator.

[johlee_103-1730239573592.png](https://www.servicenow.com/community/image/serverpage/image-id/398237i89C789EE4239DE3B/image-dimensions/427x223/is-moderation-mode/true?v=v2)

2. Click on **Now Assist Features**, then **Other** to find your published skill.

[johlee_104-1730239586285.png](https://www.servicenow.com/community/image/serverpage/image-id/398238iA37756C7DAB97FB8/image-dimensions/735x467/is-moderation-mode/true?v=v2)

3. Click on the tab named **Available** to find your published skill. Click **Activate skill**.

[johlee_105-1730239597063.png](https://www.servicenow.com/community/image/serverpage/image-id/398239iD450E5F8156EFC3E/image-dimensions/741x374/is-moderation-mode/true?v=v2)

4. Set the Display trigger to **true**, then click **Save and continue**.

[johlee_101-1730239499756.png](https://www.servicenow.com/community/image/serverpage/image-id/398234i5119D3AE6627EE08/image-dimensions/749x380/is-moderation-mode/true?v=v2)

5. Review the next page, then click **Activate**. 

[johlee_102-1730239499756.png](https://www.servicenow.com/community/image/serverpage/image-id/398235i86B3EFC875A3B09E/image-dimensions/751x381/is-moderation-mode/true?v=v2)

6. Dismiss the message stating confirmation of activation.

# **Phase 8: See custom skill in action, on a single KCS KB article**

1. Type **kb_knowledge.list** into the filter navigator. Find the knowledge article you wish to run your custom skill on and open the record.

2. Click the **UI Action** we created – you may have named it something else.

3. Woohoo! Your KCS KB article should be automatically categorized!

[johlee_107-1730239684386.png](https://www.servicenow.com/community/image/serverpage/image-id/398241iC98110945F1DDED2/image-dimensions/773x391/is-moderation-mode/true?v=v2)

# **Phase 9: See custom skill in action, on a list of KCS KB article**

1. Type **kb_knowledge.list** into the filter navigator.

2. Using the list filter, select Class is KCS and click **Run** to get a list of only KCS KB articles.

3. Select the articles you wish to run the custom skill on. Click the **UI action** we just created.

4. Congrats! Your list of KCS KB articles should be automatically categorized!

[johlee_108-1730239782098.png](https://www.servicenow.com/community/image/serverpage/image-id/398243i6BBB8D92A3DD9E4B/image-dimensions/720x360/is-moderation-mode/true?v=v2)

**Future improvement ideas**

The purpose of this lab guide is to show you what is possible with NASK. Of course, the skill we built is far from production ready. However, if you intend to continue developing this custom skill, here are some ideas for improvement:

- Additional UI sugar and feedback (e.g., loading screen) when user clicks the UI action button.
- Create a more generalizable skill to be used with any kind of KB article.
- Create additional governance measures, such as getting a human to approve LLM outputs.
- Automatically trigger the NASK skill when any new KB is submitted for review.

**Future use case ideas**

Building on this demonstration and generalizing the LLM categorization use case pattern, we can extend the Now Assist Skill Kit (NASK) to other areas like IT, SecOps, HRSD, and CSM. Here are some use case ideas to spur your creativity and experiment with NASK. Please let us know if you build any of them!

**IT**

- Categorization of incidents based on text description data.
- Assignment of requests based on text description data.

**IT Operations**

- Summarization of alerts, to alert groups, to many alert groups based on description and other data.
- Categorization of these summarizations to assign work to the right team.

**Security**

- Categorization of security events, incidents, vulnerabilities based on text description data.

**Customer Service**

- Assignment of customer case to correct customer service or another team.

**HR**

- Assignment of HR case to correct team.

## Related
- [[Now Assist case Summaization in custom tables]]
- [[Now Assist for CSM - Resolution Notes Generation]]
- [[Now Assist for ITSM Handling Customization Scenari]]

- [[Now Assist]]
- [[Build Custom AI Skills with Now Assist Skill Kit S]]
- [[Introducing Custom Record Summarization Now Assist]]
- [[Now Assist in AI Search]]
- [[GenAI]]