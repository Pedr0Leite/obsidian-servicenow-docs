---
aliases:
  - "Angular provider"
tags:
  - service-portal
  - angularjs
  - directives
  - widgets
---

# Angular provider

# Directives

Creating Custom Widgets>Directives

Directives in AngularJS are extended HTML attributes.  AngularJS has a number of built-in directives, all starting with *ng*, such as:

- *ngApp*
- *ngRepeat*
- *ngShow*
- *ngModel*
- *ngClick*

AngularJS allows user-defined directives to extend the functionality 
of HTML in applications.  The directives can attach a specified behavior
 to:

- *Element (<macro-name></macro-name>)*
- *Attribute (<div macro-name><div>)*
- *CSS Class (<div class="macro-name">)*
- *Comments (<!-- macro-name -->)*

## Create an Angular Provider

Directives are defined as Angular Providers.

![](https://developer.servicenow.com/app_store_learnv2_serviceportal_utah_createcustomwidgets_images_servicenow_sp_todoprovider.png)

In the main ServiceNow browser window, use the *All* menu to open **Service Portal > Angular Providers**.

Directive names use camelCase which must be referenced using kebab-case in HTML.  For example, a directive named *myDirective* is *<my-directive>* in HTML. In kebab-case:

- All letters are lowercase
- Spaces are replaced by hyphens
- Hyphens are inserted before letters which were uppercase

The *Client Script* field defines what the directive does.

In the example, the directive has several properties:

- ***template***: The HTML to render.
- ***restrict***: Specifies which methods can invoke the directive: *Element*, *Attribute*, *Class*, or *Comment*.
- ***replace***: Tells AngularJS to replace the element the directive is declared on.
- ***scope***: An object that contains a property for each isolate scope binding. This is typically used when making components reusable.
- ***link***: The link function is executed while attaching the template to the DOM.

Any valid [directive syntax](https://docs.angularjs.org/guide/directive) can be used in an Angular Provider.

## Related

- [[ServiceNow – Service Portal]]
- [[Using the Link Function in Service Portal Widgets]]
- [[AngularJS in SN]]
- [[Portal Methods]]