---
aliases:
  - "Remove duplicates_various ways"
area: "Scripts"
source: custom
tags:
  - javascript
  - array-methods
  - scripting
  - scripts
---

# Remove duplicates_various ways

A grab-bag of plain-JS array utilities: array intersection (`arrDifference`), and four different ways to dedupe an array (`filter`+`indexOf`, a reusable `disctinct` predicate, a manual `unique_array` builder, and a sort-then-skip-adjacent version). Good reference when picking a dedupe approach for a GlideRecord result set converted to an array.

```javascript
var arr1 = ['1@cin.com','asdf2',3,4];
var arr2 = ['1@cin.com', 'pedro@dsalkj.com',3,4,5,6, 'asdf2'];

function arrDifference (arr1, arr2) {

            var arr = [];
            arr1 = arr1.toString().split(',').map(String);
            console.log("FIRST: " + arr1);
            arr2 = arr2.toString().split(',').map(String);
            console.log(arr2);

            // for array1
            for (var i in arr1) {
               if(arr2.indexOf(arr1[i]) != -1)
                arr.push(arr1[i]);
                console.log(arr);
            }
            // for array2
            for(i in arr2) {
               if(arr1.indexOf(arr2[i]) != -1)
               arr.push(arr2[i]);
              console.log(arr);
            }


            return arr.sort((x,y) => x-y);

         }
        console.log(arrDifference(arr1,arr2));


var arr3 = [ '1@cin.com', '5', 'asdf2', '3', '4', '1@cin.com', '3', '4', 'asdf2', 'pedro@dsalkj.com', '5', '5' ];
/*-----------------------------------------------------------------------*/
//Renmove duplicates V1
var x = (arr) => arr.filter((v,i) => arr.indexOf(v) === i);
console.log(x(arr3));

//Renmove duplicates V2
var disctinct = function(value, index, self){
  return self.indexOf(value) === index;
}

//Renmove duplicates V3
var removeDuplicates =  function(arr){
  var unique_array = [];
  for(var i = 0; i<arr.length; i++){
    if(unique_array.indexOf(arr[i]) == -1){
      unique_array.push(arr[i]);
    }
  }
  return unique_array;
};

var emails_and_sysID =  [''];
var emails_two = ['']

var array_concat = emails_two.concat(emails_and_sysID);

var disctinct_two = emails_and_sysID.filter(disctinct);

console.log(disctinct_two);
console.log(removeDuplicates(array_concat));
console.log(removeDuplicates(emails_two));
console.log(emails_two.filter(disctinct));

var emails_3 = [''];

// var gr = new GlideRecord('sys_user');
// 		gr.addQuery('active', true);
// 		gr.addQuery('email', emails);
// 		gr.query();
// 		while(gr.next()){
//       sysID.push(gr.sys_id.getValue()); //get the sysID of that record and store it in sysID array || never forget to use the getValue with the push and switch/case
// 			var index = emails.indexOf(gr.email.getValue()); //get the value of the email from the gliderecord and get the index of it
// 			emails.splice(index, 1); //remove the email that you found the match
//       var newEmails = emails.map()
// 		}
//Compare two Arrays and remove duplicates
var removeDuplicates_V2 = function(arr1, arr2){
  var count = 0;
  var start = false;
  var newSysID = [];
  for(i=0; i<arr1.length; i++){
    for(k = 0; k < arr2.length; k++){
        if(arr1[i] == arr2[k]){
          start = true;
        }
    }
    count++;
    if(count == 1 && start == false){
      newSysID.push(arr1[i]);
    }
    start=false;
    count=0;
  }
  return newSysID;
}


console.log(removeDuplicates_V2(emails_and_sysID, emails_two));




var removeDuplicates_V3 = function (arr){
  var temp=new Array();
  arr.sort();
  for(i=0;i<arr.length;i++){
    if(arr[i]==arr[i+1]) {continue}
    temp[temp.length]=arr[i];
  }
  return temp;
}

console.log(removeDuplicates_V3(emails_and_sysID, emails_two));
```

## Related

- [[Fun with array methods!]]
- [[sortObjByMultipleValues]]
