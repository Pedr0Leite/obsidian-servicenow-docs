---
title: "Event rules page not loading"
aliases:
  - KB0685033
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0685033
kb_number: KB0685033
last_modified: 2024-04-07
---

## Event rules page not loading

  

### Issue

Issue:

Event rule module page is not loading. 

ie:

![](sys_attachment.do?sys_id=f86d910bdbad97c02328f3231f9619ed)![](sys_attachment.do?sys_id=445e518bdbad97c02328f3231f961929)![](sys_attachment.do?sys_id=7b1c6c2edb42b450e515c22305961998)

From Chrome console debug tool, there were error related to angularjs.

GET https://<INSTANCE\_NAME>.service-now.com/styles/sa.eventRules/sa\_event\_rule\_includes.cssx?v=10-13-2017\_1804 net::ERR\_ABORTED

$sa\_event\_rules.do:75 GET https://<INSTANCE\_NAME>.service-now.com/scripts/sa.eventRules/js\_includes\_sa\_assu\_event\_rules.jsx?v=10-13-2017\_1804&lp=Wed\_Apr\_18\_19\_00\_04\_PDT\_2018&c=13\_252 net::ERR\_ABORTED

...

GET https://<INSTANCE\_NAME>.service-now.com/scripts/sa.eventRules/js\_includes\_sa\_assu\_event\_rules.jsx?v=10-13-2017\_1804&lp=Wed\_Apr\_18\_19\_00\_04\_PDT\_2018&c=13\_252 net::ERR\_ABORTED

angular\_includes\_1.4.jsx?v=10-13-2017\_1804:8 Uncaught Error: \[$injector:modulerr\] [http://errors.angularjs.org/1.4.8/$injector/modulerr?p0=sa.eventRules&p1=Error%3A%20%5B%24injector%3Anomod%5D%20http%3A//errors.angularjs.org/1.4.8/%24injector/nomod%3Fp0%3Dsa.eventRules%20%20%20%20at%20https%3A//](http://errors.angularjs.org/1.4.8/$injector/modulerr?p0=sa.eventRules&p1=Error%3A%20%5B%24injector%3Anomod%5D%20http%3A//errors.angularjs.org/1.4.8/%24injector/nomod%3Fp0%3Dsa.eventRules%20%20%20%20at%20https%3A//)<INSTANCE\_NAME>.service-now.com/scripts/angular\_includes\_1.4.jsx%3Fv%3D10-13-2017\_1804%3A8%3A416%20%20%20%20at%20https%3A//<INSTANCE\_NAME>.service-now.com/scripts/angular\_includes\_1.4.jsx%3Fv%3D10-13-2017\_1804%3A26%3A186%20%20%20%20at%20b%20(https%3A//<INSTANCE\_NAME>.service-now.com/scripts/angular\_includes\_1.4.jsx%3Fv%3D10-13-2017\_1804%3A25%3A251)%20%20%20%20at%20https%3A//<INSTANCE\_NAME>.service-now.com/scripts/angular\_includes\_1.4.jsx%3Fv%3D10-13-2017\_1804%3A25%3A494%20%20%20%20at%20https%3A//<INSTANCE\_NAME>.service-now.com/scripts/angular\_includes\_1.4.jsx%3Fv%3D10-13-2017\_1804%3A40%3A117%20%20%20%20at%20n%20(https%3A//<INSTANCE\_NAME>.service-now.com/scripts/angular\_includes\_1.4.jsx%3Fv%3D10-13-2017\_1804%3A9%3A333)%20%20%20%20at%20g%20(https%3A//<INSTANCE\_NAME>.service-now.com/scripts/angular\_includes\_1.4.jsx%3Fv%3D10-13-2017\_1804%3A39%3A488)%20%20%20%20at%20eb%20(https%3A//<INSTANCE\_NAME>.service-now.com/scripts/angular\_includes\_1.4.jsx%3Fv%3D10-13-2017\_1804%3A43%3A249)%20%20%20%20at%20c%20(https%3A//<INSTANCE\_NAME>.service-now.com/scripts/angular\_includes\_1.4.jsx%3Fv%3D10-13-2017\_1804%3A21%3A463)%20%20%20%20at%20yc%20(https%3A//<INSTANCE\_NAME>.service-now.com/scripts/angular\_includes\_1.4.jsx%3Fv%3D10-13-2017\_1804%3A22%3A274)

at angular\_includes\_1.4.jsx?v=10-13-2017\_1804:8

at angular\_includes\_1.4.jsx?v=10-13-2017\_1804:40

at n (angular\_includes\_1.4.jsx?v=10-13-2017\_1804:9)

at g (angular\_includes\_1.4.jsx?v=10-13-2017\_1804:39)

at eb (angular\_includes\_1.4.jsx?v=10-13-2017\_1804:43)

at c (angular\_includes\_1.4.jsx?v=10-13-2017\_1804:21)

at yc (angular\_includes\_1.4.jsx?v=10-13-2017\_1804:22)

at Zd (angular\_includes\_1.4.jsx?v=10-13-2017\_1804:21)

at HTMLDocument.<anonymous> (angular\_includes\_1.4.jsx?v=10-13-2017\_1804:296)

at i (jquery2\_includes.jsx?v=10-13-2017\_1804:17)

Solution:

Run cache.do at Filter navigator

![](sys_attachment.do?sys_id=bf1cac2edb42b450e515c223059619a2)

and revisit the page (sa\_event\_rules) after cache run finish.
