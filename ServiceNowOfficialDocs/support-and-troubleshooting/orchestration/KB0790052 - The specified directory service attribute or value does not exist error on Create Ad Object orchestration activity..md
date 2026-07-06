---
title: "The specified directory service attribute or value does not exist error on Create Ad Object orchestration activity."
aliases:
  - KB0790052
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0790052
kb_number: KB0790052
last_modified: 2024-04-08
---

## Issue

When you use Create AD Object activity and pass certain values on the ObjectData field such as SN (for surname) you get the following error on the ECC message:

The attribute syntax specified to the directory service is invalid.  
  
HRESULT: \[-2147016693\]  
  
Stack Trace: at System.DirectoryServices.DirectoryEntry.CommitChanges()  
at CommitChanges(Object , Object\[\] )  
at System.Management.Automation.DotNetAdapter.AuxiliaryMethodInvoke(Object target, Object\[\] arguments, MethodInformation methodInformation, Object\[\] originalArguments)

## Resolution

You can either fix the format or remove the objectAD property. This would resolve the issue.
