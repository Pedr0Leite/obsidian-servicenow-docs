---
title: "BenchmarkRunner"
aliases:
  - BenchmarkRunner
tags:
  - servicenow-dev-program
  - code-snippet
  - benchmarkrunner
  - script-includes
---

# BenchmarkRunner
This Script Include is a tool for benchmarking individual functions, or comparing the execution time or two functions, to determine whether one method of doing something is faster than another, and by how much. 

For example (as you can see in the example below), comparing whether it's faster to *stringify* an object, or *parse* a JSON string into an object. 

## compareFunctions(methodOne, methodTwo, iterations, args)
Execute two functions with the specified arguments, and get info about which was faster
(and by how much).

## benchmarkSingleFunction(functionToBenchmark, iterations, args)
Benchmark a single function, and return information about how long it took for the specified number of iterations, and how long each iteration took on average. 

## Example server-side call (background script)
```javascript
var bmr;
var argsArray = [
	{
		"some_object": {
			"some_object": {
				"some_object": {
					"some_number": 123,
					"some_string": "abc123",
					"some_boolean": 123,
					"some_null": null,
					"some_method": function() {
						return "some_string";
					}
				}
			}
		}
	}
];

argsArray.push(JSON.stringify(argsArray[0]));

/*
	argsArray[0] now contains the object, and argsArray[1] contains the
	 stringified object.
	We'll test whether it's faster to stringify an object, or to parse an
	 object string.
 */

bmr = new BenchmarkRunner()

bmr.printComparisonResults(
	bmr.compareFunctions(
		thingOne,
		thingTwo,
		20000,
		argsArray
	),
	20000
);

function thingOne(arrArgs) {
	var strObj = JSON.stringify(arrArgs[0]);
	return strObj;
}

function thingTwo(arrArgs) {
	var objObj = JSON.parse(arrArgs[1]);
	return objObj;
}

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/README|Script Includes]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/Script Includes/sys_script_include_config|sys_script_include_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/API Model Template for New Application/README|API Model Template for New Application]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add Business Days/README|Add Business Days]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Add and Remove Group Member/README|Add and Remove Group Member]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Script Includes/Advanced REST API Integration with Retry Logic/README|Advanced REST API Integration with Retry Logic]]
