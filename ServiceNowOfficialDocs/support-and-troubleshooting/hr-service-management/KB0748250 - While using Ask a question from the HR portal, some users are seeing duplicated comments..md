---
title: "While using \"Ask a question\" from the HR portal, some users are seeing duplicated comments."
aliases:
  - KB0748250
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0748250
kb_number: KB0748250
last_modified: 2024-04-07
---

## While using "Ask a question" from the HR portal, some users are seeing duplicated comments.

  

### Issue

# Symptoms

While using "Ask a question" from the HR portal, some users are seeing their first comment duplicated.

# Release

Kingston, London, Madrid

# Cause

There is a line in the 'sn-chat' widget that needs to be updated.

# Resolution

Make the following change to the client script of the sn-chat widget.

function repeatMessageV3(message) {  
if($scope.messages && $scope.messages.length > 0)  
\- return $scope.messages\[0\].sequence == message.id;  
\+ return $scope.messages\[$scope.messages.length - 1\].sequence == message.id;  
return false;  
}

replace the line starting with '-' with line starting with '+'

# Additional Information

The resolution was taken from similar PRB1328897 and resolves this issue as well.
