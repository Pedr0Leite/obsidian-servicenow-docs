---
aliases:
  - "External users cannot open links in Virtual Agent chat"
area: "AI & VA"
source: raw-inbox
tags:
  - virtual-agent
  - now-assist
  - acl
  - csm
  - service-portal
  - support-case
---

# External Users Cannot Open Links in Virtual Agent Chat

## Overview

External users may receive a **403: You do not have permissions to access this page** error when they select links presented in the Virtual Agent or Now Assist chat on the Customer Service Management portal.

This article documents the issue described in ServiceNow support case **CASE RECORD**, including the reproduction steps, probable cause, and the solution proposed by ServiceNow Technical Support.

> **Status:** The solution described below was proposed by ServiceNow Technical Support. The source page does not confirm that the change has been implemented or that the issue has been resolved.

## Symptoms

When an external customer uses the chat on the `/csm` portal, links returned in the conversation are visible but cannot be opened. Selecting one of these links results in the following error:

```text
403: You do not have permissions to access this page.
```

## Steps to Reproduce

1. Open the `/csm` portal in the DEV1 or DEV3 environment.
2. Impersonate an external user. The support case used **USER NAME** as the example.
3. Enter a chat query such as:

   ```text
   Consultancy on demand
   ```

4. Select a link returned in the Virtual Agent or Now Assist chat.
5. Confirm that the portal displays a 403 permission error.

## Probable Cause

ServiceNow Technical Support identified the affected user as an external user and reported that the following Access Control List rule was failing:

```text
now.virtual-agent.content.* - ux_route
```

The existing ACL is read-only, so it cannot be modified directly to accommodate the required external-user access.

## How the Issue Was Debugged

Use **Debug Security** to identify the ACL that is denying access. Reproduce the issue while debugging security for the affected external user, then review the security trace for the failing ACL. In this case, the trace identified:

```text
now.virtual-agent.content.* - ux_route
```

This provides a concrete starting point for the remediation instead of changing ACLs based only on the 403 message.

## Proposed Solution

Create a new ACL based on the existing read-only ACL:

```text
now.virtual-agent.content.* - ux_route
```

Configure the new ACL with a role that satisfies the business access requirement. ServiceNow Technical Support specifically proposed associating the following role:

```text
snc_external
```

If granting `snc_external` is not feasible, use another role that is appropriate for the intended external-user access model.

## Impact of Allowing `snc_external`

Cloning the read-only ACL and associating the clone with `snc_external` enables external users to use the Virtual Agent Popup Content Experience. They can fill out out-of-the-box or custom Form Content Topic Blocks and complete Service Catalog requests directly in the chat window.

This change grants access to the `ux_route` layout, but it does not bypass downstream security controls. External users must still pass:

- Table-, record-, and field-level ACLs.
- Service Catalog **Available For** criteria.

If a user passes the `ux_route` ACL but does not have permission to read a specific record or catalog item, the chat component may display an empty frame or a data-level permission error. The cloned ACL therefore enables the conversational experience without automatically exposing secured data.

For deployments that expose Virtual Agent on public portals or authenticated external portals such as `/csm` or `/csp`, allowing `snc_external` on the cloned ACL aligns with the expected Customer Service Management access model and helps prevent a broken chat experience.

## Implementation Considerations

Before applying the change, review the new ACL carefully to ensure that it grants only the access required for external users to open the intended chat links.

Recommended validation:

- Create the new ACL rather than attempting to modify the read-only ACL.
- Confirm that the selected role matches the business requirement.
- Test with an external user in DEV1 or DEV3.
- Repeat the original reproduction steps.
- Verify that authorized links open successfully.
- Verify that unrelated routes and content remain inaccessible.
- Document the ACL and include it in the appropriate update set before promotion.

## Validation Criteria

The change can be considered technically successful when:

1. An external user can select an authorized link returned by Virtual Agent or Now Assist chat.
2. The link opens without a 403 permission error.
3. The new ACL does not provide access to unrelated or restricted content.
4. Existing internal-user access continues to work as expected.

## Rollback

If the new ACL grants unintended access or causes regressions, deactivate or remove the newly created ACL and retest the original access behavior. Do not modify the original read-only ACL.

## Reference

- ServiceNow support case: **RECORD NUMBER**
- Issue: **Client can't open links in portal chat**
- Proposed by: ServiceNow Technical Support

## Related

- [[now-assist-faqs-general]]
