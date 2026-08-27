---
title: "Scan QR Code Page is not loading in Clinician Portal for Vaccine Administration Management"
aliases:
  - KB0955955
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0955955
kb_number: KB0955955
last_modified: 2024-02-10
---

## Scan QR Code Page is not loading in Clinician Portal for Vaccine Administration Management

  

### Issue

When using the **Clinician Portal** as a part of **Vaccine Administration Management (VAM)** you are finding that the **Scan QR Code** Page is not loading as expected.

  

#### Steps To Reproduce:

1.  Using an **instance** with **Vaccine Administration Management** installed
2.  Navigate to **Vaccine Administration Management > Clinician Portal**
3.  Click **Scan a code**
4.  See that the Page is **blank**

  

### Cause

This is happening because the **QR Code Scanner Portal Widget** is missing from your instance.

It is **missing** because you **already** have a **\[sp\_widget\]** **Record** with **ID = "qr\_code\_scanner"** in your instance **before** you installed **VAM.**

  

Since the **ID Field** on **\[sp\_widget\]** must be **unique** then the **System** is **preventing** the **VAM Version** of the **Widget** from being inserted and therefore it cannot be displayed as expected in your **Clinician Portal**.

### Resolution

1.  Go to **\[sp\_widget\]** **Table List** 
2.  Query for **ID = "qr\_code\_scanner"**
3.  Change the **ID** field to a **different** **name** which **is not** **"qr\_code\_scanner"**
4.  Import the **VAM** **QR Code Scanner Widget** (See **sp\_widget\_b077f4c873c62010ff25e1d28bf6a707.xml** attachment).
