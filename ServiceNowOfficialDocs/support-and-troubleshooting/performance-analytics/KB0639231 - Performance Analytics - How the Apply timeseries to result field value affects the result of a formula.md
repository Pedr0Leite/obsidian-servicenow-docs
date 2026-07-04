---
title: "Performance Analytics - How the \"Apply timeseries to result\" field value affects the result of a formula"
aliases:
  - KB0639231
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0639231
kb_number: KB0639231
last_modified: 2025-09-17
---

## Performance Analytics - How the "Apply timeseries to result" field value affects the result of a formula

  

### Issue

PA - How the 'Apply timeseries to result' field value affects the result of a formula  
  

### Release

All Releases

### Resolution

# Procedure

* * *

Automated Indicator 1 : Indicator 1 – New : Number of New incidents

Automated Indicator 2 : Indicator 2 – Open : Number of Open incidents

Formula Indicator : demo formula 

              Calculation : \[\[Indicator 1 - New\]\] / \[\[Indicator 2 - Open\]\]

These are new indicators and we collected scores only for January 2017.

Keep in mind that "[Formula indicators round fractional results using Banker's rounding or mathematical rounding depending on the indicator Precision](https://docs.servicenow.com/csh?topicname=r_FormulaRounding.html&version=latest)."

<table style="border-collapse: collapse; border: none; height: 146px;" border="1" width="658" cellspacing="0" cellpadding="0"><tbody><tr style="height: 6.6pt;"><td style="width: 305.75pt; border: 1pt solid windowtext; padding: 0in 5.4pt; height: 6.6pt;" valign="top" width="306"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">&nbsp;</p></td><td style="width: 31.35pt; border-top: 1pt solid windowtext; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-image: initial; border-left: none; padding: 0in 5.4pt; height: 6.6pt;" valign="top" width="31"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">Precision</p></td><td style="width: 63.25pt; border-top: 1pt solid windowtext; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-image: initial; border-left: none; padding: 0in 5.4pt; height: 6.6pt;" valign="top" width="63"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">Timeseries</p></td></tr><tr style="height: 12.55pt;"><td style="width: 305.75pt; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-left: 1pt solid windowtext; border-image: initial; border-top: none; padding: 0in 5.4pt; height: 12.55pt;" valign="top" width="306"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">Indicator 1 – New : Number of New incidents</p></td><td style="width: 31.35pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0in 5.4pt; height: 12.55pt;" valign="top" width="31"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">2</p></td><td style="width: 63.25pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0in 5.4pt; height: 12.55pt;" valign="top" width="63"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">-None-</p></td></tr><tr style="height: 13pt;"><td style="width: 305.75pt; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-left: 1pt solid windowtext; border-image: initial; border-top: none; padding: 0in 5.4pt; height: 13pt;" valign="top" width="306"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">Indicator 2 – Open : Number of Open incidents</p></td><td style="width: 31.35pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0in 5.4pt; height: 13pt;" valign="top" width="31"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">2</p></td><td style="width: 63.25pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0in 5.4pt; height: 13pt;" valign="top" width="63"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">-None-</p></td></tr><tr style="height: 15.7pt;"><td style="width: 305.75pt; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-left: 1pt solid windowtext; border-image: initial; border-top: none; padding: 0in 5.4pt; height: 15.7pt;" valign="top" width="306"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">demo formula : [[Indicator 1 - New]] / [[Indicator 2 - Open]]</p></td><td style="width: 31.35pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0in 5.4pt; height: 15.7pt;" valign="top" width="31"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">5</p></td><td style="width: 63.25pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0in 5.4pt; height: 15.7pt;" valign="top" width="63"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">-None-</p></td></tr><tr style="height: 9.85pt;"><td style="width: 305.75pt; border-right: 1pt solid windowtext; border-bottom: 1pt solid windowtext; border-left: 1pt solid windowtext; border-image: initial; border-top: none; padding: 0in 5.4pt; height: 9.85pt;" valign="top" width="306"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">Widget</p></td><td style="width: 31.35pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0in 5.4pt; height: 9.85pt;" valign="top" width="31"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;">&nbsp;</p></td><td style="width: 63.25pt; border-top: none; border-left: none; border-bottom: 1pt solid windowtext; border-right: 1pt solid windowtext; padding: 0in 5.4pt; height: 9.85pt;" valign="top" width="63"><p style="margin: 0in 0in 0.0001pt; font-size: 12pt; font-family: Calibri;"><strong><span style="color: red;">By Month AVG +</span></strong></p></td></tr></tbody></table>

Apply timeseries to result is a field on the Formula indicator.

Apply timeseries to result value

![](sys_attachment.do?sys_id=91f5ec299308be14101833527cba10e0)

If "Apply timeseries to result" is **true** we calculate the Average on the result of the Formula which is "Column C". 

If "Apply timeseries to result" is **false** we calculate the Average per Column (an AVG on "Column A" then on "Column B") and we apply the formula calculation on the calculated average values (54,86 / 245,71 = 0,22326).

![](sys_attachment.do?sys_id=1df5ec299308be14101833527cba10e2)

In the scenario below, both the Numerator and Denominator have 0 scores recorded for some days. This affects the formula's result when 'Apply timeseries to result' is set to TRUE, as it excludes the days with no scores from the final calculation while performing the AVERAGE \[**By Month AVG** or **By Month AVG+\]** 

# ![](/sys_attachment.do?sys_id=19f5ec299308be14101833527cba10dd)

Note: For automated indicators, if Value When Nil = 0 is set, the indicator-level score is populated as 0. However, breakdown/element-level entries do not get individual 0 values. Instead, they inherit the parent-level score (i.e., for the day) as 0, which is logically applied in calculations. If 0 entries were created for every element, it would result in unnecessary high data volume in the table without adding relevant value.
