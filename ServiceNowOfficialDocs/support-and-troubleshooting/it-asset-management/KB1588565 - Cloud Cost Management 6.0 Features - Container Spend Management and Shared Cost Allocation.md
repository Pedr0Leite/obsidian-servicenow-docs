---
title: "Cloud Cost Management 6.0 Features - Container Spend Management and Shared Cost Allocation"
aliases:
  - KB1588565
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1588565
kb_number: KB1588565
last_modified: 2025-12-12
---

## Cloud Cost Management 6.0 Features - Container Spend Management and Shared Cost Allocation

  

**Container spend management**

**Description**

Cloud-based Kubernetes services from AWS, GCP, and Azure have become increasingly utilized by companies deploying workloads on cloud infrastructure. This mirrors the broader trend of rising adoption of Kubernetes container orchestration technology.​

With this rise in adoption, there is also a rise in spend for these services. However reporting and allocation of this spend has been challenging because of the nature of this service :​

-   Containers are shared resources and its hard to find out which application consumed how much of the underlying resources to be able to allocate it fairly.​
-   Providers show the spend at the abstract level (kubernetes cluster) whereas for accurate allocation, customers need breakdown at more granular levels like namespaces or cost of each underlying asset that is part of the Kubernetes cluster.

Hence, this feature leverages the data and relationships discovered by ServiceNow discovery to provider deeper breakdown of the Kubernetes spend. 

**Log Location and Debug Properties**

-   Validate in the **Cloud Cost Management Workspace** Job execution(sn\_clin\_core\_insights\_execution) to verify if the **Spend** job executions is completed successfully.
-   Verify the **Execution Log** (sn\_cld\_intg\_core\_execution\_log) ,**Flow engine context** (sys\_flow\_context) and **Flow engine log entry**(sys\_flow\_log) tables for any errors related to spend flow execution.
-   Verify the errors in system logs (syslog.list) table with the **Source** prefix labelled as sn\_cld\_intg, sn\_clin and sn\_cld\_spend to see all the unknown/technical errors around the job execution time.

**Symptoms and Facts**

The spend for a Kubernetes cluster will be generated only if cost allocation tags are enabled for a Kubernetes cluster in their respective consoles for AWS and GCP providers. For AWS provider, cost allocation tags need to be enabled at the account level and for GCP, it is at the Kubernetes Engine. For the Azure provider, the Kubernetes spend will be generated only if the default node resource group is provisioned during AKS deployment and has this naming convention _MC\_{name of the cluster resource group}\_{name of the cluster}\_{location of the cluster}._

**Troubleshooting Path/Diagram**

![](/sys_attachment.do?sys_id=5b58481d9335b61c057c7de86cba1091)

-   Billing data download tiggers.​
-   Billing data download fetches Kubernetes cluster line items and maps each asset or resource of the cluster to Kubernetes cluster based on the tags for AWS and GCP providers. 
-   CI placement triggers as part of billing download for CI type Kubernetes cluster cmdb\_ci\_Kubernetes\_cluster​.
-   After the billing download completes successfully, Spend execution will trigger.​ 
-   Tag Category 40 column should be populated with the name of the cluster for each asset or resource in the cluster and to the cluster resources in the 'sn\_cld\_spend\_core\_monthly\_aggregated\_cost' table for all 3 providers.

Note : Here assets/resources refer to Network/VM/Load Balancer.. Etc

**Technical details**

**AWS Provider:**

-    Enable below mentioned cost allocation tags at account level  for a Kubernetes cluster in AWS Management Console before you run a AWS Billing download job to view the Kubernetes spend.

               Static tag keys containing cluster name : aws:eks:cluster-name, user:eks:cluster-name, eks:cluster-name 

               Dynamic tag keys of the following format :

                   kubernetes.io/cluster/<Cluster-Name> : shared/owned   
                   alpha.eksctl.io/cluster-name : <Cluster-Name> 

-   Tag "sn\_ccm\_k8\_cluster\_name" will be added to the resources already having tags specified above during aws billing download.

**GCP Provider:**

-   Enable cost allocation tag "goog-k8s-cluster-name" for each Kubernetes cluster before you run a Google Cloud Billing download job to view the Kubernetes spend.
-   Tag "sn\_ccm\_k8\_cluster\_name" will be added to the resources already having tags "goog-k8s-cluster-name" during GCP billing download.

**Azure Provider:**

-   Tag "sn\_ccm\_k8\_cluster\_name" will be added to the Kubernetes cluster during billing download based on meter category "Azure Kubernetes Service". Tag value will be the name of the cluster. 
-   Tag "sn\_ccm\_k8\_cluster\_name" will be added to the assets/resources of cluster present in the infrastructure/managed resource group after ‘Spend Report monthly Aggregated Cost’ table population as part of post spend execution. 
-   The default name for this infrastructure resource group is MC\_<resourcegroupname>\_<clustername>\_<location>. 

**Script includes:**

<table class="MsoNormalTable" style="width: 450.5pt; border-collapse: collapse;" border="1" cellspacing="0" cellpadding="0"><tbody><tr style="height: 133.95pt;"><td style="width: 120.1pt; border: solid windowtext 1.0pt; padding: 0cm 0cm 0cm 0cm;" valign="top"><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.0pt;">Mid Server Script includes&nbsp;</span></strong><strong><span style="font-size: 8.0pt;">&nbsp;<span style="color: #283d40;">&nbsp;</span></span></strong></p></td><td style="width: 330.4pt; border: solid windowtext 1.0pt; border-left: none; padding: 0cm 0cm 0cm 0cm;" valign="top"><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.0pt;">AWSCSVRecordProcessor</span></strong><span style="font-size: 8.0pt;">: This is the script containing the logic to add cost allocation tags and the 'sn_ccm_k8_cluster_name' tag to the assets/resources of the Kubernetes cluster and 'sn_ccm_k8_cluster_name' to the Kubernetes cluster for AWS provider.</span></p><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.0pt;">AzureAsynCostUsageNodeDataConstructor</span></strong><span style="font-size: 8.0pt;">: This is the script containing the logic to add 'sn_ccm_k8_cluster_name' to the Kubernetes cluster for Azure provider.</span></p><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.0pt;">&nbsp;</span></p><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.0pt;">GCPBillingNodeDataConstructor</span></strong><span style="font-size: 8.0pt;">: This is the script containing the logic to add cost allocation tag 'goog-k8s-cluster-name'&nbsp;and the 'sn_ccm_k8_cluster_name' tag to the assets/resources of the Kubernetes cluster and 'sn_ccm_k8_cluster_name' to the Kubernetes cluster for GCP provider</span></p></td></tr><tr style="height: 169.15pt;"><td style="width: 120.1pt; border: solid windowtext 1.0pt; border-top: none; padding: 0cm 0cm 0cm 0cm;" valign="top"><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.0pt;">Script Includes&nbsp;</span></strong><strong><span style="font-size: 8.0pt;">&nbsp;</span></strong></p></td><td style="width: 330.4pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0cm 0cm 0cm 0cm;" valign="top"><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.0pt;">AWSCIHandlerForKubernetesClusterIREObject</span></strong><span style="font-size: 8.0pt;">:&nbsp;</span><span style="font-size: 8.0pt;">This is the script containing the logic for AWS Kubernetes cluster CI Placement</span></p><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.0pt;">AzureCIHandlerForKubernetesClusterIREObject</span></strong><span style="font-size: 8.0pt;">&nbsp;:&nbsp;</span><span style="font-size: 8.0pt;">This is the script containing the logic for Azure Kubernetes cluster CI placement.</span></p><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.0pt;">GCPCIHandlerForKubernetesClusterIREObject</span></strong><span style="font-size: 8.0pt;">:&nbsp;</span><span style="font-size: 8.0pt;">This is the script containing the logic for GCP Kubernetes cluster CI placement.</span></p><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><u><span style="font-size: 8.0pt;">AggregatedMonthlySpendUtil</span></u></strong><u><span style="font-size: 8.0pt;">:&nbsp;</span></u><span style="font-size: 8.0pt;">This is the script containing the logic to add&nbsp;</span><span style="font-size: 8.0pt;">'</span><span style="font-size: 8.0pt;">sn_ccm_k8_cluster_name</span><span style="font-size: 8.0pt;">'</span><span style="font-size: 8.0pt;">&nbsp;</span><span style="font-size: 8.0pt;">tag to the assets/resources of cluster present in the infrastructure/managed resource group after ‘Spend Report monthly Aggregated Cost’ table population as part of post spend execution.&nbsp;</span></p></td></tr><tr style="height: 58.5pt;"><td style="width: 120.1pt; border: solid windowtext 1.0pt; border-top: none; padding: 0cm 0cm 0cm 0cm;" valign="top"><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.0pt; font-family: 'Segoe UI', sans-serif;">Data Broker Server Script</span></strong></p><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.0pt; font-family: 'Segoe UI', sans-serif;">Table:sys_ux_data_broker_transform</span></p></td><td style="width: 330.4pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0cm 0cm 0cm 0cm;" valign="top"><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.0pt;">Cluster Cost Transformer</span></strong><span style="font-size: 8.0pt;">: Transformer for Cloud Insights Workspace to get the service category costs for a cluster.</span></p><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><strong><span style="font-size: 8.0pt;">Spend dashboard transformer</span></strong><span style="font-size: 8.0pt;">: Transformer for Cloud Insights Workspace to get Kubernetes cluster cost in <strong>Kubernetes Spend Analytics</strong> dashboard</span></p></td></tr><tr style="height: 60.4pt;"><td style="width: 120.1pt; border: solid windowtext 1.0pt; border-top: none; padding: 0cm 0cm 0cm 0cm;" valign="top"><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.0pt;">Tables&nbsp;</span><span style="font-size: 8.0pt;">&nbsp;</span></p></td><td style="width: 330.4pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0cm 0cm 0cm 0cm;" valign="top"><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.0pt;">sn_cld_spend_core_monthly_cost</span></p><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.0pt;">sn_cld_spend_core_monthly_aggregated_cost</span></p><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.0pt;">sn_cld_intg_core_tag_category</span></p><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.0pt;">sn_cld_intg_core_tag_name_value</span></p></td></tr><tr style="height: 33.75pt;"><td style="width: 120.1pt; border: solid windowtext 1.0pt; border-top: none; padding: 0cm 0cm 0cm 0cm;" valign="top"><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.0pt;">Flow&nbsp;</span><span style="font-size: 8.0pt;">&nbsp;</span></p></td><td style="width: 330.4pt; border-top: none; border-left: none; border-bottom: solid windowtext 1.0pt; border-right: solid windowtext 1.0pt; padding: 0cm 0cm 0cm 0cm;" valign="top"><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.0pt;">AWS: Generate AWS Spend Report</span></p><p style="margin: 0cm; font-size: 12pt; font-family: Calibri, sans-serif;"><span style="font-size: 8.0pt;">Azure and GCP:</span> <span style="font-size: 8.0pt;">Spend Orchestrator</span></p></td></tr></tbody></table>

**Troubleshooting**

-   CI Placement: CI placement happens as part of the billing download. All related logs are available as part of the insight pipeline execution stage logs.​To look for the CI placement information or error search with the class name for Kubernetes cluster cmdb\_ci\_Kubernetes\_cluster.

![](/sys_attachment.do?sys_id=df58481d9335b61c057c7de86cba1098)

-   Once the billing download is complete, verify that tag 'sn\_ccm\_k8\_cluster' is added to each asset or resource of the cluster and to the cluster resources in the AWS (sn\_cld\_intg\_aws\_cost\_usage) and GCP (sn\_cld\_intg\_gcp\_cost\_usage) node tables.

-   Once the spend execution is complete, verify that the Tag Category 40 column should be populated with the name of the cluster for each asset or resource in the cluster and to the cluster resources in the 'sn\_cld\_spend\_core\_monthly\_aggregated\_cost' table for all 3 providers.

-   Verify that out of the box tag category is created for Kubernetes cluster with the name ‘Kubernetes cluster name’ and tag name‘sn\_ccm\_k8\_cluster’ mapped with Tag category 40.
-   Verify the errors in system logs (syslog.list) table related to identification engine while doing CI placement for cmdb\_ci\_kubernetes\_cluster.

**Shared cost allocation feature overview**

**Description:**

  In any organization, cloud resources are shared across multiple business units, departments, cost centers or projects.  It is therefore necessary to do the following:​

-   Identify shared cloud resources using tags​
-   Download billing details for these shared cloud resources​
-   Define policies that specify how the costs associated with these cloud resources are shared across Business units, Divisions, Departments or Cost Centers.​
-   Apply these policies on the billing details downloaded​
-   Generate reports that provide the breakup of direct and shared costs across all cloud resources​
-   For Kubernetes containers, the costs can be shared across multiple namespaces.​

**Shared Cost Policies for Kubernetes Namespaces:**

Prerequisite: To get all the namespaces of a Kubernetes cluster, we need to run Auto K8s Discovery using patterns. We query the namespace column from the cmdb\_ci\_kubernetes\_cluster table while displaying namespace values during the creation of Shared Cost Policies for Kubernetes clusters.

Please find the reference link below for Kubernetes Discovery using Patterns: [https://www.servicenow.com/docs/bundle/zurich-it-operations-management/page/product/service-mapping/concept/kubernetes-discovery.html](https://www.servicenow.com/docs/bundle/zurich-it-operations-management/page/product/service-mapping/concept/kubernetes-discovery.html)

Below are the steps to be followed for creating the Kubernetes Shared Cost policies:

1.  Navigate to Cloud Cost Management Workspace → Operations → Shared Cost Allocation Policies
2.  Click New/Edit button
3.  Select Service Category: Kubernetes Service
4.  Set Resource Type: Kubernetes Cluster
5.  Enter the Kubernetes cluster name in the Kubernetes Cluster field
6.  Fill in all mandatory fields
7.  Reapply policies or run billing download to populate the spend grouped by namespaces for the newly created Shared Cost policy

Shared Cost policies should be created to view spend grouped by Kubernetes namespaces in the spend analytics page. Out of the box (OOB), the system automatically creates Shared Cost policies with the Even allocation type for each Kubernetes cluster that has namespaces. These are created after the billing execution completes or when Shared Cost policies are reapplied. Customers can create their own custom shared cost allocation policies for Kubernetes clusters with the highest priority order.

**Log Location and Debug Properties**

-   Verify the errors in system logs (syslog.list) table with the **Source** prefix labelled as sn\_cld\_intg, sn\_clin and sn\_cld\_spend to see all the unknown/technical errors around the job execution time.

**Troubleshooting Path/Diagram**

 **![](/sys_attachment.do?sys_id=8758481d9335b61c057c7de86cba1063)**

-   Validate active shared cost policy is present 
-   Validate policy matching records is present in monthly aggregated spend table with active state.

**Technical details**

<table style="width: 0px;" border="1"><tbody><tr style="height: 101px;"><td style="width: 566px;" colspan="1" rowspan="1"><div><div><p><a href="https://citestinstance17.service-now.com/sys_script_include.do?sys_id=39e060a443953110e9f117091fb8f26a&amp;sysparm_record_target=sys_script_include&amp;sysparm_record_row=1&amp;sysparm_record_rows=12&amp;sysparm_record_list=nameCONTAINSSharedCost%5EORDERBYname" target="_blank" rel="noopener noreferrer">SharedCostController</a>​</p></div></div></td><td style="width: 566px;" colspan="1" rowspan="1"><div><div><p>&nbsp;This is the main script which will be called once user will click on re-apply policy.​</p></div><div><p>This will clear all existing record present in shared cost table and re-run policy&nbsp;execution.​</p></div><div><p>​</p></div></div></td></tr><tr style="height: 83px;"><td style="width: 566px;" colspan="1" rowspan="1"><div><div><p><a href="https://citestinstance17.service-now.com/sys_script_include.do?sys_id=738a986043953110e9f117091fb8f2e1&amp;sysparm_record_target=sys_script_include&amp;sysparm_record_row=7&amp;sysparm_record_rows=12&amp;sysparm_record_list=nameCONTAINSSharedCost%5EORDERBYname" target="_blank" rel="noopener noreferrer">SharedCostPolicyExecution</a>​</p></div></div></td><td style="width: 566px;" colspan="1" rowspan="1"><div><div><p>This script contains the policy execution part it will figure out all the unique policy&nbsp;depending upon run order and other cost distribution parameters. This will also find&nbsp;out cost for source and target costs.​</p></div></div></td></tr><tr style="height: 66px;"><td style="width: 566px;" colspan="1" rowspan="1"><div><div><p><a href="https://citestinstance17.service-now.com/sys_script_include.do?sys_id=9c4f5c2443953110e9f117091fb8f2cb&amp;sysparm_record_target=sys_script_include&amp;sysparm_record_row=11&amp;sysparm_record_rows=12&amp;sysparm_record_list=nameCONTAINSSharedCost%5EORDERBYname" target="_blank" rel="noopener noreferrer">SharedCostSplitProcessor</a>​</p></div></div></td><td style="width: 566px;" colspan="1" rowspan="1"><div><div><p>This script include will split the cost depending upon allocation type and spilt the&nbsp;cost and create records in shared cost policy.​</p></div></div></td></tr><tr style="height: 101px;"><td style="width: 566px;" colspan="1" rowspan="1"><div><div><p><a href="https://citestinstance17.service-now.com/sys_script_include.do?sys_id=cff0adc64369f110e9f117091fb8f29d&amp;sysparm_record_target=sys_script_include&amp;sysparm_record_row=2&amp;sysparm_record_rows=3&amp;sysparm_record_list=nameCONTAINSSharedCostK8%5EORDERBYname" target="_blank" rel="noopener noreferrer">SharedCostk8sPolicyHandler</a>​</p></div></div></td><td style="width: 566px;" colspan="1" rowspan="1"><div><div><p>This script include will check all the records present in spend table having tag 40&nbsp;populated and service category is Kubernetes Service.​</p></div><div><p>It will generate Auto generated policy for namespace only.​</p></div></div></td></tr><tr style="height: 66px;"><td style="width: 566px;" colspan="1" rowspan="1"><div><div><p>&nbsp;SharedCostk8sPolicyExecution​</p></div></div></td><td style="width: 566px;" colspan="1" rowspan="1"><div><div><p>&nbsp;This script will handle all the&nbsp;kubernetes&nbsp;policies execution it will list all&nbsp;policy depending upon run order.​</p></div></div></td></tr><tr style="height: 83px;"><td style="width: 566px;" colspan="1" rowspan="1"><div><div><p><a href="https://citestinstance17.service-now.com/sys_script_include.do?sys_id=9c4f5c2443953110e9f117091fb8f2cb&amp;sysparm_record_target=sys_script_include&amp;sysparm_record_row=11&amp;sysparm_record_rows=12&amp;sysparm_record_list=nameCONTAINSSharedCost%5EORDERBYname" target="_blank" rel="noopener noreferrer">SharedCostK8SplitProcessor</a>​</p></div></div></td><td style="width: 566px;" colspan="1" rowspan="1"><p>This script include will split the cost&nbsp;depending upon allocation type&nbsp;and spilt&nbsp;the cost and create records in shared cost&nbsp;policy for&nbsp;kubernetes&nbsp;cluster.</p></td></tr></tbody></table>

**Tables:**

1. sn\_cld\_spend\_core\_sc\_policy​  
2. sn\_cld\_spend\_core\_sc\_policy\_target​  
3. sn\_cld\_spend\_core\_monthly\_shared\_cost

**Known Errors and Workarounds:** 

Exception while executing request: Transaction cancelled: maximum execution time exceeded​  
​  
To resolve this error follow the below steps:​  
  ​  
 1. Go to Transaction Quota Rules ​  
​  
 2. Search for 'REST Batch API request timeout'​  
​  
 3. Increase the timeout to 300 seconds.

Kubernetes Spend for “Group by Kubernetes namespace”:

We reserved TagCategory40 to store the Kubernetes cluster name for reporting spend by Kubernetes clustername and Kubernetes namespace. OOB, all Kubernetes cluster resources are tagged with sn\_ccm\_k8\_cluster\_name.However, the current issue is that this tag is added only when the Kubernetes resource already has at least one tag key-value pair. If a resource has no existing tags, the sn\_ccm\_k8\_cluster\_name tag is not populated, causing spend to not appear in the Spend Analytics dashboard for Group By Kubernetes clustername or Kubernetes namespace.

A fix will be available in the upcoming release. Customer currently affected can contact the support to get a fix via update sets.
