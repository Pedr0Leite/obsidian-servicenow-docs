---
aliases:
  - "Now Assist Panel (NAP) Troubleshooting Guide Commo"
area: "AI & VA"
source: notion-export
tags:
  - now-assist
  - troubleshooting
  - genai
  - admin
  - virtual-agent
---

# Now Assist Panel (NAP) Troubleshooting Guide: Common Issues and Solutions

Based on frequent community discussions and ServiceNow support cases, this comprehensive guide addresses the most common Now Assist Panel issues and provides step-by-step solutions to resolve them.

# **Common Issue #1: Unable to Turn on Now Assist Panel - "Turn On" Button Deactivated**

### **Problem Description**

When the user navigates to the Now Assist Experiences in the Now Assist Admin console, even though they can see that Now Assist Panel is included in the license the button to it "Turn on" is deactivated.

**[Screenshot 1: Show the Now Assist Admin console with the deactivated "Turn on" button]** *Screenshot should display: Now Assist Experiences page showing Now Assist Panel with grayed-out/disabled "Turn on" button*

### **Root Cause**

The user has the role sn_nowassist_admin.user. This role only allows read access, preventing the customer from turning on the Now Assist Panel.

### **Solution Steps**

1. **Check User Roles**: Navigate to User Administration > Users
2. **Locate the affected user** and review their assigned roles

**[Screenshot 2: User Roles Configuration]** *Screenshot should display: User Administration > Users page showing a user record with roles tab highlighting the problematic sn_nowassist_admin.user role*

1. **Remove the problematic role**: Remove the sn_nowassist_admin.user role from the affected user.

**[Screenshot 3: Role Removal Process]**

*Screenshot should display: User roles list with sn_nowassist_admin.user role being removed/unchecked*

1. **Assign appropriate administrative role**: Ensure the user has proper Now Assist administrative permissions
2. **Test the functionality**: Return to Now Assist Admin console and verify the "Turn on" button is now active

**[Screenshot 4: Resolved State]** *Screenshot should display: Now Assist Admin console with the "Turn on" button now active/clickable*

### **Prevention Tips**

- Always assign roles following the principle of least privilege
- Use appropriate Now Assist admin roles based on user responsibilities
- Refer to [Now Assist Admin roles documentation](https://www.servicenow.com/docs/csh?topicname=roles-installed-with-now-assist-admin.html&version=latest) for role details

---

# **Common Issue #2: Now Assist Panel Throws Internal Server Error 500**

### **Problem Description**

When trying to use the Now Assist panel in the header and clicking on it ,getting an Internal Server Error 500 error with the message com.glide.rest.util.NotFoundException

**[Screenshot 5: Internal Server Error 500]** *Screenshot should display: Browser showing the Internal Server Error 500 with the specific error message com.glide.rest.util.NotFoundException*

### **Root Cause**

The issue occurs when the Model Type configuration for the Now Assist Panel context profile is incorrectly set.

### **Solution Steps**

1. Go to sys_cs_context_profile.list

**[Screenshot 6: sys_cs_context_profile List]** *Screenshot should display: sys_cs_context_profile.list view showing all context profile records*

1. Check the "Model Type' for 'Now Assist Panel - Platform'

**[Screenshot 7: Context Profile Record]** *Screenshot should display: Specific sys_cs_context_profile record for 'Now Assist Panel - Platform' with Model Type field visible*

1. Ensure it is set to 'Now Assist Panel'

**[Screenshot 8: Incorrect Model Type]** *Screenshot should display: Model Type field showing incorrect value (not 'Now Assist Panel')*

1. If it is set to something else, then change it back to 'Now Assist Panel' and save the record.

**[Screenshot 9: Corrected Model Type]** *Screenshot should display: Model Type field corrected to show 'Now Assist Panel' value*

### **Important Note**

Please ensure to test the behavior in sub prod before making these changes in production.

### **Additional Verification Steps**

1. Clear browser cache after making the changes
2. Test with different user accounts to ensure consistency
3. Monitor system logs for any related errors

---

# **Common Issue #3: Now Assist Panel Stuck in Infinite Loading State**

### **Problem Description**

The Now Assist panel in the backend is unresponsive and seems to be always loading.

1. Log in to instance
2. Click on Now Assist Panel in Native UI
3. It stays in the loading state

**[Screenshot 10: Infinite Loading State]** *Screenshot should display: Now Assist Panel interface showing continuous loading spinner or loading indicator*

### **Root Cause**

The sys_cs_context_profile record the Now Assist Panel is inactive

### **Solution Steps**

1. The sys_cs_context_profile record for the Now Assist Panel comes from the following plugin: com.glide.cs.genai
2. Repair the plugin which will make the record active and it will resolve the issue.
3. The URL for the sys_cs_context_profile is: https://<instance-name>.service-now.com/sys_cs_context_profile.do?sys_id=e93cab98c7c03110b65579a988c260c4

### **Detailed Repair Steps**

1. **Navigate to Plugins**: Go to System Definition > Plugins

**[Screenshot 11: Plugins List]** *Screenshot should display: System Definition > Plugins page showing list of installed plugins*

1. **Locate the plugin**: Search for "com.glide.cs.genai"

**[Screenshot 12: GenAI Plugin Location]** *Screenshot should display: Plugin search results showing com.glide.cs.genai plugin in the list*

1. **Repair the plugin**: Right-click and select "Repair"

**[Screenshot 13: Plugin Repair Option]** *Screenshot should display: Context menu for the plugin showing "Repair" option*

1. **Monitor the repair process**: Check system logs for completion

**[Screenshot 14: Repair Progress]** *Screenshot should display: System logs or progress indicator showing plugin repair in progress*

1. **Verify the context profile**: Navigate to the sys_cs_context_profile URL provided above

**[Screenshot 15: Active Context Profile]** *Screenshot should display: sys_cs_context_profile record showing "Active" status after plugin repair*

1. **Test the panel**: Attempt to load the Now Assist Panel again

**[Screenshot 16: Successfully Loaded Panel]** *Screenshot should display: Now Assist Panel successfully loaded and responsive*

---

# **Common Issue #4: Now Assist Panel Not Visible After Activation**

### **Problem Description**

Users report that even after successfully activating the Now Assist Panel, it doesn't appear in the header or interface.

**[Screenshot 17: Missing Panel in Header]** *Screenshot should display: ServiceNow interface header without the Now Assist Panel icon/button visible*

### **Troubleshooting Steps**

1. **Check Browser Compatibility**
    - Ensure you're using a supported browser version
    - Clear browser cache and cookies
    - Disable browser extensions temporarily
2. **Verify User Permissions**
    - Confirm the user has the appropriate roles for Now Assist Panel access
    - Check if the user is in the correct groups
3. **Instance Configuration Check**
    - Verify that the Now Assist Panel plugin is active
    - Check system properties for Now Assist configuration
    - Ensure the instance has proper licensing

**[Screenshot 18: Plugin Status Check]** *Screenshot should display: Plugins page showing Now Assist related plugins with their active/inactive status*

**[Screenshot 19: System Properties Configuration]** *Screenshot should display: System Properties page showing Now Assist related configurations*

---

# **Common Issue #5: AI Agent Use Cases Not Running in Now Assist Side Panel**

### **Problem Description**

Users have created AI agent use cases, but they don't show output in the Now Assist side panel, although they work in other contexts.

**[Screenshot 20: AI Agent Use Case Working Outside Panel]** *Screenshot should display: AI agent use case functioning properly in a different context (not in the side panel)*

**[Screenshot 21: Same Use Case Not Working in Side Panel]** *Screenshot should display: The same AI agent use case not displaying or functioning in the Now Assist side panel*

### **Troubleshooting Steps**

1. **Verify Use Case Configuration**
    - Check that the use case is properly published
    - Ensure the AI agents are correctly associated with the use case
    - Verify the use case is active and not in draft state

**[Screenshot 22: AI Agent Use Case Configuration]** *Screenshot should display: AI agent use case configuration page showing published status and active state*

1. **Check Panel Integration**
    - Confirm the use case is configured for side panel display
    - Verify panel permissions and access controls
    - Check for any conflicting configurations

**[Screenshot 23: Panel Integration Settings]** *Screenshot should display: Configuration settings showing side panel integration options for the use case*

1. **Test in Different Contexts**
    - Test the use case outside the side panel
    - Compare working and non-working scenarios
    - Check system logs for integration errors

## Related
- [[Now Assist in AI Search]]
- [[Now Assist Q&A using Dynamic Translation]]
- [[GenAI]]

- [[Now Assist]]
- [[Now Assist for ITSM Handling Customization Scenari]]
- [[Agentic Workflow & AI Agents]]
- [[Introducing AI Agents and Quick Start Guide]]
- [[VA - Basic Arch and ACLs]]