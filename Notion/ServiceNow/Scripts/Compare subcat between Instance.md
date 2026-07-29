---
aliases:
  - "Compare subcat between Instance"
area: "Scripts"
source: custom
tags:
  - rest-api
  - table-api
  - glide-record
  - integrations
  - data-sync
  - scripts
---

# Compare subcat between Instance

Pulls records from a remote instance's Table API with an encoded query (URL-encoding `^`, `=`, `!`, `,`, `@` manually), then compares each remote record's `u_sub_category` against the local `u_subcategory` value and silently overwrites the local one (`setWorkflow(false)`, `autoSysFields(false)`) when they differ. Same compare-and-sync pattern as [[Compare Instance Tickets Shared-PT]] but for a data-sync fix instead of a missing-record report.

```javascript

var table = 'u_service_request'; //table

var offset = 0;
var limit = 2000;
var offsetIncrement = 2000;
var count = 0;
var total = 0;


// var encodedquery = "";

for(var i = 0; i< encodedquery.length; i++){
    if(encodedquery[i]=='^'){
      encodedquery = encodedquery.replace('^', '%5E');
    } else if(encodedquery[i]=='='){
      encodedquery = encodedquery.replace('=', '%3D');
    } else if(encodedquery[i]=='!'){
      encodedquery = encodedquery.replace('!', '%21');
    }else if(encodedquery[i]==','){
        encodedquery = encodedquery.replace(',', '%2C');
    } else(encodedquery[i]=='@')
      encodedquery = encodedquery.replace('@', '%40');
  }

gs.log('Start compare job.', 'Compare instances');


	var endpoint = 'https://test.service-now.com/api/now/table/' + table + '?sysparm_query=' + encodedquery + '&sysparm_limit=' + limit + '&sysparm_offset=' + offset;
	var r = new sn_ws.RESTMessageV2();
	r.setEndpoint(endpoint);
	r.setHttpMethod('GET');
	r.setBasicAuth('','');
	r.setRequestHeader("Accept", "application/json");
	r.setRequestHeader('Content-Type', 'application/json');
	var response = r.execute();
	var parsed = JSON.parse(response.getBody());
    // gs.print('parsed: ' + response.getBody());
	var listMissingTickets = [];

		parsed.result.forEach(function (key) {
            var gr = new GlideRecord(table);
            var answer = gr.get(key.sys_id);
            total++;

            if (answer == false) {
            }
            if (answer == true) {
                if(answer.u_subcategory != key.u_sub_category){
                    count++;
                    listMissingTickets.push(key.number);
                    // gs.print(key.number + " has a different subCategory value");
                    //gs.print('Old Value: ' + answer.u_sub_category);
                    //gs.print('New Value: ' + key.u_sub_category);
                    gr.setValue('u_subcategory', key.u_sub_category);
                    gr.setWorkflow(false);
                    gr.autoSysFields(false);
                    gr.update();
                }
            }
        });

gs.log('Total records found: ' + total, "Compare instances");
gs.log('Total records that are different: ' + count, "Compare instances");
gs.print('listMissingTickets: ' + listMissingTickets);
```

## Related

- [[REST]]
- [[Compare Instance Tickets Shared-PT]]
