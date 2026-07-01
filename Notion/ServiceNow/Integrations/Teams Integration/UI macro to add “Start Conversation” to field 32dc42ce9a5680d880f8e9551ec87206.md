---
aliases:
  - "UI macro to add “Start Conversation” to field"
tags:
  - teams-integration
  - ui-macro
  - client-script
  - integrations
---

# UI macro to add “Start Conversation” to field

### UI macro to add “Start Conversation” to field

- [ ]  Create UI macro

```jsx
<?xml version="1.0" encoding="utf-8" ?>
<j:jelly trim="false" xmlns:j="jelly:core" xmlns:g="glide" xmlns:j2="null" xmlns:g2="null">
<g:evaluate var="jvar_guid" expression="gs.generateGUID(this);" />
<j:set var="jvar_n" value="show_incidents_${jvar_guid}:${ref}"/>
		
	<a id="${jvar_n}"
	   onclick="startConversation('${ref}');"
	   name="${jvar_n}"
	   onmouseout="lockPopup(event)"
	   tabindex="0"
	   title="${gs.getMessage('Open Teams chat')}" 
	>
   <img src="ms_teams.png" width="24" height="24"/>
   </a>

<script>
	
function startConversation(reference) {
  reference = reference.substring(reference.indexOf('.')+1, reference.length);
  var v = g_form.getValue(reference);
  var email;
  var gr = new GlideRecord('sys_user');
  if (gr.get(v)) {
    email = gr.email.toString();
  }
var url = 'msteams:/l/chat/0/0?users=' + email;
var w = getTopWindow();
w.open(url);
	
}
</script>	
</j:jelly>
```

- [ ]  Add the UI macro to the attributes of the requested field

## Related

- [[Teams Integration]]
- [[Creating Custom MS Teams Cards]]
- [[Conversational integration with Microsoft Teams -]]