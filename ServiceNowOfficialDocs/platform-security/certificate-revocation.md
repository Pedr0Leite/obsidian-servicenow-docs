---
title: Quorum Controlled Certificate Revocation
description: The quorum-controlled certificate revocation for Code Signing certificates provides a secure mechanism for a Code Signing admin to revoke Code Signing certificates. The revocation process involves submitting a request that requires approval from multiple stakeholders. This workflow helps to prevent accidental or unauthorized revocations.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/platform-security/certificate-revocation.html
release: australia
topic_type: concept
last_updated: "2026-06-25"
reading_time_minutes: 1
breadcrumb: [Configure, Code Signing, Platform Security]
---

# Quorum Controlled Certificate Revocation

The quorum-controlled certificate revocation for [[code-signing-landing|Code Signing]] [[c_Certificates|certificates]] provides a secure mechanism for a Code Signing admin to revoke Code Signing certificates. The revocation process involves submitting a [[c_requestAPI|request]] that requires approval from multiple stakeholders. This workflow helps to prevent accidental or unauthorized revocations.

This topic provides the high-level process overview for securely revoking certificates between a trusted instance and a protected instance using a quorum-based approval workflow.

-   Request creation and [[export|export]] \(Trusted instance\): Initiate a quorum certificate revocation by creating a request with the required [[sc-configuration|configuration]] properties. Export the update set, which includes the revocation request and related data. See [[export_certificate|Export Revocation Request Configuration]]
-   Import and approval \(Protected instance\): Import the update set into the protected instance. Approvers receive notifications and must complete the approval workflow before the certificate is deleted. See [[import-certificate|Import the revocation request configuration]]
-   Optional MID Server restart: If enabled in the configuration, MID Servers on the protected instance are restarted after the certificate revocation. This forces immediate certificate resynchronization but can result in data loss for unprocessed or cached events. See [[cerificate-revocation-approval|Approve certificate revocation]]

**Note:**

Your **update set**expires after the time window defined by the **`com.snc.kmf.signature.validity_window`** property. If it expires, you can export a new signed update set from the trusted instance. This validity window applies to all update set operations, including export, import, and enabling Code Signing. This validity window is not related to the request time window that you specify when creating the request.

## Related

- [[export_certificate|Export Revocation Request Configuration]]
- [[import-certificate|Import the revocation request configuration]]
- [[cerificate-revocation-approval|Approve certificate revocation]]
- [[code-signing-landing|Code Signing]]
- [[c_Certificates|Certificates]]
- [[c_requestAPI|request]]
- [[export|Export]]
- [[sc-configuration|Configuration]]
