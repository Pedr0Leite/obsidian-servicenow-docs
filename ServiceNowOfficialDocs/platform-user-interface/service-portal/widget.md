### Widget

A widget is a superset of an [Angular directive](https://docs.angularjs.org/guide/directive) that is tightly coupled to a server-side JavaScript code block powered by the Rhino engine under the ServiceNow platform.

Since widgets are `read-only` to benefit from future updates, you can't update their code. If you need to make major changes,
*clone* the widget and give it another `name` and `id`.

### Widget Instance
Once you drop a widget into a column using the Service Portal Designer it will create a widget instance.
A widget instace is a reference to a widget that contains: location, properties and CSS especific for that instance. A widget used multiple times in the same page, will use multiple instances.

![Widget Instance](/assets/widget/widget-instance.png)


***Learn more:***

  - [HTML](widget_html.md)
  - [Client Script](widget_client_script.md)
  - [Server Script](widget_server_script.md)  
  - [Dependencies](widget_dependencies.md)
  - [CSS/SCSS](css.md)
  - [Embedded Widgets](widget_embedded.md)
  - [Server Script APIs](widget_server_script_apis.md)
  - [Instances](widget_instances.md)
  - [Options](widget_options.md)

## Related

- [[widget_html|Widget HTML]]
- [[widget_client_script|Widget Client Script]]
- [[widget_server_script|Widget Server Script]]
- [[widget_dependencies|Widget Dependencies]]
- [[css|Service Portal CSS]]
- [[widget_embedded|Embedded Widgets]]
- [[widget_server_script_apis|$sp API (Server Script APIs)]]
- [[widget_instances|Widget Instances]]
- [[widget_options|Widget Options]]
- [[widget_css|Widget CSS]]
- [[service_portal|Service Portal]]
- [[widget-dev-guide|Developing custom widgets]]
- [[general-guidelines-developing-widgets|General guidelines for developing widgets]]
- [[create-new-widget|Create a new widget]]
- [[widget-api-reference|Widget API reference]]
