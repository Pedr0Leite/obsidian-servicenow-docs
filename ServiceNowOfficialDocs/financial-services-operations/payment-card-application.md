---
title: Payment card
description: The Payment card application stores details of payment cards, which can be used across the entire card life-cycle, from issuance to servicing.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/financial-services-operations/payment-card-application.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Data Models, Explore, Financial Services Operations \(FSO\)]
---

# Payment card

The Payment card application stores details of payment cards, which can be used across the entire card life-cycle, from issuance to servicing.

## Overview of Payment card

The Payment card application is a data model that represents payment cards that are issued to users. It supports multiple payment card types, including credit and debit cards.

It also supports storing tokenized values for sensitive data, such as the primary account number \(PAN\).

Cards in Payment card can be associated with a Financial Account in [[financial-services-operations-core-data-model|Financial Services Operations Core]]. This relationship can then be used in a [[fso-overview|Financial Services]] Operations \(FSO\) workflow that involves a card account, such as selecting a credit or debit card containing a disputed card transaction.

\[Omitted image "payment-card-data-model.png"\] Alt text: A data model diagram showing the tables contained in Payment card, and their relationships to tables in Customer Service Install Base Management and Financial Services Operations Core.

## Accessing Payment card

Payment card is included with Financial Services Operations Core.

-   **[[payment-card-application-tables|Payment card tables]]**  
This section describes the tables in the Payment card application and shows how they store and manage physical payment card information.
-   **[[payment-card-application-roles|Payment card roles]]**  
This section outlines the core roles involved in managing payment cards in the Payment card application.

**Parent Topic:**[[data-models|Data Models]]

## Related

- [[payment-card-application-tables|Payment card tables]]
- [[payment-card-application-roles|Payment card roles]]
- [[data-models|Data Models]]
- [[financial-services-operations-core-data-model|Financial Services Operations Core]]
- [[fso-overview|Financial Services]]
