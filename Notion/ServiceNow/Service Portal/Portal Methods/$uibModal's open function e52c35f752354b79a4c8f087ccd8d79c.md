---
aliases:
  - "$uibModal's open function"
area: "Service Portal"
source: notion-export
tags:
  - service-portal
  - angularjs
  - modal
  - widgets
  - portal-methods
---

# $uibModal's open function

*Template : can be an angular ng-template tagged to your widget*

*templateURL :can be the URL where your HTML is rendered (can be a UI page too)*

*To check that navigate to UI pages and search with matching ENDPOINT or the UI page name*

*Here is the explanation for all the options or parameters
 that $uib modal can accept(I just highlighted the explanation for the 
template and templateUrl options or parameters below)*

### $uibModal's open function

### options parameter

- `animation` *(Type: `boolean`, Default: `true`)* - Set to false to disable animations on new modal/backdrop. Does not
toggle animations for modals/backdrops that are already displayed.
- `appendTo` *(Type: `angular.element`, Default: `body`: Example: `$document.find('aside').eq(0)`)* - Appends the modal to a specific element.
- `ariaDescribedBy` *(Type: `string`, `my-modal-description`)* - Sets the [`aria-describedby`](https://www.w3.org/TR/wai-aria/states_and_properties#aria-describedby) property on the modal. The value should be an id (without the leading `#`) pointing to the element that describes your modal. Typically, this will be the text on your modal, but does not include something the user
would interact with, like buttons or a form. Omitting this option will
not impact sighted users but will weaken your accessibility support.
- `ariaLabelledBy` *(Type: `string`, `my-modal-title`)* - Sets the [`aria-labelledby`](https://www.w3.org/TR/wai-aria/states_and_properties#aria-labelledby) property on the modal. The value should be an id (without the leading `#`) pointing to the element that labels your modal. Typically, this will be a header element. Omitting this option will not impact sighted users
but will weaken your accessibility support.
- `backdrop` *(Type: `boolean|string`, Default: `true`)* - Controls presence of a backdrop. Allowed values: `true` (default), `false` (no backdrop), `'static'` (disables modal closing by click on the backdrop).
- `backdropClass` *(Type: `string`)* - Additional CSS class(es) to be added to a modal backdrop template.
- `bindToController` *(Type: `boolean`, Default: `false`)* - When used with `controllerAs` & set to `true`, it will bind the $scope properties onto the controller.
- `component` *(Type: `string`, Example: `myComponent`)* - A string reference to the component to be rendered that is registered
with Angular's compiler. If using a directive, the directive must have `restrict: 'E'` and a template or templateUrl set.
    
    It supports these bindings:
    
    - `close` - A method that can be used to close a modal, passing a result. The result must be passed in this format: `{$value: myResult}`
    - `dismiss` - A method that can be used to dismiss a modal, passing a result. The result must be passed in this format: `{$value: myRejectedResult}`
    - `modalInstance` - The modal instance. This is the same `$uibModalInstance` injectable found when using `controller`.
    - `resolve` - An object of the modal resolve values. See [UI Router resolves](https://angular-ui.github.io/bootstrap/versioned-docs/2.3.2/#ui-router-resolves) for details.
- `controller` *(Type: `function|string|array`, Example: `MyModalController`)* - A controller for the modal instance, either a controller name as a
string, or an inline controller function, optionally wrapped in array
notation for dependency injection. Allows the controller-as syntax. Has a special `$uibModalInstance` injectable to access the modal instance.
- `controllerAs` *(Type: `string`, Example: `ctrl`)* - An alternative to the controller-as syntax. Requires the `controller` option to be provided as well.
- `keyboard` - *(Type: `boolean`, Default: `true`)* - Indicates whether the dialog should be closable by hitting the ESC key.
- `openedClass` *(Type: `string`, Default: `modal-open`)* - Class added to the `body` element when the modal is opened.
- `resolve` *(Type: `Object`)* - Members that will be resolved and passed to the controller as locals; it is equivalent of the `resolve` property in the router.
- `scope` *(Type: `$scope`)* - The parent scope instance to be used for the modal's content. Defaults to `$rootScope`.
- `size` *(Type: `string`, Example: `lg`)* - Optional suffix of modal window class. The value used is appended to the `modal-` class, i.e. a value of `sm` gives `modal-sm`.
- `*template` (Type: `string`) - Inline template representing the modal's content.*
- `*templateUrl` (Type: `string`) - A path to a template representing modal's content. You need either a `template` or `templateUrl`.*
- `windowClass` *(Type: `string`)* - Additional CSS class(es) to be added to a modal window template.
- `windowTemplateUrl` *(Type: `string`, Default: `uib/template/modal/window.html`)* - A path to a template overriding modal's window template.
- `windowTopClass` *(Type: `string`)* - CSS class(es) to be added to the top modal window.

Alternatively you can use SpModal modal API provided by service now which is much easier to understand than uib modal

Refer to the below link for all the methods that sp Modal provides and how you can pass parameters into spModal.

[https://developer.servicenow.com/print_page.do?release=quebec&category=null&identifier=SPModal-API&m...](https://developer.servicenow.com/print_page.do?release=quebec&category=null&identifier=SPModal-API&module=api)

## Related
- [[Angular provider]]
- [[Portals Events]]
- [[Using the Link Function in Service Portal Widgets]]

- [[Portal Methods]]
- [[Broadcast && emit && on]]
- [[ServiceNow – Service Portal]]