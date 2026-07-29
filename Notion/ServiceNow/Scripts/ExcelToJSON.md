---
aliases:
  - "ExcelToJSON"
area: "Scripts"
source: custom
tags:
  - excel-parser
  - nodejs
  - data-import
  - glide-record
  - scripts
---

# ExcelToJSON

Node.js script (runs outside the instance, not a background script) that uses `convert-excel-to-json` to parse an Excel sheet into JSON with named columns, then shows the pattern for turning each row into a `u_category` record insert. Used for bulk-importing catalog category data from a spreadsheet before scripting the actual per-row `GlideRecord` insert (e.g. via Import Set or a REST call).

```javascript

var obj = {};

const excelToJson = require('convert-excel-to-json');
const fs = require('fs');
const M = require('minimatch');

const result = excelToJson({
    source: fs.readFileSync(''),
    header:{
        rows: 1
    },
    columnToKey : {
        A: "Name",
        B: "Catalog Item (Tipo de Pedido BCTT)",
        C: "Category",
        D: "Environment",
        E: "Approval Group 1",
        F: "Assignment Group",
        G: "User Manager Approval"
    },
    sheets: 1
});
console.log('result :', result['Pedidos PRD'][1]);

// result['Pedidos PRD'].forEach(val =>{
// console.log('val :', val);
//     // var indexlabel = ptLabel.indexOf(val['A']);
//     // val['A'] = enLabel[indexlabel].toLowerCase().replace(/ /g, '_');
// })

// console.log('result.Sheet1 :', result.Sheet1);

// console.log(obj.length)

// var count = 0;

var grUCategory = new GlideRecord('u_category');
grUCategory.initialize();
grUCategory.u_name = '';
grUCategory.u_active = '';
grUCategory.u_business_service = '';
grUCategory.u_master_category = '';
grUCategory.u_description = '';
grUCategory.insert();
```

## Related

- [[Ler anexos excel via BG]]
