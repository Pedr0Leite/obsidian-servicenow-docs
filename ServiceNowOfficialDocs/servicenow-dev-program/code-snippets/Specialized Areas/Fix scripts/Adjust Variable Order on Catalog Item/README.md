---
title: "Adjust Variable Order on Catalog Item"
aliases:
  - Adjust Variable Order on Catalog Item
tags:
  - servicenow-dev-program
  - code-snippet
  - adjust-variable-order-on-catalog-item
  - fix-scripts
---

# Adjust Variable Order on Catalog Item

This Fix Script helps developers to automatically re-order all variables of a given Catalog Item or Variable Set.  
We all know the struggle, that initially we set up variables with fixed order steps such as: 100, 200, 300, 400    
However, over time, additional variables are inserted in between, resulting in a messy looking order, e.g.: 10, 15, 50, 55, 100, 200, 350, 300, 400   
This fix script should enable developers to keep their Catalog Items clean and structured, with minimal effort.   

### Instruction

At the beginning of the script you have to set the Sys ID of the Catalog Item or Variable Set where you want to re-order the variables.
The Script is built in a way, that this Sys ID can belong to either a Variable Set or Catalog Item.
Furthermore, you have to define the step size for the order. My recommendation would be to use 100.
 
```javascript
var sys_id = "e0ecd03947e29110d3c0c789826d4332"; //provide a catalog item or variable set sys id
var step_size = 100; //provide the step size for the new order
```

### Benefits

- Keep Catalog Items and Variable Sets clean and structured
- Reduce efforts maintaining variable orders

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Fields On All List Views/README|Add Fields On All List Views]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add Variable set to multiple catalog items/README|Add Variable set to multiple catalog items]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Add bulk users to VTB/README|Add bulk users to VTB]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Anonymise Data/README|Anonymise Data]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Assign user list to a specific group/README|Assign user list to a specific group]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Specialized Areas/Fix scripts/Authenticate using ScriptedRESTAPI/README|Authenticate using ScriptedRESTAPI]]
