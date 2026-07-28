<!-- RAW SOURCE — landing in raw/inbox/ per README.md, not yet ingested into wiki/. -->
<!-- Source URL: https://www.servicenow.com/community/now-assist-articles/ai-agents-and-3rd-party-integrations/ta-p/3316286 -->
<!-- Fetched: 2026-07-23 via claude-in-chrome (blocked via CLI, real browser succeeded, no login required) -->

# AI Agents and 3rd party integrations

Max Dore, ServiceNow Employee — 07-11-2025

Uses HRSD's "Benefits Enrollment Retriever" AI Agent as a worked example of integrating an AI Agent with an external system (Oracle HCM).

## Component chain

1. **AI Agent Script Tool** ("Look up benefit enrollments") builds an `iGatewayInputs` object:
   ```javascript
   const iGatewayInputs = {
     user: userGr,
     feature_name: 'benefits_management',
     service_name: 'get_benefits',
     payload: inputs.payload
   };
   ```
2. **Calling Integration Gateway Subflow**:
   ```javascript
   integrationGatewayOutput = sn_fd.FlowAPI.getRunner()
     .subflow('sn_hr_integr_fw.integration_gateway')
     .inForeground()
     .withInputs(iGatewayInputs)
     .run();
   ```
   Triggers the Integration Gateway subflow, which handles requests for all defined feature/service combinations.
3. **Decision Table Routing** — Integration Provider Mapping Decision Table maps `feature_name` + `service_name` + `user` → the correct integration subflow (in this example, "Oracle HCM – Look up benefit enrollments").
4. **Specific API Call** — the selected subflow contains an Integration Hub Action making the external API call (HTTP method, URL, auth, query params, response handling).

## Custom Integration steps (to replicate for your own integration)

| Step | Description |
|---|---|
| 1. Decision Table Entry | In Integration Provider Mapping, map custom `feature_name` + `service_name` to a new subflow, mirroring existing entries |
| 2. Create Subflow | Duplicate an existing subflow, rename, configure I/O variables for `user`, `payload`, expected outputs — **all outputs must be strings** |
| 3. Create Action | In Integration Hub, define the external endpoint (REST/SOAP), method, auth credentials, request parameters, transform response into structured output |
| 4. Script Tool Setup | In AI Agent Studio, define a Script Tool using `iGatewayInputs`, calling the Integration Gateway, returning results |
| 5. Assemble AI Agent | Include the Script Tool + conversational logic to invoke it appropriately |
| 6. Test Agent | Use AI Agent Studio's testing to simulate user interactions, verify integration handling |

## Best Practices

- **Consistent Naming** — clean `feature_name`/`service_name` conventions for routing clarity
- **Supervised Execution** — mark critical tools as supervised, requiring manual approval before execution
- **Output Formatting** — all outputs as strings, avoids parsing issues
- **Agent Isolation** — when duplicating AI Agents, ensure each agent's tool references are independently defined (preserves distinct versioning, prevents unintended overlaps)

## Why This Architecture Works

Modular (Integration Gateway supports multiple features without duplicated code); scalable (new integrations replicate the proven pattern); governance-aware (all actions run through authenticated/logged flows); clear routing logic (Decision Table is a central, understandable feature→provider→subflow map).

## Built-in Example Set (HRSD OOB AI Agents)

Tuition reimbursement, Time-off balance retrieval, Feedback lookups, Request time off.

1 Helpful · 17,133 Views

## Why this might matter to this vault

The **Integration Gateway + Decision Table routing pattern** (feature_name/service_name → decision table → subflow → Integration Hub action) is a more elaborate cousin of [[Proactive Customer Case Communicator]]'s deterministic routing tool ([[caseRoutingUtil]]) — both push branching logic out of the LLM into a script/table, but this pattern is designed specifically for pluggable external-system integrations (multiple HR providers behind one interface), which neither PCCC nor [[partner-case-summary-agent]] currently need since they're both single-table, ServiceNow-native. Worth remembering if either agent's scope ever expands to a genuinely external system.
