# ServiceNowOfficialDocs/now-intelligence/performance-analytics — File Index

Navigation index for AI agents. One row per file in this directory (312 files). Auto-generated from frontmatter — do not hand-edit; regenerate via `scripts/gen_indexes.py` if files are added/removed.

---

| File | Title | Description |
|------|-------|-------------|
| `PADU-copyDashboard_S_S.md` | PADomainUtils - copyDashboard\(String dashboardId, String runAs\) | Copy a dashboard to another domain. |
| `PAFU-getChangePercentage_S_O_O.md` | getChangePercentage\(String indicator, Object fromDate, Object toDate\) | Returns the percentage of change in the score of an indicator between two specified dates. |
| `PAFU-getChange_S_O_O.md` | getChange\(String indicator, Object fromDate, Object toDate\) | Returns the change in the score of an indicator between two specified dates. |
| `PAFU-getCurrentAggregateID.md` | getCurrentAggregateID\(\) | Returns the time series aggregate identifier (sys\_id) from the indicator of the current formula. The sys\_id is returned dynamically, as… |
| `PAFU-getCurrentBreakdownID.md` | getCurrentBreakdownID\(\) | Returns the level 1 breakdown identifier (sys\_id) from the indicator of the current formula. The sys\_id is returned dynamically, as the… |
| `PAFU-getCurrentBreakdownLevel2ID.md` | getCurrentBreakdownLevel2ID\(\) | Returns the level 2 breakdown identifier (sys\_id) from the indicator of the current formula. The sys\_id is returned dynamically, as the… |
| `PAFU-getCurrentElementID.md` | getCurrentElementID\(\) | Returns the level 1 breakdown element identifier (sys\_id) from the indicator of the current formula. The sys\_id is returned dynamically,… |
| `PAFU-getCurrentElementLevel2ID.md` | getCurrentElementLevel2ID\(\) | Returns the level 2 breakdown element identifier (sys\_id) from the indicator of the current formula. The sys\_id is returned dynamically,… |
| `PAFU-getGap_S_O.md` | getGap\(String indicator, Object onDate\) | Returns the global target gap for the specified indicator on the specified date. |
| `PAFU-getGlobalTarget_S_O.md` | getGlobalTarget\(String indicator, Object onDate\) | Returns the global target associated with the specified indicator for the specified date. |
| `PAFU-getPersonalTarget_S_O.md` | getPersonalTarget\(String indicator, Object onDate\) | Returns the personal target associated with the specified indicator for the specified date. |
| `PAFU-getScore_S_O.md` | getScore\(String indicator, Object onDate\) | Returns the score of the specified indicator for the specified date. |
| `PAFormulaUtils.md` | PAFormulaUtils API | The PAFormulaUtils API enables you to obtain a value that was calculated in the Analytics Hub and use that value as input for a formula. |
| `access-to-kpi-composer.md` | Access to KPI Composer | The level of access to KPI Composer determines whether a user can create, edit, or only view a KPI Composer project. It also determines… |
| `activate-unlimited-breakdowns.md` | Activate Data snapshots | Enable Data snapshots on an instance as a whole and on individual existing indicators (KPIs) on the instance. When Data snapshots are… |
| `add-breakdowns-project.md` | Group data by breakdown definitions | Each project can have a set of breakdown definitions that you can use to group the data in KPIs. These breakdown definitions provide the… |
| `add-filter-to-ia.md` | Add a filter to Interactive Analysis | Add a filter to show more refined information in your Interactive Analysis. |
| `add-indicators-to-widget.md` | Add widget indicators | Add any number of secondary indicators to an existing time series or list widget. |
| `add-mod-pers-tar-thresh.md` | Add or modify another user's personal target or threshold | If you can create global targets or thresholds, you can modify or add personal targets and thresholds for any user. |
| `add-personas-project.md` | Add personas to a project | Each project has several personas with different roles in the Performance Analytics solution that you are designing. A persona is a role… |
| `admin-console-tree-view-nav.md` | Tree view navigation | To navigate the admin console tree view effectively, it's good to know what the various icons and other visual data in the tree view… |
| `analytics-accessibility-options.md` | Accessibility options on dashboards | Understand how accessibility settings affect reports and Performance Analytics widgets on dashboards. Data visualizations on a Workspace… |
| `analytics-hub-uuids.md` | Analytics Hub UUIDs | Every combination of breakdowns, elements, a time series aggregation, and a domain that you specify for an indicator has a unique… |
| `apply-time-series-result-components.md` | Applying time series to result or to contributing indicators | For a formula indicator, a time series aggregation can apply either to each indicator in the formula individually or to the formula result. |
| `applying-time-series-aggregations.md` | Applying time series aggregations | You can aggregate changes in indicators into discrete time intervals. These aggregations can make trends more easily visible, or help track… |
| `associate-domain-config-dashboard.md` | Associate a domain configuration with a dashboard | Display a domain picker on a dashboard to enable users of that dashboard to view scores from specific domains. |
| `associate-domain-config-dc-job.md` | Associate a domain configuration with a data collection job | To collect Performance Analytics indicator scores from the domains specified in a domain configuration, associate that domain configuration… |
| `automated-breakdowns.md` | Automated breakdowns | An automated breakdown uses a breakdown source to determine selectable elements. |
| `automated-indicators.md` | Automated indicators | An automated indicator uses an indicator source as its data set. The indicator source specifies a table or database view, conditions for… |
| `available-in-form-analytics.md` | Preconfigured in-form analytics | Preconfigured in-form analytics are available as plugins for several applications and their associated tables and forms. |
| `bkdown-matrix-formula-indicators.md` | Breakdown matrices in formula indicators | Formula indicators inherit breakdown matrices from indicators in the formula. |
| `breakdown-relations.md` | Navigating breakdown elements with breakdown relations | Breakdown relations open a new navigation path for viewing breakdown scores, by moving from one breakdown element to another element of the… |
| `breakdown-sources.md` | Breakdown sources | Breakdown sources specify which unique values, called breakdown elements, a breakdown contains. |
| `breakdown-widgets.md` | Breakdown widgets | Breakdown widgets show indicator scores grouped by breakdown elements. Different visualizations can be used to compare the relative… |
| `c_BreakdownElementFilters.md` | Element filters | Element filters enable you to specify or limit the displayed breakdown elements on visualizations.Select the breakdown source and filter… |
| `c_BucketGroups.md` | Bucket groups for breakdown sources | Bucket groups are used to recategorize data so it can be used as a breakdown, for example by grouping a range of values into discrete… |
| `c_ClctData.md` | Collecting indicator scores | Performance Analytics uses data collection jobs to collect and clean scores and snapshots. You can also set indicator scores manually. |
| `c_CollectionCleanup.md` | Cleaning collected Performance Analytics data | Performance Analytics scores and snapshots may grow over time and should be routinely cleaned to ensure optimal performance and accurate… |
| `c_CreatingBreakdowns.md` | Indicator breakdowns | Breakdowns enable you to group or filter indicator scores by a qualitative attribute such as Priority, Category, or Assignment Group. You… |
| `c_DashboardAdministration.md` | Administering dashboards | Learn about administering dashboards including how to group dashboards, how to move a dashboard with an update set, and addressing… |
| `c_DashboardRoles.md` | Dashboard permissions | Dashboards have special granular view and edit permissions that are managed from the Sharing pane. Access control lists (ACLs) apply to… |
| `c_ExcludingBreakdownsFromFormulas.md` | Prevent a contributing indicator in a formula from following breakdowns | You can select contributing indicators in a formula to not be broken down. When a user applies a breakdown to the formula indicator, the… |
| `c_ExcludingTimeSeriesFromIndicators.md` | Exclude time series from an indicator | Some time series aggregations are inappropriate to apply to some indicators. You can exclude time series on automated, formula, and manual… |
| `c_ForecastingData.md` | Performance Analytics scores forecasts | Performance Analytics enables you to forecast future scores based on past behavior. You can forecast scores on time series widgets, time… |
| `c_GetStartedwithPA.md` | Exploring Performance Analytics | Review the use cases, components, and architecture for indicator data sources and begin to implement indicators. |
| `c_IndicatorSources.md` | Indicator sources | Indicator sources are data sets consisting of filtered records from one table or database view.To provide a filtered data set of records… |
| `c_Indicators.md` | Performance Analytics indicators | Indicators (KPIs) define a performance measurement taken at regular intervals of a business service, an activity, or organizational… |
| `c_MonitorWorkflowWorkbenchWidget.md` | Monitor a workflow with a workbench process widget | A workbench process widget is a collection of indicators that tell a story. The widget enables you to analyze multiple facets of multiple… |
| `c_PADataArchitecture.md` | Configure Performance Analytics advanced features | Define key metrics and data structure to generate scores. |
| `c_PADomainUtils.md` | PADomainUtils - Global | The PADomainUtils API enables you to copy Performance Analytics records between different domains on the same instance. |
| `c_PAWebServiceIntegrations.md` | Integrate Performance Analytics | Integrate Performance Analytics with an external system to collect scores based on remote data or to expose Analytics Hub information. |
| `c_PAWidgetsAndDashboards.md` | Configure Performance Analytics fundamentals | Create and configure indicators and breakdowns. Collect data. Display calculated indicator scores. |
| `c_PAWithDomainSeparation.md` | Domain separation and Performance Analytics | Domain separation is supported for Performance Analytics. Domain separation enables you to separate data, processes, and administrative… |
| `c_PerformanceAnalytics.md` | Performance Analytics concepts | Performance Analytics uses terms and concepts that can differ from industry norms due to the unique nature of the ServiceNow platform. |
| `c_PremiumPerformanceAnalytics.md` | Activating your Performance Analytics subscription | Without a paid Performance Analytics subscription, your use is limited to 180 days of data collection (five months for monthly indicators)… |
| `c_ResponsiveDashboards.md` | Working with responsive dashboards | Responsive dashboards enable you to share widgets such as reports and Performance Analytics visualizations in the classic environment. An… |
| `c_ShowBkdwnRltnsWdgts.md` | Showing breakdown relations on dashboards | A breakdown widget can display 1st level breakdown elements that are related to the element selected for the dashboard. The widget must be… |
| `c_SpecialDashboards.md` | Using breakdowns on dashboards | You can add breakdown sources to a dashboard. Dashboard users then can select a breakdown source and one or more breakdown elements to… |
| `c_UseIndicatorOverview.md` | Analytics Hub list of indicators | The Analytics Hub provides a list of indicators, their scores, and a customizable selection of other analytics. Click the name of an… |
| `c_UsePerformanceAnalyticsScorecards.md` | Analytics Hub | The Analytics Hub is an exploratory view of indicators, used for more detailed analysis. It lets you see trends, predictions, breakdowns,… |
| `c_WidgetInteractivity.md` | Interacting with breakdown widgets on dashboards | Performance Analytics users can interact with individual breakdown widgets on dashboards to change the visualization or breakdown. |
| `c_Widgets.md` | Performance Analytics widgets | Widgets enable you to define visualizations for indicator scores. Widgets are shown on dashboards. |
| `cancel-pa-dc-job.md` | Cancel a data collection job | Cancel an active data collection job to stop the job from collecting scores. |
| `change-dashboard-owner.md` | Change the owner of a responsive dashboard | The owner of a dashboard can edit it, and share it with other users. |
| `classic-vis-overview.md` | Reporting, dashboards, and Performance Analytics in the Core UI | Present analytics on Core UI dashboards through reports and Performance Analytics widgets. Explore Performance Analytics indicators on the… |
| `collect-data-nowintel-solutions.md` | Collect data for Platform Analytics Solutions | After you install an Platform Analytics Solution and ensure that it points at the correct data structures in your instance, collect the… |
| `collect-initial-text-analytics-data.md` | Collect initial text analytics data | When you configure text analytics for an indicator source, no data is available until a relevant data collector job is run. If you have… |
| `collected-element-display-cutoff.md` | Collected scores and com.snc.pa.breakdown\_element\_cutoff | The elements of a breakdown that the Analytics Hub and KPI Details display for a selected date depend on the number of elements and the… |
| `color-schemes-pa-widgets.md` | Color schemes | When a data visualization illustrates multiple indicators, breakdowns, or table fields, the colors of the different values can follow a… |
| `condition-operators-ind-bkdowns.md` | Conditional filters and operators for indicators and breakdowns | Conditional filters for indicator data cascade from indicator and breakdown sources up to data visualizations. Where conditions are applied… |
| `configure-job-indicator.md` | Configure a job indicator | Increase the efficiency of data collection by configuring job indicators to collect only necessary and sensible data. |
| `configure-nowintel-solutions.md` | Configure Platform Analytics Solutions | Platform Analytics Solutions come configured with the expectation that you keep your ServiceNow AI Platform data in a standard set of… |
| `configure-widget-layouts.md` | Configure the layout of a responsive dashboard | You can change the appearance of widgets; change widget layouts; change the colors of the widget title, header, and background; and show or… |
| `considerations-creating-time-series.md` | Considerations when creating a time series widget | To create a time series widget that fulfills your business goal, keep several points in mind. |
| `content-packs-in-form-analytics-published.md` | Platform Analytics solutions | Prepackaged solutions featuring Platform Analytics dashboards with data visualizations and Performance Analytics indicators (KPIs) are… |
| `create-and-edit-dashboards.md` | Create and use dashboards | Learn about different types of dashboards and how to use them. |
| `create-area-visualization-ts.md` | Create an area visualization for a time series widget | To examine the contribution of one or more indicators to a summing indicator, create a time series widget with an area visualization. |
| `create-breakdown-mapping.md` | Assign and map breakdowns | Select which breakdowns to assign to an indicator. Map which field on the indicator source references the breakdown source. If no… |
| `create-column-bkdown-widget.md` | Create a column visualization for a breakdown widget | To compare the elements of one breakdown applied to one indicator, use a column visualization. |
| `create-column-total-bkdown-widget.md` | Create a columns and total visualization for a breakdown widget | To follow changes over time in both the scores of an indicator and the relative proportion of breakdown elements for that indicator, use a… |
| `create-column-visualization-ts.md` | Create a column visualization for a time series widget | To emphasize the indicator scores over time instead of the trend in scores, create a time series widget with a column visualization. You… |
| `create-domain-configuration.md` | Create a domain configuration | Create a domain configuration to define which domains to collect scores from and how to store scores within the domain hierarchy. |
| `create-ds-automated-indicator.md` | Create a Data snapshots automated indicator | To analyze the performance of a business process that is recorded in a ServiceNow table, use an automated indicator. If you have Data… |
| `create-ds-formula-ind.md` | Create a Data snapshots formula indicator | Create a formula indicator to calculate a score from two or more Data snapshots indicators. |
| `create-ds-source.md` | Create a Data snapshots source | To provide a filtered dataset of records that you can evaluate with one or more indicators, create an indicator source. Data snapshots… |
| `create-heatmap-pivot-widget.md` | Create a heatmap visualization in a pivot widget | To group the scores of an indicator by two breakdowns, use a heatmap visualization in a pivot widget. |
| `create-indicator-definition.md` | Create an indicator definition | You can create a new KPI Composer indicator definition directly from the relevant artifact in the Data Definition tab. Fill the indicator… |
| `create-kpi-composer-project.md` | Create a KPI Composer project | As the first step in using KPI Composer, create a project. |
| `create-latest-score-widget.md` | Create a latest score visualization for a score widget | To see the change between the latest score and a previous score, use a latest score visualization in a score widget. You can also show a… |
| `create-library-element.md` | Create a library element | Convert an artifact and its children in a KPI tree into a KPI Composer cross-project library element. |
| `create-line-bkdown-widget.md` | Create a line visualization for a breakdown widget | To follow changes over time in the relative proportion of breakdown elements for an indicator, use a line visualization in a breakdown… |
| `create-line-visualization-ts.md` | Create a line visualization for a time series widget | To show the trend over time in indicator scores, create a time series widget with a line visualization. |
| `create-pareto-bkdown-widget.md` | Create a Pareto visualization for a breakdown widget | To identify the most important breakdown elements when the breakdown has a large set of elements, use a Pareto visualization. |
| `create-pie-widget.md` | Create a pie, donut, or semi-donut visualization for a breakdown widget | To show the relative proportions of the elements of a breakdown, use a pie, donut, or semi-donut visualization. |
| `create-pivot-scorecard-breakdown.md` | Create a pivot scorecard visualization for a breakdown widget | To compare the relative proportions of breakdown elements between a number of indicators, use a pivot scorecard visualization in a… |
| `create-pyramid-funnel-widget.md` | Create a pyramid or a funnel visualization for a breakdown widget | To show the relative proportions of the elements of a breakdown, particularly when the elements represent stages in a process, use a… |
| `create-real-time-score-widget.md` | Create a real-time score visualization for a score widget | To see the current score, use a real-time score visualization in a score widget. You can also show a trend line of scores. |
| `create-relation-btwn-bkdn-elements.md` | Create relations between elements of a breakdown | Use a breakdown relation to set up navigation between a hierarchy of elements within the same breakdown. A field in the breakdown records… |
| `create-relative-compare-bkdn.md` | Create a relative compare visualization for a breakdown widget | To show how the relative proportions of several indicators change over time, use a relative compare visualization for a time series. |
| `create-relative-compare-ts.md` | Create a relative compare visualization for a time series widget | To show how the relative proportions of several indicators change over time, use a relative compare visualization for a time series. |
| `create-scorecard-list-widget.md` | Create a scorecard visualization in a list widget | To list the metrics of several indicators, use a scorecard visualization in a list widget. |
| `create-scorecard-widget.md` | Create a scorecard visualization for a breakdown widget | To show the trend for the elements of one breakdown applied to one indicator, use a scorecard visualization. |
| `create-speedometer-widget.md` | Create a speedometer or a dial visualization for a score widget | To show the latest score of an indicator compared to the range of scores, use a speedometer or dial visualization in a score widget. A… |
| `create-spider-list-widget.md` | Create a spider visualization in a list widget | To plot the scores of several indicators, use a spider visualization in a list widget. |
| `create-spline-visualization-ts.md` | Create a spline visualization for a time series widget | To show the trend over time in indicator scores when you need to apply curve fitting, create a time series widget with a spline… |
| `create-stacked-col-visualization-ts.md` | Create a stacked column visualization for a time series widget | To compare and sum the scores of several indicators, create a widget as a time series with a stacked column visualization. |
| `create-stacked-column-bkdown-widget.md` | Create a stacked column visualization for a breakdown widget | To follow changes over time in the relative proportion of breakdown elements for an indicator, use a stacked column visualization in a… |
| `create-step-visualization-ts.md` | Create a step visualization for a time series widget | To emphasize changes in indicator scores between discreet points in time, create a time series widget with a step visualization. |
| `create-treemap-breakdown.md` | Create a treemap visualization for a breakdown widget | To display a hierarchy of breakdown elements, use a treemap visualization. |
| `create-word-cloud-widget.md` | Create a text widget | To help analysts visualize any patterns in user-entered text in an indicator, create a word cloud visualization in a text widget. |
| `create_widget_displays_webpage.md` | Create a widget that displays a ServiceNow UI page | You can create a ServiceNow UI page that displays a web page. You can then add that UI page to a widget that can be added to dashboards. |
| `cross-project-artifact-libraries.md` | Cross-project library elements | Library elements are single artifacts or trees of artifacts that you can reuse in multiple projects. |
| `custom-content-pdf-export-limitations.md` | Custom content PDF export limitations | When you create custom content to be placed as widgets on dashboards and home pages, you must perform extra tests before you export the… |
| `dashboard-admin-console.md` | Admin Console for Dashboards | The Performance Analytics Admin Console contains several features for dashboard management. |
| `dashboard-execs.md` | Dashboard executions | The Dashboard Executions list enables you to view how long it takes for your Core UI dashboards to load and the ID of the user who launched… |
| `dashboard-properties.md` | Responsive dashboard properties | Use properties to fine-tune dashboard behavior and appearance. |
| `dashboard-statistics-exec.md` | Dashboard execution statistics | The Dashboard Stats Executions list enables you to view how long it takes for your Core UI dashboards to load. The list includes one entry… |
| `dashboard-statistics.md` | Dashboard statistics | The Dashboard Stats list enables you to view how often each of your Core UI dashboards is run and how long it takes to run them. |
| `dashboard-url-parameters.md` | Dashboard URL parameters | Dashboard URL parameters allow you to control the visibility of headers and the breakdown sources of dashboards used in application… |
| `dashboards-landing-page.md` | Responsive dashboards in the Core UI | Responsive Dashboards enable you to display multiple performance analytics, reporting, and other widgets on a single screen. Use dashboards… |
| `data-collection-process-logging.md` | Data collection process and logging | Performance Analytics data collection jobs collect indicator scores. To debug data collection, it is helpful to understand the data… |
| `deactivate-mlb-for-indicator.md` | Deactivate Data snapshots | You can turn Data snapshots off or back on for an indicator, provided that indicator supports Data snapshots. An admin can turn the feature… |
| `define-properties-project.md` | Define properties for a project | In the Project Properties, you can associate knowledge articles, owners, and contact persons with the project. |
| `delete-indicator.md` | Delete an indicator | Delete unwanted or unused indicators from your instance. Deleting indicators is risky, so there are several restrictions. |
| `delete-pers-tar-thresh.md` | Bulk delete targets/thresholds or delete another user's personal target or threshold | If you can create global targets or thresholds, you can delete them in bulk. Use the same process to delete another user's personal targets… |
| `dependency-assessment-show-used-by.md` | Bottom-up tree view | You can see where any element in the tree view is used. This is useful when you want to change an element such as an indicator or breakdown… |
| `dependency-assessment-treeview.md` | Dependency Assessment tree view | The tree view enables admin users to see the relationships between PA entities and to know the impact of changes made to any node in the… |
| `design-kpi-tree.md` | Analysis and the KPI tree | In the Analysis tab of KPI Composer, design your KPI tree. Specify your business goals, their associated critical success factors, and the… |
| `designing-pa-solution.md` | Design your Performance Analytics solution with KPI Composer | KPI Composer ensures that your performance management strategy aligns with business goals and has support from executive sponsors. Use KPI… |
| `detect-indicators-no-scores-formula.md` | Detect indicators with no scores in a formula | As the formula creator, you can handle contributing indicators that have null scores. First set the formula indicator to calculate the… |
| `disable-mes.md` | Disable multiple element selection on a dashboard | Dashboard owners have the option to disable multiple element select on an entire breakdown dashboard. |
| `domain-separation-in-dashboards.md` | Domain separation and responsive dashboards | Domain separation is supported in dashboard creation and administration. Domain separation enables you to separate data, processes, and… |
| `ds-jobs-tables.md` | Data snapshots jobs and tables | Several types of components are installed with activation of the Data snapshots plugin, including tables and scheduled jobs. |
| `duplicate-dashboard.md` | Duplicate an Analytics and Reporting Solution dashboard | Copy an Platform Analytics Solution dashboard, including the tabs, portal pages, and canvas records. Widgets on the dashboard are not… |
| `edit-library-element.md` | Edit or delete a library element | You can add artifacts to a library element, or convert a library element back to project-based artifacts. You can also edit the data… |
| `enable-pa-db-records-scoped-apps.md` | Enable pa\_dashboard records in scoped applications | When application administration is enabled for a scoped application, access control list (ACL) rules for the scoped application are… |
| `enable-pdf-export.md` | Enable PDF export of dashboards | To export dashboards to PDF, a plugin and property are needed. |
| `enable-real-time-update-single-score-widget.md` | Enable real-time updating for single score report widgets | Real-time updates ensure that users viewing a responsive dashboard always see the most up-to-date information. |
| `example-field-mapping.md` | Example: Field mapping | The Category breakdown maps the Category field on the incident table to the Incident.Category breakdown source, which references the… |
| `example-script-mapping.md` | Example: Script mapping | The Age breakdown uses the Incident.Age.Days script to calculate the age of incidents in days and map the values to the Incident Age Ranges… |
| `explore-manage-dashboards.md` | Explore and manage dashboards | Quickly identify the relationships between Performance Analytics elements, such as dashboards, reports, and indicators. Each dashboard tab… |
| `exploring-dashboards.md` | Exploring Responsive dashboards | Learn more about dashboards with a sample workflow and reviewing the benefits it can provide for different users. |
| `export-kpi-composer-project.md` | Export a KPI Composer project | To copy a KPI Composer project between instances, first export the project as a JSON file. |
| `filter-breakdown-multiple-elements.md` | Filter dashboards on breakdown elements | Some dashboards let you apply one or more Performance Analytics breakdown elements to filter the entire dashboard. For example, you can… |
| `find-resp-db.md` | Find a responsive dashboard | Use dashboard categories, dashboard groups, and dashboard lists to find the dashboard you want to use. |
| `formula-indicators.md` | Formula indicators | Formula indicators use data from other indicators to calculate new metrics. |
| `generating-tasks-kpi-composer.md` | Generating tasks in KPI Composer | For each KPI Composer artifact in your project, you can generate a task to create an equivalent Performance Analytics element. All tasks… |
| `get-indicator-analytics.md` | Get analytics methods in formulas | To insert a calculated value from the Analytics Hub into a formula, use a method in the formula. |
| `grouping-filtering-breakdown.md` | Grouping by breakdown and filtering by breakdown | In breakdown widgets, breakdowns either group or filter indicator scores. When you create a widget, this dual purpose of breakdowns affects… |
| `guidelines-translated-dbs.md` | Guidelines for translated dashboards | Users can only find translated dashboards under certain configurations. You can translate the dashboard name to make it searchable. When… |
| `historical-data-nowintel-solution.md` | Run historical data collection for a Platform Analytics Solution | After you activate an Platform Analytics Solution, run a historical data collection job. This job gives you immediate insight from your… |
| `homepage-deprecation-help-tool.md` | Homepage deprecation | Support for homepage functionality has been phased out. It is not possible to create or edit homepages at all when Next Experience is… |
| `homepage-migration-status-table.md` | Homepage migration status table | Use the Homepage migration status table to address homepage retirement and conversion. |
| `hp-dep-help-tool-features.md` | Homepage deprecation help tool | Use the Homepage deprecation help tool to find all of your homepages in one place and convert them to dashboards, retire them, and restore… |
| `hpm-convert-homepages.md` | Convert homepages to individual dashboards | Populate the Homepage migration status table and then determine which homepages to convert to dashboards. You can convert homepages to… |
| `hpm-convert-multiple-hps-db-tabs.md` | Convert homepages to dashboard tabs | After you populate the Homepage migration status table, you can convert one or more homepages to tabs on new or existing dashboards. |
| `hpm-populate-hp-status-table.md` | Populate the homepage migration status table | The Homepage migration status table enables you to address homepage retirement and conversion. Run a scheduled workflow to populate the… |
| `hpm-restore-homepages.md` | Restore a homepage | Restore retired homepages as dashboards. |
| `hpm-retire-homepages.md` | Retire a homepage | Use the homepage migration status table to retire homepages. When you retire a homepage, you remove visibility and editing options from all… |
| `impact-analysis.md` | \(Legacy\) Dependency Assessment | Dependency Assessment enables you to view, analyze, and edit your performance analytics components including widgets, indicators, and… |
| `implementing-pa.md` | Implement Performance Analytics | Follow these steps to begin using Performance Analytics to improve your service levels. |
| `import-kpi-composer-project.md` | Import a KPI Composer project | If you have an exported KPI Composer project, you can import it to your instance. |
| `in-form-analytics.md` | In-form analytics | In-form analytics integrate performance insights into forms so that users can access important metrics in context and make better decisions. |
| `index-indicators.md` | Indexing multiple indicators in a formula | You can write a formula to measure what the gap is to the overall target of multiple, combined indicators. Such a formula indicator is… |
| `indicator-scores-reference-currency.md` | Indicator scores in reference currency | You can track the trends for monetary fields of the types Price, Currency, or FX Currency. The scores for an indicator based on any of… |
| `install-content-single-record.md` | Install a single solution metadata record | Install a single solution metadata record used by a dashboard, such as a widget, to match the latest version of the record without… |
| `install-content.md` | Install a dashboard | Use the Solution Library to install a dashboard and all its associated visualizations such as widgets and reports, and to configure… |
| `install-hp-dep-app.md` | Install the Homepage deprecation help tool | To convert, retire, and restore homepages, install the Homepage deprecation help tool. |
| `interactive-analysis-aggregations.md` | Interactive Analysis aggregations | When you work with Interactive Analysis, you can view data from the perspectives of record counts, sums, averages, and distinct counts. |
| `interactive-analysis-info-panel.md` | Interactive Analysis information panel | The Filter Info panel summarizes what the current filter shows and enables you to edit the source filter condition, bookmark an interactive… |
| `interactive-analysis-pa.md` | Interactive Analysis for Performance Analytics | Interactive Analysis enables you to quickly explore Performance Analytics data using visualizations. |
| `interactive-analysis-persistence.md` | Interactive Analysis persistence | The filters that you select persist between uses of Interactive Analysis per view and per user. |
| `interactive-analysis.md` | Interactive Analysis | Interactive Analysis enables you to quickly explore data on a list of records. |
| `interactive-filters-deduplication.md` | Interactive Analysis filter deduplication | Upon launching Interactive Analysis, duplicate filters are removed automatically from the Filters panel. You do not have to clean up the… |
| `kpi-composer-projects.md` | KPI Composer projects | KPI Composer is based on projects. Each project in KPI Composer consists of Key Performance Indicator (KPI) trees and the functional and… |
| `launch-dependency-assessment.md` | Launch Dependency Assessment | Use the Dependency Assessment tree view to view and edit Performance Analytics components including widgets, indicators, and breakdowns,… |
| `launch-interactive-analysis-pa.md` | Launch Interactive Analysis | Launch Interactive Analysis from any list. |
| `limitations-mlb.md` | Limitations and requirements for Data snapshots | Several features of indicators and breakdowns are not supported with Data snapshots and multiple breakdowns. |
| `link-automated-indicator-benchmark.md` | Link an automated indicator to a benchmark | To enable the comparison of indicators to ITSM and ITOM benchmarks, link an automated indicator to the corresponding benchmark KPI. A… |
| `list-widgets.md` | List widgets | List widgets show the scores of multiple indicators. |
| `log-details-optimized-dc.md` | Log details for optimized data collector | Starting with the Tokyo release, a new, optimized data collector is available. The log details for this data collector differ from the log… |
| `manage-responsive-dashboards.md` | Manage responsive dashboards | Depending upon their role, users can delete or duplicate responsive dashboards, and remove a user from a dashboard. All users can mark a… |
| `manual-breakdowns.md` | Manual breakdowns | In a manual breakdown, you define the breakdown elements and the indicator scores for each element manually instead of using records from a… |
| `modify-source-filter-criteria.md` | Edit source filters | You can edit a source filter in the Interactive Analysis Filter Info panel. |
| `multi-element-select-indicator-views.md` | Showing multiple elements separately or aggregated | When you select multiple elements on a dashboard, widgets that follow these elements can show their values either separately or as an… |
| `multi-level-breakdowns.md` | Data snapshots and multiple breakdowns | The Data snapshots feature in Platform Analytics allows for multiple breakdowns while analyzing your indicators (KPIs). This architecture… |
| `optimized-data-collection.md` | Optimizing data collection | The optimized Performance Analytics data collector reduces the time, memory, and CPU usage for processing large data sets. |
| `optional-settings-breakdown-widgets.md` | Additional settings for breakdown widgets | Breakdown widgets have the following optional settings for the date range, the display, the grouping breakdown, and for the column… |
| `optional-settings-ts-widgets.md` | Additional settings for time series widgets | Time series widgets have the following optional settings for display, for the date range, and for the axis labels. You can also use these… |
| `original-data-collection-process.md` | Log details for classic data collector | Performance Analytics score collection follows the process described here. To aid troubleshooting, a mapping between job steps and log… |
| `pa-admin-console.md` | Performance Analytics Admin Console | From a single console, administrators can manage Platform Analytics Solution content, manage Performance Analytics widgets and dashboards,… |
| `pa-architecture.md` | Performance Analytics architecture | Before using Performance Analytics, familiarize yourself with how the layers of architecture take you from raw database entries to… |
| `pa-chart-props.md` | Chart properties for Performance Analytics | A chart refers here to a graphical component of a Performance Analytics widget or the Analytics Hub. These properties apply only to the… |
| `pa-collection-cleanup-props.md` | Collection cleanup Performance Analytics properties | Several properties determine how long Performance Analytics scores and snapshots are maintained before the scheduled cleanup job deletes… |
| `pa-data-flow.md` | Performance Analytics data flow | Before you get started with Performance Analytics, understand how the data flows through the platform, ultimately resulting in your ability… |
| `pa-dc-props.md` | Data collector Performance Analytics properties | Data collector properties enable you to configure various limits for Performance Analytics data collection. The properties are configured… |
| `pa-default-color-scheme-props.md` | Default color scheme Performance Analytics properties | These properties set the default colors for the chart overall and for indicator targets. |
| `pa-domain-configurations.md` | Approaches to Performance Analytics with domain separation | When using Performance Analytics with domain separation, you can collect domain-specific scores. You can use global or domain-specific… |
| `pa-domain-separation-msp.md` | Grouping domains in Performance Analytics domain configurations | Instead of configuring Performance Analytics for the domains of a specific user, create a reusable domain configuration. Select domains… |
| `pa-external-data.md` | Using Performance Analytics with external data | Performance Analytics on external data sources enables you to perform detailed analysis on data that is not in your ServiceNow… |
| `pa-fiscal-year-props.md` | Fiscal year Performance Analytics properties | These properties set the year in Performance Analytics to match your company fiscal year. |
| `pa-limit-setting-props.md` | Breakdown and indicator Performance Analytics properties | These properties set limits on breakdown elements and indicators, mostly in the context of visualizations. |
| `pa-overview.md` | Performance Analytics \(Indicator data sources\) | ServiceNow Performance Analytics is an in-platform process optimization solution that utilizes indicators (KPIs) to answer key business… |
| `pa-properties.md` | Performance Analytics properties | These system properties control the behavior of Performance Analytics. |
| `pa-scores-migration.md` | Migrating indicator scores | The Performance Analytics Scores [pa\_scores] table was split into two tables. This structure helps with processing large numbers of… |
| `pa-scripts.md` | Scripting in Performance Analytics | Performance Analytics provides several script objects for use in scripts and APIs for querying Performance Analytics data. The scripts… |
| `pa-snapshots.md` | Performance Analytics snapshots | Snapshots are the lists of records (sys\_ids) that are collected at the time that the scores for those records are collected. Snapshots… |
| `pa-targets-thresholds.md` | Performance Analytics targets and thresholds | Targets and thresholds enable you to define important points in your data and provide notifications when a score reaches a specific point. |
| `pa-targets.md` | Indicator targets | Targets are goals your organization wants to achieve. Targets show the difference between the desired score at a certain date and the… |
| `pa-threshold.md` | Indicator thresholds | Thresholds define a normal range of scores for an indicator and alert you when certain events occurs, like when a score reaches an all-time… |
| `pa-vs-reporting-pa.md` | Performance Analytics indicators compared to table data | Indicator data sources address a different set of use cases than table data sources. |
| `performance-analytics-glossary.md` | Performance Analytics terms | Performance Analytics uses terms and concepts that can differ from industry norms due to the unique nature of the ServiceNow platform. |
| `performance-analytics-reference.md` | Performance Analytics reference | Reference topics provide information about roles and properties, and include a glossary of terms. |
| `personalized-visuals.md` | Personalized visuals | Configure visuals with dynamic elements to show information that applies only to the person looking at the visual on a dashboard, service… |
| `planning-indicators.md` | Planning your indicators | Before creating an indicator, clarify what goals you wish to attain with the indicator. |
| `populate-hp-migration-status-table-multi-domains.md` | Populate the homepage migration status table for multiple domains | By default, the flow to populate the homepage migration status table applies only to the global domain. You can create a flow to apply to… |
| `put-spotlight-on-records.md` | Put a Spotlight on records | Use the Spotlight feature to illuminate records that you might overlook. |
| `quick-start-tests-dashboards.md` | Quick start tests for Dashboards | Validate that Dashboards still work after you make any configuration change such as applying an upgrade. Copy and customize these quick… |
| `r_AvailableContentPacks.md` | Available Platform Analytics Solutions | The following Platform Analytics Solutions are available for their corresponding ServiceNow Performance Analytics entitlements. The… |
| `r_FormulaRounding.md` | Rounding and precision in indicators | Indicators round fractional results using "Banker's rounding" or mathematical rounding depending on the indicator Precision. |
| `r_PADU-PADomainUtils.md` | PADomainUtils - PADomainUtils\(\) | Instantiates a new PADomainUtils object to move or copy Performance Analytics records from the global domain. |
| `r_PADU-PADomainUtils_String.md` | PADomainUtils - PADomainUtils\(String domainFrom\) | Instantiates a new PADomainUtils object to move or copy Performance Analytics records from the specified domain. |
| `r_PADU-copyJob_String_String.md` | PADomainUtils - copyJob\(String paJob, String runAs\) | Copies a Performance Analytics scheduled data collection job record to another domain. |
| `r_PADU-copy_String.md` | PADomainUtils - copy\(String runAs\) | Copies Performance Analytics records to a different domain. |
| `r_PADU-isWriteable_String_String.md` | PADomainUtils - isWriteable\(String table, String id\) | Evaluate if you can write to a specific record identified by table and sys\_id. |
| `r_PADU-move_String.md` | PADomainUtils - move\(String runAs\) | Moves Performance Analytics records to a different domain. |
| `r_PADU-setFoundation_boolean.md` | PADomainUtils - setFoundation\(Boolean foundation\) | Use this method to move or copy only foundational records in a hybrid domain configuration. |
| `r_PADU-setOverrides_boolean.md` | PADomainUtils - setOverrides\(Boolean overrides\) | Use this method before copying records to set the sys\_override value of the new record to the original parent record. |
| `r_PARoles.md` | Performance Analytics roles | Assign roles to ensure that users can perform all necessary actions. |
| `r_PerformanceAnalyticsAPIExamples.md` | Performance Analytics API examples | These examples demonstrate how to perform a REST query using cURL commands, and show the data returned for each command. Each example… |
| `r_StUpPAInctMgmt.md` | Try out Complimentary Performance Analytics for Incident Management | Complimentary Performance Analytics for Incident Management is a limited version of Performance Analytics that is included in the base… |
| `real-time-scores.md` | Real-time scores | You can view some Performance Analytics scores in real-time instead of from the most recent data collection job. If real-time scores are… |
| `remove-filter-from-ia.md` | Remove a filter from Interactive Analysis | You can remove a filter from Interactive Analysis and specify whether to remove the filter element from Group by and Stack by lists in the… |
| `request-bi-service.md` | Request an analytics service | Request services associated with dashboards, such as to request a new dashboard or access to an existing dashboard.Analytics service… |
| `responsive-dashboard-role-examples.md` | Responsive dashboard role examples | Your ability to create, edit, view, or share a dashboard depends on your roles. These examples show what you can do with a dashboard based… |
| `restrict-dashboard-access-to-certain-roles.md` | Restrict responsive dashboard access to specific roles | Specify additional roles required to access the dashboard when you share a dashboard with specified users, groups, and roles. Only users… |
| `restrict-responsive-db-sharing-to-specific-roles.md` | Restrict responsive dashboard sharing by role | You can configure responsive dashboard properties to restrict which users are able to share responsive dashboards. |
| `restrict-responsive-db-sharing-w-security-rule.md` | Restrict responsive dashboard sharing with security rules | You can configure the users, roles, and groups that users can see on the Share panel when they share a responsive dashboard. |
| `review-breakdown-sources.md` | Review the breakdown sources | Breakdown sources represent the elements that you use to examine a KPI in more detail. Modify the breakdown source to limit the element… |
| `review-indicator-sources.md` | Review the indicator sources | Determine which fields contain the data you are looking for in each application you are enabling for Performance Analytics. |
| `reviewing-your-project.md` | Reviewing your project | Summarize both the created KPI Composer project artifacts and the planned Performance Analytics components. Validate the contents of your… |
| `same-breakdown-widget-dashboard.md` | Same breakdown on widget and dashboard | If a widget uses the same breakdown as the dashboard, the dashboard breakdown does not apply. |
| `schedule-job-nowintel-solution.md` | Schedule data collection for a Platform Analytics Solution | Enable the periodic data collection job for your Platform Analytics Solution. Check that the time that it runs is correct. |
| `schedule-scorecard-pdf.md` | Schedule the export and distribution of an indicator | Schedule an indicator to automate its distribution. |
| `score-widgets.md` | Score widgets | Score widgets show aggregate indicator scores. |
| `scorecard-compare-tab.md` | Compare scores | In the Analytics Hub Compare tab, compare scores on any two dates, or compare scores against linked benchmark scores. |
| `scorecard-overview-tab.md` | View scores and statistics | The Analytics Hub Overview tab shows the score for a time period, statistics, and a time series. You can set the time period for the… |
| `search-text-for-phrases.md` | Search text for phrases | You can specify phrases that text analytics searches for, instead of searching for only the most frequent individual words. |
| `select-keywords-default-drilldowns.md` | Save keywords for text analytics | You can save keywords that will always filter a text analytics widget. You can save them directly on the widget in a dashboard, choosing… |
| `select-text-analytics-stop-words.md` | Select text analytics stop words | Select words to exclude from text analysis. You can exclude words at either the indicator source or the indicator level. |
| `self-diagnostics.md` | Performance Analytics diagnostics | Identify and diagnose configuration issues using predefined scripts that examine the database for invalid records and provide suggestions… |
| `service-portal-pa-widget.md` | Performance Analytics widgets on Service Portal | You can show Performance Analytics indicators and breakdowns using Service Portal.You can activate the Performance Analytics and Reporting… |
| `set-dashboards-as-home-for-all-users.md` | Set dashboards as home for all users | You can set dashboards as home for all users. By default, the most recent dashboard a user has visited is the dashboard they see when they… |
| `set-one-db-as-home-for-specified-users.md` | Set a specific dashboard as home for specific users | Configure ServiceNow so that specified users see the same dashboard when they log in. |
| `set-specific-db-as-home-for-all-users.md` | Set a specific dashboard as home for all users | Configure ServiceNow so that all users see the same dashboard when they log in. |
| `set-up-text-analytics.md` | Set up text analytics | Select the text fields to analyze and which indicators to analyze. |
| `set-up-widgets-for-breakdown-dashboards.md` | Configure widgets for breakdown dashboards | Configure each widget that goes on a breakdown dashboard. The configuration determines whether and how the widget follows the elements… |
| `set-widget-on-click.md` | Set the on-click behavior of a widget | You can configure what happens when a user clicks on a widget. |
| `share-a-kpi-composer-project.md` | Share a KPI Composer project | You can share a KPI Composer project that you own or that you are responsible for. You can provide the user with either read-write or… |
| `solve-problems-empty-dbs.md` | Solve problems with empty dashboards | When a dashboard shows an empty page with an empty dashboard selector, the dashboard name may include special characters. |
| `solving-issues-translated-dashboards.md` | Solving issues on translated dashboards | Users can only find translated dashboards under certain configurations. You can translate the dashboard name to make it searchable. |
| `store-apps-pa-content.md` | ServiceNow Store applications with Performance Analytics content | The following applications on the ServiceNow Store include Performance Analytics components, such as a dashboard showing widgets for… |
| `synch-group-by-stack-by-elements.md` | Synchronize Group by and Stack by elements in filters | Synchronize Group by and Stack by elements in an interactive analysis when filters are added to the filter panel and when they are removed… |
| `t_AssigningAnIndicatorToABreakdown.md` | Assign an indicator to an automated breakdown | Associate automated or formula indicators with a breakdown to enable the collection of broken down scores for those indicators. |
| `t_ControlAccessToABreakdown.md` | Control ability to view breakdown elements | To limit which breakdown elements a subset of users can view on indicators, implement element security. Element security applies to… |
| `t_ControlAccessToADashboard.md` | Share a responsive dashboard | Share a dashboard with other users to create a shared view of data that you can use to collaborate. You can give other users viewing rights… |
| `t_ControlAccessToAnIndicator.md` | Control access to an indicator | You can control which user roles grant access to specific indicators. Access to an indicator is regulated in the indicator record. |
| `t_CopyADashboardURL.md` | Copy a responsive dashboard URL | It is not possible to copy a dashboard URL from the browser. You can, however, create a URL that opens the current view of the dashboard,… |
| `t_CreatASchedDataCollJob.md` | Create or schedule a data collection job | Schedule a data collection job to regularly collect Performance Analytics indicator scores and snapshots. |
| `t_CreateABreakdownRelation.md` | Create a breakdown-to-breakdown relation | To set up navigation in a visualization between the elements of two breakdowns at the same level, create a breakdown relation between the… |
| `t_CreateADashboard.md` | Create or configure a responsive dashboard in Core UI | Create a dashboard where you can add Performance Analytics widgets, data visualizations, and other content that you frequently use. You can… |
| `t_CreateAFormulaIndicator.md` | Create a formula indicator | Calculate scores from the scores of one or more other indicators. Apply mathematical operations or a preset method, such as the method to… |
| `t_CreateAManualIndicator.md` | Manual indicators | Manual indicators do not use scores collected from a database. Manual indicators are typically used for data that cannot be retrieved from… |
| `t_CreateAnAutomatedIndicator.md` | Create an automated indicator | To analyze the performance of a business process that is recorded in a ServiceNow table, use an automated indicator. If a suitable… |
| `t_CreateBreakdownFromWizard.md` | Create a breakdown from a wizard | Create a breakdown, breakdown source, and breakdown mappings, and associate the breakdown with indicators. |
| `t_CreateEmailSummaries.md` | Create an email notification for indicators | Performance Analytics can automatically generate an email with the score, change %, target, and score-target gap % of one or more… |
| `t_CreateInFormAnalyticsAction.md` | Add in-form analytics to a form | Create a UI action that enables users to view relevant analytics while completing a form. The UI action associates the table that uses the… |
| `t_CreatingABreakdownForIndicators.md` | Create an automated breakdown | To create an automated breakdown, select a breakdown source for it to use and apply access restrictions. Then map which field on the… |
| `t_CreatingIndicatorGroups.md` | Create an indicator group | For convenience, you can organize related indicators into an indicator group. When you configure some visualizations that show multiple… |
| `t_CreatingUnits.md` | Create a unit | You can define units in which Performance Analytics indicator scores are shown. Units can be numbers, percentages, currencies, quantities… |
| `t_CrtBkdnBreakdownMpngs.md` | Create a breakdown mapping on a breakdown record | Specify which field on the indicator source references the breakdown source. If no appropriate field is available, specify a script to… |
| `t_CrtIndctrIndctrWzrd.md` | Create an automated indicator with a wizard | Quickly create a Performance Analytics automated indicator with breakdowns, widgets, and data collection jobs for that indicator. You still… |
| `t_DefiningABreakdownSource.md` | Define a breakdown source | Specify a facts table to serve as a data source for breakdowns. External data is supported via Workflow Data Fabric tables. Apply… |
| `t_EditADashboard.md` | Edit a responsive dashboard | You can edit the contents of a dashboard, including Performance Analytics widgets, reports, and tabs. Because dashboards are shared, any… |
| `t_EditAJobForTheIndicator.md` | Add a collection job to an indicator | To collect scores for an automated indicator, add a collection job to that indicator. |
| `t_ExistingBreakdownDashboard.md` | Add breakdown sources to a dashboard | To enable dashboard users to filter visualizations on a dashboard by breakdown element, add breakdown sources to the dashboard. |
| `t_ExportAHomePageOrDashboardToPDF.md` | Export a responsive dashboard to PDF | Export a dashboard as a PDF so you can archive, print, or distribute it.It's possible to export any dashboard or homepage to PDF using your… |
| `t_GroupDashboards.md` | Organize dashboards into groups | Assign dashboards to groups so that users can find the dashboards they want more easily. Dashboard groups determine how dashboards appear… |
| `t_ManuallyAddingScoresForIndicators.md` | Add or edit indicator scores manually | You can manually enter score data for automated and manual indicators. Exercise care when editing scores for automated indicators. |
| `t_MoveDashboardWithUpdateSet.md` | Move a Core UI dashboard with an update set | Portal pages related to dashboard tabs aren’t automatically transferred in update sets. You can add portal pages to update sets from a… |
| `t_RunHistoricalDataCollection.md` | Collect historical data | Run a historical data collection job to collect scores and snapshots for existing records. When collecting data for the first time, such as… |
| `t_SetDashboardsAsHome.md` | Set responsive dashboards as your home | You can set dashboards as your Home. With this setting, the last dashboard you selected appears when you select the logo on the upper left… |
| `t_ViewWidgetStats.md` | View widget statistics | You can view statistics about Performance Analytics widgets to help identify and resolve problems, such as if a widget is loading slowly on… |
| `t_ViewingADataCollectionJobEvent.md` | View a data collection job event | Job events show which jobs have been executed for Performance Analytics and which actions have been triggered in your ServiceNow instance,… |
| `t_ViewingADataCollectionJobLog.md` | View the data collection job logs | Job logs display information about the data collection jobs that have run for Performance Analytics. You can view job logs, create events,… |
| `t_optimizeWidgetRenderingTime.md` | Optimize widget rendering time on responsive dashboards | Large dashboards can take a long time to render, especially when widgets depend on complex queries or queries on large tables. You can use… |
| `tables-unlimited-breakdowns.md` | Data snapshots sources and collection | Data snapshots include data sources for indicator score collection and the mapping between indicators and these sources. |
| `text-analytics-widgets.md` | Text analytics and text widgets | Text analytics reveal any patterns that exist in user-entered text fields. |
| `time-series-widgets.md` | Time series widgets | Time series widgets show changes in an indicator score over time. Different visualizations emphasize the trend in the scores or the scores… |
| `time-zones-indicator-formulas.md` | Changes to score\_start/end because of different user time zones | For formula indicators, the values of the variables score\_start and score\_end are calculated based on the time zone of the user who is… |
| `transfer-aggregation-domains.md` | Transfer domain configuration with score aggregation | To transfer between instances a Performance Analytics domain configuration that is set to aggregate scores, transfer both the configuration… |
| `troubleshoot-dashboard-permissions.md` | Solving permissions issues on a responsive dashboard | Dashboard permissions can be set in several different locations.Permissions on dashboards can be complicated. If you set a permission on a… |
| `troubleshooting-dashboard-update-set.md` | Solving errors on dashboards moved with update sets | When you move a dashboard with an update set, if errors are shown on the Update Set Preview Problems tab of the Retrieved Update Set page,… |
| `update-pa-scripts.md` | Update Performance Analytics scripts | Platform Analytics Solutions include Performance Analytics scripts to perform calculations on records. These scripts use the time stamp… |
| `upgrade-content.md` | Upgrade a dashboard | When you upgrade a dashboard, solution metadata that have updates available, including any new records added to the dashboard, are… |
| `use-library-element.md` | Use a library element | Add a library element to a KPI tree in any KPI Composer project. |
| `validate-dashboard-tabs-moved.md` | Validate that tabs are moved to a target dashboard | When you move a dashboard with an update set, validate that the tabs are moved to the target instance and are populated. |
| `view-data-collection-usage-statistics.md` | View data collection usage | To view statistics about data collection jobs, click Data Collection Overview in the Usage tile on the Performance Analytics Admin Console. |
| `view-scorecard.md` | Analytics Hub for a specific indicator | Use the Analytics Hub to analyze indicator data deeply, such as by aggregating data, comparing scores, or viewing changes over time. |
| `widgets.md` | Widgets | Objects that have been added to dashboards in Core UI are called widgets. You can create and manage widgets. Many applications have their… |
| `workflow-automated-indicators.md` | Workflow for creating indicators | Start with ServiceNow AI Platform tables and work your way up to a completed indicator with score collection that you can share on a… |
| `write-journal-entries-kpi-composer.md` | Write journal entries for a project | Keep track of your KPI Composer project with journal entries |
