---
aliases:
  - "Impersonate a user via script"
tags:
  - script-include
  - glide-record
  - impersonation
  - scripting
---

# Impersonate a user via script

```jsx
var grSCC = new GlideRecord('sn_customerservice_case');
if (grSCC.get('9a74dee183d3ba5038241c426daad33c')) {
var systemAdminSysId = "abc";
	// Start impersonation
gs.getSession().impersonate(systemAdminSysId);

grSCC.comments = 'test';
grSCC.update()
// End impersonation
session.onlineUnimpersonate();

}

```

## Related

- [[Server and Client Side Scripts]]
- [[Script include Advance structure - Inheritance]]
- [[Security & ACL]]