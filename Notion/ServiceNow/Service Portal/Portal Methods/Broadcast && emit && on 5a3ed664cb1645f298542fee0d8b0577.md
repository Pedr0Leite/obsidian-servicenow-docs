---
aliases:
  - "Broadcast && emit && on"
area: "Service Portal"
source: notion-export
tags:
  - service-portal
  - angularjs
  - events
  - widgets
  - portal-methods
---

# Broadcast && emit && on

**Detailed explanation**

$rootScope.$emit
only lets other $rootScope listeners catch it. This is good when you don't want
every $scope to get it. Mostly a high level communication. Think of it as
adults talking to each other in a room so the kids can't hear them.

$rootScope.$broadcast
is a method that lets pretty much everything hear it. This would be the
equivalent of parents yelling that dinner is ready so everyone in the house
hears it.

$scope.$emit is when
you want that $scope and all its parents and $rootScope to hear the event. This
is a child whining to their parents at home (but not at a grocery store where
other kids can hear).

$scope.$broadcast is
for the $scope itself and its children. This is a child whispering to its
stuffed animals so their parents can't hear.

## Related
- [[Angular provider]]
- [[Using the Link Function in Service Portal Widgets]]
- [[ServiceNow – Service Portal]]

- [[Portal Methods]]
- [[$uibModal's open function]]
- [[Portals Events]]