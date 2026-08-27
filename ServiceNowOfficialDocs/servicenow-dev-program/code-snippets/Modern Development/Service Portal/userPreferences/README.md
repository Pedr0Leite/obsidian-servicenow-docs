---
title: "userPreferences"
aliases:
  - userPreferences
tags:
  - servicenow-dev-program
  - code-snippet
  - userpreferences
  - service-portal
---

# userPreferences
By injecting `userPreferences` factory into your controller function you can easily get and set user preferences.

## Usage example

### Reading user preference

```javascript
api.controller=function(userPreferences) {
  /* widget controller */
  var c = this;
	
	userPreferences.getPreference('rowcount').then(function(response){
		c.rowcount = response;
	});
	
};
```

### Setting a user preference

```javascript
api.controller=function(userPreferences) {
  /* widget controller */
  var c = this;
	
	userPreferences.setPreference('rowcount', 10);
	
};
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal/Active Tickets Dashboard/README|Active Tickets Dashboard]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal/Search Sources/README|Search Sources]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal/dark-mode-switcher/README|dark-mode-switcher]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal/instance-badge/README|instance-badge]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal/sn-avatar/README|sn-avatar]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Modern Development/Service Portal/sn-choice-list/README|sn-choice-list]]
