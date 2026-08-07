---
title: "Run DiscoverNow from a script using multiple IP addresses"
aliases:
  - KB0549380
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0549380
kb_number: KB0549380
last_modified: 2024-04-30
---

## Run DiscoverNow from a script using multiple IP addresses

  

### Issue

Run DiscoverNow from a script using multiple IP addresses 

  

# Background

* * *

In ServiceNow Product Documentation, the following article, [Run DiscoverNow from a Script](https://docs.servicenow.com/ "Run DiscoverNow from a Script"), describes the basic process of running DiscoverNow from a script. However, customers who are required to run this script and also require the ability to enter multiple IP addresses, are unable to get the process to work correctly.

When reviewing the code, we noticed that all of the variables were defined globally, so we suggest that the code be encapsulated in a function. This resolves the issue. 

When using short variables such as _d_ (as seen in the following script example), and defining the variable globally, it is very easy for the variable to be overwritten if another script is also using a globally defined variable called _d_, elsewhere on the system. Encapsulating the code within a function fences off the variables, which are defined _locally_ and can not be re-defined outside of that function.

The next section provides an example for customers who may require the same functionality. 

# Example Script

* * *

function RunMyDiscoverNow() {

//Enter the IP Adresses in the Array IPAdresses, and comma seperate
//Example: "x.x.x.1, x.x.x.2, x.x.x.3"

var IPAdresses \= "10.200.218.27, 10.200.218.99, 10.200.218.191";

var iparray \= IPAdresses.split(",");

for (var i\=0; i < iparray.length; i++) {
  var ipaddr \= iparray\[i\]
  
  //Ensure that a valid MID server name is used as the 
  //2nd parameter to d.discoveryFromIP
  
  var d \= new Discovery();
  var statusID \= d.discoveryFromIP(ipaddr,'MIDSERVER1');
  gs.print("This is the address that was scanned " +ipaddr);
  } 
}

RunMyDiscoverNow();
