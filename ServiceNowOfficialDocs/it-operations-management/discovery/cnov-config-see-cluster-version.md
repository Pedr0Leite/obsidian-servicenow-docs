---
title: Display the Kubernetes cluster version in the CMDB
description: Make the Kubernetes Visibility Agent Informer populate the relevant field in the cmdb\_ci\_kubernetes\_cluster CI to display the Kubernetes cluster version.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/it-operations-management/discovery/cnov-config-see-cluster-version.html
release: australia
product: Discovery
classification: discovery
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
keywords: [Agent Client Collector, Kubernetes, Visibility, cluster version, Cloud Native Operations for Visibility, CNO for Visibility]
breadcrumb: [Install Kubernetes Visibility Agent \(KVA\) Informer, Configuring Kubernetes Visibility Agent, Kubernetes discovery using Kubernetes Visibility Agent, Discovery for containerized resources, Discovery, ITOM Visibility, IT Operations Management]
tags:
  - it-operations-management
  - discovery
  - cmdb
  - patterns
  - ci
  - type-task
---

# Display the Kubernetes cluster version in the CMDB

Make the [[acc-kubernetes-visibility-landing-page|Kubernetes Visibility Agent]] Informer populate the relevant field in the cmdb\_ci\_kubernetes\_cluster CI to display the Kubernetes cluster version.

## Before you begin

Use ServiceNow [[r-discovery|Discovery]] and [[c_ServiceMappingOverview|Service Mapping]] Patterns application version 1.11.0 or higher.

Role required: none

## Procedure

1.  Do one of the following:

    -   When using a Helm chart, in the Helm install command, set the **getClusterVersion** parameter to true:

        `--set getClusterVersion=true`

    -   When using the k8s\_informer.yaml file, set the environment variable GET\_CLUSTER\_VERSION to true.

**Parent Topic:**[Install Kubernetes Visibility Agent \(KVA\) Informer](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-operations-management/discovery/cnov-deploy-install.md)

## Related

- [[acc-kubernetes-visibility-landing-page|Kubernetes Visibility Agent]]
- [[r-discovery|Discovery]]
- [[c_ServiceMappingOverview|Service Mapping]]
