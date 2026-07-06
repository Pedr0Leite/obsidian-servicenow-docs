---
title: "Error with NagiosXI connector \"Connection test failed: Failed to connect to Nagios on test connector. Invalid API Key \""
aliases:
  - KB0755181
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0755181
kb_number: KB0755181
last_modified: 2024-04-07
---

## Issue

# Symptoms

Error occurs while testing the connection between the MID Server and the NagiosXI connector.

"Connection test failed: Failed to connect to Nagios on test connector. Invalid API Key "

# Release

All releases

# Steps to reproduce

Procedure to configure the NagiosXI connector instance.

1.  Navigate to Event Management > Event Connectors(Pull) > Connector Instances
2.  Fill in all the details such as name, Description, Credentials etc.,
3.  Click Test Connector to verify the connection between the MID Server and the connector.
4.  You will see below error message

"Connection test failed: Failed to connect to Nagios on test connector. Invalid API Key"

# Resolution

1.  Use a network tool, such as ping, to verify network connectivity from the MID Server to the Nagios Core monitor. If this works, then proceed to the next step.
2.  Please verify that the password is correct. Also make sure the API key doesn't consists of special characters(only use Alpha-numeric character) in the password.

             https://www.jamf.com/jamf-nation/discussions/13350/can-t-access-api-if-special-characters-in-password 

           ( You will find the user API key by logging into Log Server & click the user name in the top right corner. This will display the API key)

           3. If it is not visible, the API might not be enabled for that user.

            Then follow below steps to enable API access.

             Admin > General > User management 

             Edit the user and enable API access.

# Additional Information

https://docs.servicenow.com/csh?topicname=configure-nagios-connector.html&version=latest
