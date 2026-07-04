---
title: "How to migrate from Listening Posts to Integrated Experience and Service Feedback"
aliases:
  - KB2270549
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2270549
kb_number: KB2270549
last_modified: 2025-07-31
---

## Text

**Migrating from Listening Posts to Integrated Experience and Service Feedback**

* * *

**Overview:**

ServiceNow is deprecating Listening Posts, the HR-centric pulse survey tool, in favour of Integrated Experience and Service Feedback - a unified, extensible feedback framework embedded in Employee Center Pro.

This article provides the recommended steps for customers using **Listening Posts** to transition to [](https://www.servicenow.com/docs/bundle/yokohama-employee-service-management/page/product/employee-center/concept/ex-fdback-ovrvw.html)**[Integrated Experience and Service Feedback](https://www.servicenow.com/docs/bundle/yokohama-employee-service-management/page/product/employee-center/concept/ex-fdback-ovrvw.html) (EC Pro)**

* * *

**Details:**

**Why is Listening Posts being deprecated?**

Listening Posts will no longer be activated on new instances starting with the Zurich release (September 2025) and will be unsupported from the Brazil release (September 2026).

 Key reasons for deprecation:

-   Limited Scope: Focused only on HR Journeys and Lifecycle Events.
-   Redundant Functionality: Integrated Experience and Service Feedback covers all service workflows (HR, IT, etc.) and has more flexibility in terms of feedback configuration and analytics,
-   Modern UX: Integrated Experience and Service Feedback offers embedded widgets, modals, and a persistent “Give Feedback” drawer.
-   Maintenance Burden: Listening Posts is a Store app requiring separate updates and maintenance.
-   Strategic Alignment: ServiceNow is consolidating feedback into Integrated Experience and Service Feedback for a unified experience across all employee workflows

**Migration Steps:**

**Step 1: Review Your Current Listening Posts Setup**

Identify all active Listening Posts surveys and their use cases:

**Common Listening Posts use cases include:**

-   Pulse surveys tied to Journeys or Lifecycle Events
-   Voluntary feedback collection (general feedback widgets on portal pages)
-   Feedback on Campaigns or Content Pages
-   Multi-channel surveys delivered through Portal, Virtual Agent, or collaboration tools like Teams/Slack (if configured)
-   Sentiment analysis dashboards
-   Question banks and reusable survey components

**Document the following for each survey:**

-   Survey themes and questions
-   Trigger conditions (e.g., based on Journey stages, page views, or time-based events)
-   Audience targeting
-   Response sharing rules
-   Delivery channels used (e.g., Portal, Mobile, VA, Teams/Slack)

This helps ensure all existing feedback mechanisms are accounted for before configuring feedbacks in Integrated Experience and Service Feedback.

* * *

**Step 2: Prepare for Integrated Experiences and Service Feedback** 

Before configuring Integrated Experience and Service Feedback, ensure your instance meets the following prerequisites:

-   An active **Employee Center Pro** license is required.
-   Integrated Experience and Service Feedback **is supported starting with the ServiceNow Washington release**. Ensure your instance is on Washington or a later version.
-   The **Employee Center Pro** application must be version **31.0.4 or higher**.
-   To collect feedback via Outlook closure emails, install the **Outlook Actionable Messages** application (version **4.2.1 or higher**, optional).
-   Administrators configuring feedback should have **sn\_hr\_sp.esc\_admin** role.

 

* * *

**Step 3: Translate Your Listening Posts Setup to Integrated Experience and Service Feedback**

Before configuring feedback in Integrated Experience and Service Feedback, map your existing Listening Posts use cases to the corresponding Integrated Experience and Service Feedback features.

**Use the table below to guide the translation:**

<table class="MsoTableGrid" style="border-collapse: collapse; border: medium; margin-left: 0px; margin-right: auto;" border="1" cellspacing="0" cellpadding="0"><tbody><tr><td style="width: 225.4pt; border: solid windowtext 1.0pt; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-family: 'times new roman', times;"><strong><span style="color: #424242;">Listening Posts Use Case</span></strong></span></p></td><td style="width: 225.4pt; border: solid windowtext 1.0pt; border-left: none; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-family: 'times new roman', times;"><strong>Integrated Experience and Service Feedback</strong><strong><span style="color: #424242; font-weight: normal;">&nbsp;</span><span style="color: #424242;">Equivalent</span></strong></span></p></td></tr><tr><td style="width: 225.4pt; border: solid windowtext 1.0pt; border-top: none; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Pulse survey triggered by Journey stage</span></p></td><td style="width: 225.4pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Service Feedback – Workflow</span></p></td></tr><tr><td style="width: 225.4pt; border: solid windowtext 1.0pt; border-top: none; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Feedback shown on portal pages (e.g., Journey Details)</span></p></td><td style="width: 225.4pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Service Feedback – In-Page</span></p></td></tr><tr><td style="width: 225.4pt; border: solid windowtext 1.0pt; border-top: none; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Feedback on Campaigns or Content Pages</span></p></td><td style="width: 225.4pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Service Feedback – In-Page</span></p></td></tr><tr><td style="width: 225.4pt; border: solid windowtext 1.0pt; border-top: none; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Voluntary feedback widget across portal</span></p></td><td style="width: 225.4pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Experience Feedback Drawer</span></p></td></tr><tr><td style="width: 225.4pt; border: solid windowtext 1.0pt; border-top: none; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Feedback after VA conversation (if configured)</span></p></td><td style="width: 225.4pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Service Feedback – Virtual Agent</span></p></td></tr><tr><td style="width: 225.4pt; border: solid windowtext 1.0pt; border-top: none; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Survey sent via Teams/Slack</span></p></td><td style="width: 225.4pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Not natively supported (workaround via VA in Teams if applicable)</span></p></td></tr><tr><td style="width: 225.4pt; border: solid windowtext 1.0pt; border-top: none; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Survey sent via email</span></p></td><td style="width: 225.4pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0cm 5.4pt 0cm 5.4pt;" valign="top"><p style="margin-right: 0cm; margin-left: 0cm; font-size: 12pt; font-family: 'Times New Roman', serif;"><span style="font-size: 11pt; color: rgb(66, 66, 66); font-family: 'times new roman', times;">Outlook Feedback (for closure emails) or Assessments (for general surveys)</span></p></td></tr></tbody></table>

 

* * *

**Step 4: Feedback Definitions: Understanding the Types**

Integrated Experiences and Service Feedback offers two primary types of Feedback:

-   **Experience Feedback (Drawer)** – For general, voluntary feedback
-   **Service Feedback** – For targeted, contextual feedback on specific pages, workflows, and Virtual Agent interactions

![](/sys_attachment.do?sys_id=64b7814a4743ee58c4e1a325126d43a2)

When configuring Experience Feedback or Service Feedback, you can either:

-   Use built-in quick rating options (stars, thumbs, emojis) with optional comments, **OR**
-   Select an existing survey from the platform to collect more detailed, multi-question feedback.

![](/sys_attachment.do?sys_id=60f7858a4743ee58c4e1a325126d4343)

**Path to create existing surveys:**

1.  Navigate to **Survey → Surveys** in your instance.
2.  Create and publish the required survey using Survey Designer.
3.  Published surveys appear in the Survey field when configuring Feedback Definitions.

Once published, it will appear in the Surveys list when configuring an Experience or Service Feedback definition.

**Note:** Unlike Listening Posts, Integrated Experiences and Service Feedback, does not support reusable question banks or themed question sets. If you previously used Pulse Question Banks, you’ll need to create separate surveys for each theme.

![](/sys_attachment.do?sys_id=890841ca4743ee58c4e1a325126d4371)

* * *

**Step 5: Set up Feedback with Integrated Experiences and Service Feedback**

Follow these steps to set up feedback effectively with Integrated Experiences and Service Feedback:

**5.1. Set Up the Global Feedback Drawer (Voluntary Feedback on Portal & Mobile)**

  
![](/sys_attachment.do?sys_id=aa1881ca4743ee58c4e1a325126d4338)

The "Provide Feedback" drawer allows employees to share feedback anytime from anywhere on the portal or mobile app.

**To configure:**

**![](/sys_attachment.do?sys_id=44388dca4743ee58c4e1a325126d4304)**

-   Go to **Experience and Service Feedback → Feedback Configurations**
-   Turn ON the drawer and set preferences:

-   **Anonymity:** Anonymous, opt-in, or identified
-   **Privacy Message:** e.g., “Your feedback helps us improve.”
-   **Success Message:** e.g., “Thank you for your feedback!”
-   **Placement:** Left, right, top, or bottom

**If you want to customize the feedback inside the drawer:**

-   Create a **Feedback Definition** of type **Experience Feedback** to:

  
![](/sys_attachment.do?sys_id=28480dca4743ee58c4e1a325126d43fd)

-   Change the prompt text and rating style (stars, thumbs, emojis)
-   Link to a survey for more detailed feedback
-   Control when the drawer appears - immediately, after a short delay, or after the user scrolls
-   Apply **Audience Targeting** to control which employees see the drawer

* * *

## **5.2. Configure Targeted Feedback for Pages, Requests, and Journeys**

Service Feedback allows you to collect targeted, **page-specific** or **action-specific** feedback, rather than general, global feedback like the Experience Feedback drawer.

-   Go to **Feedback Definitions → New**

Configure:

1.  -   **Type:** Service Feedback (In-Page, Modal, or via Topic Page).
    -   **Target Pages**: Requests, cases, journeys, catalog items
    -   **Rating Scale:** 5-star, emoji, thumbs, etc.
    -   **Comments & Tasks:** Enable feedback tasks for low ratings.

Service Feedback can appear in different ways, depending on your configuration:

**Types of Service Feedback Placement:**

1.  **Service – In Page:** Embedded on specific pages like request forms, articles, journey pages.

**Example:** A feedback widget placed on a Journey Details page for employees to rate their experience

  
  
![](/sys_attachment.do?sys_id=3858450e4743ee58c4e1a325126d43eb)

![](/sys_attachment.do?sys_id=ab58850e4743ee58c4e1a325126d4300)

**Widget Placement Requirement:** For In-Page Feedback to appear, the Feedback Widget must be manually placed on the relevant portal pages using either Service Portal Pages or Page Designer, depending on how your portal is configured.

2.  **Service -Topic Page**: Appears on Topic Pages in Employee Center Pro for overall topic-level feedback.

**Example:** Was this Topic helpful?

  
![](/sys_attachment.do?sys_id=ab684d0e4743ee58c4e1a325126d43ff)

![](/sys_attachment.do?sys_id=d5984d4e4743ee58c4e1a325126d43cd)

**C. Service - Workflow**: Triggered by user actions, e.g., request submission, journey stage completion, Virtual Agent resolution.

![](/sys_attachment.do?sys_id=8ea8818e4743ee58c4e1a325126d438d)

  
![](/sys_attachment.do?sys_id=51b8058e4743ee58c4e1a325126d4392)

 

 

 

 

 

 

  

 

 

 

 

* * *

**5.3. Configure Virtual Agent Feedback**

We have built pre-configured Topics to capture Experience and Service Feedback via Virtual Agent. 

-   The experience feedback is configured as “give feedback” topic that is always visible to users to provide anytime feedback. 
-   The service feedback topic is configured to auto-trigger at the end of any virtual agent conversation. 
-   Admins can configure both these feedback experiences to use a simple rating scale or invoke a ServiceNow platform survey.

  
![](/sys_attachment.do?sys_id=30c8858e4743ee58c4e1a325126d4394)

![](/sys_attachment.do?sys_id=c1d8898e4743ee58c4e1a325126d43af)

* * *

**5.4. Configure Outlook Actionable Message Feedback**

Service Feedback via email notifications will be available with Outlook Actionable Messages store application (version 4.1.5 or above).

![](/sys_attachment.do?sys_id=33d84d8e4743ee58c4e1a325126d4352)

* * *

**5.5. Configure Feedback for Now Mobile** 

Experience and Service feedback functionality is available for Now Mobile users. 

-   Experience Feedback is pre-configured to appear under the ‘More’ tab for users to provide generic feedback on their mobile experience. Like the portal, it can be configured to showcase experience ratings or prompt a deeper survey questionnaire to collect feedback. 
-   Like the portal, the Service Feedback widgets are pre-configured to appear on the request pages during or after the request is fulfilled.

![](/sys_attachment.do?sys_id=70f805ce4743ee58c4e1a325126d432a)

All feedback widgets on Now Mobile appear via Mobile Employee Service Portal (MESP), so technical configurations for anonymity, feedback ratings, surveys, fatigue mitigation, and dashboard integration are consistent with the portal.

 **![](/sys_attachment.do?sys_id=d16dc1c247c3ee58c4e1a325126d4304)**

**5.6. Configure Feedback Tasks (Automated Follow-up)**

![](/sys_attachment.do?sys_id=06194dce4743ee58c4e1a325126d4339)

In Feedback Definitions:

-   Enable **Feedback Tasks** for negative scores.
-   Define:
    -   **Assignment Group** (e.g., IT Support, HR Services, Knowledge Owners).
    -   **Threshold for task creation** (e.g., score 3/5 or below).
    -   Whether to allow task skipping.
-   When a task is completed, users with identified feedback receive a resolution confirmation.

![](/sys_attachment.do?sys_id=003981024783ee58c4e1a325126d431e)

![](/sys_attachment.do?sys_id=6a49c5024783ee58c4e1a325126d433d)

* * *

**Step 6: Review Feedback Analytics** 

The new Experience and Service Feedback Dashboard offers a centralized platform for analyzing feedback across both experience and service channels. 

-   It includes dedicated views for Experience feedback, Service feedback, a combined summary, and Feedback Task Analytics. 
-   Admins can track aggregate ratings over time and filter responses by channel (such as portal or email), page, and rating, enabling organizations to derive actionable insights and drive continuous improvement. 
-   Feedback data is also integrated into the User Experience Analytics Dashboard, providing a unified view across all feedback types. 
-   The Feedback Task Analytics section further enhances visibility with visualizations by task status (Open, Skipped, Completed) and highlights the top pages generating feedback tasks.
-   ![](/sys_attachment.do?sys_id=007941424783ee58c4e1a325126d43c2)

* * *

**Step 7: Test and Validate**

-   Preview feedback prompts across all configured areas
-   Submit test feedback responses via portal, mobile, and (if applicable) email channels
-   Confirm:
    -   Feedback is recorded in dashboards
    -   Feedback tasks are generated for negative scores (if configured)
    -   Task owners can access and resolve feedback tasks

* * *

**Step 8: Monitor and Optimize**

-   Use **Feedback Fatigue Controls**:
    -   Limit prompts per session.
    -   Exclusion period between prompts.
    -   “Remind Me Later” option.
-   Regularly review the **Experience & Service Feedback Dashboard** to:
    -   Track response rates and trends
    -   Identify areas for service or content improvements
-   Adjust trigger conditions, survey questions, or visibility settings as needed
-   Train service and content owners to:
    -   Act on feedback tasks promptly
    -   Close the loop with employees when issues are resolved

* * *

**Step 9: Deactivate Listening Posts**

-   Disable Listening Posts surveys and triggers to prevent duplicates
-   Remove Listening Posts widgets from portal pages
-   Turn off Listening Posts jobs (e.g., scheduled pulses)
-   Retain historical Listening Posts data for reference if required

* * *

**Frequently Asked Questions (FAQs):**

**Q:** Will existing Listening Posts survey responses be migrated?  
**A:** No. Historical survey responses remain accessible in the system but are not migrated to **Integrated Experience and Service Feedback**.

**Q:** Can Listening Posts and Integrated Experience and Service Feedback run simultaneously?  
**A:** Running both is technically possible but not recommended. Customers are encouraged to fully migrate and deactivate Listening Posts to avoid confusion.

**Q:** How to enable Experience & Service Feedback?

**A:** For experience feedback, all deployments will have the drawer widget enabled upon upgrade/first install. However, the in-page widget is only pre-enabled for new deployments (i.e., first install). For upgrade scenarios, admins will need to manually place this widget on the portal at the designed locations via the page designer.

For Service Feedback, admins must enable and complete the full configuration upon upgrade or new installation, as it doesn’t come pre-enabled.

* * *

**Additional Resources:**

-   [Integrated Experience and Service Feedback Documentation](https://www.servicenow.com/docs/bundle/xanadu-employee-service-management/page/product/employee-center/concept/ex-fdback-ovrvw.html)
-   [Integrated Experience and Service Feedback FAQs](https://servicenow.sharepoint.com/:w:/r/sites/EmployeeExperienceProduct/_layouts/15/Doc.aspx?sourcedoc=%7BB6297746-F9ED-4631-A440-FDFDD01D23D2%7D&file=Integrated%20Experience%20&%20Service%20Feedback%20FAQs.docx=&action=default&mobileredirect=true)
-   [ServiceNow Community](https://www.servicenow.com/community/employee-center-events/employee-center-academy-integrated-services-and-experience/ec-p/2802311#M106)

* * *

**Need Assistance?**

For support with your migration to **Integrated Experience and Service Feedback**, please contact ServiceNow Support through the [Customer Support Portal](https://support.servicenow.com).
