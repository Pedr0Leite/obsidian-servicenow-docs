---
aliases:
  - "Server and Client Script"
area: "Scripts"
source: custom
tags:
  - script-include
  - client-script
  - glide-ajax
  - onchange
  - server-client-communication
  - scripts
---

# Server and Client Script

Canonical Script Include + Client Script pair: an `onChange` client script calls a `GlideAjax`-backed Script Include (`AbstractAjaxProcessor`) to look up a value server-side (customer support hours remaining for a company) and pushes the result back into the form with `g_form.setValue`. The textbook pattern for any "fetch server data on field change" requirement.

```javascript
//SCRIPT INCLUDE
var customerSupportHours = Class.create();
customerSupportHours.prototype = Object.extendsObject(AbstractAjaxProcessor, {

	timeValue: function(){
		var companyID = this.getParameter('sysparm_company');

		var timeTable = new GlideRecord('u_customer_support_hours');
		timeTable.addQuery('u_company', companyID);
		timeTable.query();
		if(timeTable.next()){
			var timeLeft = timeTable.u_time_left;
			return timeLeft;
		}
	},

    type: 'customerSupportHours'
});



//CLIENT SCRIPT
function onChange(control, oldValue, newValue, isLoading, isTemplate) {
	if (newValue === '') {
	return;
	}
   //Type appropriate comment here, and begin script below
	var company = g_form.getValue('company');

  if(company != "") {
	var timeLeftFromSI = new GlideAjax('customerSupportHours');
	timeLeftFromSI.addParam('sysparm_name', 'timeValue');
	timeLeftFromSI.addParam('sysparm_company', company);
	timeLeftFromSI.getXML(getResponse);
}
	function getResponse(response) {
		var timeLeft = response.responseXML.documentElement.getAttribute("answer");
		g_form.setValue("u_time_left", timeLeft);

  }
}
```

## Related

- [[Server and Client Side Scripts]]
