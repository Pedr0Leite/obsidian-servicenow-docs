# ServiceNowOfficialDocs/application-development/automated-test-framework-atf — File Index

Navigation index for AI agents. One row per file in this directory (178 files). Auto-generated from frontmatter — do not hand-edit; regenerate via `scripts/gen_indexes.py` if files are added/removed.

---

| File | Title | Description |
|------|-------|-------------|
| `add-parameterized-data.md` | Add parameterized data sets | Add or import test data to specify parameter runtime values. |
| `add-parameterized-value-to-step.md` | Add a parameter to a test step | Add a variable to a test step to hold a particular type of data when the test runs. |
| `add-tests-suite-filter.md` | Add tests to a suite with a filter | Automate the creation of test suites by using a filter to dynamically add tests to a test suite when they match the filter conditions.… |
| `atf-active-manual-runners-module.md` | Active manual test runners | View the client test runners table filtered to show only those runners available to run manually-started tests. |
| `atf-active-sched-runners-module.md` | Active scheduled test runners | View the client test runners table filtered to show only those runners available to run tests to be started by a schedule. |
| `atf-add-child-suite.md` | Add child test suite to parent test suite | Add to a multi-level test suite by including a child test suite within a parent test suite. |
| `atf-add-test-to-suite.md` | Add test to an existing automated test suite | Add a test to a test suite that already exists. |
| `atf-admin-overview.md` | Administering the Automated Test Framework \(ATF\) | Enable or disable the Automated Test Framework, modify retention policies, move tests between instances, control user access to the… |
| `atf-admin-properties.md` | Properties | On the Properties form, you can set parameters that control how the system executes automated tests and test suites. |
| `atf-administer-rest.md` | Administering REST test step configurations | Set request and response payload sizes, filter request and response headers, and create basic auth profiles. |
| `atf-auto-flush.md` | Autoflush form | On the Auto Flush form, you specify a retention policy for a set of records on a given test results table. |
| `atf-auto-generate-tests.md` | Auto-generate ATF tests | Auto-generate ATF tests by selecting the auto-generate option either from the Auto-generate Tests module or Tests/Suites modules. |
| `atf-biz-rule-use.md` | Automated Test Framework use case: test a business rule | This use case illustrates testing a business rule with the Automated Test Framework. |
| `atf-breakpoint.md` | Debug an automated test using breakpoints | Pause a test to troubleshoot failures or unexpected behavior by adding a breakpoint for a particular test step. |
| `atf-breakpoints-rollback.md` | Implementing breakpoints | Breakpoints allow you to pause your test at any step of a test run in order to troubleshoot and test authoring. |
| `atf-build-overview.md` | Building and running automated tests with the Automated Test Framework | Basic tasks in the Automated Test Framework. |
| `atf-cancelling.md` | Cancelling automated tests and test suites | You can cancel automated tests and automated test suites that are running or are queued to run.You can cancel an automated test suite that… |
| `atf-client-test-runner-module.md` | Client test runner | The Client Test Runner opens a browser window or tab for running manually-started client automated tests. |
| `atf-cloud-runner-browser.md` | Cloud Runner browser | If you are running a test or a test suite, select the Cloud Runner browser option to run your tests in a cloud browser. |
| `atf-compare-runs.md` | Compare results and execution times for different automated test and suite results | You can compare execution times for different runs of an automated test or automated test suite. You can also compare results over time for… |
| `atf-conf-ws-comp-examples.md` | Configurable workspace components examples | To grasp how to interact with configurable workspace components, review these examples. |
| `atf-conf-ws-components.md` | Testable Configurable Workspace components | Learn about the components and its associated actions in the configurable workspace. |
| `atf-conf-ws.md` | Testing Configurable Workspace components | Simplify test creation by directly interacting with components on most Configurable Workspace pages via the Page Inspector. |
| `atf-config-desc-script.md` | Step description generation script | In a step configuration record, the step description generation script field determines the step description that the system generates when… |
| `atf-config-script.md` | Step execution scripts | In a step configuration record, the step execution script field determines what a step with this configuration does when it runs. |
| `atf-copy-test-suite.md` | Copy an automated test suite | Reduce time when creating tests by copying an entire test suite. Rename and modify the test suite after copying. The Copy Test Suite button… |
| `atf-copy-test.md` | Copy automated test | Copy an existing test, which you can then re-name and modify. |
| `atf-create-basic-auth-profile.md` | Create a basic auth profile using the Automated Test Framework | Create basic auth profiles to specify basic authentication credentials for Send Request - Inbound test steps. |
| `atf-create-custom-category.md` | Create a custom step configuration category | Create a custom step config category. |
| `atf-create-custom-step.md` | Create custom step configuration | Create a custom step configuration that can form the basis of new steps that run on the server. |
| `atf-create-reusable-tests.md` | Create a reusable test | Create a reusable test to avoid redundancy, ensuring better test maintenance and reliable test execution across the instance. |
| `atf-create-step.md` | Add steps to an automated test | Create a series of steps for an automated test to run in a specified order. |
| `atf-create-suite.md` | Create an automated test suite | Group automated tests into a suite you can execute as a batch. |
| `atf-create-template.md` | Create an automated test steps template | Reduce testing time by creating a template containing a list of steps to add all at once to an automated test. |
| `atf-create-test.md` | Create a new automated test | Create a named automated test containing a series of steps to execute. |
| `atf-create-tests-ws.md` | Create a test for Configurable Workspace interaction via Page Inspector | Leverage the Page Inspector to create tests by directly interacting with components on most Configurable Workspace pages. |
| `atf-custom-step-types.md` | Creating custom test step configurations | Step configuration records (or step configs) define how each step type behaves. You can create new step configurations that define custom… |
| `atf-data-policy-01-use.md` | Automated Test Framework use case: test a data policy | This use case illustrates testing a data policy with the Automated Test Framework. |
| `atf-edit-step-order.md` | Edit automated test step order | By default, steps execute in the order in which you created them. You can change this order by editing the Execution Order field. |
| `atf-edit-table-cleanup.md` | Modify data retention policy for ATF test results | Modify the Auto Flush data retention policy, which designates how long the system retains data, and referencing data, for test and test… |
| `atf-edit-template.md` | Edit automated test steps template | Edit an existing test template. |
| `atf-edit-test-step.md` | Change automated test step | If necessary, edit a test step after you create it. |
| `atf-enable-tests.md` | Enable or disable executing Automated Test Framework tests | Allow or prevent tests and test suites from executing on this instance. |
| `atf-excluded-from-rollback.md` | Tables excluded from rollback after running an automated test | The Automated Test Framework tracks data created by running tests and rolls back changes after testing. The system excludes certain tables… |
| `atf-filter-rest-headers.md` | Filter REST request and response headers | You can add a list of REST request and response headers that are not to be saved in step-result records. You can filter headers that might… |
| `atf-headless-browser-properties.md` | Headless Browser system properties | Below is a table of the properties you must have as you set up the ServiceNow Headless Browser for Automated Test Framework. |
| `atf-headless-browser.md` | Headless Browser for Automated Test Framework | Improve your UI testing by automating the creation of browsers to process Automated Test Framework (ATF) User Interface (UI) tests. This… |
| `atf-inspect-page-types.md` | Inspect different page types | Inspect and troubleshoot the functionality of different page types like UI Pages, Service Portal, Standard UI, and Custom URL using the… |
| `atf-intro.md` | Getting started with the Automated Test Framework | If you are new to the Automated Test Framework, read this overview to learn what the framework can do. Next, follow the tutorial to create… |
| `atf-landing-page.md` | Automated Test Framework \(ATF\) | The Automated Test Framework (ATF) enables you to create and run automated tests to confirm that your instance works after making a change.… |
| `atf-list-ui-actions-test-step.md` | List UI actions test steps | Select a UI action from a list to perform different actions on a list or a related list. |
| `atf-metadata-exception-triage.md` | Metadata exception list | The following list of tables are not supported by the ATF tests failure resolution feature. |
| `atf-modify-retention-test-clients.md` | Manage status and retention policies for automated test client runners | Modify how often active client test runners report in to the system and how long the system retains records for inactive client test… |
| `atf-move-test.md` | Moving automated tests from one instance to another | Move automated tests from one instance to another using the normal process for update sets. |
| `atf-next-step-concepts.md` | Next steps with the Automated Test Framework | After you feel comfortable creating and running simple tests, explore the more advanced features of the Automated Test Framework. |
| `atf-optimize-perf.md` | Optimizing automatic test performance | You can troubleshoot automatic test performance by inspecting system transaction log records and potentially shorten execution time by… |
| `atf-page-inspector.md` | Page Inspector | Identify the HTML and JavaScript page components in your user interfaces that are available for custom UI testing. Enable automated testing… |
| `atf-passing-data.md` | Passing data from one automated test step to another | Some automated test steps create data that you can use as an input to a subsequent step. |
| `atf-perf-prof.md` | Performance profiling | Performance profiling allows you to do performance testing on your instances.Execute performance profiling on a test or a suite for… |
| `atf-pick-a-browser.md` | Pick a browser | If the test or test suite you are running contains steps that work with a form (any step involving a UI), or any other UI test step element… |
| `atf-ref-overview.md` | Automated Test Framework \(ATF\) reference | Reference information for the Automated Test Framework. |
| `atf-rerun-tests.md` | Re-run failed tests in an automated test suite | Re-run failed tests within a test suite without rerunning the entire suite. |
| `atf-rest-properties.md` | Automated Test Framework REST properties | These properties are installed with ATF REST. |
| `atf-retrieve-value.md` | Pass values from one automated test step to another | Assign a form field the value of an output variable returned from a previous step. |
| `atf-reuse-tests.md` | Reusable tests | Leverage reusable tests to simplify test maintenance and streamline the management of large tests and test suites. Reusable tests reduce… |
| `atf-roles.md` | Automated Test Framework roles | Automated Test Framework is installed with these roles. |
| `atf-rollup-xmpls.md` | Test suite results examples | Examples of relationship terms and how aggregated results roll up for test suites. |
| `atf-run-suite.md` | Run an automated test suite | After creating an automated test suite, run it in a non-production instance. |
| `atf-run-test.md` | Run an automated test | After creating an automated test, run it on a non-production instance. |
| `atf-sched-suite-steps.md` | Schedule an automated test suite | Schedule one or more test suites to run at a specific date and time. |
| `atf-sched-suites.md` | Working with scheduled test suites | You can schedule a test suite to run at a specified date and time.You can designate users to be notified when a scheduled test suite… |
| `atf-sched-test-runner-module.md` | Scheduled client test runner | The Scheduled Client Test Run opens a browser window for running scheduled client automated tests. |
| `atf-screenshot-modes.md` | Managing automatic test screenshot settings | Capturing many screenshots can impair test performance. You can control which types of screenshots the system captures to minimize this… |
| `atf-select2.md` | Select2 functionalities in ATF | Use the Select2 component to search and select your option from a drop-down menu easily. |
| `atf-serv-cat-use.md` | Automated Test Framework use case: test a Service Catalog request | This use case illustrates testing a service catalog request with the Automated Test Framework. |
| `atf-step-categories.md` | Test step config category form | On the Test Step Config Category form, you specify a retention policy for a set of records on a given test results table. |
| `atf-step-config-record.md` | Automated Test Framework Step Config record | The step config record controls how a test step of this type behaves. |
| `atf-step-config-xmpls.md` | Examples of step config field values | Examples of where the system displays values assigned to some of the step config fields. |
| `atf-step-result-record.md` | Step results record | The Step Results record contains information about one step in a test result. You access specific step results from the Step Results… |
| `atf-suite-sched-run-record.md` | Scheduled suite run record | A Scheduled Suite Run record associates a Suite Schedule record with a Test Suite. |
| `atf-suite-schedule-record.md` | Suite schedule record | The Suite Results record displays information about one test suite schedule. |
| `atf-suites-overview.md` | Building and running automated test suites | Run a group of tests in a specific order to test an application or a group of related features. |
| `atf-templates.md` | Working with test step templates | Test step templates contain a list of steps to be added all at once to an automated test. |
| `atf-test-admin-module.md` | Administration | The Administration module contains forms for configuring and managing the automated test framework. |
| `atf-test-build-execution.md` | Automated Test Framework \(ATF\) test building and execution | Build and execute the ATF tests and test suites using the information in this section. |
| `atf-test-log-record.md` | Test logs record | The Test Results Item (test log) record contains console logging and test execution information. |
| `atf-test-record-form.md` | Test record form | In the Test record form, you view and edit values of fields for the test record. |
| `atf-test-results-module.md` | Test results | Each time you run a test, the automated test framework creates a record of the test results. Use the Test Results module to view details… |
| `atf-test-results-record.md` | Test results record | A Test Results record contains detailed results information about one test execution. Client Error Details and Failure Details sections… |
| `atf-test-runners.md` | Working with client test runners | If an automated test includes steps that involve a form or any other user-interface (UI) element, it runs those steps in a browser tab or… |
| `atf-test-suite-record.md` | Test suite form | The Test Suite form contains information about one test suite. |
| `atf-test-suite-results-record.md` | Test suite results record | The Test Suite Results record displays information about the results of one execution of one test suite. |
| `atf-test-template-record.md` | Automated Test Template record | The Test Template record contains information about one test template. |
| `atf-test-triage.md` | Accelerate ATF tests failure resolution | Resolve ATF test failures faster using the actionable support provided by the new ATF failure insights feature. You can achieve it by… |
| `atf-test-type-testing.md` | Automated Test Framework \(ATF\) test types and techniques | Experience the different types of ATF tests and testing techniques. |
| `atf-tut-build-first.md` | Build and run your first automated test | Follow these step-by-step instructions to create and run your first automated test. This test creates a new user record.Create a new… |
| `atf-use-backref.md` | Automated Test Framework use case: reference a value from a previous step | This use case illustrates assigning a form field the value of an output variable from a previous step. |
| `atf-use-basic-form.md` | Automated Test Framework use case: test basic form operations | This use case illustrates testing basic form operations with the Automated Test Framework. |
| `atf-use-cases.md` | Automated Test Framework use case examples | Use cases can help you construct tests for common scenarios. |
| `atf-use-rest-retrieve-incident.md` | Automated Test Framework use case: retrieve an incident using REST-Inbound | The Get Newly Created Resource via REST API Test test is provided with the Automated Test Framework, and uses the REST - Inbound and assert… |
| `atf-use-script-include.md` | Automated Test Framework use case: test a script include | This use case illustrates testing a script include with the Automated Test Framework. |
| `atf-use-template.md` | Add a predefined list of steps \(template\) to an automated test | With test templates you can add a predefined list of steps to a test. Any list of steps that follows a set pattern makes a good candidate… |
| `atf-view-manually-add-whitelisted-browser-errors.md` | Manually allow client errors | Manually create allowed client error entries as needed in the Allowed Client Errors table. |
| `atf-view-progress.md` | View the progress of automated tests | When an automated test is running, view its progress in the Run Test progress dialog. |
| `atf-view-results-consolidated.md` | View test results and automated test results | View test results from completed test and test suite runs. Carefully consider the results of automated test runs and perform any corrective… |
| `atf-view-systrans-log.md` | View transaction data for automated test results | To help troubleshoot performance issues with automatic tests, you can inspect related records from the transactions log entry… |
| `attachment-test-steps.md` | Attachment test steps | Test an attachment-dependent business rule by uploading an attachment either from a form or from a server-side API call. For example, you… |
| `automated-test-framework-design-considerations.md` | Automated Test Framework design considerations | Create reliable, scalable, and efficient tests by following these design considerations. |
| `automated-test-framework.md` | Exploring Automated Test Framework | The Automated Test Framework helps you ensure the integrity of your instance by enabling the creation and execution of automated tests… |
| `available-quick-start-tests.md` | Available quick start tests by application or feature | Validate that your instance still works after you make any configuration change such as apply an upgrade or develop an application. Copy… |
| `browser-recommendations-atf.md` | Browser recommendations for Automated Test Framework | Configure client test runner browsers to run automated tests and avoid performance degradations. |
| `create-custom-ui-test.md` | Create a custom UI test | Test components in custom UI pages. |
| `create-parameterized-test.md` | Create a parameterized test | Build a test that uses variables to store test data. |
| `custom-ui-test-steps.md` | Custom UI test steps | Test customized user interfaces such as UI pages and UI macros by retrieving their HTML and JavaScript page components and identifying the… |
| `develop-testable-components.md` | Override component test actions | Change the testing properties of a particular page component using HTML attributes that are specific to Automated Test Framework. Use… |
| `domain-separation-auto-test-framework.md` | Domain separation and Automated Test Framework | Domain separation is supported in the Automated Test Framework. Domain separation enables you to separate data, processes, and… |
| `enable-page-inspector.md` | Enable and use the page inspector | Enable a developer setting to inspect UI pages that open within the platform. Use the Manual Page Inspector to inspect pages that open in a… |
| `headless-browser-add-secrets-docker-windows.md` | Add secrets to Docker for Headless Browser setup in Microsoft Windows | Create a Docker secret that stores the password of the ServiceNow user who will log into the instance to execute the tests. Docker Secrets… |
| `headless-browser-add-secrets-docker.md` | Add secrets to Docker for Headless Browser setup in Linux | Create a Docker secret, which stores the password of the ServiceNow user who will log into the instance to execute the tests. Docker… |
| `headless-browser-certificates-windows.md` | Generate certificates for Headless Browser setup for Microsoft Windows | Generate TLS/SSL certificates to secure the Docker REST API and authenticate HTTP requests. |
| `headless-browser-certificates.md` | Generate certificates for Headless Browser setup for Linux | Generate TLS/SSL certificates to secure the Docker REST API and authenticate HTTP requests. |
| `headless-browser-configure-atf-windows.md` | Configure Automated Test Framework \(ATF\) for Headless Browser in Microsoft Windows | Step 7 in the Microsoft Windows setup for the ServiceNow Headless Browser for ATF: Configure ATF with properties. |
| `headless-browser-configure-atf.md` | Configure ATF for Headless Browser in Linux | Step 6 in the Linux setup for the ServiceNow Headless Browser for ATF: Configure ATF with properties. |
| `headless-browser-configure-docker-windows.md` | Configure Docker for Headless Browser setup in Microsoft Windows | Configure Docker Server to authenticate all requests. |
| `headless-browser-configure-docker.md` | Configure Docker for Headless Browser setup in Linux | Complete Step 2 in the Linux setup for the ServiceNow Headless Browser for ATF: Configure Docker Server to authenticate all requests. |
| `headless-browser-create-docker-image-containers-windows.md` | Create the Docker image and containers for Headless Browser setup in Microsoft Windows | Pull the Docker image from the Public Registry. |
| `headless-browser-create-docker-image-containers.md` | Create the Docker image and containers for Headless Browser setup in Linux | Pull the Docker image from the Public Registry. |
| `headless-browser-install-docker.md` | Install Docker for Headless Browser setup for Microsoft Windows | Step 1 in the Windows setup for the ServiceNow Headless Browser for Automated Test Framework: Install Docker. |
| `headless-browser-instance-setup-windows.md` | Set up instance for Headless Browser in Microsoft Windows | Step 6 in the Microsoft Windows setup for the ServiceNow Headless Browser for ATF: Set up your instance so it can support the Headless… |
| `headless-browser-instance-setup.md` | Set up instance for Headless Browser in Linux | Step 5 in the Linux setup for the ServiceNow Headless Browser for ATF: Set up your instance so it can support the Headless Browser. |
| `headless-browser-procedure-linux.md` | Headless Browser setup for Linux | The ServiceNow Headless Browser for Automated Test Framework provides automation so you can skip having to manually open a browser during… |
| `headless-browser-procedure-windows.md` | Headless Browser setup for Microsoft Windows | The ServiceNow Headless Browser for Automated Test Framework (ATF) provides automation so you can skip having to manually open a browser… |
| `headless-browser-troubleshoot.md` | Headless Browser troubleshooting | These tips can help you troubleshoot your Linux or Microsoft Windows setup of the ServiceNow Headless Browser for Automated Test Framework. |
| `headless-browser-verify-tests-windows.md` | Verify Headless Browser procedures for ATF in Microsoft Windows | Verify that your Headless Browser setup procedures have been successful. |
| `headless-browser-verify-tests.md` | Verify Headless Browser procedures in Linux | Step 7, the final step in the Linux setup for the ServiceNow Headless Browser for ATF: Verify that your Headless Browser setup procedures… |
| `identify-and-resolve-client-errors.md` | Identify and resolve client errors | Identify client errors and resolve them in client-side scripts.There are several types of common client error. |
| `mutual-exclusion-rule.md` | Mutually exclusive tests | Prevent conflicting tests from running in parallel by marking them as mutually exclusive. For example, when the system identifies tests… |
| `override-component-data-type.md` | Override component data type | Use the sn-atf-data-type and sn-atf-data-type-params attributes to override the type of field displayed in a Set Component Value test step. |
| `parallel-testing.md` | Parallel testing | Reduce test design time by running multiple tests and test suites in parallel. Design tests to run in parallel by avoiding resource… |
| `parameterized-tests.md` | Parameterized tests | Run a test multiple times with different test data for each run. Create parameters to store test data for each test run. |
| `quick-start-tests.md` | Quick start tests | Copy and customize quick start tests provided by the ServiceNow AI Platform to validate that your instance works after you make any… |
| `reported-client-errors.md` | Reported client errors | The Reported Client Error module lists test logs across all tests that are client errors and have failed. You can review individual test… |
| `rest-test-steps.md` | REST test steps | Test custom inbound web services and backwards compatibility by making REST calls. |
| `run-module.md` | Run | Start a client test runner and view information about test runners and test runs. |
| `run-scheduled-test-suite-script.md` | Run a scheduled test suite using a script | Execute a scheduled UI test suite immediately using a script without having to wait for the scheduled time. You can use this method while… |
| `scripting_atf.md` | Add output variables to scripted steps | Execute the following steps to add additional outputs in Run Server Side Script and Custom Scripted StepConfig test steps.Modify the test… |
| `server-test-steps.md` | Server test steps | Test business logic and background processes by performing operations on the server. |
| `step-configuration-categories-module.md` | Step configuration categories | The Step Configuration Categories module opens a list of records specifying the step categories on the Add Step dialog. From this module,… |
| `step-configurations-module.md` | Step configurations | Step configuration records define how each type of step behaves. |
| `step-environments-module.md` | Step environments | A test step environment specifies where the step executes (for example, server versus browser). In this release, custom step configs can… |
| `suite-results-module.md` | Suite results | The Suites Results module opens the Suites Results table. |
| `suite-schedules-module.md` | Suite schedules | Open the Suites Schedules table. You can drill down to see details about the results of individual schedules or create a new schedule. |
| `suites-module.md` | Suites | The Suites module opens the Test Suites table. You can create, edit, and run test suites from this table. |
| `table-cleanup.md` | Table cleanup | The Table Cleanup module opens a list of records specifying the retention policies for test result and test suite result tables and the… |
| `test-step-categories.md` | Automated Test Framework \(ATF\) test step categories | Find test steps for a particular user interface or ServiceNow AI Platform feature. |
| `test-steps-app-navigator-category.md` | Application Navigator category | Verify the functionality of menus and modules in the application navigator.Verifies the visibility, or lack thereof, of selected… |
| `test-steps-catalog-portal-category.md` | Service Catalog in Service Portal category | Validate catalog item transactions and requester flows from Service Portal.Open a record producer in the Service Portal.Open a catalog item… |
| `test-steps-conf-ws-tests-category.md` | Configurable Workspace category | Interact directly with the configurable workspace components for simpler test creation.Navigate to a workspace page using a URL. The… |
| `test-steps-custom-ui-category.md` | Custom UI category | Validate the behavior of page components on custom user interfaces.Set component values on a custom UI page.Assert that the specified text… |
| `test-steps-email-category.md` | Email category | Use Automated Test Framework (ATF) to test email notifications, outbound email flows, and inbound email responses.Verify that a certain… |
| `test-steps-form-category.md` | Form category | Validate the functionality of fields and UI actions on a form.Open a form to a new record in the specified table and Form UI.Open a form to… |
| `test-steps-forms-portal-category.md` | Forms in Service Portal category | Validate the functionality of fields and UI actions in Service Portal form widgets.Opens a form in a portal.Sets the values of fields in a… |
| `test-steps-list-related-list.md` | List and Related List | Validate the functionality and visibility of records and UI actions in lists and related lists.Validate the visibility of the selected… |
| `test-steps-rest-category.md` | REST category | Verify the functionality of REST calls.This test step begins with the REST API Explorer. Use the REST API Explorer to create and specify… |
| `test-steps-reusable-tests-category.md` | Reusable Tests category | Create reusable test components that can be incorporated into various other tests (regular or reusable test), minimizing redundant test… |
| `test-steps-server-category.md` | Server category | Perform server-side operations. For example, query and update a record, impersonate a user, or run a server-side script. Create a user with… |
| `test-steps-service-catalog-category.md` | Service Catalog category | Validate single catalog item transactions as well as requester and fulfiller flows in Service Catalog.Open a catalog item.Open a record… |
| `test-steps-ui-category.md` | UI category | Validate the functionality of the UI actions.Executes a client-side test script entirely in the browser without requiring server-side… |
| `test-templates-module.md` | Test templates | The Test Templates module opens a list of available templates. From this module, you create, view, and edit test templates. |
| `tests-module.md` | Tests | The Tests module opens the Test table. From here, you can add, edit, and run tests. By opening an individual test record, you can view and… |
| `ui-test-steps.md` | UI test steps | Test user interfaces by mimicking user actions and interacting with the visible components of a page. |
| `waiting-running-suite-runs-module.md` | Waiting/running suite runs | The Waiting/Running Suite Runs module opens a list of records showing the test suites waiting to be run. |
| `waiting-running-test-runs.md` | Waiting/running test runs | The Waiting/Running Test Run module opens a list of records showing the tests waiting to be run. |
| `whitelist-errors-from-step-results-related-list.md` | Allow client errors from step results | Allow client errors as you review step results. |
| `whitelist-errors-from-test-log-related-list.md` | Allow client errors from the test logs | Allow client errors as you review test logs. |
| `whitelist-errors-from-test-results.md` | Allow client errors from test results | Allow client errors as you review test results. |
| `whitelisted-client-error-records.md` | Allowed client error records | Review the list of existing Allowed Client Error [sys\_atf\_whitelist] records to see which client errors produce warnings and which are… |
| `whitelisted-client-errors.md` | Allowed client errors | Add known client errors to the allowed client errors list to allow tests and steps to continue running when a specific error occurs. Set… |
