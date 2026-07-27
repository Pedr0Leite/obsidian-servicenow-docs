# ServiceNowOfficialDocs/it-operations-management/event-management — File Index

Navigation index for AI agents. One row per file in this directory (380 files). Auto-generated from frontmatter — do not hand-edit; regenerate via `scripts/gen_indexes.py` if files are added/removed.

---

| File | Title | Description |
|------|-------|-------------|
| `Alert-Groups.md` | Alert grouping types and creation methods | Explore different alert grouping types, understand their descriptions, and learn about their creation methods to enhance problem… |
| `EM-insert-health-job.md` | Configure the Event Management - Insert Health Monitor scheduled job | Determine what the Event Management - Insert Health Monitor scheduled job is to monitor. After the job runs, you can view the ServiceNow… |
| `NLP-alerts.md` | Verify text-based clustering solution | Event Management uses Natural Language Processing (NLP) algorithms to identify common text patterns in alerts and create alert groups… |
| `Understand-Service-Maps.md` | Understand Service Maps | Service maps show active alerts for CIs and the relationships between CIs. By viewing this information, you can better understand the… |
| `access-itom-config-console.md` | Access Event Management configuration console | Access the IT Operations Management configuration console to set up Event Management and configure AIOps capabilities. |
| `add-cmdb-tables-impact-cal.md` | Add CMDB tables or classes for impact calculation | Add the CMDB tables that contain application services to be considered during impact calculation, helping ensure accurate and relevant… |
| `add-impact-cal-services.md` | Add application services for impact calculation | Specify the application services that must be considered during impact calculation to ensure accurate service impact assessment. |
| `add-property-enabling-statistics-processing.md` | Enable processing of event process statistics | Enable the system property that switches on statistics processing for events to let the platform collect and analyze metrics such as event… |
| `add-property-statistics-processing-period.md` | Configure statistics processing period | Set the time period, in seconds, for collecting event processing statistics. For example, you can set a time period twice as long as the… |
| `add-secondary-alert.md` | Add secondary alert manually to an existing alert group | Add any relevant alert discovered during the review of an automated alert group as a secondary alert to improve the group's completeness… |
| `add-suggested-relationship.md` | Add a CI relationship to CMDB Group CI Relations | Add a CMDB group CI relationship for a CI class to enable accurate alert group generation. |
| `agent-mid-connect.md` | Connect the agent to the MID Web Server using TLS | Connect the agent to the MID Web Server to enable configuring mTLS on your MID Web Server and agent. |
| `aiops-conf-console.md` | Configure Event Management using Setup Hub | The ITOM Configuration console gives administrators a single place to complete all Event Management setup steps — from installing plugins… |
| `alert-assignment-group.md` | Alert assignment groups for teams | Alert assignment groups assign alerts to the right teams promptly and automatically, improving overall incident management capabilities. |
| `alert-clustering-definitions.md` | Create an alert clustering definition | Define alert clustering conditions to trigger one or more alert clustering tags, which help create alert groups from fewer alerts. Creating… |
| `alert-clustering-predefined-definition-list.md` | List of predefined tag-based alert grouping definitions | A list of the predefined alert clustering definitions provided with the Tag Based Alert Clustering Engine  application. |
| `alert-clustering-predefined-definition.md` | Activate a predefined alert clustering definition | Activate the predefined alert clustering definitions provided with the Tag-Based Alert Clustering Engine application before use. Utilizing… |
| `alert-clustering-predefined-tag-list.md` | List of predefined alert grouping tags | A list of the predefined alert clustering tags provided with the Tag Based Alert Clustering Engine  application. |
| `alert-clustering-predefined-tag.md` | Attach a predefined tag to a tag-based alert grouping definition | Get started faster with alert clustering by attaching a predefined alert clustering tag to a tag-based alert clustering definition in Event… |
| `alert-clustering-tag-definitions-concept.md` | Tag cluster alert grouping | Tag cluster alert grouping enables you to easily create groups of alerts. It is a non-code method of alert grouping that correlates alerts… |
| `alert-clustering-tags.md` | Create alert clustering tags | Create streamlined alert correlations with alert clustering tags by grouping alerts that share identical or similar tags based on your… |
| `alert-correlation-rule-form.md` | Alert correlation rule form | Manage the fields that define how alerts are correlated and grouped. |
| `alert-execution.md` | Alert execution information | Alert execution information provides a reference to the actions that have been performed concerning the alert. Among the information… |
| `alert-filter-aggregated.md` | Apply alert group filters to aggregated groups | Reduce noise by locating only aggregated alert groups that match a configured filter. Aggregated groups are groups created for alerts with… |
| `alert-filtering.md` | Configure filters for automatic alert groups | Filter alerts and alert groups to reduce alert noise. Only alerts that match the filter are included in the group of the selected group… |
| `alert-group-use-cases.md` | Alert grouping and use cases | Alert grouping methods range from user-defined approaches, like Manual and Rule-based to advanced, fine-tunable algorithms, including… |
| `alert-grp-jobs-parameters.md` | Scheduled jobs and parameters for alert grouping | Automate alert organization by configuring jobs to group alerts based on predefined criteria and parameters. |
| `alert-insight-information.md` | Alert insight information | Alert insight aids faster alert triage, enabling a quicker way to find a solution and expose the probable root cause of the selected alert. |
| `alert-management-rule.md` | Alert management rules for resolving alerts | You can configure Event Management to respond to alerts automatically. An alert management rule determines the required alert response,… |
| `alert-priority-group.md` | Priority group | For better triage and focus, alerts that have a higher priority are brought to the top of the alert list. This placement brings to your… |
| `alert-priority.md` | Alert priority | Determine the order in which to handle alerts according to the alert priority score. Multiple factors determine the alert priority score… |
| `alert-query-form.md` | Alert Query form | You can combine similar alerts that meet specific criteria for a particular service by creating an alert query. |
| `alert-rule-execution.md` | Alert executions information | Alert executions information provides a reference to the alert management rule actions that are performed. This information appears in the… |
| `alert-similarity.md` | Alert similarity | Finding alerts that are similar to the alert that you are currently investigating can help save troubleshooting time by seeing how similar… |
| `alert-tags.md` | Alert tags | Alert tags allow consolidation for all normalized fields and improve the admin experience to transform and normalize alert fields… |
| `apache-kafka-consumer-connector.md` | Apache Kafka Consumer Connector | The Apache Kafka Consumer connector instance enables you to create events from messages collected from the Apache Kafka topic as a JSON… |
| `application-service-event-management.md` | Application services in Event Management | An application service is a set of interconnected applications and hosts which are configured to offer a service to the organization. |
| `apply-quick-response-in-alert.md` | Apply a quick response in an alert | In an alert, use the Quick Response feature to apply remediation to the alert or to launch a web application. |
| `assign-aiops-role-grp.md` | Assign group or team to Event Management operator role | Assign the evt\_mgmt\_operator role to groups to enable operations teams to work with alerts and manage Event Management workflows. |
| `assign-aiops-user-role.md` | Assign user to Event Management admin role | Assign the evt\_mgmt\_admin role to users who will be in charge of Event Management configuration and operational control. |
| `assign-operator-view-in-express-list.md` | Assign users and groups to predefined Express List views | Assign individual users and user groups to preconfigured Express List views to make sure that they focus on specific services, priorities,… |
| `assigning-alert-assignment-group-precedence.md` | Assigning alert assignment group precedence | Assign alert assignment group precedence to make sure that alerts are routed to the appropriate team members. |
| `auto-close-alerts.md` | Alert table clean up | The Scheduled Jobs feature runs a script to automatically close alerts in the Alerts [em\_alert] table that meet specific conditions,… |
| `aws-events-transform-script.md` | Integrate AWS platform as a data source | Integrate Amazon Web Services (AWS) with Event Management. To add AWS platform as a data source, configuration is required in the AWS… |
| `azure-events-authentication.md` | Integrate Azure Monitor with OAuth authentication | Integrate Microsoft Azure with Event Management by authenticating Azure V1 or V2 tokens in the Azure Monitor. |
| `azure-events-webhook.md` | Integrate Azure Monitor with basic authentication | Integrate Microsoft Azure with Event Management by adding a standard webhook in Azure Monitor. |
| `azure-integration.md` | Integrate Azure Monitor as an authenticated data source | Integrate Microsoft Azure with Event Management by adding the Azure Monitor as an authenticated data source. |
| `bind-alerts-CI-app-host-monitoring.md` | Bind alerts to CIs using CI identification | Bind alerts to specific applications on hosts using event rules to ensure accurate tracking and to improve issue resolution speed—leading… |
| `bind-ci-event-mapping.md` | Example: Bind alerts to CIs using dynamic CI types | Use event field mapping to dynamically bind alerts to the appropriate CIs based on event attributes, eliminating the need for separate… |
| `binding-alert-CI-host-default.md` | Binding alerts to a specific host CI \(default binding\) | Binding alerts to Configuration Items (CIs) using the Node field or the CI Identifier field ensures accurate event association. By… |
| `c_EM.md` | Event Management | ServiceNow Event Management is a robust application that helps keep your IT systems healthy by spotting problems quickly and fixing them.… |
| `c_EMAlert.md` | Manage and monitor alerts | An alert is a notification for selected events that are considered to be important and require attention. Event Management generates alerts… |
| `c_EMAlertRule.md` | Alert lifecycle configuration | Event Management provides various modules, templates, and properties for configuring alerts and the actions that execute for these alerts. |
| `c_EMConfiguration.md` | Event Management setup | After activating Event Management, set it up to receive and process events, and generate and analyze alerts. |
| `c_EMEvent.md` | Event Management Integrations | An event is a notification from one or more monitoring tools that indicate something of interest has occurred, such as a log message,… |
| `c_EMEventCorrelationRules.md` | Rule-based alert grouping | Rule-based alert grouping is created by alert correlation rules. These rules allow you to manually classify alerts as primary or secondary… |
| `c_EMEventFieldMapping.md` | Event field mapping configuration | Use Event field mappings rules to map values from specific fields to values in other fields. |
| `c_EMEventIdentifier.md` | Event identifiers | Event identifiers uniquely distinguish one event from another. Event Management uses these identifiers to determine whether to create a new… |
| `c_EMHowImpactTree.md` | How alerts work with CIs in maintenance | When a CI is in maintenance, the impact tree, the service map, and Alerts tab are updated based on various factors. |
| `c_EMImpactCalculation.md` | Alert impact calculation | Impact calculation shows the magnitude of an outage on CIs, services, alerts, and alert groups. The system uses factors such as impact… |
| `c_EMIntegrateRequirementEvent.md` | Event field format for event collection | Event Management requires all events to use a standard form, regardless of how they arrive at the instance. |
| `c_EMSLAsForBSAndCIs.md` | SLAs for application services and CIs | Event Management supports the creation of SLAs for application services and for CIs. |
| `c_EMSNMPtrapHA.md` | Configure SNMP Trap collection for high availability | For SNMP traps, the MID Server requires failover configuration for the trap listener. |
| `c_SACorrelatedAlertGroups.md` | Automated alert grouping | Automated alert grouping is a process that uses historical data to automatically organize similar alerts into groups. These alerts could be… |
| `c_SALearnedPattersReport.md` | Learned patterns report | The Learned Patterns report helps assess the efficiency of alert aggregation and identify recurring alert patterns. It enables proactive… |
| `c_ServiceAnalyticsOverview.md` | Alert grouping | Alert grouping is the process of organizing and consolidating related alerts into sets based on common characteristics or criteria. This… |
| `catchpoint-event-collection.md` | Integrate Catchpoint events | Integrate Catchpoint with Event Management by adding an alert webhook in the Catchpoint platform. |
| `ci-binding-alert.md` | Binding alerts to CIs | CI binding or linking is the process of finding and connecting a Configuration Item (CI) from the Configuration Management Database (CMDB)… |
| `ci-binding-process-flow.md` | Binding process flow | Learn the process of binding Configuration Items (CIs) to alerts. This includes handling event arrival, binding alerts using available… |
| `ci-device-binding.md` | Bind alerts to a specific device | Bind each alert directly to the originating device to establish a clear source of impact. This ensures accurate troubleshooting, reduces… |
| `ci-matching-ci-is-host.md` | Bind host CIs using CI field matching | When CI Field Matching is used and the CI is a host, the Node value from the alert is used for binding. The system compares the Node with… |
| `ci-matching-ci-non-host.md` | Bind non-host CIs using CI field matching | If no match is found using the Node field, the system uses the CI identifier field to match alerts with non-host CIs based on attributes… |
| `ci-matching-manual-field.md` | Bind CIs using CI field matching and handling column name differences | Bind CIs by matching event Additional information fields with CI attributes. If column names differ, manually create an additional… |
| `ci-remediation.md` | CI Remediation | Alert and configuration item (CI) remediations help troubleshoot and resolve underlying problems that generate alerts. Remediation is based… |
| `clean-alert-tables.md` | Clean alert history and impact status tables | Schedule jobs to mark and remove old alert records in the Alert History [em\_alert\_history] and Impact Status [em\_impact\_status] tables,… |
| `cmdb-alert-group-properties.md` | CMDB alert grouping — properties and functionality | Learn about the key properties and functionality of CMDB alert grouping, which facilitate efficient alert organization based on… |
| `cmdb-alert-grouping-use-cases.md` | Use cases for CMDB based alert grouping | Use cases for CMDB grouping enhance alert management by correlating alerts based on Configuration Item relationships, improving visibility,… |
| `cmdb-alert-groups.md` | CMDB based alert grouping | CMDB based alert grouping helps organizations manage alerts by organizing them according to their related configuration items (CIs) within… |
| `configuration-management-job-em.md` | Periodically run an event forwarding job | Schedule an event forwarding job to periodically send events to all target instances with active event forwarding configurations when the… |
| `configure-alert-aggregation.md` | Configure pattern based alert grouping | Configure the Alert Aggregation Learner (Service Analytics Alert Aggregation Learner - Daily), an offline job that runs daily to process… |
| `configure-alert-correlation-logic-order.md` | Configure alert correlation logic order | Improve alert management by enabling users to customize correlation logic order. This feature empowers you to fine-tune correlation methods… |
| `configure-alert-insight-properties.md` | Alert insight properties | Use these properties to configure alert insight. |
| `configure-alert-remediation-subflows.md` | Configure alert remediation actions | Run commands to perform alert remediation on remote Linux and Windows CIs. |
| `configure-azure-bi-directional-connector.md` | Configure Azure Monitor Bi-directional connector | The Azure Monitor Pull connector sends information from ServiceNow Event Management to the Azure Portal. The pull connector sends the alert… |
| `configure-cloud-observability-event-collection.md` | Configure ServiceNow Cloud Observability event collection | Integrate ServiceNow Cloud Observability with Event Management by adding a standard webhook in the ServiceNow Cloud Observability platform.… |
| `configure-contextual-colors-icons.md` | Configure contextual colors and icons | Use the Contextual colors and icons form to configure color, text, and icons to have different default or custom contexts, identified by a… |
| `configure-dynatrace-connector.md` | Configure the Dynatrace metrics connector instance | Configure the Dynatrace connector instance to receive Metric Intelligence raw data from the Dynatrace server. |
| `configure-em-context-extension.md` | Configure the MID WebService Event Collector Context | Configure the MID WebService Event Collector Context to provide a URL method to push event messages from an external source to the MID… |
| `configure-event-forwarding-em.md` | Set up event forwarding | Create an event forwarding configuration record to enable events to flow from one ServiceNow instance to another instance. Forwarding… |
| `configure-icinga-connector.md` | Configure event collection from an Icinga2 connector | Configure the Icinga 2 (Icinga) connector instance to receive events while monitoring your network resources. |
| `configure-kafka-consumer-connector.md` | Configure the Apache Kafka Consumer connector | Configure the Apache Kafka Consumer connector instance to create events from streaming messages collected by the Apache Kafka connector. |
| `configure-kafka-metrics-connector.md` | Configure the Kafka metrics connector instance | Configure the Kafka metric consumer connector instance to read message send to Kafka server over topic. |
| `configure-listener-transform-script.md` | Integrate with push connectors | Integrate with a push connector to connect to an external event source. Push connectors process the collected event messages and transform… |
| `configure-logic-monitor-connector.md` | Configure event collection from Logicmonitor | The Logicmonitor pull connector sends information from Event Management to Logicmonitor. It sends responses received from a Push connector… |
| `configure-manual-cluster.md` | Configure a manual cluster | Provide redundancy capabilities of an entire cluster in case of failure of one or more CIs in that cluster. By viewing the relative impact… |
| `configure-mid-web-server-extension-mTLS.md` | Configure mTLS authentication for a MID Web Server | Enhance security in your MID Web Server extension by enabling mTLS authentication. |
| `configure-mid-web-server-extension-metric-data.md` | Configure key-based MID Web Server authentication | Provide added security to your MID Web Server extension by using key-based authentication. Generate an authentication token to be sent in… |
| `configure-mid-web-server-extension.md` | Configure the MID Web Server extension | The MID Web Server is a MID Server extension that enables developing REST APIs to send events and metrics to the MID Server. The extension… |
| `configure-midserver-event-collection.md` | Configure a MID Server for event collection using a push operation \(listener\) | The MID Server supports the collection of event messages, using the MID Web Server to collect data from external sources and transforming… |
| `configure-midwebserver-extension-form.md` | Event Management MID Web Server extension form | Fields in the form for creating or modifying a MID Web Server extension. |
| `configure-midwebserver-extension-secure.md` | Configure a secure MID Web Server extension | Configure a TLS listener for extra security and encryption of data transferred to and from the MID Web Server extension. Access both a… |
| `configure-nagios-connector.md` | Configure event collection from NagiosXI | Configure the NagiosXI connector instance to receive events from the Nagios Core monitor. |
| `configure-nagios-metrics-connector.md` | Configure the Nagios metrics connector instance | Configure the Nagios metric connector instance to receive Metric Intelligence raw data from the Nagios server. |
| `configure-nnmi-connector.md` | Configure event collection from NNMi | Configure the HP Network Node Manager i (NNMi) connector instance to receive events while monitoring your network resources. |
| `configure-obm-connector.md` | Configure event collection from OBM | Configure the Operation Bridge Manager (OBM), also known as OMi v2, connector instance to receive alerts from the OBM server. The OBM… |
| `configure-omi-connector.md` | Configure event collection from HP OMi | Configure the HP Operations Manager (OMi) connector instance to receive alerts from the HP OMi server. |
| `configure-op5-connector.md` | Configure OP5 or OP5\_v2 connector | Configure the OP5 or OP5\_v2 Monitor connector instance to receive alerts from an OP5 Monitor source. |
| `configure-opsview-connector.md` | Configure Opsview\_v2 connector | Configure the Opsview\_V2 connector instance to receive alerts from an Opsview Monitor source. |
| `configure-prtg-connector.md` | Configure PRTG connector | Configure the PRTG connector instance to receive alerts from a Paessler PRTG Network Monitor source. |
| `configure-push-connector-instance.md` | Configure a push connector instance | Configure a push connector instance to receive the events from an external system. |
| `configure-sap-fwd-alerts-badi.md` | Configure SAP to forward alerts to your BADI | After setting up SAP Solution Manager monitoring, you must configure SAP to forward alerts to the BADI (Business Add-in) you create as the… |
| `configure-sap-solman-alert-inbox.md` | Configure the alert inbox in SAP Solution Manager | Configure SAP solution manager to retrieve alerts in the system by enabling the alert inbox with the SOA manager. |
| `configure-sap-solution-mgr.md` | Configure RFC in SAP Solution Manager | As part of enabling communication with Event Management, you must create a Remote Function Call (RFC) in the SAP Solution Manager and… |
| `configure-sapsolman-connector.md` | Configure SAP Solution Manager connector | Configure the SAP Solution Manager (Solman) connector instance to enable communication between the SAP Solution Manager and Event… |
| `configure-snmp-trap-listener.md` | Configure the SNMP traps listener to receive OEM traps | Configure the SNMP trap listener to receive traps from Oracle Enterprise Manager (OEM). |
| `configure-snmp-trapkeyfilter.md` | Configure message keys to spread SNMP object identifiers | By default, most SNMP trap events are processed by a single Event Management processing job. This can negatively effect event processing.… |
| `configure-solarwinds-connector.md` | Configure the SolarWinds metrics connector instance | Configure the SolarWinds connector instance to receive Metric Intelligence raw data from the SolarWinds server. |
| `configure-threshold-monitoring.md` | Configure a self-health monitor | You can configure a self-health monitor to track Event Management components and see that they do not exceed the specified threshold. |
| `configure-vcenter-connector.md` | Configure event collection from vCenter | Configure the VMware vCenter Server (vCenter or vCenter\_V2) connector instance to receive events from your VMware vSphere environment. |
| `configure-zabbix-metrics-connector.md` | Configure the Zabbix metrics connector instance | Configure the Zabbix Metric connector instance to receive Metric Intelligence raw data from the Zabbix server. |
| `connector-domain-metadata.md` | Connector domain metadata | Override push connector default domain metadata values installed with Event Management with the values in the event HTTP request, including… |
| `connectors-and-listeners.md` | Configure Event Management connectors | Event Management provides many connectors to pull or push events from external devices. Connectors are available from the ServiceNow store… |
| `convert-manual-to-application-service.md` | Convert manual services to application services using API | You can use a JavaScript API to convert existing manual services to application services. Event Management can use application services to… |
| `coordinating-alert-response-with-automated-alert-grouping.md` | Synchronizing alert response with automated alert grouping | Synchronize alert response with grouping by ensuring alert management jobs runs after alert grouping jobs—this prevents duplicate actions… |
| `create-alert-management-rule.md` | Create an alert management rule | Create an alert management rule to track alerts and resolve them by determining the required response, for example, to open an incident or… |
| `create-an-application-service.md` | Manually create an application service in Event Management | You can manually create an application services. Event Management can use application services to monitor service performance and identify… |
| `create-credentials-basic-auth.md` | Create basic auth server credentials | Create credentials to access a ServiceNow instance. |
| `create-credentials-nagiosix.md` | Create Nagios XI server credentials | Create credentials to access Nagios XI server. |
| `create-credentials-solarwinds.md` | Create SolarWinds monitor credentials | Create a Basic Auth credential in ServiceNow to store the SolarWinds user name and password that the SolarWinds monitor connector uses to… |
| `create-credentials-vrealize.md` | Create vRealize credentials | Create credentials to access vRealize. |
| `create-credentials-zabbix.md` | Create Zabbix server credentials | Create credentials to access Zabbix server. |
| `create-custom-create-incident-subflow.md` | Create a custom subflow for alerts | You can create a subflow according to your requirements. For example, you can resolve alerts, notify teams, or run remediation actions. |
| `create-event-rules.md` | Event rules | Use event rules to generate alerts for tracking and remediation. Event rules are stored in the Event Rule [em\_match\_rule] table.… |
| `create-incidents.md` | Create incidents | Configure automation rules to automatically create incidents from alerts that require immediate attention and resolution. |
| `create-integration-account.md` | Create integration account | Create a dedicated account with the evt\_mgmt\_integration role for third-party monitoring systems to push events to ServiceNow. |
| `create-keys-and-certificates.md` | Create keys and certificates | Create keys and certificates in your root directory to enable Transport Layer Security (TLS) setup. TLS setup is necessary before you can… |
| `create-maintenance-rule.md` | Create maintenance rules | Use maintenance rules to mark CIs in maintenance status. When in maintenance status, these CIs are excluded from impact calculation. |
| `create-or-edit-event-rule.md` | Create or edit an event rule | You can create event rules to generate alerts for tracking and remediation. Use team-based integrations in event rules to make sure that… |
| `create-push-connector-configuration-parameter.md` | Create a push connector configuration parameter | Some connectors have no parameters that are shipped out of the box. Therefore, it’s necessary to create and add the parameter to the push… |
| `create-service-group.md` | Create an application service group | Create service groups to combine similar services. Organize services by groups to perform actions simultaneously on multiple services and… |
| `create-solution-similarity.md` | Create an Event Management similarity solution | Create and train a solution that applies machine learning to a collection of words to target and suggest similar alerts in your instance… |
| `cross-business-service-impact.md` | View impact of child service on parent service | In the map view of an application service, the severity of a child service is propagated to its parent service. |
| `custom-configure-threshold-monitoring.md` | Create a self-health monitor to use custom health monitor script | You can create a self-health monitor to use custom health monitor script to monitor specified Event Management components. |
| `datadog-events-integration.md` | Integrate Datadog platform events | Integrate Datadog with Event Management by adding a standard webhook in the Datadog console. |
| `datadog-events-webhook.md` | Integrate Datadog with basic authentication | Integrate Datadog with Event Management by adding a standard webhook in the Datadog console. |
| `datadog-oauth-authentication.md` | Integrate Datadog with OAuth authentication | Integrate Datadog with Event Management by authenticating Datadog V1 or V2 tokens in the Datadog Monitor. |
| `delay-incidents.md` | Delay incidents | Configure delay rules to postpone incident creation for alerts that may resolve automatically or represent transient conditions. |
| `delete-suggested-relationship.md` | Delete a CI relationship from CMDB Group CI Relations | Delete a CMDB group CI relationship to limit available relationships for CMDB alert grouping, helping to reduce noise and improve alert… |
| `dependency-view-map.md` | View the Dependency map for CMDB alerts | The Dependency map illustrates how and why alerts are grouped, simplifying troubleshooting and issue management. It reveals connections… |
| `disable-network-traffic-grouping.md` | Disable network traffic-based alert grouping | Disable network traffic-based alert grouping to prevent alerts from being grouped solely by network activity, reducing noise during traffic… |
| `domain-self-health.md` | Monitor self-health with domain separation | Use domain separation to enable self-health to display Event Management health issues that are based on data, rules, and settings from the… |
| `domain-separation-connectors-personalization.md` | Event Management Connectors domain personalization | Create events in different domains for all Event Management connectors using just a single connector instance by personalizing domain… |
| `domain-separation-event-management.md` | Domain separation and Event Management | Domain separation is supported in Event Management. Domain separation enables you to separate data, processes, and administrative tasks… |
| `dynatrace-connector-instance-form.md` | Dynatrace connector instance form | The Dynatrace connector instance form displays the fields you must fill in when creating a Dynatrace connector instance. |
| `dynatrace-connector-instance-value-parameters.md` | Dynatrace connector instance value parameters | The following table displays the Dynatrace connector instance value parameters that you can fill in, as needed, when creating a Dynatrace… |
| `dynatrace-events-integration.md` | Integrate Dynatrace platform events | Integrate Dynatrace with Event Management by adding Dynatrace as an authenticated data source. |
| `dynatrace-events-webhook.md` | Integrate Dynatrace with basic authentication | Integrate Dynatrace with Event Management by adding a standard webhook in the Dynatrace console. |
| `dynatrace-oauth-authentication.md` | Integrate Dynatrace with OAuth authentication | Integrate Dynatrace with Event Management by authenticating Dynatrace V1 or V2 tokens in the Dynatrace Monitor. |
| `edit-widget.md` | Performance Analytics Edit Widget dialog box | Fields in the dialog box for editing a Performance Analytics dashboard widget. |
| `eif-events-integration.md` | Integrate Event Integration \(EIF\) format event connector | Use the push connector that allows events to be forwarded from products, generally from IBM, that support the Event Integration (EIF)… |
| `eif-events-severity.md` | EIF events warning severity | If the EIF event payload has a warning severity, it will be mapped differently in the ServiceNow instance. |
| `em-architecture.md` | Event Management architecture | Event Management architecture integrates data collection, processing, and alerting into a unified system for streamlined IT issue detection… |
| `em-collaborate-from-alert.md` | Collaborate from within an alert | You can collaborate with colleagues and write work notes while working in an alert. |
| `em-process-flow.md` | Event Management process flow | Event Management collects, analyzes, and converts events into alerts, enabling efficient tracking and remediation. |
| `enable-alert-grouping.md` | Configure scheduled job-based alert grouping | Set up rules and parameters to group related alerts automatically, streamlining alert management and reducing alert noise. |
| `enable-network-traffic-grouping.md` | Enable network traffic-based alert grouping | Activate network traffic-based alert grouping to automatically correlate and reduce alert noise by grouping related events based on network… |
| `enable-tls-agent.md` | Connect the agent to the MID Server using mTLS | Before configuring mTLS authentication on the agent, you must run a series of commands that enable configuring Transport Layer Security… |
| `enrich-alerts.md` | Alert enrichment automations | Configure alert enrichment rules to automatically add context and metadata to incoming alerts for better analysis and response. |
| `event-collection-BMCTrueSight.md` | Event collection from BMC TrueSight and BMC TrueSight\_v2 | The MID WebService Event Collector enables you to collect JSON formatted event messages sent from BMC TrueSight Operations Management… |
| `event-collection-GCP.md` | Event collection from Google Cloud Platform \(GCP\) | The MID WebService Event Collector enables you to collect JSON formatted event messages sent from Google Cloud Platform (GCP). |
| `event-collection-MicrosoftAzure.md` | Event collection from Microsoft Azure Monitor | The MID WebServer Event Collector enables you to collect JSON formatted event messages sent from the Microsoft Azure portal. |
| `event-collection-custom-payloads.md` | Event collection from custom payloads | The MID WebService Event Collector enables you to collect event information from custom payloads in JSON, XML, or plain text format. |
| `event-collection-logicmonitor.md` | Event collection from Logicmonitor | The MID WebService Event Collector enables you to collect JSON formatted event messages from the Logicmonitor. |
| `event-collection-thousandeyes-oauth.md` | Integrate ThousandEyes with OAuth authentication | Create credentials in the instance and configure the ThousandEyes webhook. |
| `event-collection-via-MID-using-push.md` | Pushing events to the MID Server using web service API | Configure the MID WebService Event Collector to provide a URL method to push event messages to the MID Server. |
| `event-content-pack.md` | Event Management Platform Analytics Solutions | Platform Analytics Solutions contain preconfigured dashboards. These dashboards contain actionable data visualizations that help you… |
| `event-forwarding-em.md` | Event forwarding | Accelerate the event processing testing life cycle by forwarding a stream of events from your ServiceNow production environment to your… |
| `event-forwarding-properties-em.md` | Event forwarding properties | Several system properties enable you to customize an event forwarding job. |
| `event-input-information.md` | Use event input information | The Event Input pane that is included in the steps to create an event rule provides a reference to the information that you can use when… |
| `event-management-reference.md` | Event Management reference | Reference topics provide additional information about mapping and fine-tuning application services using Event Management lists and forms. |
| `event-table-rotation.md` | Modify event table rotation | Table rotation is used by Event Management, by default, to contain the growth of event [em\_event] tables within the rotation table group. |
| `exclude-learned-patterns.md` | Exclude patterns from learned patterns | Exclude CI-based or CI class-based alerts and patterns when you encounter alerts incorrectly added to a learned pattern by the Learned… |
| `exploring-event-management.md` | Exploring Event Management | Explore Event Management to understand its overview, process flow, user roles, and benefits for comprehensive IT issue monitoring and… |
| `find-similar-alerts.md` | Find similar alerts | You can find alerts similar to the alert currently being investigated. Save troubleshooting time by reviewing similar alerts to see how… |
| `followup-worknotes-review-service-candidate.md` | Follow up on work notes and review service candidate | Track and follow up on work notes while reviewing the service candidate to ensure all actions and updates are captured. This helps maintain… |
| `gcp-events-integration.md` | Integrate Google Cloud Platform \(GCP\) events | Integrate Google Cloud Platform (GCP) with Event Management by adding a standard webhook in the GCP console. |
| `grafana-events-integration.md` | Integrate Grafana events with basic authentication | Integrate Grafana with Event Management by adding a standard webhook in the Grafana console. |
| `grafana-events-oauth-authentication.md` | Integrate Grafana with OAuth authentication | Integrate Grafana with Event Management with ServiceNow using OAuth authentication. |
| `grafana-integration.md` | Integrate Grafana events | Integrate Grafana with Event Management by adding Grafana as an authenticated data source. |
| `group-alerts.md` | Alert group automations | Configure grouping rules to automatically consolidate related alerts into single actionable items for more efficient incident management. |
| `honeycomb-event-integration.md` | Integrate Honeycomb events | Integrate Honeycomb with Event Management by creating a webhook and configuring it as a trigger in the Honeycomb platform. |
| `ignore-alerts.md` | Alert ignore automations | Configure ignore rules to automatically suppress alerts that are not actionable or relevant to your operations team. |
| `improve-event-mgmt-performance.md` | Enhance Event Management performance | The Event Management Accelerator plugin ensures that Event Management maintains performance at a high level. This plugin is optional. |
| `install-aiops-setup-hub.md` | Install AIOps using Setup Hub | Use Setup Hub's guided installation experience to activate the required AIOps plugins and configure your environment — reducing setup time… |
| `install-discovery.md` | Install Discovery | Configure Discovery to lay the groundwork for AIOps success by establishing a key foundation for your team. |
| `install-event-management.md` | Install Event Management | Retrieve the most updated apps for the Event Management application (com.glideapp.itom.snac) in the ServiceNow Store. Periodically check… |
| `install-integration.md` | Install integrations | Access Integrations Launchpad to configure and install integrations for Event Management monitoring tools. |
| `installed-domain-properties.md` | Domain properties installed with Event Management | Use the domain properties installed with Event Management to provide the metadata that points to the appropriate table to identify the… |
| `instana-events-integration.md` | Integrate Instana events | Integrate Instana with Event Management by adding a standard webhook in the Instana console. |
| `instana-integration.md` | Integrate Instana events | Integrate Instana with Event Management by adding Instana as an authenticated data source. |
| `instana-oauth-authentication.md` | Integrate Instana with OAuth authentication | Integrate Instana with Event Management with ServiceNow using OAuth authentication. |
| `integrate-aws-api-key.md` | Integrate AWS with REST API key token | Integrate using an API key to establish secure communication and automate data exchange via REST API. This simplifies integration, enabling… |
| `integrate-azure-api-key.md` | Integrate Azure with REST API key token | Integrate using an API key to establish secure communication and automate data exchange via REST API. This simplifies integration, enabling… |
| `integrate-grafana-api-key.md` | Integrate Grafana with REST API key token | Integrate using an API key to establish secure communication and automate data exchange via REST API. This simplifies integration, enabling… |
| `integrate-newrelic-api-key.md` | Integrate New Relic with REST API key token | Integrate using an API key to establish secure communication and automate data exchange via REST API. This simplifies integration, enabling… |
| `integrate-scout-apm-events.md` | Integrate Scout APM events | Enable the collection of events from Scout APM by authenticating Scout APM as a data source to integrate it with Event Management. |
| `integrate-sumologic-api-key.md` | Integrate Sumo Logic with REST API key token | Integrate using an API key to establish secure communication and automate data exchange via REST API. This simplifies integration, enabling… |
| `integrate-thousandeyes-api-key.md` | Integrate ThousandEyes with REST API key token | Integrate using an API key to establish secure communication and automate data exchange via REST API. This simplifies integration, enabling… |
| `integrate-with-panopta.md` | Integrate Panopta as a data source | Integrate the Panopta cloud-based monitoring solution with Event Management. To add Panopta as a data source, configuration is required in… |
| `learn-deploy-to-production.md` | Learn how to deploy Event Management to production | Understand the process and considerations for deploying Event Management configurations from development to production environments using… |
| `learn-the-basics.md` | Learn the basics | ServiceNow Event Management and AIOps help IT operations teams manage high alert volumes by reducing noise and turning raw events into… |
| `license-usage.md` | View Event Management license usage | Event Management is licensed based on the number of CIs bound to alerts during the last year. For alerts that are not bound to CIs, the… |
| `lightstep-event-collection.md` | Integrate ServiceNow Cloud Observability Events | Integrate ServiceNow Cloud Observability with Event Management by adding a standard webhook in the ServiceNow Cloud Observability platform.… |
| `log-analytics-alert-grouping.md` | Related log entities alert grouping | The Related log entities (formerly known as Health Log Analytics alert grouping automatically gathers HLA alerts that originate from the… |
| `logicmonitor-events-integration.md` | Integrate Logicmonitor events | Integrate Logicmonitor with Event Management to send events into ServiceNow by adding a webhook using Basic Authentication, it will also be… |
| `manage-views-express-list-admin.md` | Create a predefined Express List view for users | Configure an Express List view for users to make sure that they focus on specific services, priorities, or alerts. You can set the filters,… |
| `manage-views-express-list.md` | Configuring Express List views for users and user groups | Centrally control what users monitor by predefining views in Express List and assigning them to users and user groups. |
| `manual-alert-grouping.md` | Manual alert grouping | Manual alert grouping involves organizing and categorizing alerts based on user-defined criteria and direct intervention. |
| `manual-cluster-in-a-manual-service.md` | Configuring CIs in a manual service as a manual cluster | Configure or modify a CI as a specific CI or a generic CI class in a manual service (that was not discovered automatically) as a manually… |
| `map-kafka-message-payload-attributes-to-alert-fields.md` | Map Kafka message payload attributes to alert fields | Map Kafka message attributes to alert fields to make alerts based on the messages more meaningful. Use event field mapping to map Kafka… |
| `metric-collection-otel.md` | Metric collection from OpenTelemetry \(Otel\) metrics | The MID WebService metric Collector enables you to collect JSON and protobuf formatted metrics sent from OpenTelemetry (Otel). |
| `mid-web-server-api-key-authentication.md` | Configure MID Web Server API key authentication | Authenticate incoming requests from clients to the MID Web Server extension using API key authentication. API authentication is a secure… |
| `mid-web-server-mTLS-authentication.md` | MID Web Server and agent mTLS Authentication | Mutual authentication using the Transport Layer Security protocol (mTLS) is a secure, certificate-based authentication scheme. With mTLS,… |
| `mid-web-server.md` | MID Web Server | The MID Web Server is part of the common infrastructure of the MID Server. |
| `migrate-manual-2-application-service.md` | Convert manual services to application services | You can convert existing manual services to application services. Event Management can use application services to monitor service… |
| `migrate-transform-scripts.md` | Use legacy listener transform scripts | Use legacy listener transform scripts when upgrading a ServiceNow AI Platform instance from Paris or earlier. These scripts can be run as… |
| `ml-solutions-em.md` | Machine learning solutions for Event Management | Build solutions for Event Management with Predictive Intelligence. |
| `modify-a-manual-cluster.md` | Modify a manual cluster | Modify an existing manual cluster by changing the service, the specific CI, the generic CI class, or the description in case of an… |
| `monitor-event-processing-metrics.md` | View event processing statistics | Extract statistics from your instance to ensure that performance is not affected and extract metrics related to event processes to monitor… |
| `monitor-services.md` | View monitored services | View all services that Event Management supports, such as, alert groups, discovered services, application services, and technical services.… |
| `nagios-connector-instance-form.md` | Nagios connector instance form | The Nagios connector instance form displays the fields you must fill in when creating a Nagios connector instance. |
| `nagios-connector-instance-value-parameters.md` | Nagios connector instance value parameters | The following table displays the Nagios connector instance value parameters that you can fill in, as needed, when creating a Nagios… |
| `network-traffic-correlation-grouping.md` | Network traffic based alert grouping | The Network traffic based alert grouping method groups alerts by analyzing network traffic connections between processes across hosts. It… |
| `new-relic-events-integration.md` | Integrate New Relic platform events | Integrate New Relic with Event Management by adding a standard webhook in the New Relic old and new consoles. |
| `operator-adjust-impact-rules.md` | Adjust alert impact while triaging an alert | As an Event Management operator, you might need to modify the impact that an alert has on an application service and on the CIs in a… |
| `operator-advanced-tasks.md` | Advanced tasks for the Event Management operator | As an Event Management operator, you might need to perform additional tasks that are outside of your typical workflow, or tasks that you… |
| `operator-alerts-CIs-in-maintenance.md` | Handle alerts while CIs are in maintenance | When an alert occurs on a CI that is in the maintenance state, the alert state is also changed to maintenance. You should find and monitor… |
| `operator-application-services.md` | Application services for Event Management operators | As an Event Management operator, you need to understand what application services are. |
| `operator-associate-kb.md` | Associate a knowledge base article with an alert | As an Event Management operator, you can associate a knowledge base (KB) article with the alert to capture additional information about the… |
| `operator-close-alert.md` | Operator phase 3: Close an alert | After you take action on an alert, you can verify several items on the alert and then close it. |
| `operator-create-dashbaord-view.md` | Customize your alert list view | You can create one or more customized alert list views that show only the information pertinent to you. For example, you might want to… |
| `operator-events-alerts.md` | An overview of alerts for Event Management operators | As an Event Management operator, you need to understand how an alert is generated from an event, what to look for in an alert, and how… |
| `operator-guide-em.md` | Event Management Operator Tutorial | As an Event Management operator, your role is to find alerts, analyze them, and take action to help resolve the underlying issue. |
| `operator-handle-alerts-flapping.md` | Work with flapping alerts | If an alert is in the flapping state, you might need to triage the alert again. |
| `operator-launch-web-app.md` | Launch a web application from an alert | As an Event Management operator, you can also launch a web application from an alert. The web application might be a console for the event… |
| `operator-phase-acknowledge-analyze.md` | Operator phase 1: Analyze and acknowledge an alert | As an Event Management operator, the first thing you should do is access alerts and then find the ones you want to focus on. You can open… |
| `operator-phase-triage-incident.md` | Operator phase 2: Triage an alert | After you analyze and acknowledge an alert, you must triage it. The triage phase involves verifying alert correlation and taking an action… |
| `operator-process.md` | What Event Management operators do | As an Event Management operator, your typical workflow involves three phases: analyzing an alert and its effect on application services,… |
| `operator-put-alert-into-maintenance.md` | Put an alert into maintenance | As an Event Management operator, you can put an alert into maintenance if the alert does not require any further action, but you still want… |
| `operator-run-remdiation.md` | Run a remediation workflow on an alert | As an Event Management operator, you can also run a workflow on your ServiceNow instance that helps remediate the alert. For example, you… |
| `operator-user-interfaces.md` | Event Management operator environment | As an Event Management operator, your primary work environment is the Service Operations Workspace dashboard. |
| `oracle-cloud-events-integration.md` | Integrate Oracle Cloud Infrastructure alarms | Integrate Oracle Cloud Infrastructure (OCI) alarms with Event Management to send events into ServiceNow by adding a https subscription… |
| `otto-aiops-dashboards.md` | Dashboards | Access Event Management dashboards to monitor system performance, alert trends, and operational metrics for your IT operations. |
| `overriding-default-binding.md` | Overriding default binding | Overriding default binding allows flexibility in linking alerts to CIs beyond the default Node-based matching. This helps customize alert… |
| `pattern-identifiers-grouping.md` | Understanding pattern identifiers | A pattern identifier is a set of criteria or attributes (such as alert type, affected system, etc.) used to group similar alerts. It helps… |
| `perf-analytics-widget-customize.md` | Customize Platform Analytics elements | Customize the appearance of widgets when viewing Platform Analytics visualizations. |
| `personalize-domain-separation-pull-connectors.md` | Personalize domains for pull connector events to use in event creation | Configure pull connectors to personalize domain separation of events so you can use them to create events in domains other than the user's… |
| `personalize-domain-separation-push-connectors.md` | Personalize domains for push connector events to use in event creation | Configure push connectors to personalize domain separation of events so you can use them to create events in different domains other than… |
| `platform-upgrade-and-event-management.md` | Event Management during a platform upgrade | During a platform upgrade Event Management jobs whose Upgrade safe flag is marked as true remain running. |
| `populate-custom-alert-fields.md` | Custom alert fields | You can populate custom alert fields with data contained in Additional information field of the event. |
| `probable-rca.md` | Probable Root Cause Analysis \(RCA\) | Shorten the mean time to repair (MTTR) by discovering the root cause of an alert. |
| `processing-events.md` | Processing Events | Event processing is the process of taking events or streams of events, analyzing them and taking automatic action. The process includes… |
| `prometheus-events-integration.md` | Integrate Prometheus events | Integrate Prometheus with Event Management by adding a standard webhook in Prometheus's Alert Manager. |
| `ptrn-attributes-alrt-aggregate.md` | Specify and manage pattern identifier attributes for alert grouping | The Alert Aggregation Learner analyzes alerts and identifies patterns using a defined set of alert and configuration item (CI) attributes.… |
| `push-connector-instance-form.md` | Push connector instance form | Push Connector Instance form displays the fields that you must fill when you create or modify a connector. |
| `push-event-listener.md` | Configure a push connector | You can configure listeners and connectors to push event information to the instance or MID Server. |
| `r_EMBestPractice.md` | Event Management configuration preferences | Preferred settings of properties and general configuration. |
| `r_InstalledWithEventManagement.md` | Components installed with Event Management | Activating the Event Management (com.glideapp.itom.snac) plugin adds several roles, scheduled jobs, and tables.Roles used by the Event… |
| `refresh-event-rule.md` | Refresh event rules | Manually update event rules to reflect current event information because once an event rule is created, the Event Additional info and Event… |
| `remove-aiops-user-role-discovery.md` | Remove user from Discovery admin role | Remove user from the discovery\_admin role when you no longer need them. |
| `remove-aiops-user-role.md` | Remove user from Event Management admin role | Remove user from the evt\_mgmt\_admin role when you no longer need them. |
| `remove-alert-from-group.md` | Remove an alert from an alert group | Remove an alert if you want to improve the group's accuracy and usefulness in troubleshooting an incident. If this action leaves the group… |
| `remove-cmdb-tables-impact-cal.md` | Remove CMDB tables or classes from impact calculation | Exclude unnecessary CMDB tables or classes from impact calculation to improve performance and focus on relevant data. |
| `remove-impact-cal-services.md` | Remove application services from impact calculation | Exclude specific application services from impact calculation to reduce noise and focus on critical components. |
| `restore-excluded-patterns.md` | Restore excluded patterns | Restoring excluded patterns to the learned patterns report lets you reintegrate valuable insights lost due to incorrect alerts. This… |
| `review-alerts.md` | Review alerts | Access the Express List interface to review and manage alerts in your Event Management system. |
| `rotate-tables-purge-data.md` | Rotate event and alert table for cleanup | The growth of data tables impedes performance. Preserve instance performance by event table rotation and alert table cleanup for status and… |
| `run-multiple-alert-group-scheduled-jobs.md` | Run multiple scheduled jobs for alert grouping | Run multiple scheduled jobs in parallel to group alerts. This helps prevent overwhelming the system during surges (alert storms). |
| `sap-manager-connector.md` | SAP configurations enabling the SAP Solution Manager connector | Configure your SAP environment to work with the ServiceNow Event Management platform so you can use the SAP Solution Manager connector. |
| `sap-pull-connector.md` | Use the SAP Solution Manager Pull connector | The SAP Solution Manager Pull connector sends information from Event Management to the SAP Solution Manager. The Pull connector sends… |
| `sap-push-connector.md` | Use the SAP Solution Manager Push connector | The MID Server web service Event Collector enables you to collect alerts sent from the SAP Solution Manager through event stream… |
| `sap-sol-certificate-view-update.md` | View and update your SAP Solution Manager certificate | View your SAP Solution Manager certificate, and update the certificate if necessary. |
| `sap-solman-configurations.md` | SAP Solution Manager setup configurations | As part of the SAP Solution Manager setup, you must perform several configurations to enable SAP Solution Manager to interact with Event… |
| `sap-view-alerts.md` | View alerts in the SAP Solution Manager inbox | You can view alerts generated in SAP Solution Manager to see any pressing issues. All alerts also forward to Event Management automatically. |
| `sapsolman-transaction-codes.md` | SAP Solution Manager transaction codes | The transaction code abbreviations that you can use in the SAP interface when working with the SAP Solution Manager connector. |
| `sapsolman-view-interface-debugging-table.md` | View the SAP interface log | View the SAP interface log to help you debug issues. |
| `scom-connector-instance-form.md` | SCOM connector instance form | The SCOM connector instance form displays the fields you must fill in when creating a SCOM connector instance. |
| `scom-event-rules.md` | SCOM metric event rules | The base system comes with Microsoft System Center Operations Manager (SCOM) metric event rules. SCOM metric event rules bind event metrics… |
| `self-monitoring.md` | Self-health monitors for Event Management | Use the Event Management self-health monitors to track Event Management features and resolve issues. |
| `send-events-via-web-service.md` | Pushing events to the instance using web service API | You can use a web service interface, supported by ServiceNow, that operates on the JSON object as the data input and output format. |
| `sentry-events-collection.md` | Integrate Sentry events | Integrate Sentry with Event Management by adding a standard webhook in the Sentry platform. |
| `set-mid-web-server.md` | Install the .pem file in the MID unified keystore and set up the MID Web Server | Install the .pem file into the MID unified keystore and set up the MID Web Server to enable configuring mTLS on your MID Web Server and… |
| `set-rca-change-query-filters.md` | Customize RCA settings | Modify default settings that determine RCA behavior. |
| `shared-impacted-services-grouping.md` | Shared impacted services alert grouping | The Shared impacted services alert grouping automatically gathers related alerts under the business service they affect. When your IT… |
| `simulate-event-processing.md` | Simulate event processing | You can simulate event processing logic on events and display the resulting alert to better understand which rules are executed on a given… |
| `solarwinds-connector-instance-form.md` | Solarwinds connector instance form | The Solarwinds connector instance form displays the fields you must fill in when creating a Solarwinds connector instance. |
| `solarwinds-connector-instance-value-parameters.md` | Solarwinds connector instance value parameters | The following table displays the Solarwinds connector instance value parameters that you can fill in, as needed, when creating a Solarwinds… |
| `solution-version-activated.md` | Activate Event Management solution version | The system activates the most recent version of the solution, but you can activate any previously trained Event Management solution version… |
| `start-self-health.md` | Start or stop self-health monitoring | You can control the starting or stopping of the self-health monitor feature by configuring the self-health monitoring property. The first… |
| `subflows-provided.md` | Event Management subflows in the base system | The subflows provided with the base system appear in the Remediation Subflows area of alert management rules. |
| `sumologic-events-integration.md` | Integrate Sumo Logic events | Use the Sumo Logic push connector to integrate Sumo Logic with Event Management by adding a standard webhook in the Sumo Logic platform. |
| `t_EMActivatePlugin.md` | Request Event Management | AIOps Experience plugin (sn\_sow\_aiops) requires a separate subscription and must be activated by ServiceNow personnel. This plugin… |
| `t_EMAssignRoleSCOMGroup.md` | Limit collected SCOM alerts to specific SCOM groups | Limit the collection of SCOM alerts to only those alerts that belong to the specified SCOM group. |
| `t_EMAssignRoleSvcGroup.md` | Assign a role to a service group | Assign an Event Management role to the application service group to ensure that group members can manage and act on alerts. |
| `t_EMBindApplication.md` | Bind alerts to a specific process | Bind specific server processes to their corresponding Configuration Items (CIs) in the CMDB to ensure accurate mapping and visibility. This… |
| `t_EMBindServiceCI.md` | Example: Binding alerts to non-host CIs | Bind alerts to an application service (a non-host CI) using event rules and event field mapping. This example demonstrates how to achieve… |
| `t_EMCloseAlert.md` | Close an alert | Close an alert by an event or a user action. Closing an alert also closes any related incident that is not already resolved or closed. |
| `t_EMComposeOuput.md` | Configure an event rule to customize alert content | You can configure an event rule to customize alert content. You can customize the order of the fields and select which fields display. The… |
| `t_EMConfigAlertStateFlapDetect.md` | Configure alert flapping | Set flapping properties to determine when an alert enters and exits the flapping state. Flapping can indicate configuration problems (that… |
| `t_EMConfigInfraRelation.md` | Create an infrastructure relationship for related CIs | Infrastructure relationships show CIs that are connected to a application service but are not necessary parts of the service.… |
| `t_EMConfigureAnEventCorrelationRule.md` | Create an alert correlation rule | Create an alert correlation rule to designate primary and secondary alerts. The primary alert is identified as the root cause of the alert… |
| `t_EMConfigureConnectorInstance.md` | Configure a pull connector | Configure a pull connector to schedule the frequency of event collection. |
| `t_EMConfigureDomainSeparation.md` | Configure Event Management domain separation | You can configure Event Management for domain separation to create logically defined domains that limit unauthorized access to data. When… |
| `t_EMConfigureEmailConnector.md` | Configure event collection from email | Configure an inbound email action to send email notifications when events and alerts are triggered. |
| `t_EMConfigureHPOMConnector.md` | Configure event collection from HPOM | Configure the HPOM connector instance to receive events from HP Operations Manager (HPOM). |
| `t_EMConfigureHypericConnectorJS.md` | Configure event collection from Hyperic | Configure the Hyperic connector instance to receive events from the VMware vRealize Hyperic server. |
| `t_EMConfigureImpactRule.md` | Adjust impact rules for a CI | Configure impact rules to customize the impact calculation for discovery services and manual services. The impact rules update the overall… |
| `t_EMConfigurePurge.md` | Purge impact status and alert history | Automatically cleans up outdated impact statuses and alert history from the database to free up space, improve system performance, and… |
| `t_EMConfigureSCOMConnector.md` | Configure the SCOM connector instance | Configure the Microsoft System Center Operations Manager (SCOM) connector instance to receive alerts and Metric Intelligence raw data from… |
| `t_EMConfigureSCOMConnectorInstance.md` | Configure alert collection from SCOM | Alerts from the Microsoft System Center Operations Manager (SCOM) are collected using the SCOM connector instance. |
| `t_EMConfigureSolarwindsConnectorJS.md` | Configure event collection from SolarWinds monitor | Configure the SolarWinds monitor connector instance to receive events from the SolarWinds monitor. |
| `t_EMConfigureZabbixConnector.md` | Configure event collection from Zabbix server | Configure the Zabbix server connector instance to receiving alerts from the Zabbix server. |
| `t_EMConfigurevRealizeConnectorJS.md` | Configure event collection from vRealize | Configure the VMware vRealize Operations (vRealize or vRealize\_V2) connector instance to receive events from the vRealize Operations Log… |
| `t_EMCreateAlertGroup.md` | Create an alert query | An alert query is a set of alerts that meet specific criteria for a particular service. |
| `t_EMCreateAlertRule.md` | Migrate an alert action rule to an alert management rule | Existing alert action rules from an earlier release can be executed, but cannot be modified. Alert action rules that have been migrated… |
| `t_EMCreateAnSLAConfiguration.md` | Create an SLA configuration for CIs | Create an SLA configuration from the Event Management application to determine which CIs are available for SLAs. |
| `t_EMCreateCustomConnectorDefinition.md` | Create a custom pull connector | You can create a customized pull connector that requires a script, connector definition, and connector instance, to retrieve events on… |
| `t_EMCreateEmailNotificationBusinessService.md` | Configure email notification on application service severity change | Configure an email notification to notify users when there is an application service severity change. |
| `t_EMCreateEventFieldMapping2.md` | Create event field mappings | Use event field mappings to map values from specific event fields to values in other fields to provide more comprehensive information in an… |
| `t_EMCreateEventManually.md` | Testing and sending events | You can manually test and send events to confirm that Event Management properly manages events and generates alerts. |
| `t_EMCreateFilter.md` | Filter the events that an event rule applies to | Define a filter to restrict to which events the event rule must apply. Configure the filter by providing a set of conditions that each… |
| `t_EMCreateIncidentfromAlert.md` | Create incident or security incident from an alert | When an alert must be escalated and assigned to someone who can resolve the underlying issue, you can open an incident. |
| `t_EMCreateSLADefForCI_BS.md` | Create an SLA definition for a CI or application service | You can create SLA definitions for CIs and application services just as you can for other task records in the instance. |
| `t_EMFindEventNoRule.md` | Find events that are not matched to rules | Find events that are not matched to any rules, and determine if it is necessary to create event rules to manage them. |
| `t_EMGetBaselineServiceMapping.md` | Activate and configure Service Mapping for top-down discovery | A top-down discovery provides a list of CIs and their interrelationships. This information is useful for managing software services and… |
| `t_EMISetThresholdEvent.md` | Set a threshold to suppress alert generation | The event threshold is the rate upon which Event Management generates an alert. Receiving multiple events for a device over a short… |
| `t_EMLaunchAnApplication.md` | Launch web application from alert | You can launch a web application from an alert that matches the conditions set in an alert action rule. |
| `t_EMLimitTheRecordsForSLAConfigFilter.md` | Limit the records for the SLA configuration filter | If too many records are returned by the SLA configuration filter, you can add a property to set the maximum number of records. |
| `t_EMManageEvent.md` | View events | Event Management tracks individual events to manage external systems. These events are notifications from monitoring tools indicating… |
| `t_EMMonitorManualService.md` | Monitor alerts for an application services | To view information for application services only, navigate to the application services list. From this list, you can open service maps to… |
| `t_EMPutAnAlertIntoMaintenance.md` | Place an alert into maintenance | You can manually place any alert into maintenance to hide it from the Alerts list and Agent Workspace. |
| `t_EMReopenAlert.md` | Reopen an alert | Additional events can cause reopening of alerts, or you can reopen an alert by changing its state. When an alert reopens, any associated… |
| `t_EMResolveCloseIncidentAlert.md` | Resolve an incident related to an alert | When you resolve an incident that is associated with an alert, the alert can also close according to the evt\_mgmt.incident\_closes\_alert… |
| `t_EMSNMPTrapEvent.md` | Configure event collection for SNMP traps | The SNMP listener runs on the MID Server, which acts as a collection endpoint for SNMP traps. The MID Server sends the traps to the… |
| `t_EMSetDefaultConnector.md` | Configure a default MID Server for connectors | You can set a default MID Server for connectors to ensure that there is always a MID Server available to receive external events. |
| `t_EMSetTheAlertActiveInterval.md` | Configure the alert active interval | The active interval property (evt\_mgmt.active\_interval) determines how Event Management handles a new event that is similar to events… |
| `t_EMUpgradeNetcoolConnector.md` | Configure event collection from IBM Netcool | Configure the IBM Netcool\_V2 connector to receive events from IBM Netcool/OMNIbus Object Servers and Impact Servers. The IBM Netcool\_V2… |
| `t_EMUseOverviewDashboard.md` | Use the Event Management overview dashboard | The Event Management overview module uses Performance Analytics to present data from your instance for you to better visualize and… |
| `t_EMViewAlert.md` | View alert information | View a list of all alerts for application services s, and then manage individual alerts as necessary. |
| `t_EMViewAlertFlapping.md` | View alerts in the flapping state | You can view alerts that are specifically in the flapping state. |
| `t_EMViewAlertHistory.md` | View discovered service history | The discovered service history shows the frequency of discovered services for a particular time period. |
| `t_EMViewAlertmaintenance.md` | View all alerts by the maintenance status | The Maintenance status indicates that the CI is under maintenance. For example, there is a software upgrade, and the issues can result from… |
| `t_EMViewDashboard.md` | Monitor service health | On the Operator Workspace, you can view alerts by application services, technical service, and alert group. For services, you can also open… |
| `t_EMViewEventGroup.md` | View patterns for event group creation | Event groups are sets of events that do not have a matching event rule. You can view the patterns in a group of events to learn the impact… |
| `t_EMViewEventRule.md` | View event rules | You can view all event rules on the Event Rules list. |
| `t_EMViewImpactTree.md` | View the impact tree | The impact tree shows the relationships between CIs and the relative percentage impact for each child CI. This information is available for… |
| `t_EMViewRuleApply.md` | Find rules that will be applied to an event | View the rules that will be applied on an event to determine how this event will be processed. |
| `t_EMViewTopology.md` | View an alert impact on CIs in a service map | You can view service maps to see active alerts for CIs and the relationship between CIs. By viewing this information, you can better… |
| `t_SAAddAlertCorrelatedAlertGrp.md` | Create alert group manually | Manually create an alert group to organize and manage related alerts when not using scheduled jobs. This provides flexibility to group… |
| `t_SACreateCIRemediation.md` | Create or edit CI remediation | Create a CI remediation rule that lets users manually apply an Orchestration workflow for resolving issues with specific CIs associated… |
| `t_SAViewRemediationTasks.md` | View remediation tasks | Event Management automatically creates a remediation task to capture every remediation that was applied to a CI or to an alert. It gives… |
| `tag-based-alert-clustering-definition-form.md` | Event Management tag based alert grouping definition form | The form for creating or modifying a tag based alert clustering definition displays detailed information about the definition. |
| `tag-based-alert-clustering-tag-form.md` | Event Management tag based alert clustering tag form | The form for creating or modifying a tag based alert clustering tag displays detailed information about the tag. |
| `team-based-integrations-properties.md` | Team-based integration properties | Team-based integration system properties enable you to customize the assignment group functionality for existing and new customers for… |
| `team-based-integrations.md` | Team-based integrations in Event Management | Team-based integrations empower teams to optimize event processing within Event Management to enhance efficiency and operational… |
| `text-based-alert-groups.md` | Text-based alert grouping | In text-based alert grouping, alerts are organized and correlated based on specific text patterns or keywords within the alert content.… |
| `thousandeyes-events-integration.md` | Integrate ThousandEyes platform events | Integrate ThousandEyes with Event Management by adding a standard webhook in the ThousandEyes console. |
| `thousandeyes-events-webhook.md` | Integrate ThousandEyes with basic authentication | Integrate ThousandEyes with Event Management by adding a webhook in the ThousandEyes platform. |
| `training-ops-team.md` | Training operations team | Get your L1/L2 operators up to speed with ServiceNow Event Management. This section walks through the key concepts, tools, and workflows… |
| `unified-grouping.md` | Mixed alert grouping | Mixed alert grouping combines multiple strategies—currently CMDB-based, tag-based, related log entities-based, and shared impacted… |
| `user-guide.md` | Using Event Management | As an Event Management operator, your role is to find alerts, analyze them, and take action to help resolve the underlying issue. |
| `using-event-management.md` | Configuring Event Management | Event Management administrators administer events, manage and monitor alerts, aggregate alerts, and work review and monitor services'… |
| `view-alert-execution-information.md` | View alert execution information | You can click any link in the Alert Executions list to view the alert execution information of the referenced item. This information… |
| `view-alert-group-reasoning.md` | Configure work notes to capture alert grouping justifications | As alerts are added to a group, a message is recorded in the alert’s Work notes field to explain why the alert was included in the group.… |
| `view-self-health-manual-service.md` | View the Event Management self-health application services map | You can view Event Management application services maps to have a visualization of the data on configuration items (CIs) that comprise this… |
| `view-similarity-examples.md` | Review Event Management similarity examples | Review the similarity examples and scores that the system provides during solution training to see how the selected alert record compares… |
| `view-solution-training-progress.md` | View Event Management solution training progress | View solution training progress or statistics to determine whether a solution is available or how long the next training cycle might take… |
| `word-collection-similarity-solution.md` | Similarity solutions | Similarity solutions enable you to use Machine Learning (ML) to compare the text in a resolved alert record to an open alert record to… |
| `zabbix-connector-instance-form.md` | Zabbix connector instance form | The Zabbix connector instance form displays the fields you must fill in when creating a Zabbix connector instance. |
| `zabbix-connector-instance-value-parameters.md` | Zabbix connector instance value parameters | The following table displays the Zabbix connector instance value parameters that you can fill in, as needed, when creating a Zabbix… |
