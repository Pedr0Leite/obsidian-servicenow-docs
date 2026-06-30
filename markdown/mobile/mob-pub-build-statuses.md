---
title: Mobile Publishing build statuses
description: Learn what the Mobile Publishing build statuses "Build in progress" and "Ready for testing" mean and what actions they require from you.
locale: en-US
canonical_url: https://www.servicenow.com/docs/r/mobile/mob-pub-build-statuses.html
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Request, test, &amp; publish, Custom branded apps, Configuring the Mobile Platform, Mobile Platform]
---

# Mobile Publishing build statuses

Learn what the Mobile Publishing build statuses "Build in progress" and "Ready for testing" mean and what actions they require from you.

## "Build in progress"

Your app's build status is "Build in progress" while ServiceNow® creates your branded app and sends it to Apple or Google for approval. The time to build is based on whether your app uses public or private distribution and on which operating system you choose. The time to build process takes the amount of time shown in the following diagram:

\[Omitted image "build-in-prog-flochart.png"\] Alt text: Diagram showing that private iOS apps take 2-4 weeks; private android apps take 1 week; public iOS apps take 1 week; and public android apps take 1 week or less

## "Ready for testing"

When the build status becomes "Ready for testing," one of the following actions is required based on the following factors:

-   Operating system
-   Whether the branded mobile app is for private or public distribution
-   Type of mobile application management \(MAM\) you use
-   If the request is for a new branded app or a request to update an existing branded app

|New/Update|Operating System|Private/Public distribution|"Ready for testing" action required|
|----------|----------------|---------------------------|-----------------------------------|
|New|Android|Private|See [[testpubnu-andapp-privdist|Test and publish a new branded Android app for private distribution]].|
|New|iOS|Private|See [[testpubnu-iosapp-privdist|Test and publish a new branded iOS app for private distribution]].|
|New|Android|Public|See [[testpubnu-andapp-pubdist|Test and publish a new branded Android app for public distribution]].|
|New|iOS|Public|See [[testpubnu-iosapp-pubdist|Test and publish a new branded iOS app for public distribution]].|
|Updated|Android|Private|See [[testpub-updat-and-app-priv|Test and publish an updated Android app for private distribution]].|
|Updated|iOS|Private|See [[testpub-updat-ios-app-priv|Test and publish an updated iOS app for private distribution]].|
|Updated|Android|Public|See [[testpub-updat-and-app-pub|Test and publish an updated Android app for public distribution]].|
|Updated|iOS|Public|See [[testpub-updat-ios-app-pub|Test and publish an updated iOS app for public distribution]].|

**Parent Topic:**[[request-test-pub-branded-mob-app|Request, test, and publish a branded mobile app]]

## Related

- [[testpubnu-andapp-privdist|testpubnu andapp privdist]]
- [[testpubnu-iosapp-privdist|testpubnu iosapp privdist]]
- [[testpubnu-andapp-pubdist|testpubnu andapp pubdist]]
- [[testpubnu-iosapp-pubdist|testpubnu iosapp pubdist]]
- [[testpub-updat-and-app-priv|testpub updat and app priv]]
- [[testpub-updat-ios-app-priv|testpub updat ios app priv]]
- [[testpub-updat-and-app-pub|testpub updat and app pub]]
- [[testpub-updat-ios-app-pub|testpub updat ios app pub]]
- [[request-test-pub-branded-mob-app|Request, test, and publish a branded mobile app]]
