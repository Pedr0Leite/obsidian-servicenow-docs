---
aliases:
  - "Compare Instance Tickets Shared-PT"
area: "Scripts"
source: custom
tags:
  - rest-api
  - table-api
  - domain-separation
  - glide-record
  - integrations
  - migrations
  - scripts
---

# Compare Instance Tickets Shared-PT

Background script that paginates through another instance's Table API (`sn_ws.RESTMessageV2`, `sysparm_limit`/`sysparm_offset`) for a given table/domain/date-range, then checks locally with `GlideRecord.get(sys_id)` whether each remote record exists here — logging which ones are missing. Used to reconcile shared/domain-separated tickets between two instances.

```javascript
//sys_domain=caa4bb730a0aa02800f6e1da7ef95afc^
var table = 'incident'; //table
var startDateTime = "'2014-01-01','00:00:00'";
var endDateTime = "'2019-11-09','23:59:59'";

var offset = 0;
var limit = 20000;
var offset = 0;
var offsetIncrement = 20000;
var count = 0;
var total = 0;
var flag = true;

gs.log('Start compare job.', 'Compare instances');

while(flag) {
	var endpoint = 'https://.service-now.com/api/now/table/' + table + '?sysparm_query=' +
		"sys_created_on%3E%3Djavascript:gs.dateGenerate(" + startDateTime + ")%5Esys_created_on%3C%3Djavascript:gs.dateGenerate(" + endDateTime + ")%5Esys_domain%3Dcaa4bb730a0aa02800f6e1da7ef95afc" +
// 		"task.sys_domain%3Dcaa4bb730a0aa02800f6e1da7ef95afc" +
		"%5EORDERBYDESCsys_created_on&sysparm_fields=sys_id%2Cnumber&sysparm_limit=" + limit + "&sysparm_offset=" + offset;
	//%2C  - sysparm_fields separator
	var r = new sn_ws.RESTMessageV2();
	r.setEndpoint(endpoint);
	r.setHttpMethod('GET');
	r.setBasicAuth('esb.user', '6e1978b3a8');
	r.setRequestHeader("Accept", "application/json");
	r.setRequestHeader('Content-Type', 'application/json');
	var response = r.execute();
	var parsed = JSON.parse(response.getBody());

	var listMissingTickets = {};

	parsed.result.forEach(function (key) {
		var gr = new GlideRecord(table);
		var yes = gr.get(key.sys_id);
		total++;
		if (yes == false) {
			//Prints and counts the number of the records that don't exist in the current instance
			count++;
			gs.log(key.number + " Is Missing", "Compare instances");
// 			gs.log(key.sys_id + " Is Missing", "Compare instances");

// 			listMissingTickets[key.number] = "" + key.closed_at;
		}
// 		if (yes == true) {
// 			//Prints and counts the number of the records that do exist in the current instance
// 			//count++;
// // 			gs.print(key.number + " Is Found");
// 			gs.print(key.sys_id + " Is Found");
// 		}
	});
	// 		gs.log('Test1: ' + total, "Joao Test");
	// 		gs.log('Test2: ' + flag, "Joao Test");
	// 		gs.log("Missing tickets " + JSON.stringify(listMissingTickets), "Compare instances");

	if (flag && total == limit + offset) {
		offset = offset + offsetIncrement;
	} else {
		flag = false;
	}

}

gs.log('Total records found: ' + total, "Compare instances");
gs.log('Total records missing: ' + count, "Compare instances");
```

## Related

- [[REST]]
- [[Domain Separation]]
- [[Compare subcat between Instance]]
