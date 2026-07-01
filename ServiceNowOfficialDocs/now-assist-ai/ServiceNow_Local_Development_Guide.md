# ServiceNow Local Development Guide

Personal reference for setting up and working with ServiceNow development tooling locally.

---

## 1. Developer Instance

Get a free Personal Developer Instance (PDI) from developer.servicenow.com before anything else.

- [[application-development/developer-sandboxes/administering-sandboxes|Administering sandboxes]]
- [[application-development/developer-sandboxes/dev-sbx-general-guidelines|Sandbox general guidelines]]
- [[application-development/developer-sandboxes/dev-sbx-entitlements|Sandbox entitlements]]
- [[application-development/developer-sandboxes/dev-sbx-installing|Installing a sandbox]]
- [[application-development/developer-sandboxes/allocating-sandboxes|Allocating sandboxes]]

---

## 2. CLI

The ServiceNow CLI is the entry point for most local tooling.

- [[application-development/servicenow-cli/download-cli|Download the CLI]]
- [[application-development/servicenow-cli/configure-profile|Configure a profile]]
- [[application-development/servicenow-cli/create-default-profile|Create a default profile]]
- [[application-development/servicenow-cli/create-named-profile|Create a named profile]]
- [[application-development/servicenow-cli/find-extensions|Find CLI extensions]]
- [[application-development/servicenow-cli/create-command|Create command reference]]

---

## 3. SDK (now-sdk)

The now-sdk enables TypeScript-based local development with type checking and build/deploy pipelines.

- [[application-development/servicenow-sdk/configuring-servicenow-sdk|Configuring the SDK]]
- [[application-development/servicenow-sdk/authenticate-instance-now-sdk|Authenticate with now-sdk]]
- [[application-development/servicenow-sdk/authenticate-instance-oauth|Authenticate via OAuth]]
- [[application-development/servicenow-sdk/authenticate-instance-basic-auth|Authenticate via basic auth]]
- [[application-development/servicenow-sdk/build-deploy-application-now-sdk|Build and deploy an application]]
- [[application-development/servicenow-sdk/business-rule-api-now-ts|Business Rule API (TypeScript)]]
- [[application-development/servicenow-sdk/client-script-api-now-ts|Client Script API (TypeScript)]]
- [[application-development/servicenow-sdk/acl-api-now-ts|ACL API (TypeScript)]]
- [[application-development/servicenow-sdk/atf-test-now-ts|ATF test API (TypeScript)]]

---

## 4. IDE Plugin (VS Code)

- [[application-development/servicenow-ide-family-release/configuring-servicenow-ide|Configuring the IDE plugin]]
- [[application-development/servicenow-ide-family-release/build-applications-servicenow-ide|Build applications in the IDE]]
- [[application-development/servicenow-ide-family-release/create-application-servicenow-ide|Create an application]]
- [[application-development/servicenow-ide-family-release/create-application-file-servicenow-ide|Create an application file]]
- [[application-development/servicenow-ide-family-release/clone-git-repository-servicenow-ide|Clone a Git repository]]
- [[application-development/servicenow-ide-family-release/connect-git-provider-oauth-2|Connect Git provider via OAuth 2.0]]
- [[application-development/servicenow-ide-family-release/connect-git-provider-basic-auth|Connect Git provider via basic auth]]
- [[application-development/servicenow-ide-family-release/convert-application-servicenow-ide|Convert an existing application]]
- [[application-development/servicenow-ide-family-release/create-use-javascript-modules-ide|Create and use JavaScript modules]]
- [[application-development/servicenow-ide-family-release/configure-mid-server-source-control|Configure MID Server source control]]

---

## 5. Studio (Classic)

Browser-based IDE inside the instance. Still the go-to for viewing/editing all app files in one place.

- [[application-development/servicenow-studio-classic/access-servicenow-studio|Access Studio]]
- [[application-development/servicenow-studio-classic/builders-in-servicenow-studio|Builders available in Studio]]
- [[application-development/servicenow-studio-classic/build-agent-in-servicenow-studio|Build an AI Agent in Studio]]
- [[application-development/servicenow-studio-classic/app-deployment-servicenow-studio|App deployment from Studio]]
- [[application-development/servicenow-studio-classic/add-collabs-app-servicenow-studio|Add collaborators to an app]]
- [[application-development/servicenow-studio-classic/change-your-development-experience|Change your development experience]]

---

## 6. Update Sets

Use update sets when working outside source control or on instances without Git integration.

- [[application-development/system-update-sets/get-started-update-sets|Get started with update sets]]
- [[application-development/system-update-sets/create-select-update-set|Create and select an update set]]
- [[application-development/system-update-sets/configure-system-update-sets|Configure update sets]]
- [[application-development/system-update-sets/customizations-tracked-update-sets|What gets tracked]]
- [[application-development/system-update-sets/default-update-sets|Default update sets]]
- [[application-development/system-update-sets/exploring-system-update-sets|Explore update sets]]
- [[application-development/system-update-sets/delete-update-set-cautions|Cautions when deleting]]

---

## 7. Team Development & Source Control

- [[application-development/team-development/administer-team-development|Administer team development]]
- [[application-development/team-development/c_InstanceHierarchies|Instance hierarchies]]
- [[application-development/team-development/c_LocalChanges|Local changes]]
- [[application-development/team-development/c_NavigatingLocalChangeLists|Navigating local change lists]]
- [[application-development/team-development/c_PullsAndPushes|Pulls and pushes]]
- [[application-development/team-development/c_CodeReview|Code review]]
- [[application-development/team-development/c_CodeReviewWorkflow|Code review workflow]]
- [[application-development/team-development/c_ExclusionPolicies|Exclusion policies]]

---

## 8. Automated Test Framework (ATF)

- [[application-development/automated-test-framework-atf/atf-admin-overview|ATF admin overview]]
- [[application-development/automated-test-framework-atf/atf-admin-properties|ATF admin properties]]
- [[application-development/automated-test-framework-atf/atf-add-test-to-suite|Add tests to a suite]]
- [[application-development/automated-test-framework-atf/atf-add-child-suite|Add child suites]]
- [[application-development/automated-test-framework-atf/add-parameterized-data|Add parameterized data]]

---

## 9. API Reference (Scripting)

- [[api-reference/server-api-reference/server-api-reference|Server-side Glide API reference]]
- [[api-reference/cllent-mobile-api-reference/cllent-mobile-api-reference|Client-side API reference]]
- [[api-reference/scripts/scripts|Script Includes reference]]
- [[api-reference/rest-apis/rest-apis|REST API reference]]

---

## 10. Custom Notes (this vault)

- [[now-assist-ai/ai-agents/AI Agents Knowledge Base|AI Agents — debugging & best practices]]
- [[now-assist-ai/ai-search/Get Similar Records AIS Script Documentation|AI Search — getSimilarRecords & AIS tuning]]
