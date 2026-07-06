---
title: "Query ldap server"
aliases:
  - Query ldap server
tags:
  - servicenow-dev-program
  - code-snippet
  - query-ldap-server
  - script-includes
---

# Query ldap server by config sys_id
Interact with GlideLDAP using a fluent wrapper. Handy for querying ldap server for non-persistent data for example via remote tables.

# How to use it?
Configure LDAP server in *ldap_server_config* table
Query server from serverside script using script include LDAPQuery

# Example 1: get one entry

```javascript
var result = new LDAPquery()
	.setRDN('')                                      //set relative start 
	.setFilter('uid=einstein')                       //set filter
	.setConfig('2fd003c083e07e10557ff0d6feaad3d7')   //set the sys_id for ldap_server_config record
	.getOne();                                       //returns first entry as js object
gs.info(result.telephoneNumber);
```
```
output:
*** Script: 314-159-2653
```

# Example 2: get the iterable for query

```javascript
var result = new LDAPquery()
	.setRDN('ou=scientists') 
	.setPagination(1000)                              //set how many records per page
	.setConfig('2fd003c083e07e10557ff0d6feaad3d7')
	.getIterable();                                   //returns iterable result object

var item;
while (item = result.next()) {
	gs.info(JSON.stringify(j2js(item), null, 2)); //note that next returns a java object, hence the j2js to convert to js
}
```
```
output:
*** Script: {
  "dn": "ou=scientists,dc=example,dc=com",
  "objectClass": "groupOfUniqueNames^top",
  "ou": "scientists",
  "source": "ldap:ou=scientists,dc=example,dc=com",
  "uniqueMember": "uid=einstein,dc=example,dc=com^uid=tesla,dc=example,dc=com^uid=newton,dc=example,dc=com^uid=galileo,dc=example,dc=com",
  "cn": "Scientists"
}
*** Script: {
  "dn": "ou=italians,ou=scientists,dc=example,dc=com",
  "objectClass": "groupOfUniqueNames^top",
  "ou": "italians",
  "source": "ldap:ou=italians,ou=scientists,dc=example,dc=com",
  "uniqueMember": "uid=tesla,dc=example,dc=com",
  "cn": "Italians"
}
LDAP SEARCH: >>Next Page 
```

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
