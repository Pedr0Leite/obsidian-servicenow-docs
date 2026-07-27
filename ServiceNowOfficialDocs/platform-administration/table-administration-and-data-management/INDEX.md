# ServiceNowOfficialDocs/platform-administration/table-administration-and-data-management — File Index

Navigation index for AI agents. One row per file in this directory (130 files). Auto-generated from frontmatter — do not hand-edit; regenerate via `scripts/gen_indexes.py` if files are added/removed.

---

| File | Title | Description |
|------|-------|-------------|
| `CreateRateType.md` | Create a rate type | You can create rate types using the Rate Types feature. |
| `approve-time-card.md` | Approve or reject a time card | As a time card approver, you can view and approve or reject a submitted time card. |
| `approve-time-sheet.md` | Approve or reject a time sheet | View, approve, or reject time sheet or time cards for your user, for the given week, in a single step. |
| `assign-time-sheet-policy-to-user.md` | Assign a time sheet policy to a user | As a time card administrator, you can assign a time sheet policy to a user. |
| `auto-generate-time-cards.md` | Auto-generate time cards | As an admin, you can configure a scheduled job to generate time cards automatically for project tasks assigned to time card users. |
| `background-script-recovery.md` | Use the Script Execution History module to roll back a Scripts-Background execution | You can roll back the database actions of a script executed using the Scripts-Background module. |
| `c_AssignmentRulesModule.md` | Assignment rules module | The Assignment rules module allows you to automatically set a value in the assigned\_to and assignment\_group fields when a set of… |
| `c_AutomaticMatchingOfDisplayValues.md` | Automatic matching of display values | During the import of XML records, the system attempts to match some reference field display values to a local sys\_id value. |
| `c_CreateABaseline.md` | Create a baseline | A Planned Task Baseline is a record of the start and end times of the planned task at a particular moment in time. |
| `c_CreatingDatabaseViews.md` | Joining tables using database views | Join tables into a single view and then create a report based on that view. |
| `c_DataDictionaryTables.md` | Data dictionary tables | Access details related to tables, columns, and field labels in your instance. |
| `c_DataLookupRules.md` | Data lookup rules | Data lookup rules offer a generic way to change any field value, not just assignment fields. |
| `c_DatabaseViews.md` | Working with database views for reporting | A database view defines table joins for reporting purposes. |
| `c_DefineAssignmentRules.md` | Defining assignment rules | The instance can automatically assign a task to a user or group based on pre-defined conditions by using data lookup rules and assignment… |
| `c_DeleteATable.md` | Deleting custom tables | Administrators can delete custom tables that are no longer needed. For example, delete a table from an application that is under… |
| `c_DictionaryAttributes.md` | Altering tables and fields using dictionary attributes | Dictionary attributes alter the behavior of the table or field that the dictionary record describes. Administrators can add or modify… |
| `c_DictionaryOverrides.md` | Dictionary overrides | Dictionary overrides provide the ability to define a field on an extended table differently from the field on the parent table. |
| `c_EnableExportDebugLogging.md` | Enable export debug logging | When the property glide.export.debug is true, the instance logs export processing including database query time and the time taken to write… |
| `c_ExportAndImportXMLFiles.md` | Exporting and importing data via XML | Migrate data from one instance to another by exporting and importing XML files. |
| `c_ExportData.md` | Exporting data | Export data from the ServiceNow AI Platform in a variety of formats. |
| `c_ExportLimits.md` | Export limits | The platform provides a default upper limit for data exports. |
| `c_ExportingCurrencyFields.md` | Exporting currency fields to Excel | Exporting currency fields to Excel applies Account formatting and can be configured to convert all values to US dollars or to export values… |
| `c_ManageCosts.md` | Manage costs | When the cost management feature is enabled, time cards can be used to manage the cost of labor in the Cost Management application. |
| `c_ManyToManyTaskRelations.md` | Creating many-to-many task relations | By default, tasks can be related to each other using a parent/child relationship, such as a Problem with a group of child Incidents or a… |
| `c_MarkAsSolutionButton.md` | Mark as Solution button | The Mark as Solution button is added to the KB popup view and displayed when you search the knowledge base from a task record. |
| `c_MeasureTimeAndEffort.md` | Measure time and effort | The Planned Task [planned\_task] table provides standard fields for tracking duration and effort. |
| `c_ModifyTheGlideDurationsFormat.md` | Modify the Glide durations format | To convert fields that are displayed in milliseconds (such as 'Resolution Time' on the Incident table) to a duration format… |
| `c_PlannedTask.md` | Extending the Task table with Planned tasks | The Planned Task plugin provides a Planned Task [planned\_task] table that extends the Task [task] table. |
| `c_PrecBetweenAssignmentAndBusRules.md` | Precedence between data lookup, assignment, and business rules | Scripts, assignment rules, business rules, workflows, escalations, and engines all take effect in relation to a database operation, such as… |
| `c_RecordTimeWorked.md` | Record time worked | The time card retrieves time accrued on a project or spent working on any record in the Task table from the Time worked field. |
| `c_SchemaMapForTables.md` | Viewing table references and extensions | View table relationships in a visual manner using the schema map. |
| `c_SpecifyAFieldToReturn.md` | Specify a field to return | Restrict or specify a field that you want returned by the joined table. |
| `c_SpecifyTheNumberOfRecordsToReturn.md` | Configuring the number of records to return | Specify the number of records to return for a database view when the view is used in a script. |
| `c_SystemDictionary.md` | System dictionary | View a list of all tables in columns in your instance from the system dictionary. |
| `c_TableAdministration.md` | Table administration | A table is a collection of records in the database. Each record corresponds to a row in a table, and each field on a record corresponds to… |
| `c_TaskTable.md` | Working with the Task table | The Tasks [task] table is one of the core tables provided with the base system. |
| `c_TaskTableFlattening.md` | Table flattening | Table flattening stores a hierarchy of related tables as one table in a relational database. |
| `c_TimeCards.md` | Time cards | Time cards are used to record the time worked on a task by a task assignee. |
| `c_UseDisjunctionsInComplexQueries.md` | Using disjunctions in complex queries | ServiceNow performs conjunction (AND) statements before disjunction (OR) statements in a query. |
| `c_ViewTheSchemaMap.md` | Analyzing table relationships | The schema map shows the selected table in yellow, typically centered, and all tables related to that table, typically shown at the sides. |
| `c_WorkflowAssignments.md` | Workflow assignments | An alternative to creating data lookup or assignment rules is to create one or more workflow tasks that assign a task record as part of a… |
| `config-connect-credentials-aliases-for-gsheets.md` | Configure ServiceNow connection and credential aliases for Google sheets | Configure connection and credential aliases to authenticate an integration between your ServiceNow instance and Google Drive. |
| `configure-app-registry-gsheets.md` | Create an application registry for Google Sheets on a ServiceNow instance | Register the Google Drive application in your ServiceNow instance to enable OAuth authorization for exporting table records directly to… |
| `copy-time-sheet.md` | Copy time cards from a previous time sheet | Another option for creating time cards is to copy them from an existing timesheet, which copies all the time cards (for project as well as… |
| `create-a-function-field-to-perform-a-database-function.md` | Create a function field to perform a database function | Create a function field that displays the results of a database function, such as a mathematical operation, field length computation, or… |
| `create-record-hierarchy.md` | Create a record hierarchy | Build a record hierarchy between records in the same table. |
| `create-time-sheet-policy.md` | Create a time sheet policy | As a time card administrator, you can create a time sheet policy to define the requirements for time card users to record their time… |
| `create-time-sheet.md` | Create a time sheet | As a time card user, you can create a time sheet to group all your time cards for the given week and submit them in a single step. |
| `create-timecards-through-worker-portal.md` | Create time cards and log time through Time Sheet Portal | After you create time cards in Time Sheet Portal, log time in the time cards. |
| `custom-tables.md` | Custom tables | Custom tables enable you to expand the functionality of the ServiceNow AI Platform and create custom applications. |
| `data-export-reference.md` | Data export reference | Reference topics provide details on exporting data. |
| `data-hierarchies.md` | Building hierarchical queries | Simplify and build more efficient queries by leveraging hierarchical relationships in the condition builder. |
| `default-values-headers-values.md` | Default values for column headers and column values | Default values are used for column headers and column values, unless overridden by query parameters, Export Set fields, or system… |
| `delete-recovery.md` | Use the Delete Recovery module to restore a deleted record | You can recover a deleted record and all related changes. The recovery must be done within seven days of the record being deleted. |
| `display-function-results-in-a-database-view.md` | Display function results in a database view | Add a function field to the output of a database view to see function results. |
| `displaying-function-results-in-a-database-view.md` | Displaying function results in a database view | Enhance the display of a database view by adding a function field to the output to display function results. |
| `domain-separation-time-card.md` | Domain separation and Time Card | Domain separation is supported in Time Card. Domain separation enables you to separate data, processes, and administrative tasks into… |
| `drop-custom-index.md` | Drop a custom index | Remove a custom index by dropping it from a table. |
| `example-left-join-db-view.md` | Example left join in creating a database view | This example shows the proper settings when using left-joins to add tables to a database view. |
| `exploring-table-administration.md` | Exploring ServiceNow AI Platform tables | Applications use tables and records to manage data and processes, such as Incident, Problem, and CMDB. Tables can extend other tables,… |
| `export-form-data.md` | Export data from a record | Export a record to PDF or XML. |
| `export-list-data.md` | Export data from a list | Export a list of records to a variety of file formats. |
| `export-xml-file.md` | Export data to XML | Export data from a source instance to an XML file. |
| `field-types-affected.md` | Field types affected by export controls | Different field types are affected differently by export controls. |
| `import-xml-file.md` | Import data from XML | After you have successfully exported data from the source instance to XML, import the XML file directly to the target instance. |
| `make-field-read-only.md` | Make a field read only | Control whether a field is read only and whether it can be changed by a client script and server-side APIs. |
| `query-parameters-display-value.md` | Query parameters for display value and header | Use query parameters to export the display value or raw value of fields and the field label or field name for headers. |
| `r_BaselineAssignmentRulesExample.md` | Baseline assignment rules example | A baseline instance contains certain assignment rules. |
| `r_DatabaseViewsInTheBaseSystem.md` | Database views in the base system | Certain views are included in the base system with the Database Views and Database Views for Service Management plugins. |
| `r_DictionaryEntryForm.md` | Dictionary entry form | The Dictionary Entry form was redesigned to provide an Advanced view and additional fields. You might need to configure the form to see all… |
| `r_GlobalDefaultFields.md` | Global default fields | When you create a new custom table, several fields appear in the Table Columns embedded list. For all tables, required system fields are… |
| `r_ImportantPlannedTaskTableFields.md` | Important planned task table fields | The Planned Task table has these fields. |
| `r_ImportantTaskTableFields.md` | Important Task table fields | The Task table is a base class that provides fields for the core ITSM applications such as Incident, Problem, and Change Management. All… |
| `r_JournalFields.md` | Journal fields | Journal fields work together to create a log of changes and comments as tasks are worked on. |
| `r_PlannedTaskScripts.md` | Planned task scripts | Several business rules and one script include determines the dynamic calculation of crucial Planned Task fields. |
| `r_PluginManifest.md` | Plugin manifest | When the plugin is activated, the Task Relationships application is available with certain modules. |
| `r_RefDefaultManyToManyRels.md` | Reference default many-to-many relationships | Some many-to-many relationships are defined by default. |
| `r_UIActions.md` | Task relationships with UI actions | After defining task relationships, you can use UI Actions to define the task relationship when a new task is being created from an old task. |
| `read-only-option.md` | Configuring read-only security options | Control the ability to edit read-only fields by configuring read-only options. |
| `reminder-table.md` | Reminder table | The Reminder [reminder] table provides a way to auto-generate reminders for a task. |
| `roll-back-rollback-context.md` | Roll back patch upgrades or plugin activations | Use the Rollback Contexts module to roll back patch upgrades and plugin activations. |
| `rollback-context-properties.md` | Rollback context properties | Change the default expiration period for different types of rollback context records. |
| `rollback-delete-recovery.md` | Roll back and delete recovery | With rollback contexts, you can roll back certain actions such as a patch upgrade, plugin activation, and background script executions, and… |
| `set-default-time-sheet-policy.md` | Set a time sheet policy as default policy | As a time card administrator, you can set a time sheet policy as the default policy. The default policy is a global time sheet policy which… |
| `set-up-oauth-app-gsheets-api.md` | Set up the OAuth application on the Google Sheets API | Set up the OAuth application on the Google Sheets API so that you can authenticate requests from your ServiceNow instance to access Google… |
| `setup-gsheet-export.md` | Exporting your table records to Google Sheets | Integrate your ServiceNow instance and Google Cloud Console so that you can export table records directly to the cloud-based Google Sheets… |
| `storage-aliases.md` | Storage aliases | Learn about the role storage aliases play in data manipulation and field creation in the ServiceNow AI Platform. |
| `submit-time-card.md` | Submit a time card | As a time card user, once a time card for the week is updated with the time worked, you can submit the time card individually. |
| `submit-time-sheet-other-users.md` | Log time and submit time sheets of your resources | As a user manager, you can log time and submit the time sheet of your resources. |
| `submit-time-sheet.md` | Submit a time sheet | Once the time sheet is updated with time worked, you can submit the time sheet for the week to submit all the time cards for the week… |
| `submit-timesheet-workerportal.md` | Submit time sheet through Time Sheet Portal | Once you update the time sheet with time worked for a given week, submit it for approval. |
| `system-properties-display-value-header.md` | System properties for display value and header | Use system properties to export the display value or raw value of fields and the field label or field name for headers. |
| `t_ActivateTimeCardManagement.md` | Activate Time Card Management | Administrators can activate the Time Card Management plugin (com.snc.time\_card). The plugin also activates the Performance Analytics -… |
| `t_AddATableToTheDatabaseView.md` | Add a table to the database view | Specify the table to join to the database view. |
| `t_AssignmentModuleRule.md` | Create an assignment rule | Automatically assign a record according to one or more conditions in an assignment rule. Assignment rules are designed to run at the time… |
| `t_BreakUpALargeExport.md` | Break up a large export | If the number of records to be exported exceeds the actual export limit, you may want to break the export into smaller increments that do… |
| `t_CallURLExportProgrammatically.md` | Call URL export programmatically | Dynamically export data from a script or web service by calling a URL export from any programming language. |
| `t_ConfiguringRollupForPlannedTask.md` | Configure rollup for planned task fields | You can configure the planned task fields to roll up the field values in the parent entity. |
| `t_CreateADatabaseView.md` | Create a database view | Create the database view. |
| `t_CreateAManyToManyRelationship.md` | Create a many-to-many table relationship | Create a bi-directional relationship between two tables, so that the related records are visible from both tables in a related list. |
| `t_CreateAPlannedTask.md` | Create a planned task | Planned Tasks are created on planned task child tables. |
| `t_CreateATable.md` | Create a table | Administrators and application developers can create custom tables to store application data. After you create a table, you can also modify… |
| `t_CreateATimeCard.md` | Create a time card | You can create time cards to log time against the work you have done. |
| `t_CreateCustomIndex.md` | Create a table index | Build indexes to access the data held in your tables more easily. |
| `t_DataLookupRule.md` | Create an assignment data lookup rule | Automatically assign a record using Data Lookup and Record Matching. |
| `t_DefineADictionaryOverride.md` | Define a dictionary override | Use a dictionary override to allow a field in a child table to have a different value or behavior than the same field in a parent table.… |
| `t_DefineARelationshipType.md` | Define a relationship type | Create type codes that define the relationship between parent and child tasks. |
| `t_DefineATaskRelationshipAllowed.md` | Define a task relationship allowed from the task relationship type record | Define the Task Relationships Allowed from the Task Relationship Type record. |
| `t_DeleteACustomTable.md` | Delete a custom table | If you no longer need a custom table, you can delete it after you delete all the records in the table. |
| `t_DeleteAllRecordsFromATable.md` | Delete all records from a table | You may decide to delete all the records on a table without deleting the table itself. For example, the administrator may want to delete… |
| `t_ExportDirectlyFromTheURL.md` | Export directly from a URL | Dynamically export data from a script or web service by building a URL query. |
| `t_GenerateASchemaMap.md` | Generate a schema map | Generate a schema map to view different parts of the database schema. |
| `t_ModifyADictionaryEntryFromAForm.md` | Modify dictionary entries | Modify dictionary entries by configuring a field on a form or from the Dictionary module. |
| `t_ModifyTheDisplayedField.md` | Modify the displayed field | The list view of the Reference Lookup defines the fields displayed in the Task Relations field and editing interface. |
| `t_PlannedTaskHierarchy.md` | Planned task hierarchy | The Task Hierarchy tool available for Planned Task displays the relationship between parent and child planned tasks. |
| `t_RelabelAColumn.md` | Relabel a column | Sometimes, two different tables may have fields of the same name that are both important (such as two tables with a sys\_updated\_on… |
| `t_RequestManyToManyTaskRelations.md` | Request many to many task relations | The Many to Many Task Relations plugin (com.snc.task\_relations) is included with several plugins. You can request activation of the plugin… |
| `t_RestoreADeletedRecordAndRef.md` | Use the Deleted Records module to restore a deleted record | You can recover deleted records that are in audited tables. |
| `t_TableHierarchyAndTheExtModel.md` | View a table hierarchy and the extension model | Determine the extension model used by a table. |
| `t_TestTheDatabaseView.md` | Test the database view | Verify that the database view works correctly. |
| `table-extension-and-classes.md` | Table extension and classes | Enable one or more child tables to share fields and records with a parent table. Administrators and application developers can only extend… |
| `table-relationships.md` | Table relationships | You can create relationships between tables by extending tables, referencing records in another table, creating many-to-many relationships,… |
| `tables-fields-and-forms.md` | ServiceNow AI Platform tables and data | ServiceNow provides options for managing your data on the ServiceNow AI Platform. |
| `task-table-structure.md` | Task table structure | The Task table structure provides a framework to organize and store task-related data, and includes extensive customization options. |
| `test-read-only-options.md` | Test read-only options | Test read-only behavior on a non-production instance before updating Read only option field values on your production instance. |
| `time-card-management.md` | Time Card Management | The Time Card Management feature enables time card users such as task assignees to report and track their time for the assigned tasks. |
| `time-sheet-policies.md` | Time sheet policies | Time sheet policies contain the policies to which a time sheet, or a time card must adhere. |
| `time-sheets.md` | Time Sheets | A time sheet groups all the time cards for a user for the given week. |
| `using-table-administration.md` | Managing tables and indexes | Administrators can modify the database structure using table administration tools. |
| `worker-portal.md` | Time Sheet Portal | Time Sheet Portal categorizes and displays all your assigned tasks in a single view for a given week. The portal enables you to record time… |
