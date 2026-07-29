---
aliases:
  - "portal_fields_to_back_fields"
area: "Scripts"
source: custom
tags:
  - catalog-item
  - item-option-new
  - sys-dictionary
  - service-catalog
  - glide-record
  - scripts
---

# portal_fields_to_back_fields

Reads catalog variables (`item_option_new`) created today by a given user, maps each portal variable type (Check Box, Single Line Text, Date, etc.) to the equivalent `sys_dictionary` internal type, then generates the matching backend table field. Bridges "variables defined on a catalog item" to "columns on the table that will store them" when building out a custom table to receive catalog request data.

```javascript
var encodedQueryVariables = 'sys_created_onONToday@javascript:gs.beginningOfToday()@javascript:gs.endOfToday()^sys_created_by=pedro.leite';
// var encodedQueryVariables = 'sys_created_onONToday@javascript:gs.beginningOfToday()@javascript:gs.endOfToday()^sys_created_by=pedro.leite^name=client_age';

//variable types : dictionary internal types
var typeHashMap = {'CheckBox':'boolean', 'Single Line Text':'string', 'Multi Line Text': 'string', 'Date':'glide_date', 'Lookup Select Box':'choice'};

var variables = new GlideRecord('item_option_new');
variables.addEncodedQuery(encodedQueryVariables);
variables.query();

while(variables.next()){
    var typeValue = variables.getDisplayValue('type');

    if(typeHashMap[typeValue]){

        //new field
        var dictionary = new GlideRecord('sys_dictionary');
        dictionary.initialize();
        dictionary.setValue('name', 'name of table here');
        dictionary.setValue('internal_type', typeHashMap[typeValue]);
        dictionary.setValue('column_label', variables.sys_name);
        dictionary.setValue('element', variables.name);
        dictionary.setValue('sys_scope', ''); //Scope app

        if(typeValue == 'Multi Line Text'){
            dictionary.setValue('max_length', '400');

        }
        dictionary.insert();
    }
}
```

## Related

- [[Possible Ways for Making an Attachment Mandatory S]]
- [[ServiceNow – Service Catalog]]
