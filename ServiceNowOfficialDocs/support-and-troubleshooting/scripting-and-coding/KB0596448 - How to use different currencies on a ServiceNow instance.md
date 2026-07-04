---
title: "How to use different currencies on a ServiceNow instance"
aliases:
  - KB0596448
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0596448
kb_number: KB0596448
last_modified: 2026-04-06
---

## How to use different currencies on a ServiceNow instance

  

### Issue

Users may get confused by the results of filtering, sorting, and displaying currency fields when the system works with at least two currencies for each value. The system has a session currency determined by the user's locale setting, and a reference currency determined by the system locale for each currency value. If multiple currencies are allowed on the instance, then users might be dealing with additional currency values.

Note that aggregations and filtering use the reference currency, and that the user sees the session currency. Because of changing conversion rates, the filtered reference currency values might not result in the same order as the session currency values would suggest. The same sort of issue happens with aggregations.  
  

## Symptoms

Lists filtered on currency fields might not be in the expected order because the reference currency values are used for filtering but session currency values are displayed.

Aggregation of currency fields might not produce the expected results because reference currency values are aggregated and then converted to the session currency.

Currency values might not be formatted as expected because currency values are formatted based on the user's locale and not on the currency code.

### Cause

The confusion is caused by the difference between session and reference currencies, changing conversion rates, and different session currencies used by different users, for example in reports.

### Resolution

## About currency processing

* * *

A currency field holds a value, a currency code, and a reference currency value. The currency code is a three-letter ISO currency code and identifies the currency in which the value is specified. The reference currency value is a number representing the currency value in the reference currency. The reference currency value is calculated by a rate conversion when the currency value is saved.

Price fields are a type of currency field that have special features for conversion and display. For example, the Service Catalog uses price fields.

Currency fields are used to represent the following items:

-   The price of something, for example, the price of a phone
-   A transaction, for example, money spent on a contract
-   A value on which arithmetic operations can be performed, for example, the hourly rate of a service multiplied by the number of hours

## Locales

There are two settings for locale: the system locale and the user locale.

## System locale

The system locale is set using the **_glide.system.locale_** property. The value is of the format _Language.Country_ where the language is an ISO 639 language code and the country is an ISO 3166 language code. Internally, this value used as specified by Java. The system locale setting should be in the [Java supported locales](http://www.oracle.com/technetwork/java/javase/javase7locales-334809.html "Java supported locales") list.

The system locale should be set once on a fresh zboot because reference currency values in currency fields are assumed to be in the currency implied by the system locale.

**Warning**: Do not change the system locale after currency values have been entered into the instance. When you change the system locale, the reference currency values are not adjusted, that is, there is no rate conversion. This persistence results in invalid aggregations and filtering.

## User locale

The user locale is determined by the following, in order of consideration

1.  Test local set using _**glide.system.locale.test**_ (for SN Technical Support use)
2.  User record in which both country and language are specified
3.  System locale set using the property _**glide.system.locale**_
4.  Browser locale

## Currencies and single currency mode

* * *

The system uses two kinds of currency, session and reference.<?p>

The _session_ currency is defined for the user by the user's locale or single currency mode. The _reference_ currency is determined by the system locale. The reference currency is a standard used across the entire instance. Each time a value is entered in a currency or price field, the system stores three pieces of information:

-   The value as entered, in the user's locale
-   The currency code, in the user's locale
-   The value converted to the reference currency using the current exchange rate

**Note**: In multiple-currency mode, the currency code saved in currency field might not be the same as the session currency code. For example, the session currency could be the Euro and the number entered could be in Japanese Yen.

## Session currency

When users view a currency value, they can see the value as entered or in the session-currency format. The format contains:

-   The currency symbol
-   The value converted to the session currency and shown in a localized number format.

The user's locale determines the session currency format.

The number format can differ in features such as the decimal separator based on the locale; for example, the US formatting is 1,234,567.89 while German formatting is 1.234.567,89.

The session currency is determined by the following, in order of consideration

1.  Single currency mode set up using _**glide.i18n.single\_currency**_ and _**glide.i18n.single\_currency.code**_
2.  Default currency for the user's locale

## Reference currency

In order to perform calculations on heterogeneous currency values, the platform stores currency values converted to a system currency, referred to as the _reference_ currency. Every currency field in the system contains a reference currency value.

The reference currency is determined by the following, in order of consideration

1.  System locale set using the _**property glide.system.locale**_
2.  Java default locale, typically en.US

The reference currency is typically US dollars.

The filtering and aggregation features use the reference currency value to perform calculations. This can yield inaccurate results because of conversion rate changes.

## Single currency mode

The purpose of single currency mode is to enable all users of the platform to see currency values in the same currency. For this mode to be set up properly, the following properties have to be set:

-   _**i18n.single\_currency**_ – true or false
-   _**i18n.single\_currency.code**_ – the three-letter ISO currency code
-   The system locale _**glide.system.locale**_

 Single currency mode has the following limitations:

-   Single currency mode does not change the reference currency**.** So when calculations are performed (aggregation/filtering), some rate conversions might lead to unexpected results.
-   Single currency mode changes the currency in the user views and does not change the number formatting**.** So even through users in different countries see currency values in one currency, the number formatting (as determined by the user's locale) might not be what they expect.
-   The input of currency values is constrained to be in the single currency so the features of price fields can't be used.

The effects of rate conversions can be avoided by setting the system locale and the reference currency to be the single currency. However, the currency format is still determined by the user's locale. When the single currency and the user locale are different, the currency display might not be what a user expects.

## Price field

* * *

A price field is a currency field that enables control over conversions and display. The Service Catalog uses price fields.

The conversion and display selections can be chosen per price field and can be changed at any time. There are three variations:

-   **Calculated** \[Default\]: Behaves the same as the currency field type. Whenever conversions are performed, the latest currency conversion rates are used. When the price field is displayed, it is shown in the user's session currency.
-   **Fixed**: When the price field is displayed, it is shown in the currency code used when the value was entered. Whenever conversions are performed, the latest currency conversion rates are used.
-   **Multiple:** Enables you to enter multiple price values for an item using a different currency for each price. The field's value is the value entered in the user's session currency; otherwise, the first price entered is converted to the user's session currency. Whenever conversions are performed, the latest currency rates are used.

     **Note:** The first value entered is used during display. The additional values are not used during calculations.

For examples of using price field, refer to the tables used in Service Catalog.

## Presentation

* * *

Currency values are presented differently in list and form views.

## List View

Currency values are displayed in the user's session currency formatted for display in the user's locale. This is typically the currency symbol followed by a formatted number, but can be different based on the locale. Currency symbols are stored in the fx\_currency table.

Different field types appear as follows:

-   Currency field type: Value in user's session currency
-   Price field type/Calculated: Value in user's session currency
-   Price field type/Fixed: Value in currency as entered by the user
-   Price field type/Multiple: Value associated with the user's session currency if this value exists; otherwise, the first value entered is converted to the user's session currency

### Toggle values shown

A Globe icon is displayed beside the currency value (Geneva onwards) that enables the value to be changed to one of the following:

-   Value as entered by the user
-   Value in session currency
-   Value as entered and, in brackets,  the value in reference currency.

The icon appears when the user's session currency is different from the currency entered by the user. Clicking the icon cycles through the listed displays.

### Preview

In the preview for the record, currency values are shown as entered formatted for display in user's locale.

### Aggregation

Currency columns can have basic aggregation operations applied to them. These include total, group by, average, minimum, and maximum. Aggregation is done in two steps:

1.  Aggregate the reference currency values for all records
2.  Convert this aggregate to the user's session currency for display

**Note**: Because the conversion rate between the currency field's value (what is displayed) and its reference currency value (used for the aggregation) might have changed, the result may not be what the user expects.

**Note**: This limitation extends to different price types.

-   For price type Fixed, the calculated reference value can be old.
-   For price type Multiple, the reference value used is for the first price entered. The values in other currencies are not used.

The aggregate value is shown formatted in user's locale with a currency symbol.

(ISTANBUL) Starting in Istanbul, currency fields are stored with four fraction digits, and aggregates have four fraction digits. For upgrades, this value is controlled by a property. 

### Filtering

You can set up filters on currency fields. The currency value is entered as a currency code and numeric value. Filtering is done in two steps:

1.  The filter currency value is converted to the reference currency.
2.  The filter's calculated reference value is compared with the reference value in the records.

Matching records are shown in the list view.

**Note**: Because the conversion rate used when the filter is run might be different than the conversion rate used when calculating the reference values in the individual records, filtering results might not provide the expected result.

**Note:** This limitation extends to different price types.

-   For price type Fixed, the calculated reference value can be old.
-   For price type Multiple, the reference value used is for the first price entered. The values in other currencies are not used.

## Form View

In the form view, currency values are shown in the currency in which they were entered. A combo box gives the list of currencies available in the system. The format is determined by the user's locale.

When entering or changing the numeric value, format the value in the format specified by the user's locale.

In the form for a new record, the combo box with the list of currencies has the reference currency selected, and the numeric value is set to zero. 

### Editing a price field

A price field's currency code and numeric value can be changed in a form. An edit icon is shown next to the price field. Clicking the edit icon displays a form that can be used to edit all details of the price field:

-   Currency: List of currencies enabled in the system in the combo box
-   Amount: Numeric value formatted in the user's locale
-   Type: Combo box with Calculated, Fixed, Multiple  
    -   When the price type is changed to Multiple, the system creates child records for all the currencies enabled in the platform populated with values converted from the amount field using latest currency conversion rates.
    -   The price type can be modified any time.

### Read-only record

If the record is read only, the currency value is shown as entered and formatted for display in the user's locale. A price field shows the session currency value. 

### Single Currency Mode

In single currency mode, the currency is a label and cannot be changed. The form for editing the details of fields previously mentioned cannot be accessed because the edit icon is not shown.

### Editing the currency instance table

From Helsinki onward, an edit icon appears next to the field for users who can edit the currency instance table fx\_currency\_instance. This allows users with the financial\_mgmt\_user role to edit the values associated with the currency field. 

**Note**: Do not edit the fx\_currency\_instance table. The platform maintains this table, and your changes could have unintended consequences.

## Reporting

* * *

Currency values in reports are in the user's session currency formatted in the user's locale with a currency symbol. The user depends on how the report is run.

-   Shared report: The user who runs the report
-   Scheduled report: Generally run as the user who scheduled the report

The two user-specific values in the report are:

-   User session currency
-   Converted value

**Note:** A user that has a different session currency than the person who runs a report might receive unexpected results.

## Currency Conversion

* * *

Currency values may be converted to other currencies when stored and accessed.

-   The currency value is converted to reference currency when stored, whether on insert or update.
    
    This means the reference currency value is saved as well as the currency value.
    
-   The currency value is converted to the user's session currency for display.
    
-   The value entered for a filter from currency specified in the filter is converted to the reference currency.
    

## Rate table

Conversion rates are stored in the table fx\_rate. Each record contains the conversion rate from a given currency to the Euro. The rates are updated daily from the ECB website from a scheduled job called ECB Exchange Rate Load.

## Rate usage

A currency conversion from one currency to another involves two rates

-   Rate to convert from one currency to Euro
-   Rate to convert from Euro to the second currency

Whenever a conversion is performed, the platform uses the latest conversion rates. Therefore, calculations can potentially yield unexpected results. For example:

-   Different currency values can have different rates applies to them while storing the reference currency value. Aggregation therefore can combine values at different rates and convert back at another rate.
-   A filter value is converted at current rates while the values it filters in the database can be converted at different rates. A filter for $100 at today's rate can match a value of $99 obtained at yesterday's rates.

**Note**: For display purposes, the currency value used is what the user entered converted to session currency. However, for aggregation and filtering, the reference currency value is used. This enables currency values converted at different rates to be compared together.

## Import/Export

* * *

In general, currency values crossing the boundaries of the platform are represented in the user's session currency and formatted in the user's locale.

## Import/Transform

Currency values are imported as strings just like other fields. The default transform mapping to a currency field uses **setDisplayValue**(). The expected format for this function is:

-   A number formatted in the user's locale: this is taken as a value in the user's session currency, for example, 1,234.56.
-   This number prefixed by the three-letter currency code separated by a semicolon, for example, EUR;1.234,56.

This behavior can be customized in transform map scripts.

## Export

Currency values are exported in the user's session currency formatted in the user's locale except when exporting as XML. When exporting currency in XML, the value is in the reference currency value with no formatting.

### Related Links

## Scripting with currency values

* * *

In a scripting environment, currency fields are accessible as GlideElements.

## API

The following table lists the methods and how they work. The example values use a currency value of 21345.67 in Japanese yen (1563.72 in Euros and 1152.48 in US dollars) with the user's locale set to German (de.DE) and reference currency set to USD.

<table style="border: 1pt solid #4f81bd;" width="443" cellpadding="5"><tbody><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>Method name</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p><strong>Description</strong></p></td><td style="border: 1pt solid #4f81bd;" width="80"><p><strong>Example</strong></p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>getValue()</strong></p><p><strong>(access as record.field)</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Return the currency value in the user's session currency as an unformatted number.</p></td><td style="border: 1pt solid #4f81bd;" width="80"><p>1563.72</p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>getReferenceValue()</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Return the currency value in the reference currency as an unformatted number.</p></td><td style="border: 1pt solid #4f81bd;" width="80"><p>1152.48</p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>getSessionValue()</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Return the currency value in the user's session currency as an unformatted number.</p></td><td style="border: 1pt solid #4f81bd;" width="80"><p>1563.72</p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>getCurrencyValue()</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Return the currency value as entered as an unformatted number. <strong>Note</strong>: This is the currency value as entered, which might not be the session currency or the reference currency.</p></td><td style="border: 1pt solid #4f81bd;" width="80"><p>21345.67</p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>getDisplayValue()</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Return the currency value in the user's session currency formatted in the user's locale with a currency symbol.</p></td><td style="border: 1pt solid #4f81bd;" width="80"><p>€1.563,72</p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>getSessionDisplayValue()</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Return the currency value in the user's session currency formatted in the user's locale with a currency symbol.</p></td><td style="border: 1pt solid #4f81bd;" width="80"><p>€1.563,72</p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>getReferenceDisplayValue()</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Return the currency value in the reference currency formatted in the user's locale with a currency symbol.</p></td><td style="border: 1pt solid #4f81bd;" width="80"><p>$1.152,48</p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>getCurrencyDisplayValue()</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Return the currency value as entered formatted in the user's locale with a currency symbol.</p></td><td style="border: 1pt solid #4f81bd;" width="80"><p>¥21.345,67</p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>getCurrencyString()</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Return the currency value as entered as an unformatted number prefixed by the 3-letter ISO currency code separated by a semicolon.</p></td><td style="border: 1pt solid #4f81bd;" width="80"><p>JPY;21345.67</p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>getCurrencyCode()</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Return the 3-letter ISO currency code for the currency value as entered.</p></td><td style="border: 1pt solid #4f81bd;" width="80"><p>JPY</p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>getSessionCurrencyCode()</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Return the 3-letter ISO currency code for the user's session currency.</p></td><td style="border: 1pt solid #4f81bd;" width="80"><p>EUR</p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>getReferenceCurrencyCode()</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Return the 3-letter ISO currency code for the reference currency.</p></td><td style="border: 1pt solid #4f81bd;" width="80"><p>USD</p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>setValue()</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Set the currency value as:</p><ul style="list-style-position: inside;"><li>An unformatted number which is taken as a value in the user's session currency.</li><li>An unformatted number prefixed by a 3-letter currency code separated by semicolon.</li></ul></td><td style="border: 1pt solid #4f81bd;" width="80"><ul style="list-style-position: inside;"><li>4369.21</li><li>JPY; 4369.21</li></ul><p>&nbsp;</p></td></tr><tr><td style="border: 1pt solid #4f81bd;" width="192"><p><strong>setDisplayValue()</strong></p></td><td style="border: 1pt solid #4f81bd;" width="171"><p>Set the currency value as</p><ul style="list-style-position: inside;"><li>A number formatted in user's locale that is taken as a value in the user's session currency.</li><li>2.&nbsp;&nbsp;&nbsp;&nbsp; A number formatted in user's locale prefixed by a 3-letter currency code separated by semicolon.</li></ul></td><td width="80"><ul style="list-style-position: inside;"><li>4.369,21</li><li>JPY; 4.369,21</li></ul></td></tr></tbody></table>

## Significant fraction digits

The numeric values returned by the API contain two fraction digits. Although currency conversion rates may have more fraction digits, currency fields store only two fraction digits. APIs that accept numeric values round fraction digits to two places.

-   APIs that return values such as **getValue**() return up to two decimal places.
    
    The trailing zeros are removed for values read from the database, but if a value such as 00 is set later, these can return 1.00. The return value is not consistent.
    
-   APIs that return display values such as **getDisplayValue**() contain up to two decimal places.
    
    This could sometimes return two places even for values such as 7.10, but could remove training zeros at other times. The return value is not consistent.
    
-   GlideAggregate returns 2 decimal places 
    

(ISTANBUL) From Istanbul onward, currency values can contain four fraction digits.

-   APIs that return values such as **getValue**() return up to four decimal places. Trailing zeros are always removed.
-   APIs that return display values such as **getDisplayValue**() have at least two decimal places and up to four decimal places.
-   GlideAggregate returns four decimal places.

## Working with currency values

To display currency values use the display APIs. To work with currency values in any way other than display, use the APIs that return/accept unformatted numbers.

**Note:** Do not use the **getDisplayValue**() methods and then process the string to remove formatting information before performing calculations on the value.

### Getting values

APIs such as **getValue**(), **getCurrencyValue**(), and the like return unformatted numbers as strings. The floating point value can be obtained by using the JavaScript function **parseFloat**(). The resulting value can be used to perform calculations. The currency associated with these values can be obtained by the APIs that return the currency code. You can also use the **getCurrencyCode**() methods to determine the currency for a field.

var rate = parseFloat(current.base\_rate);

var currencyCode = current.base\_rate.getCurrencyCode();

### Setting values

Use the setValue() method to set the value of a currency field. If the currency is the user's session currency, use a plain number (either floating point number of a string containing it), otherwise prefix the value with the 3-letter ISO currency code.

var totalCost = rate\*current.hourly\_rate;

currency.total\_cost= currencyCode + ";" + totalCost;

### Deleting values

When a record containing a currency value is deleted, the platform deletes any associated currency records. However this does not happen under all conditions when **deleteMultiple**() is called.

**Note**: Do not use **deleteMultiple**() for tables with currency fields. Always iterate through each record and delete each record individually.

## Auditing

When a table containing a currency field is audited, currency values are audited. The value entered in the audit record is the numeric value in the session currency. The currency code/symbol is not present. The lack of an indication regarding what the number means or what the currency code is can cause confusion when the locale of the user viewing the record is different from the the user who updated the record.

From Istanbul onward, the value entered in the audit record can be changed to be the currency value as entered by the user in the format USD;1234.56. This is controlled by the glide property _**glide.sys.audit\_currency\_value**_. The default value is false. When set to **true**, auditing uses the new format.

## Tables

### fx\_currency

This table contains the currencies set up in the platform. Each record holds the three-letter ISO currency code, the symbol for the currency, and whether the currency is active. This information can be accessed from the **System Localization** menu.  
  
Any combo box with a list of currencies, for example, form view for a record with a currency field, will contain the list of currencies in this table that are marked active.  
  
**Note**: Do not delete existing records in fx\_currency. Deleting an existing record will invalidate all related currency/price records.

### fx\_currency\_instance

This table holds the currency value for the Currency field type. Each record holds the currency as a reference to the fx\_currency table, the numeric value, the reference value, and the reference currency.  
  
**Note:** Currency data is de-normalized. The parent record contains the reference currency value in its currency column. An fx\_currency\_instance record holds the sys\_id of the parent record that contains the numeric part of the reference currency value.

### fx\_price

This table holds the currency value for the Price field type. Each record holds the currency as a reference to the fx\_currency table, the numeric value, the reference value, and the reference currency.  
Based on the price type, there can be additional records.

-   -   Fixed, Calculated: single record
    -   Multiple: There is the primary currency value that has the parent field empty, and there are additional records containing currency values in other currencies that have the parent field set to the sys\_id of the record with the primary currency value.

**Note**: Currency data is de-normalized. The parent record contains the reference currency value in its currency column. An fx\_price record holds the sys\_id of the parent record that contains the currency value.

### fx\_rate

This table stores currency conversion rates. Each record holds the currency as a reference to the fx\_currency table and a conversion rate to convert that currency to Euros. Each record also holds the system fields for creation and update time that are used to retrieve the latest rate.  
Conversions from one currency to another may look up two rate records.

## ECB Download

A scheduled ECB Exchange Rate Load job that runs daily downloads rates from the website of the European Central Bank (ECB) and adds records in the fx\_rate table.

## Deletion

Records in fx\_currency\_instance/fx\_price are deleted when the currency value is deleted from the parent record. However, this does not always happen when **deleteMultiple**() is used. This is a known limitation of the currency API.

When **deleteMultiple**() is allowed, currency records can be orphaned. This does not affect functionality; however, the tables can grow large.

Using **deleteMultiple**() is not allowed under specific conditions like the following:

-   Delete business rules (before or after)
-   Parent table is audited
-   Parent table has iterative delete attribute set
-   Parent table has update sync set

**Note**: Do not use **deleteMultiple**() on records with currency fields.
