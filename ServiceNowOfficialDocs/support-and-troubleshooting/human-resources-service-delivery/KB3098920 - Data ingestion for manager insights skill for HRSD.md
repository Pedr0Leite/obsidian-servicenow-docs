---
title: "Data ingestion for manager insights skill for HRSD"
aliases:
  - KB3098920
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3098920
kb_number: KB3098920
last_modified: 2026-06-18
---

## Data ingestion for manager insights skill for HRSD

  

# Knowledge Base: Adding Custom Data to Manager Insights Skill

## Overview

This article explains how to add custom data points to the Manager Insights skill so they are included in the AI-generated insights. By implementing the Manager Insights extension point, you can add organization-specific metrics and activities to the context sent to the Large Language Model (LLM).

## Use Case

The Manager Insights skill provides AI-generated summaries of team activities for managers. Out-of-the-box (OOTB), it includes standard HR metrics. However, organizations may have custom data points (e.g., wellness activities, expense submissions, learning completions) that they want to include in the AI-generated insights.

**Example Scenario:** Custom metrics like "Wellness Activities" or "Expense Submissions" are visible on the manager overview page but are not currently included in the AI-generated insights. This guide shows how to add them.

* * *

## Prerequisites

-   ServiceNow instance with Now Assist for HR Service Delivery (HRSD) {com.sn\_hr\_gen\_ai} and Manager Hub {com.sn\_mh} installed
-   Administrator or appropriate role to create Script Includes and modify extension points
-   Understanding of JavaScript and ServiceNow scripting

* * *

## Extension Point Details

**Extension Point Name:** `sn_hr_gen_ai.EmployeePersonaAssistant`  
**Sys ID:** `016677c79f8b1210ab46fb0e6a0a1cfb`  
**Navigation:** System Definition > Extension Points

### API Methods

The extension point requires implementation of two methods:

#### 1\. getProfileSummaries

Returns the summary of activities for multiple users in a given time frame.

```
/**
 * @param {Array} userIds - Array of user sys_ids to retrieve data for
 * @param {Object} filters - Filter object containing startDate, endDate, and other filters
 * @returns {Object} Summary data keyed by userId
 */
getProfileSummaries: function(userIds, filters) {
    // Query your custom tables and return data for each user
    // Example structure:
    // {
    //   "user_sys_id_1": {
    //     "userId": "user_sys_id_1",
    //     "customMetrics": {
    //       "wellnessActivities": 5,
    //       "expenseSubmissions": 3
    //     }
    //   }
    // }
}
```

#### 2\. getProfileTrends

Returns trends data and prompts for a manager's team.

```
/**
 * @param {String} managerId - sys_id of the manager
 * @param {Object} reporteeData - Object containing reportee summary information
 * @returns {Object} Trends data including prompts and at-risk activities
 */
getProfileTrends: function(managerId, reporteeData) {
    // Analyze the reportee data and identify trends or at-risk activities
    // Example structure:
    // {
    //   "prompts": [
    //     {
    //       "type": "wellness_concern",
    //       "message": "Some team members have low wellness participation",
    //       "priority": "medium"
    //     }
    //   ],
    //   "atRiskActivities": [
    //     {
    //       "userId": "user_id",
    //       "riskType": "pending_expenses",
    //       "severity": "high"
    //     }
    //   ]
    // }
}
```

* * *

## How It Works

When a manager clicks "Generate Insights" in the Manager Insights widget:

1.  **Manager Insights Service** retrieves the manager's team members (reportees)
2.  **Extension Point Framework** calls all active implementations of `sn_hr_gen_ai.EmployeePersonaAssistant`
3.  **For each implementation:**
    -   Calls `getProfileSummaries(reporteeIds, filters)` to collect custom activity data
    -   Merges the data with OOTB metrics using `Object.assign()`
    -   Calls `getProfileTrends(managerId, reporteeData)` to identify trends
4.  **Context Assembly:** All data is formatted and sent to the LLM as context
5.  **AI Generation:** The LLM generates insights based on the complete context
6.  **Display:** The insights are shown in the Manager Insights widget

**Important:** Data from multiple implementations is merged using `Object.assign()`. Use unique keys (like userId) to avoid overwriting data from other implementations.

* * *

## Implementation Steps

### Step 1: Create Extension Point Implementation

1.  Navigate to **System Definition > Extension Points**
2.  Search for extension point with sys\_id: `016677c79f8b1210ab46fb0e6a0a1cfb`
3.  Click **New** under the "Implementations" related list
4.  Fill in the details:
    -   **Name:** Custom Manager Insights Data Provider
    -   **API Name:** `CustomManagerInsightsDataProvider`
    -   **Active:** true
    -   **Application:** Your scoped application

### Step 2: Create the Script Include

Create a Script Include with the following structure:

```
var CustomManagerInsightsDataProvider = Class.create();
CustomManagerInsightsDataProvider.prototype = {
    initialize: function() {
        // Initialize any required variables or constants
    },

    getProfileSummaries: function(userIds, filters) {
        var summaries = {};
        
        // Validate inputs
        if (!userIds || userIds.length === 0) {
            return summaries;
        }
        
        // Get date filters
        var startDate = filters.startDate || gs.daysAgo(30);
        var endDate = filters.endDate || gs.nowDateTime();
        
        // Query your custom tables to get data for each user
        // Example: Query wellness activities table
        // var gr = new GlideRecord('x_custom_wellness_activity');
        // gr.addQuery('user', 'IN', userIds.join(','));
        // gr.addQuery('activity_date', '>=', startDate);
        // gr.addQuery('activity_date', '<=', endDate);
        // gr.query();
        
        // Build the summaries object with your custom data
        // summaries[userId] = { userId: userId, customMetrics: {...} };
        
        return summaries;
    },

    getProfileTrends: function(managerId, reporteeData) {
        var trends = {
            prompts: [],
            atRiskActivities: []
        };
        
        // Validate inputs
        if (!managerId || !reporteeData) {
            return trends;
        }
        
        // Analyze the reportee data to identify trends
        // Example: Check if any team members have low activity counts
        // for (var userId in reporteeData) {
        //     var userData = reporteeData[userId];
        //     if (userData.customMetrics.wellnessActivities < 2) {
        //         trends.prompts.push({
        //             type: 'wellness_concern',
        //             message: 'Low wellness participation detected',
        //             priority: 'medium'
        //         });
        //     }
        // }
        
        return trends;
    },

    type: 'CustomManagerInsightsDataProvider'
};
```

### Step 3: Update Manager Insights Skill Prompts (Critical)

After adding custom data through the extension point, you must update the Manager Insights skill prompts to instruct the LLM to use this new data.

1.  Navigate to **Now Assist > Skills**
2.  Search for, open and duplicate the **Manager Insights** skill
3.  Edit the skill's **System Prompt** or **Context Instructions**
4.  Add instructions about your custom data points, for example:

```
In addition to the standard HR metrics, the context includes custom data points:
- wellnessActivities: Number of wellness activities completed by each team member
- expenseSubmissions: Number of expense submissions by each team member

When generating insights:
- Mention wellness participation trends if notable
- Flag team members with low wellness activity (< 2 activities)
- Highlight any pending expense submission issues
- Provide actionable recommendations based on these custom metrics
```

**Without updating the skill prompts, the LLM may not effectively use your custom data in the generated insights.**

* * *

## Testing the Implementation

### 1\. Verify Extension Point Registration

```
// Run in Scripts - Background
var extensionPoint = new GlideRecord('sys_extension_point');
extensionPoint.get('016677c79f8b1210ab46fb0e6a0a1cfb');
gs.info('Extension Point: ' + extensionPoint.name);

var impl = new GlideRecord('sys_extension_instance');
impl.addQuery('extension_point', extensionPoint.sys_id);
impl.addQuery('active', true);
impl.query();
while (impl.next()) {
    gs.info('Implementation: ' + impl.name + ' (Active: ' + impl.active + ')');
}
```

### 2\. Test the Extension Point

```
// Run in Scripts - Background

// Test data - replace with actual sys_ids
var managerId = 'manager_sys_id_here';
var reporteeIds = ['reportee1_sys_id', 'reportee2_sys_id'];
var validatedFilters = {
    startDate: gs.daysAgo(30),
    endDate: gs.nowDateTime()
};

// Get all extension point implementations
var extensions = new GlideScriptedExtensionPoint().getExtensions('sn_hr_gen_ai.EmployeePersonaAssistant');

// Initialize result objects
var trends = {};
var summary = {};

// Call each extension point implementation
for (var i = 0; i < extensions.length; i++) {
    var ep = extensions[i];
    try {
        ep.initialize();

        // Handle getProfileSummaries
        if ('getProfileSummaries' in ep && typeof ep.getProfileSummaries === 'function') {
            var summaryData = ep.getProfileSummaries(reporteeIds, validatedFilters);
            if (summaryData) {
                gs.info('Summary data from ' + ep.type + ': ' + JSON.stringify(summaryData, null, 2));
                Object.assign(summary, summaryData);
            }
        }

        // Handle getProfileTrends
        if ('getProfileTrends' in ep && typeof ep.getProfileTrends === 'function') {
            var reporteeData = summary;
            var trendsData = ep.getProfileTrends(managerId, reporteeData);
            if (trendsData) {
                gs.info('Trends data from ' + ep.type + ': ' + JSON.stringify(trendsData, null, 2));
                Object.assign(trends, trendsData);
            }
        }
    } catch (exception) {
        gs.error('[Test] Exception calling extension point: ' + ep.type + ' - ' + exception);
    }
}

// Display final results
gs.info('=== FINAL SUMMARY ===');
gs.info(JSON.stringify(summary, null, 2));
gs.info('=== FINAL TRENDS ===');
gs.info(JSON.stringify(trends, null, 2));
```

### 3\. Verify in Manager Insights UI

1.  Navigate to the Manager Hub (sn\_mh\_overview page)
2.  Open the Manager Insights widget (Team Brief widget with AI Summary Viewer)
3.  Click "Generate Insights" button
4.  Verify that the AI-generated summary includes references to your custom data points
5.  Check System Logs for any errors

* * *

## Troubleshooting

### Debugging Extension Point Calls

Add logging to your implementation to track what data is being sent:

```
getProfileSummaries: function(userIds, filters) {
    gs.info('[CustomManagerInsights] getProfileSummaries called with ' + userIds.length + ' users');
    
    var summaries = {};
    // Your implementation
    
    gs.info('[CustomManagerInsights] Returning data for ' + Object.keys(summaries).length + ' users');
    return summaries;
}
```

Check **System Logs > System Log > All** after generating insights to see your debug output.

### Common Issues

#### Issue: Custom data not appearing in AI insights

-   Verify extension point implementation is active
-   Check System Logs for JavaScript errors
-   Ensure data structure matches expected format (userId as key)
-   **Verify you updated the Manager Insights skill prompts** to instruct the LLM to use the custom data
-   Test the extension point directly using the test script above

#### Issue: Extension point not being called

-   Verify the plugin `com.sn_hr_gen_ai` is active
-   Check that the Script Include is in the correct application scope
-   Ensure the extension point implementation record is active

* * *

## Summary

To add custom data to Manager Insights:

1.  **Create an extension point implementation** for `sn_hr_gen_ai.EmployeePersonaAssistant`
2.  **Implement the two required methods** (`getProfileSummaries` and `getProfileTrends`)
3.  **Return data in the expected structure** (userId as key for summaries)
4.  **Update the Manager Insights skill prompts** to instruct the LLM how to use your custom data
5.  **Test thoroughly** using the provided test scripts before deploying

The extension point provides a clean, maintainable way to customize Manager Insights while preserving upgrade compatibility.

* * *

## Additional Resources

-   ServiceNow Documentation: Extension Points
-   ServiceNow Documentation: Manager Hub
-   ServiceNow Documentation: Now Assist for HR Service Delivery
