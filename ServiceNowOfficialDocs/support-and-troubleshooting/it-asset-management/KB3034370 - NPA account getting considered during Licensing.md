---
title: "NPA account getting considered during Licensing"
aliases:
  - KB3034370
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3034370
kb_number: KB3034370
last_modified: 2026-05-22
---

## NPA account getting considered during Licensing

  

### Issue

SaaS subscriptions linked to discovered users are flagged as `non_person_account = true` continuing to count toward the License Required value on the publisher's licensed software model. Setting the flag, remapping subscriptions to test users, and rerunning reconciliation has no effect on the count. The behaviour is consistent across SaaS publishers and integration types.

### Facts

This is working as expected. NPA (non-person account) records are not excluded from SAM reconciliation.

### Release

-   Yokohama,
-   Zurich

### Cause

-   The non\_person\_account field on the discovered user record is not consumed by SaaS reconciliation as an exclusion condition. Its only function is to participate in the SAM subscription license calculation, specifically the 15:1 compression rule that aggregates multiple non-person identities owned by a single primary user into a fractional license count.
-   SaaS reconciliation is model-driven. It evaluates subscription records against the subscription conditions defined on each software model and matches the resulting demand against entitlements. There is no out-of-the-box logic that inspects the non\_person\_account flag on the linked discovered user when reconciling against the licensed model. As a result, a subscription tied to a flagged user still matches the licensed model's conditions and continues to contribute to License Required. This is expected platform behaviour, not a defect.

### Resolution

Route the non-person subscriptions to a dedicated software model with a zero-cost entitlement so they are claimed away from the licensed model during reconciliation.

-   Navigate to Software Asset > Models and create a new software model or a sub-model under the publisher and product.
-   On the new model, add a subscription condition: `discovery_user.non_person_account = true`. Preview matching subscriptions before saving to confirm the reference field resolves correctly in the customer's instance.
-   If the new model and the original licensed model could both match the same subscription, configure model priority so the non-person model is evaluated first. Without explicit priority, reconciliation may continue binding the subscription to the licensed model.
-   Create an entitlement against the new model. Set the rights quantity above the expected non-person subscription count, set the unit cost to zero, and set the effective and expiration dates wide enough to cover the reconciliation window and future runs.
-   Run reconciliation against the publisher. Confirm that the non-person subscriptions now resolve to the new model, and the original licensed model's License Required value has dropped by the corresponding count.
