---
aliases:
  - "Now Assist for ITSM Handling Customization Scenari"
area: "AI & VA"
source: notion-export
tags:
  - now-assist
  - genai
  - itsm
  - summarization
  - troubleshooting
  - customization
---

# Now Assist for ITSM: Handling Customization Scenarios for Resolution Notes Generation

With Now Assist ITSM’s [Resolution Notes Generation](https://docs.servicenow.com/bundle/washingtondc-it-service-management/page/product/now-assist-itsm/task/resolve-incident-now-assist.html) capability, agents can quickly generate resolution summary based on the current incident’s data from targeted input fields. When an incident state is changed to Resolve state, the system triggers and displays the resolution summary in a popup which the agent can review, update, and use to resolve the incident.

This works great out of the box, however when customers have customized their resolution workflows around changing the incident state to Resolve, such use cases may need to be handled for Now Assist ITSM’s Resolution Notes Generation capability to function as expected.

We will highlight some of these scenarios based on findings in Vancouver and Washington releases along with some tips to resolve such use cases.

- ********** ***IMPORTANT DISCLAIMER AROUND CUSTOMIZATIONS*** ***********

*In general, customizations are not officially supported, but often need to be worked around to get the needed functionality. This document attempts to help with handling of a few customization scenarios.   Also note that custom tables inherited from OOTB incident table is not supported, however since it does work in most cases, we have included here, but only as tips to work around the use case.*

- ***********************************************************************************

**Scenario 1: Incident’s Resolve UI Action button is custom**

**Tips to Work around:**

As part of the Now Assist ITSM plugin activation, by design the install will deactivate the custom Resolve UI Action and activate the out of the box Resolve UI Action.  When working with customized Resolve UI Actions, ideally, all customizations should be brought over to a duplicated copy of the out of box Resolve UI Action with ActionName= resolve_incident_gen_ai.  Further after upgrading to each family or patch release, it is up to customers to ensure any needed out of the box updates for the UI Action are brought over to the customized one, otherwise there is potential for unexpected outcomes from such customizations.

To revert to the custom UI Action towards ensuring Resolution Notes get generated, below guidelines can be followed:

1. Deactivate the out of the box UI Action where:
    - Name=Resolve
    - Table=incident
    - ActionName= resolve_incident_gen_ai
2. Changes for handling custom Resolve UI Action
    1. Alternative 1 (recommended)
        - Duplicate the out of the box UI Action where:
            - Name=Resolve
            - Table=incident
            - ActionName= resolve_incident_gen_ai
        - Bring over customizations into this duplicated Resolve UI Action and ensure it is active.
        - Leave the original custom Resolve UI action deactivated
    2. Alternative 2 (less preferred, but should work in most cases)
        - Re-activate the custom Resolve UI Action, making sure it has below code in the very beginning of the script:
            - **********************
            
            *//Set the 'State' value to 'Resolved'*
            
            *g_form.setValue('state', 6);*
            
            *g_form.setValue('incident_state', 6);*
            
            *gsftSubmit(null, g_form.getFormElement(), 'sysverb_update');*
            
            *//Call the UI Action and skip the 'onclick' function*
            
            *gsftSubmit(null, g_form.getFormElement(), '<ACTION NAME>');*
            
            *//MUST call the 'Action name' set in this UI Action*
            
            **********************
            
3. ***Client Script changes***: As Maint user (NOW Support case will be needed if Maint access is not available), duplicate the out of box onChange Client Script: ***Record Resolution GenAI – Incident*** using Insert and Stay and activate the newly created client script making sure its set to Active.

This should allow the Resolution Notes to be generated and display in the popup as expected. In case we still run into issues, refer to the Appendix section of this document to rule out some known issues by applying the suggested workaround if needed.

**Scenario 2: Incident table is custom and extended from out of the box incident table (with or without a custom resolve UI Action button)**

**Tips to Work around:**

While custom inherited incident tables are not supported, customers that are using their own custom table for incident extending from out of the box incident table can follow the tips provided in this section to configure Resolution Notes Generation for such a custom table.

1. ***Client Script Update***: As Maint user (NOW Support case will be needed if Maint access is not available), duplicate the out of box onChange Client Script: Script ‘***Prepare form view for resolve modal***’ using Insert and Stay and point the Table field to the custom Incident table.
2. **Now Assist Skill Config Table Updates:**
    1. Go to ***sn_nowassist_skill_config*** table and open record where:
        - ***Name***=Resolution notes generation **
        - ***Skill family***=Incident (or Incident Assist
            
            [nilimadesai_0-1717025971970.png](https://www.servicenow.com/community/image/serverpage/image-id/360796i39B5A7E069C271C9/image-dimensions/672x273?v=v2)
            
    2. Create a new ***Now Assist Skill Configs*** (***sn_nowassist_skill_config*** table***)*** record and set the fields similar to the existing OOB record we just opened. Update the name field to easily identify the record is for the custom incident table and save the record.
    3. From the newly created ***Now Assist Skill Configs*** record’s ***Now Assist Skill Config Var Sets*** Related List, open the list in a new tab so that the ***New*** UI Action is available.
    4. Also open the ***Choose Input*** record from the ***Now Assist Skill Config Var Sets*** Related List in a separate tab***.***
    5. Create a new ***sn_nowassist_skill_config_var_set** record for the **sn_nowassist_skill_config*** record we created and set its field values same as the out of box ***Choose Input*** record for ***sn_nowassist_skill_config*** table and set fields as per below and save the record:
        - Name: Choose Input
        - Skill Config: <Skill Config record name created in Step2 above>
        - Config Type: Record Resolution Template
        - For Variables:
            - ***Input: <custom Incident*** table name>
            - Input Fields: Short Description, Description, Additional Comments, Work Notes
            - Resolution Notes Output Field: Resolution Notes
3. In case the Resolve UI Action is custom versus being extended from out of box UI Action, then follow all the guidelines outlined in Scenario 1: Resolve UI Action button is custom above to accommodate the custom UI Action.

**Scenario 3: There are additional mandatory fields (than out of the box) for setting the Incident state to Resolve**

**Tips to Work around:**

When there are additional mandatory fields enabled as a pre-requisite for setting the incident state to Resolve, it is best to add such additional fields to the Resolution popup. This also facilitates a good user experience by allowing all such mandatory fields to be reviewed and updated as part of the resolution.

This can be accomplished by configuring the form layout for either of the 2 views depending in which UI we are in, to include such mandatory fields. :

- **UI16:** ***ui16_incident_resolve_modal*** view
- **SOW:** ***sow_incident_resolve_modal*** view

**Scenario 4a: Resolve UI Action does not display in Workspace UI, but shows up in UI16**

**Tip to Work around:**

- While this may not work in all environments with this issue, ensure 'Format for Configurable Workspace' is checked in the Resolve UI action

**Scenario 4b: There are 2 Resolve UI Action buttons showing up in SOW**

Check in sys_ui_action and sys_declarative_action_assignment records where table is incident. In SOW, if the *Resolve* sys_ui_action record has the *Workspace Form Button* toggle enabled, then it will be displayed in workspace UI. There may also be a sys_declarative_action_assignment record that is Active and Enabled.

In such scenarios, the *Workspace Form Button* toggle for the appropriate *Resolve* sys_ui_action record can be unchecked so that only the sys_declarative_action_assignment record handling Resolution Notes Generation skill is displayed in SOW.

**Scenario 5: Resolution Notes clears out when Resolution Code or other custom fields on Resolution popup are updated after initial LLM prediction**

After the initial LLM prediction is made for Resolution Notes, the resolution code and resolution notes fields are populated on the Resolution popup. Once initially populated, if the Resolution code value is modified by agent, in out of box configuration, the Resolution Note is left unchanged. However, many customers may have built in mechanisms to clear out the Resolution note based on updated resolution code or other values.

**Tips to Work around:**

- Check existing onChange Client scripts or other mechanisms that clear out Resolution notes value to avoid LLM predicted values from getting cleared out.

**Scenario 6: Resolved choice value for Incident table's state and incident_state field is anything other than *6***

The OOB choice value for Resolved state and incident_state fields on incident table is ***6.*** Customers using a different value than 6 will need to handle this in the ***Resolve*** UI Action with Action Name of  ***resolve_incident_gen_ai.***

For Workspace UI, in case Declarative Actions are used for Resolve action, then this will also need to be handled within the Declarative Actions.

**Scenario 7: Configuring Additional Role based access for Resolve UI Action** **in Service Operations Workspace** 

The below configuration explains the use case where customers would like to separate resolution note generation functionality in Service Operations Workspace. The recommended approach creates two UI Actions. One visible to users with the defined role linked to the resolution generation skill and another visible to users who do not have the role. Service Operations Workspace uses UX form actions and Screens to manipulate the visibility of buttons.

The below steps show how to configure the following actions and screens for role-based criteria:

1. Go to the [sys_ux_form_action] table and duplicate the record where [Declarative Action = sow_incident_resolve]. Call the new record *Resolve-genai*.
2. Also duplicate the declarative action {[[sys_declarative_action_assignment] and give it a new name such as and give it a new name such as sow_incident_resolve_genai.
    
    [nilimadesai_1-1717027765504.png](https://www.servicenow.com/community/image/serverpage/image-id/360799i437772C5B4DDB4C7/image-dimensions/746x276?v=v2)
    
3. Open the new resolve genAI declarative action and click the Advanced view related link to show the additional configuration fields
4. Populate the form with the following:
    
    [nilimadesai_2-1717027855344.png](https://www.servicenow.com/community/image/serverpage/image-id/360800iEB08AFB97322757C/image-dimensions/737x420?v=v2)
    
    - You can specify the role of interest in the Script Condition field
    - Scroll to the related list and link the following UX Add on Event Mappings. You can refer to the OOTB sow_incident_resolve declarative action to populate the form. The records below are copies of the OOTB UX Add On Mappings for the OOTB resolve button linked to the new declarative action.
        
        [nilimadesai_4-1717027996561.png](https://www.servicenow.com/community/image/serverpage/image-id/360802iF43E76A65B8797FD/image-dimensions/696x160?v=v2)
        
5. Navigate to the [ sys_ux_form_action_layout ] table and open the record where table=incident
6. Open the UX Form Action Layout Items related list and add the new role restricted resolve button to the list
7. Navigate back to [sys_ux_form_action] and open the OOTB resolve button
8. Open the related declarative action sow_incident_resolve
9. Click Advanced view in the related links
10. Update the Script Condition field to only surface when the user does not have the role of interest
    
    [nilimadesai_5-1717028122505.png](https://www.servicenow.com/community/image/serverpage/image-id/360803i7D534474A4780194/image-dimensions/745x437?v=v2)
    
11. Navigate to [sys_ux_screen] open record where sys_id = 98f52401b7d73110a7ba0f68ee11a95d
12. Scroll to the UX Screen Condition related list and create a new screen condition with the following (refer to screenshot):
    
    [nilimadesai_6-1717028170951.png](https://www.servicenow.com/community/image/serverpage/image-id/360804i81E22D5078A4E605/image-dimensions/743x422?v=v2)
    

Now Assist Resolve UI Action should now be separate between the roles in SOW.

**Appendix – Other Known Issues related to Resolution Notes and how to work around** 

- Resolution Notes popup may break as a result of misplaced usage of OOB ProblemModalUIHelper UI Scripts within OOB Now Assist
    - Known Error with Workaround: [KB1641421](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1641421)
- Resolution Notes Generation model renders incorrect page on model in UI 16 if a Condition based View Rule exists
    - Known Error with Workaround: [KB1642531](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1642531)

## Related
- [[Introducing Custom Record Summarization Now Assist]]
- [[GenAI]]
- [[Now Assist in AI Search]]

- [[Now Assist]]
- [[Now Assist for CSM - Resolution Notes Generation]]
- [[Now Assist Panel (NAP) Troubleshooting Guide Commo]]
- [[Now Assist case Summaization in custom tables]]