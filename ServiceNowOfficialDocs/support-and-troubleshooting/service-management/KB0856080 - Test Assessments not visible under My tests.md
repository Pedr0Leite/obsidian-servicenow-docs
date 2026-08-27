---
title: "Test Assessments not visible under My tests"
aliases:
  - KB0856080
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856080
kb_number: KB0856080
last_modified: 2024-04-08
---

## Test Assessments not visible under My tests

  

### Issue

Under the "My Tests" module, the user is unable to see all his pending Test Assessments.

### Release

Orlando

### Cause

The test cases that are missing were created on the 19th of august while the assessments were created on the 11th of august.  
Meaning: The missing tests were added after the assessment was created which is why they do not appear in the assessment.  

### Resolution

The assessments are created when the "Test Manager" clicks on "Notify Tester" in the test plan.  
Unfortunately, there is no way to add tests to an assessment created above. The user would have two options:  
1\. Delete the old test plan and create a new test plan that includes all the tests (including the new ones) and then click "Notify Tester" for fresh assessments to be created.  
2\. Create a new separate test plan with just the new tests and then click "Notify Tester" so that a fresh assessment is created for the new tests.
