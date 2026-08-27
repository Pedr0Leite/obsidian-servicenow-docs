---
aliases:
  - "EfficientGlideRecord (Client-side)"
area: "Frameworks Libraries"
source: notion-export
tags:
  - glide-record
  - client-scripting
  - glide-ajax
  - performance
  - frameworks
---

# EfficientGlideRecord (Client-side)

# [EfficientGlideRecord](https://snprotips.com/efficientgliderecord) (Client-side) (LINK)

![](https://images.squarespace-cdn.com/content/v1/56709605c647ada061ec9ed8/77bdafc0-7f02-40de-a96b-a20e9d08b7b9/ServiceNow+-+Third+Edition+1.jpg?format=300w)

EfficientGlideRecord is a client-side API class, from which you can perform asynchronous client-side GlideRecord-style queries while **maximizing performance** (eliminating the negative performance impact of using the client-side GlideRecord object) and **without having to create a separate GlideAjax Script Include**!

Every senior ServiceNow developer knows that *client-side GlideRecord queries are slow and inefficient*, and that it's far preferable to use a **GlideAjax** call. However, GlideAjax can be a REAL pain to implement. I've got [an *entire article*](https://ajax.snc.guru/) about using GlideAjax from both a client and server perspective. Even I have to look up my own article from time to time to remind myself of the correct patterns when I need to use it, and I groan every time I think about having to create ***yet another* Script Include** just to handle this one little use-case in this unique application scope or something.

A couple days ago, I was whingeing on the [ServiceNow Developers Discord](https://discord.snc.guru/) about the poor performance (and inaccurate documentation) of the client-side GlideRecord API. I was wishing there was something better that didn’t require me to make a whole separate Script Include just to query a single record from the database and get the value of a few fields on that record in my Client Script.

![](https://images.squarespace-cdn.com/content/v1/56709605c647ada061ec9ed8/7ed599ed-bf1e-457c-a776-786871ca6580/has+to+be+a+better+way.gif?format=300w)

Unfortunately, that’s just the way it is. Client-side GlideRecord is massively inefficient, far too slow, and returns way too much unnecessary data to be used commonly in production code. *GlideAjax is simply the best and most efficient method for looking up data from client-side scripts*.

### At least, *it was*… ***until now***!

Around noon, after searching for a better solution for another couple of hours, I finally decided:"*FINE. I'll write my OWN GlideRecord! With better performance, and more functionality!*"

So, I did. And now I’m sharing that solution with you!

This consists of two files: A client-callable Script Include that does the back-end work for us, and a Global UI Script that acts as the client-side GlideRecord alternative (which I very creatively named `EfficientGlideRecord`)

# Index

- [EfficientGlideRecord APIs](https://snprotips.com/efficientgliderecord#EfficientGlideRecord)
    - [addField(fieldName)](https://snprotips.com/efficientgliderecord#addField)
    - [addQuery(fieldName, operator, fieldValue)](https://snprotips.com/efficientgliderecord#addQuery)
    - [addEncodedQuery(encodedQueryString)](https://snprotips.com/efficientgliderecord#addEncodedQuery)
    - [addNullQuery(fieldName)](https://snprotips.com/efficientgliderecord#addNullQuery)
    - [addNotNullQuery(fieldName)](https://snprotips.com/efficientgliderecord#addNotNullQuery)
    - [orderBy(fieldName)](https://snprotips.com/efficientgliderecord#orderBy)
    - [orderByDesc(fieldName)](https://snprotips.com/efficientgliderecord#orderByDesc)
    - [setLimit(recordLimit)](https://snprotips.com/efficientgliderecord#setLimit)
    - [get(recordSysID)](https://snprotips.com/efficientgliderecord#get)
    - [query(callbackFn)](https://snprotips.com/efficientgliderecord#query)
    - [hasNext()](https://snprotips.com/efficientgliderecord#hasNext)
    - [next()](https://snprotips.com/efficientgliderecord#next)
    - [canRead(fieldName)](https://snprotips.com/efficientgliderecord#canRead)
    - [getValue(fieldName)](https://snprotips.com/efficientgliderecord#getValue)
    - [getDisplayValue(fieldName)](https://snprotips.com/efficientgliderecord#getDisplayValue)
- [Download](https://snprotips.com/efficientgliderecord#download)
- [Changelog](https://snprotips.com/efficientgliderecord#changelog)
- [Upcoming features](https://snprotips.com/efficientgliderecord#upcoming)
- [Code](https://snprotips.com/efficientgliderecord#code)

---

**Enjoying this article? Don’t forget to [subscribe to SN Pro Tips](https://snprotips.com/subscribe)**!

We never spam you, never sell your information to marketing firms, and never send you things that aren’t relevant to ServiceNow.We typically *only send out 1-4 newsletters per year*, but trust me - you don't want to miss them!

[**Subscribe here!**](https://snprotips.com/subscribe)

---

# EfficientGlideRecord

This new client-side API, *EfficientGlideRecord*, is a nearly-drop-in-replacement for the client-side GlideRecord API, at least when it comes to queries. I may implement insert/update/delete functionality in a later version.

The client-side API documentation is below. The actual code for the Script Include and Global UI Script can be found in [**this gist**](https://gist.github.com/thisnameissoclever/4ae299258bb6c1a1400394dd411d339f), or at the bottom of this page.

---

# addField(fieldName)

Add a field to retrieve from the target record(s).Any fields not specified by calling this method will not be available on the resulting EfficientGlideRecord object in the callback function after calling *.query()*. In this case, a warning will be shown in the console, and *.getValue('field_name')* will return a blank string.If a second argument (*getDisplayValue*) is not specified and set to true, then the field's display value will not be available on the resulting EfficientGlideRecord object in the callback function. In this case, *.getDisplayValue('field_name')* will return a blank string.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| fieldName | String | True | Add a field to retrieve from the target record(s).Any fields not specified by calling this method will not be available on the resulting EfficientGlideRecord object in the callback function after calling .query(). In this case, a warning will be shown in the console, and .getValue('field_name') will return a blank string.If a second argument (getDisplayValue) is not specified and set to true, then the field's display value will not be available on the resulting EfficientGlideRecord object in the callback function. In this case, .getDisplayValue('field_name') will return a blank string. |

**Example**

`var egrIncident = new EfficientGlideRecord('incident');
egrIncident.addField('number')
    .addField('assignment_group', true)
    .addField('assigned_to', true);

egrIncident.get('some_incident_sys_id', function(egrInc) {
    g_form.addInfoMessage(
        egrInc.getValue('number') + '\'s assignment group is ' +
        egrInc.getDisplayValue('assignment_group') + ' (sys_id: ' +
        egrInc.getValue('assignment_group') + ')\n' +
        'The assignee is ' + egrInc.getDisplayValue('assigned_to') + ' (sys_id: ' +
        egrInc.getValue('assigned_to') + ')'
    );
});`

---

## addQuery(fieldName, operator, fieldValue)

Add a query to the EfficientGlideRecord object.

By specifying a field name, operator, and value, you can perform all sorts of queries.

If only

**two arguments**

are specified, then it's assumed that the first is the field name and the second is the field value. The operator will automatically be set to

```
"="
```

.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| fieldName | String | True | The name of the field to perform the query against. |
| operator | String | False | The operator to use for the query.Valid operators: `=`, `!=`, `&gt;`, `&gt;=`, &lt;, &lt;`=`, `STARTSWITH`, `ENDSWITH`, `CONTAINS`, `DOES NOT CONTAIN`, `IN`, `NOT IN`, `INSTANCEOF`Note: If only two arguments are specified (fieldValue is not defined), then the second argument will be treated as the value, and the operator will automatically be set to `"="`. |
| fieldValue | String | True | The value to compare, using the specified operator, against the specified field. |

### Example

```
var egrIncident = new EfficientGlideRecord('incident');
    egrIncident.addField('number')
        .addField('assignment_group', true)
        .addField('assigned_to', true);

    egrIncident.get('some_incident_sys_id', function(egrInc) {
        g_form.addInfoMessage(
            egrInc.getValue('number') + '\'s assignment group is ' +
            egrInc.getDisplayValue('assignment_group') + ' (sys_id: ' +
            egrInc.getValue('assignment_group') + ')\n' +
            'The assignee is ' + egrInc.getDisplayValue('assigned_to') + ' (sys_id: ' +
            egrInc.getValue('assigned_to') + ')'
        );
    });
```

---

## addEncodedQuery(encodedQueryString)

Add an encoded query string to your query. Records matching this encoded query will be available in your callback function after calling .query().

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| encodedQueryString | String | True | The encoded query string to use in your query. |

### Example

```
var egrIncident = new EfficientGlideRecord('incident');
egrIncident.addField('number');
egrIncident.addField('assignment_group', true);
egrIncident.addField('assigned_to', true);
egrIncident.addEncodedQuery('some_encoded_query_string');

egrIncident.get('some_incident_sys_id', function(egrInc) {
    g_form.addInfoMessage(
        egrInc.getValue('number') + '\'s assignment group is ' +
        egrInc.getDisplayValue('assignment_group') + ' (sys_id: ' +
        egrInc.getValue('assignment_group') + ')\n' +
        'The assignee is ' + egrInc.getDisplayValue('assigned_to') + ' (sys_id: ' +
        egrInc.getValue('assigned_to') + ')'
    );
});
```

---

## addNullQuery(fieldName)

Shorthand for

```
.addQuery(fieldName, '=', 'NULL')
```

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| fieldName | String | True | The name of the field to use in your query, getting only records where this field is empty. |

### Example

```
//Get IDs, numbers, and assignment groups for all child Incidents with missing short descriptions
new EfficientGlideRecord('incident')
    .addQuery('parent', g_form.getUniqueValue())
    .addNullQuery('short_description')
    .addField('number')
    .addField('assignment_group', true) //Get display value as well
    .query(function (egrIncident) {
        var incidentsWithoutShortDesc = [];
        while (egrIncident.next()) {
            incidentsWithoutShortDesc.push(egrIncident.getValue('number'));
        }
        if (incidentsWithoutShortDesc.length > 0) {
            g_form.addErrorMessage(
                'The following child Incidents have no short description:<br />* ' +
                incidentsWithoutShortDesc.join('<br />* ')
            );
        }
    });
```

---

## addNotNullQuery(fieldName)

Shorthand for this.addQuery(fieldName, '!=', 'NULL');.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| fieldName | String | True | The name of the field to use in your query, getting only records where this field is not empty. |

### Example

```
new EfficientGlideRecord('incident')
    .setLimit(10)
    .addQuery('assignment_group', '!=', 'some_group_sys_id')
    .addQuery('assigned_to', 'some_assignee_sys_id')
    .addNotNullQuery('assignment_group')
    .addField('number')
    .addField('short_description')
    .addField('assignment_group', true) //Get display value as well
    .orderBy('number')
    .query(function (egrIncident) {
        while (egrIncident.next()) {
            var logMsg = '';
            if (egrIncident.canRead('short_description')) {
                logMsg += 'Short description value: ' + egrIncident.getValue('short_description') + '\n';
            }
            if (egrIncident.canRead('number')) {
                logMsg += 'Number: ' + egrIncident.getValue('number') + '\n';
            }
            if (egrIncident.canRead('assignment_group')) {
                logMsg += 'Assignment group: ' + egrIncident.getValue('assignment_group') + ' (' +
                    egrIncident.getDisplayValue('assignment_group') + ')';
            }

            console.log(logMsg);
        }
    });
```

---

## orderBy(fieldName)

Orders the queried table by the specified column, in ascending order.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| fieldName | String | True | Orders the queried table by the specified column, in ascending order |

### Example

```
//Get IDs, numbers, and assignment groups for all child Incidents with missing short descriptions
new EfficientGlideRecord('incident')
    .addQuery('parent', g_form.getUniqueValue())
    .addNullQuery('short_description')
    .addField('number')
    .addField('assignment_group', true) //Get display value as well
    .orderBy('number')
    .query(function (egrIncident) {
        var incidentsWithoutShortDesc = [];
        while (egrIncident.next()) {
            incidentsWithoutShortDesc.push(egrIncident.getValue('number'));
        }
        if (incidentsWithoutShortDesc.length > 0) {
            g_form.addErrorMessage(
                'The following child Incidents have no short description:<br />* ' +
                incidentsWithoutShortDesc.join('<br />* ')
            );
        }
    });
```

---

## orderByDesc(fieldName)

Orders the queried table by the specified column, in descending order

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| fieldName | String | True | Orders the queried table by the specified column, in descending order |

### Example

```
//Get IDs, numbers, and assignment groups for all child Incidents with missing short descriptions
new EfficientGlideRecord('incident')
    .addQuery('parent', g_form.getUniqueValue())
    .addNullQuery('short_description')
    .addField('number')
    .addField('assignment_group', true) //Get display value as well
    .orderByDesc('number')
    .query(function (egrIncident) {
        var incidentsWithoutShortDesc = [];
        while (egrIncident.next()) {
            incidentsWithoutShortDesc.push(egrIncident.getValue('number'));
        }
        if (incidentsWithoutShortDesc.length > 0) {
            g_form.addErrorMessage(
                'The following child Incidents have no short description:<br />* ' +
                incidentsWithoutShortDesc.join('<br />* ')
            );
        }
    });
```

---

## setLimit(recordLimit)

Limits the number of records queried from the database and returned in the response.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| limit | Number | True | The limit to use in the database query. No more than this number of records will be returned. |

### Example

```
//Does at least one child Incident exist without a short description?
new EfficientGlideRecord('incident')
    .setLimit(1)
    .addQuery('parent', g_form.getUniqueValue())
    .addNullQuery('short_description')
    .addField('number')
    .query(function (egrIncident) {
        if (egrIncident.hasNext()) {
            g_form.addErrorMessage(
                'At least one child Incident exists without a short description.'
            );
        }
    });
```

---

## get(recordSysID)

Gets a single record, efficiently, from the database by sys_id.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| sysID | String | True | The sys_id of the record to retrieve. Must be the sys_id of a valid record which the user has permissions to see, in the table specified in the constructor when instantiating this object. |
| callbackFn | Function | True | The callback function to be called when the query is complete.When the query is complete, this callback function will be called with one argument: the EfficientGlideRecord object containing the records resultant from your query. After querying (in your callback function), you can call methods such as `.next()` and `.getValue()` to iterate through the returned records and get field values. |

### Example

```
var egrIncident = new EfficientGlideRecord('incident');
egrIncident.setLimit(10);
egrIncident.addField('number');
egrIncident.addField('assignment_group', true);
egrIncident.addField('assigned_to', true);

egrIncident.get('some_incident_sys_id', function(egrInc) {
    g_form.addInfoMessage(
        egrInc.getValue('number') + '\'s assignment group is ' +
        egrInc.getDisplayValue('assignment_group') + ' (sys_id: ' +
        egrInc.getValue('assignment_group') + ')\n' +
        'The assignee is ' + egrInc.getDisplayValue('assigned_to') + ' (sys_id: ' +
        egrInc.getValue('assigned_to') + ')'
    );
});
```

---

## query(callbackFn)

Perform the async query constructed by calling methods in this class, and get the field(s) from the resultant record that were requested by calling

```
.addField(fieldName, getDisplayValue)
```

.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| callbackFn | Function | True | The callback function to be called when the query is complete.When the query is complete, this callback function will be called with one argument: the EfficientGlideRecord object containing the records resultant from your query. After querying (in your callback function), you can call methods such as .next() and .getValue() to iterate through the returned records, and get field values. |

### Example

```
new EfficientGlideRecord('incident')
    .setLimit(10)
    .addQuery('assignment_group', '!=', 'some_group_sys_id')
    .addQuery('assigned_to', 'some_assignee_sys_id')
    .addNotNullQuery('assignment_group')
    .addField('number')
    .addField('short_description')
    .addField('assignment_group', true) //Get display value as well
    .orderBy('number')
    .query(function (egrIncident) {
        while (egrIncident.next()) {
            console.log(
                'Short description value: ' + egrIncident.getValue('short_description') + '\n' +
                'Number: ' + egrIncident.getValue('number') + '\n' +
                'Assignment group: ' + egrIncident.getValue('assignment_group') + ' (' +
                egrIncident.getDisplayValue('assignment_group') + ')'
            );
        }
    });
```

---

## hasNext()

Check if there is a "next" record to iterate into using .next() (without actually positioning the current record to the next one).

Can only be called from the callback function passed into

```
.query()
```

/

```
.get()
```

after the query has completed.

### Example

```
//Does at least one child Incident exist without a short description?
new EfficientGlideRecord('incident')
    .setLimit(1)
    .addQuery('parent', g_form.getUniqueValue())
    .addNullQuery('short_description')
    .addField('number')
    .query(function (egrIncident) {
        if (egrIncident.hasNext()) {
            g_form.addErrorMessage(
                'At least one child Incident exists without a short description.'
            );
        }
    });
```

---

## next()

Iterate into the next record, if one exists.

Usage is the same as GlideRecord's

```
.next()
```

method.

Can only be run from the callback function after a query using

```
.query()
```

or

```
.get()
```

.

### Example

```
new EfficientGlideRecord('incident')
    .setLimit(10)
    .addQuery('assignment_group', '!=', 'some_group_sys_id')
    .addQuery('assigned_to', 'some_assignee_sys_id')
    .addNotNullQuery('assignment_group')
    .addField('number')
    .addField('short_description')
    .addField('assignment_group', true) //Get display value as well
    .orderBy('number')
    .query(function (egrIncident) {
        while (egrIncident.next()) {
            console.log(
                'Short description value: ' + egrIncident.getValue('short_description') + '\n' +
                'Number: ' + egrIncident.getValue('number') + '\n' +
                'Assignment group: ' + egrIncident.getValue('assignment_group') + ' (' +
                egrIncident.getDisplayValue('assignment_group') + ')'
            );
        }
    });
```

---

## canRead(fieldName)

Returns true if the specified field exists and can be read (even if it's blank).

Will return false in the following cases:

- The specified field on the current record cannot be read
- The specified field does not exist in the response object (which may happen if you don't add the field to your request using .addField()).
- The specified field does not exist in the database

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| fieldName | String | True | The name of the field to check whether the user can read or not. |

### Example

```
new EfficientGlideRecord('incident')
    .setLimit(10)
    .addQuery('assignment_group', '!=', 'some_group_sys_id')
    .addQuery('assigned_to', 'some_assignee_sys_id')
    .addNotNullQuery('assignment_group')
    .addField('number')
    .addField('short_description')
    .addField('assignment_group', true) //Get display value as well
    .orderBy('number')
    .query(function (egrIncident) {
        while (egrIncident.next()) {
            var logMsg = '';
            if (egrIncident.canRead('short_description')) {
                logMsg += 'Short description value: ' + egrIncident.getValue('short_description') + '\n';
            }
            if (egrIncident.canRead('number')) {
                logMsg += 'Number: ' + egrIncident.getValue('number') + '\n';
            }
            if (egrIncident.canRead('assignment_group')) {
                logMsg += 'Assignment group: ' + egrIncident.getValue('assignment_group') + ' (' +
                    egrIncident.getDisplayValue('assignment_group') + ')';
            }

            console.log(logMsg);
        }
    });
```

---

## getValue(fieldName)

Retrieve the database value for the specified field, if the user has permissions to read that field's value.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| fieldName | String | True | The name of the field to retrieve the database value for. |

### Example

```
//Get IDs, numbers, and assignment groups for all child Incidents with missing short descriptions
new EfficientGlideRecord('incident')
    .addQuery('parent', g_form.getUniqueValue())
    .addNullQuery('short_description')
    .addField('number')
    .addField('assignment_group', true) //Get display value as well
    .query(function (egrIncident) {
        var incidentsWithoutShortDesc = [];
        while (egrIncident.next()) {
            incidentsWithoutShortDesc.push(egrIncident.getValue('number'));
        }
        if (incidentsWithoutShortDesc.length > 0) {
            g_form.addErrorMessage(
                'The following child Incidents have no short description:<br />* ' +
                incidentsWithoutShortDesc.join('<br />* ')
            );
        }
    });
```

---

## getDisplayValue(fieldName)

Retrieve the display value for the specified field, if the user has permission to view that field's value.

Can only be called from the callback function after the query is complete.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| fieldName | String | True | The name of the field to retrieve the display value for. |

### Example

```
//Get assignment groups for child Incidents for some reason
new EfficientGlideRecord('incident')
    .addQuery('parent', g_form.getUniqueValue())
    .addField('assignment_group', true) //Get display value as well
    .query(function (egrIncident) {
        var assignmentGroupNames = [];
        while (egrIncident.next()) {
            assignmentGroupNames.push(egrIncident.getDisplayValue('assignment_group'));
        }
        //todo: Do something with the assignment group names
    });
```

---

# [**Download Latest**](https://gist.github.com/thisnameissoclever/4ae299258bb6c1a1400394dd411d339f?ts=4)

You can simply copy-and-paste the code into a new Script Include and Global UI Script in your environment, by copying the code from [this Gist](https://gist.github.com/thisnameissoclever/4ae299258bb6c1a1400394dd411d339f?ts=4).

# Changelog

- [v1.0](https://gist.github.com/thisnameissoclever/4ae299258bb6c1a1400394dd411d339f?ts=4)
    - Initial public release

# Upcoming features

- Ability to insert/update/delete using EfficientGlideRecord
- Probably some bug-fixes. I've tested this thoroughly and am not aware of any bugs, but you jerks are probably going to identify some tiny little bug in my code that will make the inside of my brain itch until I fix it.
    - *Just kidding, I absolutely adore people who report any bugs in my code. Please do tell me if you notice any actual or potential bugs.*
- If you have additional feature-requests, please **let me know in the comments below the announcement article!**

# Code

Below, you can see the exact code in the Gist, which you can copy and paste into your environment if you prefer that over importing the XML for the Script Include using the above instructions.

## Related
- [[Tips & tricks]]

- [[Frameworks Libraries]]
- [[AngularJS in SN]]
- [[ReactJS in SN]]