---
title: Perform tests using the Test Case form
description: Perform tests from an assigned test case and record results using the Test Case form.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/it-business-management/test-management/t\_PerformTestsUsingTheTestCaseForm.html
release: australia
product: Test Management
classification: test-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Performing tests and updating the test status, Test Management 1.0, Test Management applications, Strategic Portfolio Management]
tags:
  - it-business-management
  - test-management
  - qa
  - defects
  - itbm
  - type-task
---

# Perform tests using the Test Case form

Perform [[c_Tests|tests]] from an assigned test case and record results using the Test Case form.

## Before you begin

Role required: tm\_tester

## Procedure

1.  Navigate to **All** &gt; **Test Management** &gt; **Test Execution** &gt; **[[c_TestPlans|Test Plans]]**.

2.  Click the assigned test case in the **[[c_TestCases|Test Cases]]** related list.

3.  Set the **Execution Status** field on the Test Case form to **In progress** and click **Save**.

4.  In the Tests related list, open the first test.

    The test order is determined by the number in the **Order** field.

5.  Set the **Status** field for the test to **In progress**.

6.  Right-click the form header and click **Save**.

7.  Perform the steps outlined in the **Detailed description** field.

8.  Record the result in the **Actual result** field.

9.  Compare the actual result to the expected result and update the test status in the **Status** field to one of the following:

    -   Passed
    -   Failed
    -   Blocked
10. Click **Update**.

11. Repeat steps 4-10 for the remaining tests in the test case.

12. After all of the tests are complete, update the test case status.

    For more information, see [Update the status of a test case](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-business-management/test-management/t_UpdateTheStatusOfATestCase.md).


**Parent Topic:**[Performing tests and updating the test status](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-business-management/test-management/c_Tester.md)

## Related

- [[c_Tests|Tests]]
- [[c_TestPlans|Test plans]]
- [[c_TestCases|Test cases]]
