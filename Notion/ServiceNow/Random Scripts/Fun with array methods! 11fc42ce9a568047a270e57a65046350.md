---
aliases:
  - "Fun with array methods!"
area: "Random Scripts"
source: notion-export
tags:
  - array-methods
  - javascript
  - glidequery
  - random-scripts
  - scripting
---

# Fun with array methods!

I've seen a couple of questions around working with arrays so I
 thought I'd write an article on some methods that are available to us 
in the system. There are also a few that *aren't* available and only work with ES6 (like array.find()).

I don't know *everything* so if you see any errors or places that I can clarify things, let me know in the comments below!

# Array Methods

If you build an array in JavaScript there a few methods that are 
available to you. The ones that you're most likely to come across are 
array.indexOf() and array.join(). The indexOf method allows you to find 
if an element is in an array and it'll either return the position in the
 array or -1 if it's not found. E.g., ["apple", 
"banana"].indexOf("apple") will return 0 since it's the first in the 
array and .indexOf("cherry") would return -1. The join method 
concatenates the array based on a separator value you give it.

But those ones are easy, there are a lot of examples and posts about those, so let's move on!

The one's I want to talk about today are **forEach**, **map**, **some**, and **filter**.

## Background

Each of these methods has similar syntax for using them. They are a 
method attached to an array, and they require a callback function, which
 can be defined elsewhere or in-line. Each of the methods I'm going to 
discuss today can take three arguments; **element**, **index**, and **array**.

```jsx
// Method A - The callback function

Array.method(callbackFn);

function callbackFn(element) {
   // do stuff with element
}

// Method B - Inline callback function

Array.method(function(e) {
   // do stuff with e
});
```

## forEach

**forEach** is like a for...in loop (you know, the 
classic var i=0; i<array.length; i++) in that it iterates over each 
item in an array and can do some "stuff" with the array element. I find 
forEach a little easier to read so let's kick it off with an example.

Let's say we have a catalog item for adding new configuration items 
and the CIs are stored in a multi-row variable set 
(MRVS). Alternatively, you could be getting this information from a 
supplier's API, from purchase orders, etc. The only thing that matters 
for this example is that we have either an array, or a stringified 
array.

```jsx
/* current.variables.new_ci_list =
"[ {
  "hostname" : "computer1",
  "ip" : "10.0.0.2"
}, {
  "hostname" : "computer2",
  "ip" : "10.0.0.3"
} ]"
*/

var config_items = JSON.parse(current.variables.new_ci_list);

config_items.forEach(function(ci){
   var ciGr = new GlideRecord('cmdb_ci_computer');
   ciGr.initialize();
   ciGr.setValue('name', ci.hostname);
   ciGr.setValue('ip_address', ci.ip);
   ciGr.insert();
});
```

In this example we're taking the entire MRVS, converting it to a 
JavaScript object using JSON.parse and then we iterate over each row, 
creating a cmdb_ci_computer record for each row

**But wait!** There can be times that you want to use the reliable for...in loop, and that's when you want to use a **break** to end your loop early and not have to iterate through every single item.

## map

The **map** method *creates a new array* 
populated with the result of calling your function on every item in your
 array. Here we can do some neat things with callbacks too so I'll show a
 few examples.

Have you ever come across an array of stringified JSON? No? Oh. Well I
 have! Here you can use JSON.parse as the callback function on your 
array to have it converted into an array of objects, which will make it 
easier to iterate and do things with.

```jsx
var jsonStrings = [ "{\"key1\":\"value1\"}", "{\"key2\":\"value2\"}" ];

var jsonArray = jsonStrings.map(JSON.parse);

gs.info(jsonArray);

/*
[
  {
    "key1": "value1"
  },
  {
    "key2": "value2"
  }
]
*/
```

Now we can use that jsonArray variable with a forEach to process the data! Cool. What else?

Ever have an array with awkward white spaces in it?

```jsx
var ughSoManySpaces = [ "apple ", " banana ", " cherry\n" ]

var freshAndClean = ughSoManySpaces.map(String.trim);

gs.info(freshAndClean);
/*
[
  "apple",
  "banana",
  "cherry"
]
*/
```

Let's say you have an array of objects and we want to concatenate 
some of the fields. Here we'll say we have a bunch of users, but we just
 want their full name.

```jsx
var users = [ { "last_name": "Romanoff", "first_name": "Natasha" }, { "last_name": "Barton", "first_name": "Clint" } ];

var fullNames = users.map(function(user) {
    return gs.getMessage("{0} {1}", [ user.first_name, user.last_name ]);
});

gs.info(fullNames);
/*
[
  "Natasha Romanoff",
  "Clint Barton"
]
*/
```

One more. Same as the previous example, but the only thing you care 
about is one of the properties. Here we'll say we have a bunch of users,
 but we just want the usernames.

```jsx
var users = [ { "username": "nromanoff", "first_name": "Natasha" }, { "username": "cbarton", "first_name": "Clint" } ];

var firstNames = users.map(function(user) { return user.username; });

gs.info(firstNames);
/*
[
  "nromanoff",
  "cbarton"
]
*/
```

We'll talk about this one a little more down below, but for now I 
think that gives a good idea of what it does and how you can use it.

## some

Time for **some** fun. Get it? The **some** method tests if there is at least one element in the array that passes a test in your function. **some** will return true if it finds *any*
 element in your array that evaluates as true from your function. The 
neat part about this is that it will stop testing values when it finds 
its first true result.

For this example, we have an array of numbers and we want to know if 
any of them are divisible by 2. We'll print out the element that's being
 processed so we can see how it stops at the first true result.

```jsx
var numbers = [ 1, "cherry", 2, 4, 6, 8, 10 ];

var divisibleByTwo = numbers.some(function(number) {
    gs.info(number);
    return number % 2 === 0;
});

gs.info(divisibleByTwo);

/*
1
cherry
2
true
*/
```

We can see from the gs.info output that it evaluated 1, cherry, and 
2, and stopped when it got to 2 because it found an element that met our
 test of the element being divisible by two.

the some method is pretty straight forward so I'll just give one more
 example. We're going to look at an array of user objects for a specific
 person.

```jsx
var theBobs = [
{ "first_name": "Bob", "last_name": "Slydell" },
{ "first_name": "Bob", "last_name": "Porter" },
{ "first_name": "Bob", "last_name": "Seger" },
{ "first_name": "Bob", "last_name": "Squarepants" },
{ "first_name": "Bob", "last_name": "L'Builder" },

];

var spongeyBob = theBobs.some(function(bob) {
    return gs.getMessage("{0} {1}", [ bob.first_name, bob.last_name ]) === "Bob Squarepants";
});

gs.info(spongeyBob);
// true
```

## filter

On to **filter**! ****This method creates a new array *with all the elements*
 that pass the test in our function. It's a little bit like some where 
we want our function to evaluate true/false for each element. But in 
this case, instead of stopping at the first result and only telling us 
whether *any* element passes, it gives us back an array containing the specific elements that pass.

There's a super common example for getting unique elements out of an 
array that's worth discussing (Side-note: ServiceNow has a global API 
called [ArrayUtils](https://developer.servicenow.com/dev.do#!/reference/api/rome/server_legacy/c_ArrayUtilAPI#r_AU-unique_A?navFilter=ArrayUtil) that also has a unique method).

```jsx
var notUnique = [ "a", "a", "b", "c", "a", "b" ];

var unique = notUnique.filter(
  function (letter, index, originalArray){
  	return originalArray.indexOf(letter) === index;
});

gs.info(unique);
/*
[
  "a",
  "b",
  "c"
]
*/
```

Let's unpack this one! If you remember way back when in the **Background** section, we discussed that each of these methods can take three parameters: **element**, **index**, and **array**.
 The other important bit is that the indexOf method tells you the first 
place that the element is seen in the array. So here's what's happening.
 We're calling the filter method with the letter (the array element), 
the index (its place in the array), and the originalArray (the third, 
array parameter). The test that we built checks for the first place the 
letter appears in the array and whether it's the same index (position) 
as the element we're currently looking at.

When **filter** starts, we have the letter a with an 
index of 0 because it's the first element in the array (remember that 
arrays start at 0). indexOf will return 0 because that's the first time 
the letter appears, and 0 === 0 so its returned as a value. The second 
element it processes is *another* letter a. This time index is 1 
because it's the second item in the array. indexOf still returns 0 
because that's the first time that it appears in the array. 1 != 0 so it
 evaluates as false and it's not returned. It continues on with each 
other element in the array, checking them all the same way.

Let's get back to working with objects. In this example we have an 
array of food objects and with their allergens listed as a property. We 
have some users who are allergic to peanuts so we only want foods that 
are nut free!

```jsx
var foods = [
  { "name": "Peanut Butter Cup", "allergens": [ "peanut", "milk" ] },
  { "name": "Jelly Beans", "allergens": [] },
  { "name": "Kit Kat", "allergens": [ "milk", "wheat" ] }
];

var peanutFree = foods.filter(function(food){
  return food.allergens.indexOf("peanut") === -1;
});

gs.info(peanutFree);

/*
[
  {
    "name": "Jelly Beans",
    "allergens": []
  },
  {
    "name": "Kit Kat",
    "allergens": [
      "milk",
      "wheat"
    ]
  }
]
*/
```

# Cool story. What now?

Have you heard of the GlideQuery API? Not Glide*Record*, but Glide*Query*? If not, you can read all about it in [Peter Bell's GlideQuery Series](https://developer.servicenow.com/blog.do?p=/tags/glidequery/) on the ServiceNow Developer Blog. I'm not going to go over how GlideQuery works, but what's important is that it uses the [**Stream** API](https://docs.servicenow.com/bundle/paris-application-development/page/app-store/dev_portal/API_reference/Stream/concept/StreamGlobalAPI.html#StreamGlobalAPI), which has the methods we listed above plus a toArray method.

You should definitely go read [GlideQuery - Stream Processing Part 1](https://developer.servicenow.com/blog.do?p=/post/glidequery-p6/) and [GlideQuery - Stream Processing Part 2](https://developer.servicenow.com/blog.do?p=/post/glidequery-p7/) for more depth in how to leverage GlideQuery and excellent examples of using these methods (and more!).

So, one last example before we leave. Here you have a single username
 and you want the sys IDs of all the groups that they manage.

```jsx
var user = 'Cab Approver';
var userid= gs.getUser().getUserByID(user).getID();
var managedGroups = new global.GlideQuery('sys_user_group')
.where('manager',userid)
.select()
.toArray(100)
.map(function(e){return e.sys_id;});

gs.info(managedGroups);
/*
[
  "5f63e48fc0a8010e00eeaad81cd4dd37",
  "b85d44954a3623120004689b2d5dd60a",
  "b97e89b94a36231201676b73322a0311"
]
*/
```

# Recap!

Arrays are cool and there are some awesome methods available to you 
to help you process data. When you find yourself doing a for...in, keep 
in mind that there some other options that might make your code a little
 easier to read for the next person who comes along.

## Related

- [[Random Scripts]]
- [[Create translation for an existing choice]]
- [[Ler anexos excel via BG]]
- [[EfficientGlideRecord (Client-side)]]