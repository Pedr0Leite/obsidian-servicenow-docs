---
title: "Transaction cancelled :   are they normal/expected?"
aliases:
  - KB0793080
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0793080
kb_number: KB0793080
last_modified: 2025-09-29
---

## Transaction cancelled : are they normal/expected?

  

### Issue

Are "maximum execution time exceeded" and "cancelled by other transaction"  messages normal/expected or not?

### Release

All releases

### Cause

Transaction cancelations can be normal or expected behaviour, but it depends on the transaction.

For example "cancelled by other transaction" can come from an autocompleter;

A user typing in an autocomplete box will trigger an ajax transaction after a delay of more the 250ms , then another transaction is triggered if the user types an additional letter. The first transaction will be cancelled and a new transaction is triggered with the new string.

This is just one example but there are other places in the platform where this can happen.  
  
The "maximum execution time exceeded" is governed by the quota rules and i would not recommend to change these.  These can be a problem or again can be normal behaviour. For example a presence transaction has a time limit of 10 seconds, then a user loads a form in more than 10 seconds the presence transaction will be cancelled and retried in 15 seconds, this is a normal behaviour.

### Resolution

Problem transactions that get cancelled in the instance are transactions which take a very long time (out of the box this is 5 minutes) and are cancelled, in order o identify these, it is best to look at the Client Transactions module and sort by the response time / client response time
