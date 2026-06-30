---
title: Configure Task Intelligence for Customer Service
description: Install the Task Intelligence for Customer Service application and configure the different features: record categorization, language detection, Sentiment Analysis, and Document Intelligence for Customer Service.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/customer-service-management/configure-task-intelligence.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Task Intelligence for Customer Service, Machine learning solutions, Implement Intelligence, Configure, Customer Service Management]
---

# Configure Task Intelligence for Customer Service

Install the Task Intelligence for Customer Service application and configure the different features: [[case-categorization-overview|record categorization]], [[case-language-detection|language detection]], [[case-sentiment-analysis|Sentiment Analysis]], and [[csm-document-intelligence|Document Intelligence for Customer Service]].

## Install and configure Task Intelligence features

Complete the following tasks to install Task Intelligence for Customer Service and configure the features.

|Task|Description|
|----|-----------|
|[[install-task-intelligence-cs-app|Install the Task Intelligence for Customer Service application]]|You can install the Task Intelligence for Customer Service application \(com.snc.csm\_ml\_task\) if you have the admin role.|
|[[case-categorization-configure|Configure record categorization]]|Activate the required plugins and import training data. Then you can create and train a model to predict field values.|
|[[case-sentiment-analysis-configure|Configure Sentiment Analysis]]|Activate the required plugins, enable the sentiment analysis property, and [[configure-data-model-roles|assign roles]]. Then you can train a model to predict case sentiment.|
|[[case-language-detection-configure|Configure language detection]]|Activate the required plugins and the ServiceNow translator to use the language detection feature. Then you can set up a model to detect the case language.|
|[[csm-doc-intel-configuring-|Configure Document Intelligence for Customer Service]]|Enable Document Intelligence for Customer Service and create use cases to extract data.|

## Set up and deploy Task Intelligence models

Once you have completed the configuration tasks, you can use the [[csm-task-intel-admin-center|Task Intelligence Admin Console]] to set up and deploy models for record categorization, sentiment analysis, and language detection. You can also use the Task Intelligence Admin Console to access the Document [[intelligence-csm|Intelligence]] Admin interface, which you can use to create document processing use cases.

<table id="table_ang_qtp_fvb"><thead><tr><th>

Task

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[[csm-task-intel-create-cat-solution|Create a model to predict record fields]]

</td><td>

Create and train a model to predict fields for cases and interactions.

</td></tr><tr><td>

[[csm-task-intel-create-sentiment-solution|Create a model to predict case sentiment]]

</td><td>

Edit and test the pre-trained sentiment model to predict sentiment for customer service cases.

</td></tr><tr><td>

[[csm-task-intel-create-language-solution|Create a model to detect case language]]

</td><td>

Edit and test the pre-trained model to detect the language used to create customer service cases.

</td></tr><tr><td>

[[csm-task-intel-create-di-use-case|Create a Document Intelligence use case]]

</td><td>

Create a use case to identify the information to extract from email and case attachments.

</td></tr><tr><td>

[[create-a-model-to-predict-similar-cases|Create a model to predict similar cases]]

</td><td>

Test and edit the pre-trained similar cases model for predicting similarity in customer service cases and create a new model for custom cases.

</td></tr><tr><td>

[[edit-a-case-prediction-model|Edit a model]]

</td><td>

Edit the case models that have already been trained and deployed. Change the model configurations, view the updated training results, and redeploy the model.

</td></tr><tr><td>

[[export-a-task-intelligence-model|Export a model]]

</td><td>

Export a Task Intelligence model to another instance.

</td></tr><tr><td>

[[create-a-custom-similar-case-model|Create a custom similar case model]]

</td><td>

Set up a training model to help it recognize similarities between two types of tables by comparing their fields.

 The model looks at the prediction fields of a prediction table and the training fields of a training table. It uses the similarities in these fields to predict similar records.

</td></tr></tbody>
</table>**Related topics**  


[[csm-task-intelligence|Task Intelligence for Customer Service]]

[[use-task-intelligence|Use Task Intelligence for Customer Service]]

## Related

- [[install-task-intelligence-cs-app|Install the Task Intelligence for Customer Service application]]
- [[case-categorization-configure|Configure record categorization]]
- [[case-sentiment-analysis-configure|Configure Sentiment Analysis]]
- [[case-language-detection-configure|Configure language detection]]
- [[csm-doc-intel-configuring-|Configure Document Intelligence for Customer Service]]
- [[csm-task-intel-create-cat-solution|Create a model to predict record fields]]
- [[csm-task-intel-create-sentiment-solution|Create a model to predict case sentiment]]
- [[csm-task-intel-create-language-solution|Create a model to detect case language]]
- [[csm-task-intel-create-di-use-case|Create a Document Intelligence use case]]
- [[create-a-model-to-predict-similar-cases|Create a model to predict similar cases]]
- [[edit-a-case-prediction-model|Edit a model]]
- [[export-a-task-intelligence-model|Export a model]]
- [[create-a-custom-similar-case-model|Create a custom similar case model]]
- [[csm-task-intelligence|Task Intelligence for Customer Service]]
- [[use-task-intelligence|Use Task Intelligence for Customer Service]]
- [[case-categorization-overview|Record categorization]]
- [[case-language-detection|Language detection]]
- [[case-sentiment-analysis|Sentiment Analysis]]
- [[csm-document-intelligence|Document Intelligence for Customer Service]]
- [[configure-data-model-roles|Assign roles]]
- [[csm-task-intel-admin-center|Task Intelligence Admin Console]]
- [[intelligence-csm|Intelligence]]
