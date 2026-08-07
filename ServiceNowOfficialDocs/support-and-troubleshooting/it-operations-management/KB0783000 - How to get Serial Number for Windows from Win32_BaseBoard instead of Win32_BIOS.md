---
title: "How to get Serial Number for Windows from Win32_BaseBoard instead of Win32_BIOS"
aliases:
  - KB0783000
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0783000
kb_number: KB0783000
last_modified: 2024-04-08
---

## How to get Serial Number for Windows from Win32\_BaseBoard instead of Win32\_BIOS

  

### Issue

Need to fetch Serial Number info of a Windows device from Win32\_BaseBoard.SerialNumber instead of Win32\_BIOS

### Cause

Sometimes, the "Win32\_BIOS.SerialNumber" pulled in the right serial number information "SerialNumber=ABCDEFGH" whereas the Win32\_BaseBoard.SerialNumber pulled in "SerialNumber=/ABCDEFGH/LMNOPQRSTUVW/".

If the requirement would be to only have 'ABCDEFGH' as the serial number, then the follow the steps in Resolution section.

### Resolution

To fix the serial\_number issue for the devices, modify library pattern "Windows Identity - Hardware Information" => id = "2ba886d6dbc12200c06776231f96194b"  
https://INSTANCE\_NAME.service-now.com/sa\_pattern.do?sys\_id=2ba886d6dbc12200c06776231f96194b  
  
Moved "Add Win32\_BaseBoard.SerialNumber to temporary table" before step "Add Win32\_BIOS.SerialNumber to temporary table"  
\======================================  
step {  
name = "Add Win32\_BaseBoard.SerialNumber to temporary table"  
comment = "Temporary table containing one serial number row with normalized columnsThis table is needed due to lack of functionality adding rows to existing table with \\u201CTransform Table\\u201D operation."  
if {  
condition = all {  
is\_not\_empty {get\_attr {"Win32\_BaseBoard\[\*\].SerialNumber"}}  
not\_contains {  
get\_attr {"Win32\_BaseBoard\[\*\].SerialNumber"}  
"null"  
}  
not\_contains {  
get\_attr {"Win32\_BaseBoard\[\*\].SerialNumber"}  
"None"  
}  
}  
on\_true = transform {  
src\_table\_name = "Win32\_BaseBoard"  
target\_table\_name = "serialNumberTempTableRow"  
operation {  
set\_field {  
field\_name = "serial\_number"  
value = get\_attr {"Win32\_BaseBoard\[1\].SerialNumber"}  
}  
set\_field {  
field\_name = "serial\_number\_type"  
value = "baseboard"  
}  
}  
}  
on\_false = nop {}  
}  
}  
step {  
name = "Union serialNumberTempTable with cmdb\_serial\_number"  
comment = "Union serialNumberTempTable with cmdb\_ci\_serial\_number"  
union {  
table1\_name = "serialNumberTempTableRow"  
table2\_name = "cmdb\_serial\_number"  
result\_table\_name = "cmdb\_serial\_number"  
}  
}  
step {  
name = "Add Win32\_BIOS.SerialNumber to temporary table"  
comment = "Temporary table containing one serial number row with normalized columnsThis table is needed due to lack of functionality adding rows to existing table with \\u201CTransform Table\\u201D operation."  
if {  
condition = all {  
is\_not\_empty {get\_attr {"Win32\_BIOS\[\*\].SerialNumber"}}  
not\_contains {  
get\_attr {"Win32\_BIOS\[\*\].SerialNumber"}  
"null"  
}  
not\_contains {  
get\_attr {"Win32\_BIOS\[\*\].SerialNumber"}  
"None"  
}  
}  
on\_true = transform {  
src\_table\_name = "Win32\_BIOS"  
target\_table\_name = "serialNumberTempTableRow"  
operation {  
set\_field {  
field\_name = "serial\_number"  
value = get\_attr {"Win32\_BIOS\[1\].SerialNumber"}  
}  
set\_field {  
field\_name = "serial\_number\_type"  
value = "bios"  
}  
}  
}  
on\_false = nop {}  
}  
}  
step {  
name = "Union serialNumberTempTable with cmdb\_serial\_number"  
comment = "Union serialNumberTempTable with cmdb\_ci\_serial\_number"  
union {  
table1\_name = "serialNumberTempTableRow"  
table2\_name = "cmdb\_serial\_number"  
result\_table\_name = "cmdb\_serial\_number"  
}  
\======================================  
  
Re-run the discovery on the same IP and see that it fetches the expected serial number.
