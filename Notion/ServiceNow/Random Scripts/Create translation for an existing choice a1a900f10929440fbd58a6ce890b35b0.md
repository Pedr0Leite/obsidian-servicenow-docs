---
aliases:
  - "Create translation for an existing choice"
area: "Random Scripts"
source: notion-export
tags:
  - translations
  - sys-choice
  - background-scripts
  - glide-record
  - random-scripts
---

# Create translation for an existing choice

```jsx
var targetLang = "en";
var originalLang = "pt";

var choice = new GlideRecord('sys_choice');
choice.addEncodedQuery("name=^language=" + originalLang);
choice.query();
while (choice.next()) {
    var checkChoiceOtherLang = new GlideRecord('sys_choice');
    checkChoiceOtherLang.addQuery("language", targetLang);
    checkChoiceOtherLang.addQuery("value", choice.value);
    checkChoiceOtherLang.query();

    var checkIfOtherLangExist = checkChoiceOtherLang.getRowCount();
    if(checkIfOtherLangExist == 0){
        var choiceOtherLang = new GlideRecord('sys_choice');
        choiceOtherLang.initialize();
        choiceOtherLang.dependent_value = choice.dependent_value;
        choiceOtherLang.sequence = choice.sequence;
        choiceOtherLang.inactive = choice.inactive;
        choiceOtherLang.hint = choice.hint;
        choiceOtherLang.name = choice.name;
        choiceOtherLang.language = targetLang;
        choiceOtherLang.label = choice.label;
        choiceOtherLang.value = choice.value;
        choiceOtherLang.element = choice.element;
        choiceOtherLang.dependent_value = choice.dependent_value;
        choiceOtherLang.insert();
    }
}
```

## Related

- [[Random Scripts]]
- [[Fun with array methods!]]
- [[Ler anexos excel via BG]]