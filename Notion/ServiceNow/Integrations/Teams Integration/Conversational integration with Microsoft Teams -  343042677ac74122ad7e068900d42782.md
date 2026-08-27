---
aliases:
  - "Conversational integration with Microsoft Teams -"
area: "Integrations"
source: notion-export
tags:
  - teams-integration
  - virtual-agent
  - integrations
  - troubleshooting
  - conversational-interfaces
---

# Conversational integration with Microsoft Teams - installation, FAQ, and troubleshooting

[](https://www.servicenow.com/community/image/serverpage/image-id/85387i4C1F40EBDBA72F4F/image-size/large?v=v2&px=999)

# Conversational integration with Microsoft Teams - Installation, FAQ, and troubleshooting

**(As of Vancouver GA)**

### Table of contents

### 1. Installation

### 2. FAQ, Security FAQ

### 3. Troubleshooting

### 1. Conversational integration with Microsoft Teams installation

### Prerequisites

It is recommended to be on the latest release patch which may contain
 updates and fixes. You should have the following plugins installed:

- Virtual Agent, or Virtual Agent Lite
- ITSM Virtual Agent conversations (Store release)
- HR Virtual Agent conversations (Store release)
- ServiceNow ‘admin’ role.

Microsoft requirements:

- Microsoft 365 developer account, or Microsoft Azure account
- Access to Microsoft 365 admin center, and Microsoft Teams admin
center. If you attempt to install the Teams integration without the
'admin' role, you will receive an error (error code=9).

The integration does not support the Microsoft Teams freemium 
account, which uses email accounts other than Microsoft Office 365 
accounts.

### 

### Recommended experience

It is recommended you start with the **ITSM integration with Microsoft Teams** or **HRSD integration with Microsoft Teams** store
 applications. These applications provide a richer employee 
experience that combines the power of the ServiceNow platform with 
Microsoft Teams. These are available in the [ServiceNow Store.](https://store.servicenow.com/) To see installation and configuration steps, please visit the documentation:

- [Install IT Service Management with Microsoft Teams](https://docs.servicenow.com/bundle/vancouver-employee-service-management/page/product/sn-teams/concept/sn-ms-teams.html)
- [Install HR Service Delivery with Microsoft Teams](https://docs.servicenow.com/bundle/vancouver-employee-service-management/page/product/sn-teams/concept/sn-ms-teams-hr.html)

If you only plan to use the Virtual Agent in Team or upgrading from a
 previous Virtual Agent-Microsoft Teams integration, see the following 
section:

### 

### Conversational integration only installation steps with video

**Video of a demo setup: Installing the conversational integration with Microsoft Teams:**

**First**, be sure you have a Microsoft 365 account with admin privileges (admin.microsoft.com accessible).

In the Quebec+ release, the “Conversational Integration with 
Microsoft Teams” store application is required to install the Microsoft 
Teams integration. Install the most recent release of the store app. It 
is available for Quebec+ only.

1. Request the “Conversational Integration with Microsoft Teams” app from the ServiceNow Store.

[](https://www.servicenow.com/community/image/serverpage/image-id/85389i726005403D43EA58/image-size/large?v=v2&px=999)

2. After several minutes, go to your instance and navigate to “All 
Available Applications > All”. Search for “Conversational Integration
 with Microsoft Teams”. Click “Install”.

[](https://www.servicenow.com/community/image/serverpage/image-id/85388i89F1665E9329D8D1/image-size/large?v=v2&px=999)

3. After installation of the plugin, navigate to the Conversational 
Interfaces Home Page > Settings > General > Channels, and you 
will see that the “Add Integration” install button is now enabled for 
Teams. (Without the plugin installed, the button will be grayed 
out.) Select "Integrate with Now Virtual Agent".

[](https://www.servicenow.com/community/image/serverpage/image-id/294309i5F06F34690E53B58/image-dimensions/553x264?v=v2)

4. ServiceNow asks to be taken to a 3rd party site. This brings 
up the Microsoft login page. Log in with your Microsoft 
credentials. Then click “Accept” on the next page.

[](https://www.servicenow.com/community/image/serverpage/image-id/85399i01728ACAE4538082/image-size/large?v=v2&px=999)

5. After installation is successful, you can also check back on the 
“Channels and Integrations” page to see your MS Teams tenant name 
included.

[](https://www.servicenow.com/community/image/serverpage/image-id/294304i62F9A2EECA511ADD/image-dimensions/678x362?v=v2)

### **Adding the Now Virtual Agent to Microsoft Teams**

If you’ve already installed the ITSM integration, created a Manifest
 and uploaded it as a custom app to Microsoft Teams, you can skip this 
step. Otherwise, see here for steps to download our Now Virtual Agent 
app from the Microsoft Teams app store.

6. With the MS Teams client open, click on the “…” button and then 
search for “ServiceNow Virtual Agent”. Our “Now Virtual Agent” app will 
appear in the search results.

**Note:** If you're unable to find the app, be sure your
 administrator has allowed 3rd party apps for Teams in Org-wide 
settings. This is done in the Teams' administrator panel, under "Teams 
apps".

[](https://www.servicenow.com/community/image/serverpage/image-id/85400i24601B22C778963B/image-size/large?v=v2&px=999)

7. Click on the app, and click ‘Add’.

[](https://www.servicenow.com/community/image/serverpage/image-id/85393iE98C1383FD904C0C/image-size/large?v=v2&px=999)

8. Congrats! You’ve now successful installed the MS Teams 
integration. The bot will automatically reach out to you to connect your
 account. If not, type “hi” to start it.

[](https://www.servicenow.com/community/image/serverpage/image-id/85394i21DCFE455823104A/image-size/large?v=v2&px=999)

### 

### **Logging in and linking as an end-user**

The Now Virtual Agent bot should automatically be available to 
you. ServiceNow uses the user’s Microsoft profile and MS Teams email 
address as a match to automatically link users. If auto-linking is not 
available or does not work, here are steps to manually link an 
account.

1. When users first open the Virtual Agent in Teams, they will be
prompted to manually link their MS Teams account with their ServiceNow
account. When prompted, click “Link to ServiceNow”

[](https://www.servicenow.com/community/image/serverpage/image-id/85396i04E264B73614BB3D/image-size/large?v=v2&px=999)

2. You will be prompted with this screen below. Ensure that you are logged into your ServiceNow account and click “Confirm”.

[](https://www.servicenow.com/community/image/serverpage/image-id/85406i34D477487DE23145/image-size/large?v=v2&px=999)

**Next steps:** If you want to brand your app by changing the name and icon, see the steps [here](https://community.servicenow.com/community?id=community_article&sys_id=3b4f487edbe17490904fa9fb1396195b).

### 

### 2. Virtual Agent integration with MS Teams FAQ

**Is Live Agent Chat supported? Is it possible to open directly to a live agent in Teams?**

Yes. To connect with a Live Agent on Teams, just type “agent” or 
select "Live Agent Support" from the available topics menu. Agent chat 
on MS Teams works with agents communicating via Workspace.

As of the Quebec release with the Teams integration store app, Connect Support is *not* supported.

You can start a live agent conversation automatically in Teams by 
creating system property: com.glide.cs.cccif.live_agent_only, and 
setting it to ‘true’.

[](https://www.servicenow.com/community/image/serverpage/image-id/85395i3BF605481168910F/image-size/large?v=v2&px=999)

**The output text formatting is strange/inconsistent.**

MS Teams renders HTML output as image and strips out the intended 
formatting. To avoid formatting issues, use output types other than 
HTML. If you are experiencing this issue with out-of-box ITSM topics, 
please go to the ServiceNow Store and update your ITSM Virtual Agent 
Conversations to the latest release. See below for the old HTML 
formatting versus when using updated text or script output.

[](https://www.servicenow.com/community/image/serverpage/image-id/85401iD90A4BA1AB05A533/image-size/large?v=v2&px=999)

**Is it possible to change the chatbot name, description, and icon?**

Yes. See this [article](https://www.servicenow.com/community/virtual-agent-nlu-articles/ms-teams-branding-for-the-conversational-integration/ta-p/2310815) for instructions on branding your Teams bot.

[](https://www.servicenow.com/community/image/serverpage/image-id/85397iAC541F86179DC8BB/image-size/large?v=v2&px=999)

**Does NLU work with MS Teams?**

Yes.

**Do we support on-premise customers?**

Yes.

**Can I install the Teams integration on a PDI (personal developer instance?)**

No. PDIs are on a different data center without some necessary entitlements.

**Does Teams work with domain-separated instances?**

Yes. For outbound communication from agents to employees, it is 
expected that the agent has a user provisioned in the corresponding 
tenant.

**Is it possible for my MS Teams tenant to support multiple ServiceNow instances?**

Yes as of the San Diego release. See the documentation on how to implement [here](https://docs.servicenow.com/bundle/sandiego-servicenow-platform/page/administer/virtual-agent/concept/va-integ-single-teams.html).
 On earlier releases, if you attempt to install the same Microsoft Teams
 tenant on multiple instances, you may be asked to override the first 
instance, and Virtual Agent may not respond correctly. That said, you 
can support multiple MS Teams tenants in a single ServiceNow instance.

**I can't find the Now Virtual Agent app in the Teams app store.**

Be sure your administrator has allowed Now Virtual Agent (or 3rd 
party apps more broadly) in the Teams' administrator panel, under "Teams
 apps".

**I just migrated between different instances, e.g. between sub-prod and prod, and my integration is no longer working.**

You need to re-install the integration in the new instance after migrations.

**How do I raise awareness of the Virtual Agent bot in MS Teams with my users?** 

An admin can install the Virtual Agent app to all users and pin an 
app in Teams to make it easily accessible. This can be done in the 
Microsoft Teams admin center in “Teams app > Setup policies”. See MS 
Teams documentation on [Teams app setup policies](https://docs.microsoft.com/en-us/microsoftteams/teams-app-setup-policies).

**Does MS Teams support file upload?**

Yes, you can also copy and paste images in the text box.

**Am I able to preview ServiceNow content such as Knowledge articles in Teams?**

The Virtual Agent bot in Teams can embed knowledge articles and 
catalog items into MS Teams. The system property to enable this is: sn_va_teams.view_non_video_msft_task_module = true

**How do I get rid of the "response sent to app" message bar that appears in Virtual Agent responses?**

You can then disable the message bar by setting sn_va_teams.hide_teams_response_message = false.

**What are some usable shortcuts or commands when in Teams?** 

In Teams, you can use the following commands for actions such as 
beginning and ending conversations. These actions can be found in the ***sys_cs_contextual_action*** table.

| **Command** | **Description** |
| --- | --- |
| Hi | Begin a new conversation or access option for transferring to a live agent. |
| agent | Begin a new conversation or access option for transferring to a live agent. |
| bye | Leave a live chat conversation when no live agent is available (the bot does not respond). |
| help | Displays a short list of useful commands. |
| logout | Unlink your ServiceNow account from a messaging integration. |
| notification or notifications | Subscribe to or unsubscribe from notifications. |
| restart | End the current conversation and begin a new one. |

**Is it possible to restrict Virtual Agent topics from MS Teams**

In the topic condition script, use “vaContext.devicetype == Teams” as a condition to exclude topics from the MS Teams channel.

{ if(vaContext.deviceType === 'Teams'){

return false;

}

**Are promoted topics visible in Microsoft Teams?**

Yes, you can make promoted topics appear in Greetings when using 
Microsoft Teams. Create a new 'Custom Greetings & Setup' record, and
 for the condition, set 'devicetype' IS 'teams'. Then add the promoted 
topic you want to appear in Teams. Since it's a new record, don't forget
 to add Setup Topics like greetings and fallback too.

**Is guest access allowed to access VA topics?**

Yes. Topics with role = ‘public’ are shown to guest users. Guest user
 access is controlled in the Teams admin center, “Org-wide settings” 
page.

**How do I remove the "Continue as Guest" option when users link accounts?**

This requires Maint access, which ServiceNow support engineers may 
have access to. Navigate to the VA Designer and modify the 
_link_account_adapter topic. Comment out the script that shows the 
"Continue as Guest" button. Save and publish the topic.

**I'm trying to change the Teams greeting message, but it's 
controlled differently than the greetings message that appears on web.**

While the web client uses the Messages table [sys_ui_message] to configure the greeting and closing messages, Microsoft Teams use system messages. To change them, modify the system messages in Chat Setup as follows:

- For greetings that call vaSystem.getTopicSelectionMessage(), modify the value of com.glide.cs.topic_picker_msg.
- For closings that call vaSystem.endConversation(), modify the value of com.glide.cs.conversation_ended_msg.

**Does the Teams integration use IntegrationHub transactions?**

Yes, chat and notifications in Microsoft Teams consume IHub 
transactions. Certain ITSM integration features also use transactions, 
e.g. Chat-to-call feature and Notify Connector.

**What is the max size of a Teams message?**

The max message size is 40 KB, including all markups, so roughly ~28 KB of content.

**Is Microsoft Teams supported in Now Assist?**

Yes, of the Vancouver Patch 7/Washington release. After installing 
the integration, enable your Microsoft Teams tenant as a Display 
Location in the Now Assist in Virtual Agent setup:

[](https://www.servicenow.com/community/image/serverpage/image-id/337941iD9DDDAC2F960178E/image-dimensions/572x245?v=v2)

### Security FAQ

**What data does the ServiceNow Virtual Agent app on MS Teams access from Teams? What permissions does it ask for?**

A pop-up with the permissions will appear during installation (see 
above). ServiceNow Teams will access basic user info (name, username, 
email). In Azure they are mapped to the following API permissions 
(Microsoft Graph):

- offline_access - Maintain access to data you have given it access to.
- User.Read - Sign in and read user profile
- openid - Sign users in
- email - View users' email address
- profile - View users' basic profile

**What kind of data is stored by ServiceNow/Teams, and for how long?**

We capture chat messages in our Interaction table and import into 
incident records where configured. The retention rate for chat messages 
on the Teams side is based on your Teams admin settings. For more 
information on security permissions regarding our integration with 
Teams, see [this article](https://community.servicenow.com/community?id=community_article&sys_id=ef047b4b1b27f010c16b43f6fe4bcbb8).

ServiceNow does not extract any other data from MS Teams outside the integration.

**What authentication is used for the integration?**

JWT token for inbound authentication and OpenID Connect (OIDC) for outbound. See [https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-protocols-oidc](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-protocols-oidc) for more information.

Tokens are signed using standard asymmetric encryption algorithms such as RS256. For more details, please refer [here](https://docs.microsoft.com/en-us/azure/active-directory/develop/access-tokens#validating-the-signature).

For inbound messages, the request is authenticated on proxy using the
 Authorization header. It validates the token expiry and additional 
claims (issuer, ClientID, serviceURL) in the token. If the token is 
valid, it forwards the request to the instance.

Client secret of the Virtual Agent bot is stored on Proxy Server. For
 outbound messages, ServiceNow instance sends a request to proxy which 
in turn calls Bot Conversation API to send request to MS Teams.

ServiceNow does not store certificates 
within an instance or anywhere else to access the secret. All the 
conversations between MS Teams and ServiceNow are through HTTPS.

**Who should I ask about other MS Teams security questions?**

Please log a Case. Other information such as the Teams integration architecture diagram is available upon request.

### 3. Troubleshooting guide

**Patching guidance:** Most issues with installation, account linking, responsiveness, or notifications are resolved in the latest release patches.

**Store app update guidance:** Many issues in Teams can be addressed by updating the store app to the latest version. Download the latest version [here](https://store.servicenow.com/$appstore.do?ref=appmgmt&instanceid=18ada1f9dba0f598b1eb9027c59619da#!/store/application/8be385e4776110105d7b3882a910610e/). Release notes can be found [here](https://docs.servicenow.com/bundle/store-release-notes/page/release-notes/store/analytics-intelligence-reporting/store-rn-conversational-integration-ms-teams.html).

Debugging guidance: When troubleshooting, it is helpful to check the 
system logs: “System Log” > “All” when running into Microsoft Teams 
issues.

When opening Microsoft Teams to test, be sure you are logged in with 
your Microsoft 365 account and not your organization-provisioned 
Microsoft account, such as [@Servicenow](https://www.servicenow.com/community/user/viewprofilepage/user-id/5544).com. Otherwise you may run into issues or not have access to Teams at all.

**I’m unable to click the “Install” button for the MS Teams integration**

If the Install button on the “Messaging Apps Integration” page is 
disabled, ensure that you have first installed the Conversational 
Integration with Microsoft Teams plugin. If already installed, you can 
also try repairing the plugin. You should also see a record for “VA 
Teams Adapter Provider” in the sys_cs_provider table.

**I received a system log error message: 'Sorry, you don't have enough rights to install: no thrown error'**

You need the virtual agent admin role to install the integration.

**I** **receive an installation error: the browser URL contains sysparm_proxy_err_code=1**

The user must have admin role in the ServiceNow instance.

**I receive an installation error: the browser URL contains sysparm_proxy_err_code=4, 5.**

Check the system log for message: “Post mapping to datacenter 
failed:”. This is an internal error with the collaboration 
proxy authentication on our datacenter. Please log a high priority 
case.

**I** **receive an installation error: the browser URL contains sysparm_proxy_err_code=7**

Go to the message_auth table and see if a record exists for your 
tenant id (ServiceNow Virtual Agent Teams App – xxx-xxx-xxx...). Delete 
the record, then retry installation.

**I** **receive an installation error: the browser URL contains sysparm_proxy_err_code= 9**

The user installing the Teams/Slack integration does not have the 
'admin' role with (or not logged into) the Microsoft tenant/Slack 
workspace.

**I have issues linking my account, e.g. I do not receive a message to link my account.**

Check to see if there’s already a conversation record 
in sys_cs_client_adapter and sys_cs_conversation. Select and delete 
the latest record for the user. Then try starting a conversation 
again with “hi”.

Check system logs to see if you get this message:

*WARNING *** WARNING *** Get for non-existent record: oidc_provider_configuration:, initializing*

*WARNING *** WARNING *** No record found in oidc_provider_configuration for sysId=*

How to resolve this error:

1. Go to the oauth_oidc_entity table and select "ServiceNow Virtual Agent Teams App".
2. In the "OAuth OIDC Provider Configuration" field, click the magnifying glass and select "Microsoft Teams", and click Update.
3. Restart Microsoft Teams.

Note: Other than troubleshooting, making manual changes to records on sys_cs_client_adapter is *not* recommended.

**How do I unlink a user account?**

1. From MS Teams, type “logout”, to log out of the Virtual Agent app.
2. Go to “Self-Service > My Profile”. In the Related Links, click on “View linked account”.

[](https://www.servicenow.com/community/image/serverpage/image-id/85398iD463FC5C0473B3B6/image-size/large?v=v2&px=999)

3. Check the box for the MS Teams integration, and then click “Actions on selected rows” and click “Unlink account”.

[](https://www.servicenow.com/community/image/serverpage/image-id/85403iC01716799FD71997/image-size/large?v=v2&px=999)

**How do I unlink (uninstall) a tenant?**

Navigate to the Channels and Integrations page and click the 'Remove Integration' button for the Teams integration.

[](https://www.servicenow.com/community/image/serverpage/image-id/294323i0FCD1A70411B2751/image-dimensions/554x212?v=v2)

For earlier releases, navigate 
to table: sys_cs_provider_application, select the row with 
the tenant name and Provider is “VA Teams Adapter”. Delete the row with 
the tenant name.

[](https://www.servicenow.com/community/image/serverpage/image-id/85404iB84B9F711BF917B0/image-size/large?v=v2&px=999)

**The Virtual Agent is not responding. E.g., after linking my account, when I type "Hi" nothing happens.**

**First option**

- Type “hi” or “restart” into the chat.
- If a topic or conversation is stuck or not running, test the flow in the web client (e.g. Service Portal or Designer topic tester) to
determine if the issue is with the Teams client or the broader Virtual
Agent service.

**Second option (requires editing of table records in ServiceNow instance)**

- As an administrator, navigate to sys_cs_conversation, and delete any conversations where Device Type = ‘Teams’ and State = ‘Faulted’.
- Go to System OAuth (oauth_entity table) and make sure the
“ServiceNow Virtual Agent Teams App” record id present and is using
“49471a10-fdbc-4ffb-b0b8-944f3df985d9" as the client ID. If the record
is missing, try re-installing the integration.
- User interactions are also captured in
the sys_cs_client_adapter table. Ideally, at the completion of a
conversation, in the “Adapter state” field, the conversationId reference should be ‘null’. If the user is encountering an issue and their latest adapter record does not show “conversationId: null”, delete that
record. Run “gs.cacheFlush()” in the background script to clear the
instance cache. (Other than troubleshooting, making manual changes to
records on sys_cs_client_adapter is *not* recommended.)

**Last option**

- Have the user manually log-out of the Now Virtual Agent app,
then uninstall and re-install the Virtual Agent app in Teams if they
have permission. If no other solutions work, log a case.

**I’m not receiving any notifications.**

First, check that notifications are enabled for MS Teams on the “Messaging Apps Integration” page.

Also check in the "Notification Destination Type" table that the "Teams" record is Active.

For users, ensure that you are subscribed to notifications by typing “notifications”.

If you are expecting an actionable notification, those only 
appear when there are no open conversations, i.e. after the previous 
conversation has ended, including greetings.

For system performance reasons, we recommend that notifications be targeted in its audience and not exceed the following:

- More than 100K notifications using VA as a provider in a day.
- More than 100 users using VA as a provider for a single notification.

Check the sys_cs_channel_user_profile table and make sure you 
only have one active record per user at a time. If there's more than one
 active record per user, deactivate one of the records.

**Note:** Actionable notifications are available to *ITSM Pro* subscription only.

**My live agent is not answering on Teams, even though it’s working in web.**

Check your agent chat queue to make sure it’s not configured to 
only answer when the user is requesting from a portal, e.g. a scripted 
condition that requires the interaction to come from ‘sp’.

### **Additional Resources**

[ServiceNow documentation - Conversational Integration with MS Teams](https://docs.servicenow.com/bundle/vancouver-servicenow-platform/page/administer/virtual-agent/concept/teams-conv-integration.html)

[Microsoft Teams documentation](https://docs.microsoft.com/en-us/microsoftteams/)

[KB repository on Microsoft Teams (KB0998903)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0998903)

## Related
- [[Now Assist Panel (NAP) Troubleshooting Guide Commo]]
- [[ServiceNow – Integrations]]
- [[SAML Errors and Fixes (Multiple Provider SSO)]]

- [[Teams Integration]]
- [[Integrate your self-configured bot with single Mic]]
- [[Creating Custom MS Teams Cards]]
- [[UI macro to add “Start Conversation” to field]]