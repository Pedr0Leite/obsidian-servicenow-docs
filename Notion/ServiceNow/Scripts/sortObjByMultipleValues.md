---
aliases:
  - "sortObjByMultipleValues"
area: "Scripts"
source: custom
tags:
  - javascript
  - array-methods
  - sorting
  - scripting
  - scripts
---

# sortObjByMultipleValues

Sorts an array of objects by one field with a tie-breaker on a second field, using `Array.sort` with `localeCompare` (e.g. sort by `Date` descending, then by `First_Name` alphabetically when dates match).

```javascript
var arrayOfObj = [
    {'First_Name': 'Pedro', 'Last_Name': 'Leite', 'Date': '25/04/2022'},
    {'First_Name': 'Pedro', 'Last_Name': 'Leite', 'Date': '24/04/2022'},
    {'First_Name': 'Sujith', 'Last_Name': 'Maruthingal', 'Date': '25/04/2022'},
    {'First_Name': 'John', 'Last_Name': 'Antony', 'Date': '23/04/2022'},
    {'First_Name': 'Akinrinola', 'Last_Name': 'Bolaji', 'Date': '25/04/2022'},
    {'First_Name': 'Awais', 'Last_Name': 'Waheed', 'Date': '24/04/2022'},
];

function sortBy(ar) {
    return ar.sort((a, b) => a.Date === b.Date ?
        a.First_Name.toString().localeCompare(b.First_Name) :
        b.Date.toString().localeCompare(a.Date));
  }
  console.log(sortBy(arrayOfObj));
```

## Related

- [[Fun with array methods!]]
- [[Remove duplicates_various ways]]
