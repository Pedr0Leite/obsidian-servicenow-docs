---
title: "How to upgrade a MID Server that does not have access to the AutoUpgrade install server on the Internet"
aliases:
  - KB0565184
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0565184
kb_number: KB0565184
last_modified: 2026-06-22
---

## How to upgrade a MID Server that does not have access to the AutoUpgrade install server on the Internet

  

### Issue

Note: June 22 Update:

The install server is currently experiencing high load, and MID Servers may not be able to download from the install server themselves. This process can be used to allow those MID Servers to upgrade.

These are the MID Buildstamps, and relevant file URLs for the current set of patches/version customers are likely to be upgrading to.  You may need to ckick these links several times before the file downloads. You will only need to download the files once, and then the same files can be copied to all mid servers.

If your instance version is one of the ones listed below, you can use these links insterad of doing steps 1 and 2 in the Resolution section at the bottom.

**Yokohama Patch 12 Hot Fix 2b**   
yokohama-12-18-2024\_\_patch12-hotfix2b-05-18-2026\_06-19-2026\_0219

<table style="width: 1248pt; height: 213.977px;" border="0" cellspacing="0" cellpadding="0"><colgroup><col style="width: 133pt;"><col style="width: 1115pt;"></colgroup><tbody><tr style="height: 44.7727px;"><td style="height: 44.7727px;">Upgrade</td><td style="height: 44.7727px;"><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/19/mid-upgrade.yokohama-12-18-2024__patch12-hotfix2b-05-18-2026_06-19-2026_0219.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/19/mid-upgrade.yokohama-12-18-2024__patch12-hotfix2b-05-18-2026_06-19-2026_0219.universal.universal.zip</a></td></tr><tr style="height: 22.3864px;"><td style="height: 22.3864px;">Core</td><td style="height: 22.3864px;"><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/19/mid-core.yokohama-12-18-2024__patch12-hotfix2b-05-18-2026_06-19-2026_0219.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/19/mid-core.yokohama-12-18-2024__patch12-hotfix2b-05-18-2026_06-19-2026_0219.universal.universal.zip</a></td></tr><tr style="height: 19.0909px;"><td style="height: 19.0909px;">JRE:</td><td style="height: 19.0909px;">JRE is architecture specific and only required for upgrades between major versions, such as Zurich to Australia.</td></tr><tr style="height: 22.3864px;"><td style="height: 22.3864px;">Windows x86-64</td><td style="height: 22.3864px;"><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.yokohama-12-18-2024__patch12-hotfix2b-05-18-2026_06-19-2026_0219.windows.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.yokohama-12-18-2024__patch12-hotfix2b-05-18-2026_06-19-2026_0219.windows.x86-64.zip</a></td></tr><tr style="height: 22.3864px;"><td style="height: 22.3864px;">Linux x86-64</td><td style="height: 22.3864px;"><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.yokohama-12-18-2024__patch12-hotfix2b-05-18-2026_06-19-2026_0219.linux.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.yokohama-12-18-2024__patch12-hotfix2b-05-18-2026_06-19-2026_0219.linux.x86-64.zip</a></td></tr></tbody></table>

**Yokohama Patch 13 Hot Fix 3**  
yokohama-12-18-2024\_\_patch13-hotfix3-06-09-2026\_06-19-2026\_0939

<table style="width: 1248pt;" border="0" cellspacing="0" cellpadding="0"><colgroup><col style="width: 133pt;"><col style="width: 1115pt;"></colgroup><tbody><tr style="height: 15.0pt;"><td>Upgrade</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/19/mid-upgrade.yokohama-12-18-2024__patch13-hotfix3-06-09-2026_06-19-2026_0939.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/19/mid-upgrade.yokohama-12-18-2024__patch13-hotfix3-06-09-2026_06-19-2026_0939.universal.universal.zip</a></td></tr><tr style="height: 15.0pt;"><td>Core</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/19/mid-core.yokohama-12-18-2024__patch13-hotfix3-06-09-2026_06-19-2026_0939.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/19/mid-core.yokohama-12-18-2024__patch13-hotfix3-06-09-2026_06-19-2026_0939.universal.universal.zip</a></td></tr><tr style="height: 15.0pt;"><td>JRE:</td><td>JRE is architecture specific and only required for upgrades between major versions, such as Zurich to Australia.</td></tr><tr style="height: 15.0pt;"><td>Windows x86-64</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.yokohama-12-18-2024__patch13-hotfix3-06-09-2026_06-19-2026_0939.windows.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.yokohama-12-18-2024__patch13-hotfix3-06-09-2026_06-19-2026_0939.windows.x86-64.zip</a></td></tr><tr style="height: 15.0pt;"><td>Linux x86-64</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.yokohama-12-18-2024__patch13-hotfix3-06-09-2026_06-19-2026_0939.linux.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.yokohama-12-18-2024__patch13-hotfix3-06-09-2026_06-19-2026_0939.linux.x86-64.zip</a></td></tr></tbody></table>

**Zurich Patch 7b Hot Fix 2**  
zurich-07-01-2025\_\_patch7b-hotfix2-06-18-2026\_06-19-2026\_0134

<table style="width: 1248pt;" border="0" cellspacing="0" cellpadding="0"><colgroup><col style="width: 133pt;"><col style="width: 1115pt;"></colgroup><tbody><tr style="height: 15.0pt;"><td>Upgrade</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/19/mid-upgrade.zurich-07-01-2025__patch7b-hotfix2-06-18-2026_06-19-2026_0134.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/19/mid-upgrade.zurich-07-01-2025__patch7b-hotfix2-06-18-2026_06-19-2026_0134.universal.universal.zip</a></td></tr><tr style="height: 15.0pt;"><td>Core</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/19/mid-core.zurich-07-01-2025__patch7b-hotfix2-06-18-2026_06-19-2026_0134.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/19/mid-core.zurich-07-01-2025__patch7b-hotfix2-06-18-2026_06-19-2026_0134.universal.universal.zip</a></td></tr><tr style="height: 15.0pt;"><td>JRE:</td><td>JRE is architecture specific and only required for upgrades between major versions, such as Zurich to Australia.</td></tr><tr style="height: 15.0pt;"><td>Windows x86-64</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.zurich-07-01-2025__patch7b-hotfix2-06-18-2026_06-19-2026_0134.windows.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.zurich-07-01-2025__patch7b-hotfix2-06-18-2026_06-19-2026_0134.windows.x86-64.zip</a></td></tr><tr style="height: 15.0pt;"><td>Linux x86-64</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.zurich-07-01-2025__patch7b-hotfix2-06-18-2026_06-19-2026_0134.linux.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.zurich-07-01-2025__patch7b-hotfix2-06-18-2026_06-19-2026_0134.linux.x86-64.zip</a></td></tr></tbody></table>

**Zurich Patch 9 Hot Fix 3**  
zurich-07-01-2025\_\_patch9-hotfix3-06-13-2026\_06-19-2026\_0859

<table style="width: 1248pt;" border="0" cellspacing="0" cellpadding="0"><colgroup><col style="width: 133pt;"><col style="width: 1115pt;"></colgroup><tbody><tr style="height: 15.0pt;"><td>Upgrade</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/19/mid-upgrade.zurich-07-01-2025__patch9-hotfix3-06-13-2026_06-19-2026_0859.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/19/mid-upgrade.zurich-07-01-2025__patch9-hotfix3-06-13-2026_06-19-2026_0859.universal.universal.zip</a></td></tr><tr style="height: 15.0pt;"><td>Core</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/19/mid-core.zurich-07-01-2025__patch9-hotfix3-06-13-2026_06-19-2026_0859.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/19/mid-core.zurich-07-01-2025__patch9-hotfix3-06-13-2026_06-19-2026_0859.universal.universal.zip</a></td></tr><tr style="height: 15.0pt;"><td>JRE:</td><td>JRE is architecture specific and only required for upgrades between major versions, such as Zurich to Australia.</td></tr><tr style="height: 15.0pt;"><td>Windows x86-64</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.zurich-07-01-2025__patch9-hotfix3-06-13-2026_06-19-2026_0859.windows.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.zurich-07-01-2025__patch9-hotfix3-06-13-2026_06-19-2026_0859.windows.x86-64.zip</a></td></tr><tr style="height: 15.0pt;"><td>Linux x86-64</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.zurich-07-01-2025__patch9-hotfix3-06-13-2026_06-19-2026_0859.linux.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.zurich-07-01-2025__patch9-hotfix3-06-13-2026_06-19-2026_0859.linux.x86-64.zip</a></td></tr></tbody></table>

**Zurich Patch 10 Hot Fix 1**  
zurich-07-01-2025\_\_patch10-hotfix1-06-18-2026\_06-19-2026\_0939

<table style="width: 1248pt;" border="0" cellspacing="0" cellpadding="0"><colgroup><col style="width: 133pt;"><col style="width: 1115pt;"></colgroup><tbody><tr style="height: 15.0pt;"><td>Upgrade</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/19/mid-upgrade.zurich-07-01-2025__patch10-hotfix1-06-18-2026_06-19-2026_0939.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/19/mid-upgrade.zurich-07-01-2025__patch10-hotfix1-06-18-2026_06-19-2026_0939.universal.universal.zip</a></td></tr><tr style="height: 15.0pt;"><td>Core</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/19/mid-core.zurich-07-01-2025__patch10-hotfix1-06-18-2026_06-19-2026_0939.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/19/mid-core.zurich-07-01-2025__patch10-hotfix1-06-18-2026_06-19-2026_0939.universal.universal.zip</a></td></tr><tr style="height: 15.0pt;"><td>JRE:</td><td>JRE is architecture specific and only required for upgrades between major versions, such as Zurich to Australia.</td></tr><tr style="height: 15.0pt;"><td>Windows x86-64</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.zurich-07-01-2025__patch10-hotfix1-06-18-2026_06-19-2026_0939.windows.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.zurich-07-01-2025__patch10-hotfix1-06-18-2026_06-19-2026_0939.windows.x86-64.zip</a></td></tr><tr style="height: 15.0pt;"><td>Linux x86-64</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.zurich-07-01-2025__patch10-hotfix1-06-18-2026_06-19-2026_0939.linux.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.zurich-07-01-2025__patch10-hotfix1-06-18-2026_06-19-2026_0939.linux.x86-64.zip</a></td></tr></tbody></table>

**Australia Patch 2 Hot Fix 2**  
australia-02-11-2026\_\_patch2-hotfix2-06-18-2026\_06-18-2026\_2231

<table style="width: 1248pt;" border="0" cellspacing="0" cellpadding="0"><colgroup><col style="width: 133pt;"><col style="width: 1115pt;"></colgroup><tbody><tr style="height: 15.0pt;"><td>Upgrade</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/18/mid-upgrade.australia-02-11-2026__patch2-hotfix2-06-18-2026_06-18-2026_2231.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/18/mid-upgrade.australia-02-11-2026__patch2-hotfix2-06-18-2026_06-18-2026_2231.universal.universal.zip</a></td></tr><tr style="height: 15.0pt;"><td>Core</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/18/mid-core.australia-02-11-2026__patch2-hotfix2-06-18-2026_06-18-2026_2231.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/18/mid-core.australia-02-11-2026__patch2-hotfix2-06-18-2026_06-18-2026_2231.universal.universal.zip</a></td></tr><tr style="height: 15.0pt;"><td>JRE:</td><td>JRE is architecture specific and only required for upgrades between major versions, such as Zurich to Australia.</td></tr><tr style="height: 15.0pt;"><td>Windows x86-64</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/18/mid-jre.australia-02-11-2026__patch2-hotfix2-06-18-2026_06-18-2026_2231.windows.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/18/mid-jre.australia-02-11-2026__patch2-hotfix2-06-18-2026_06-18-2026_2231.windows.x86-64.zip</a></td></tr><tr style="height: 15.0pt;"><td>Linux x86-64</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/18/mid-jre.australia-02-11-2026__patch2-hotfix2-06-18-2026_06-18-2026_2231.linux.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/18/mid-jre.australia-02-11-2026__patch2-hotfix2-06-18-2026_06-18-2026_2231.linux.x86-64.zip</a></td></tr></tbody></table>

**Australia Patch 3 Hot Fix 1**  
australia-02-11-2026\_\_patch3-hotfix1-06-18-2026\_06-19-2026\_0938

<table style="width: 1248pt;" border="0" cellspacing="0" cellpadding="0"><colgroup><col style="width: 133pt;"><col style="width: 1115pt;"></colgroup><tbody><tr style="height: 15.0pt;"><td>Upgrade</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/19/mid-upgrade.australia-02-11-2026__patch3-hotfix1-06-18-2026_06-19-2026_0938.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-upgrade/2026/06/19/mid-upgrade.australia-02-11-2026__patch3-hotfix1-06-18-2026_06-19-2026_0938.universal.universal.zip</a></td></tr><tr style="height: 15.0pt;"><td>Core</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/19/mid-core.australia-02-11-2026__patch3-hotfix1-06-18-2026_06-19-2026_0938.universal.universal.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-core/2026/06/19/mid-core.australia-02-11-2026__patch3-hotfix1-06-18-2026_06-19-2026_0938.universal.universal.zip</a></td></tr><tr style="height: 15.0pt;"><td>JRE:</td><td>JRE is architecture specific and only required for upgrades between major versions, such as Zurich to Australia.</td></tr><tr style="height: 15.0pt;"><td>Windows x86-64</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.australia-02-11-2026__patch3-hotfix1-06-18-2026_06-19-2026_0938.windows.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.australia-02-11-2026__patch3-hotfix1-06-18-2026_06-19-2026_0938.windows.x86-64.zip</a></td></tr><tr style="height: 15.0pt;"><td>Linux x86-64</td><td><a href="https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.australia-02-11-2026__patch3-hotfix1-06-18-2026_06-19-2026_0938.linux.x86-64.zip" target="_parent" rel="noopener noreferrer">https://install.service-now.com/glide/distribution/builds/package/app-signed/mid-jre/2026/06/19/mid-jre.australia-02-11-2026__patch3-hotfix1-06-18-2026_06-19-2026_0938.linux.x86-64.zip</a></td></tr></tbody></table>

* * *

If you need to upgrade a MID Server that does not have access to the AutoUpgrade install server, this article provides a manual procedure. The steps below fool the MID Server into thinking it has downloaded the files already, allowing it to upgrade itself in the normal way. If necessary, this must be done for every MID Server after every upgrade or patch of every instance, without fail.

When an instance is upgraded, the MID Server needs to upgrade itself to match and needs to [Download Upgrade Files](https://docs.servicenow.com/csh?topicname=t_DownloadMIDServerFiles.html&version=latest "Download Upgrade Files") from **https://install.service-now.com/** and if it does not have access, it fails to upgrade. The automatic [Test MID Server connectivity](https://docs.servicenow.com/csh?topicname=t_ValidateNetworkConnectivity.html&version=latest "Test MID Server connectivity") feature will check for and notify you if the MID Server can't.

![](/Warning_25x.pngx "Warning") **Warning**: A MID Server on the wrong version can cause code and data mismatches between MID Server and instance, potentially causing the MID Server to fail to process commands sent it by the instance, or the instance to not process data coming back from the MID Server. APIs related to Validation and encryption Keychains may also not match.

#### Symptom example

MID Server Agent log:

**AutoUpgrade.3600** **Performing pre-upgrade validation tests**.  
AutoUpgrade.3600 Downloading from https://install.service-now.com/glide/distribution/builds/package/mid-upgrade/2019/07/16/mid-upgrade.mid.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.preUpgradeCheck.zip  
AutoUpgrade.3600 WARNING \*\*\* WARNING \*\*\* java.net.SocketTimeoutException: connect timed out when posting to https://install.service-now.com/glide/distribution/builds/package/mid-upgrade/2019/07/16/mid-upgrade.mid.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.preUpgradeCheck.zip  
AutoUpgrade.3600 SEVERE \*\*\* ERROR \*\*\* java.net.SocketTimeoutException: connect timed out when posting to https://install.service-now.com/glide/distribution/builds/package/mid-upgrade/2019/07/16/mid-upgrade.mid.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.preUpgradeCheck.zip  
AutoUpgrade.3600 Downloading from http://install.service-now.com/glide/distribution/builds/package/mid-upgrade/2019/07/16/mid-upgrade.mid.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.preUpgradeCheck.zip  
AutoUpgrade.3600 WARNING \*\*\* WARNING \*\*\* org.apache.commons.httpclient.ConnectTimeoutException: The host did not accept the connection within timeout of 10000 ms when posting to http://install.service-now.com/glide/distribution/builds/package/mid-upgrade/2019/07/16/mid-upgrade.mid.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.preUpgradeCheck.zip  
AutoUpgrade.3600 SEVERE \*\*\* ERROR \*\*\* org.apache.commons.httpclient.ConnectTimeoutException: The host did not accept the connection within timeout of 10000 ms when posting to http://install.service-now.com/glide/distribution/builds/package/mid-upgrade/2019/07/16/mid-upgrade.mid.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.preUpgradeCheck.zip  
AutoUpgrade.3600 SEVERE \*\*\* **ERROR \*\*\* Aborting MID Server upgrade due to pre-upgrade check failure: Unable to download updates from install server**  
AutoUpgrade.3600 **Setting mid status to Upgrade Failed**  
AutoUpgrade.3600 Instance.updateAgentRecordState(), OperationalState=UPGRADE\_FAILED

The MID Server form and Issues table will also repeat the error:

Aborting MID Server upgrade due to pre-upgrade check failure: Unable to download updates from install server

![MID Server form and Issues table repeat the error, stating unresolved issue, failed upgrade, and pre-upgrade check failure](/sys_attachment.do?sys_id=487cb3fe47690bd83b05ff48436d43d0)

### Release

All versions with Windows or Linux MID Servers.

### Cause

In the following situations, your MID Server computer has no access to the install server and cannot auto-upgrade itself. You should try to resolve these configuration issues internally first, as these are our documented connectivity requirements:

-   The instance is on-premise and installed inside the customer network (with no Internet access), and the MID Server also has no internet access at all.
-   The instance is hosted in our datacenter, but although the MID Server does have access to the instance, you have not yet arranged for it to have access to our upgrade server: https://install.service-now.com/

### Resolution

This manual procedure fools the MID Server into thinking it has downloaded the files itself already, allowing it to upgrade itself in the normal way, and if necessary must be done for _every_ MID Server after _every_ upgrade or patch of _every_ instance, without fail. 

### 1) Find the filenames from the Agent log

On the MID Server computer, check the latest 'AutoUpgrade' or 'StartupSequencer' thread entries in the Agent Log for the "Missing:" ZIP file names:  
<install folder>\\agent\\logs\\agent0.log.0

AutoUpgrade.3600 Current packages:
AutoUpgrade.3600 **Installed**: \[mid-core.**kingston-10-17-2017\_\_patch0-11-06-2017\_11-11-2017\_1422**.universal.universal.zip, mid-jre.kingston-10-17-2017\_\_patch0-11-06-2017\_11-11-2017\_1422.windows.x86-64.zip\]
AutoUpgrade.3600 Assigned: \[mid-upgrade.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.universal.universal.zip, mid-core.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.universal.universal.zip, mid-jre.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636 .windows.x86-64.zip\]
AutoUpgrade.3600 **Missing**: \[mid-upgrade.**newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636**.universal.universal.zip, mid-core.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.universal.universal.zip, mid-jre.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636 .windows.x86-64.zip\]
AutoUpgrade.3600 Downloaded: \[\]

In that example, the MID Server is still Kingston Patch 0, even though the instance is already upgraded to New York Patch 0 Hotfix 2, and the three missing files in this particular example are:

-   mid-**upgrade**.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.universal.universal.zip
-   mid-**jre**.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.**windows.x86-64**.zip
-   mid-**core**.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.universal.universal.zip

![](/Note_25x.pngx "Note")**Note**: The file names and URLs you need will be specific to a particular version of the platform, that is running in your specific instance. 

### 2) Figure out the full URL for those files

The attached Excel Spreadsheet provides the links to the files for a specific version.  
Use this link to avoid the Viewer loading and turning it into a PDF: [MID Server ZIP File URL Generator.xlsx](https://support.servicenow.com/sys_attachment.do?sys_id=b36c73fe47690bd83b05ff48436d437c "MID Server ZIP File URL Generator.xlsx")

You can find the current MID Buildstamp of your instance, which is the version the MID Server should upgrade to, on the Stats page:  
https://<instance\_name>.service-now.com/stats.do

![](/sys_attachment.do?sys_id=447cb3fe47690bd83b05ff48436d4370)

Paste it into the attached spreadsheet, and find the URLs for the files identified above. The filenames are very similar, so be careful to select the correct file (e.g. mid-upgrade) and architecture (e.g. windows.x64):

![](/sys_attachment.do?sys_id=c87cb3fe47690bd83b05ff48436d436b)

![](/Note_25x.pngx "Note")**Note**: If you are running a version earlier than Paris, Orlando Patch 3, New York Patch 9, and Madrid Patch 10 Hot Fix 1b, then you will need to use the Unsigned ZIP Files lower down the spreadsheet. Otherwise use the Signed ones.

### 3) Download these files manually on another computer that has internet access and then copy those ZIP files to the MID Server folder

<install folder>\\agent\\package\\incoming

![](/Note_25x.pngx "Note")**Note**: You may be tempted to make things simpler by adding both the Windows and Linux files, so you copy the same set of files to all MID Servers regardless of the OS. Don't do that, because the MID Server may still extract them all, overwriting the correct files with the wrong ones, and breaking the upgrade.  

### 4) Prevent the Pre-Check being run

If you see the following error in the agent log, disable the MID Server "preUpgradeCheck" by adding the MID Server parameter **mid.upgrade.run\_precheck=false** to each MID Server that does not have access to the install server.

AutoUpgrade.3600 SEVERE \*\*\* ERROR \*\*\* Aborting MID Server upgrade due to pre-upgrade check failure: Unable to download updates from install server 

See [Disabling the pre-upgrade check](https://docs.servicenow.com/csh?topicname=c_UpgradeAndTestMIDServer.html&version=latest#d886430e833 "Disabling the pre-upgrade check") in the docs.

### 5) Restart the MID Server

At this point, you can wait for the AutoUpgrade thread to run again (it is on a 1-hour interval) or restart the MID Server service to force it to upgrade now.  
  
The next time the AutoUpgrade thread runs, **Downloaded:** shows the files present in the **<install folder>\\agent\\logs\\agent0.log.0** log. It then goes ahead and does the upgrade.

StartupSequencer   Downloaded: \[mid-upgrade.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.universal.universal.zip, mid-core.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636.universal.universal.zip, mid-jre.newyork-06-26-2019\_\_patch0-hotfix2-07-10-2019\_07-16-2019\_1636 .windows.x86-64.zip\]

You can then re-use the downloaded files for any other MID Servers that are also connecting to the same instance.

### Related Links

For post-Madrid releases, this should not be an issue due to defaulting to using the instance as a kind of proxy (**mid.download.through.instance=true**), meaning direct access to the install server was not necessary.

Since New York, the MID Server once again has to have access to the install server (PRB1332088/PRB627019). It is recommended that the property is set to false, and access is provided to the install server, in order to avoid API\_INT semaphore exhaustion, MID Servers failing to connect to the instance and shutting down, and extended upgrade times during instance upgrades.
