---
aliases:
  - "create_translations"
area: "Scripts"
source: custom
tags:
  - translations
  - localization
  - glide-record
  - i18n
  - sys-choice
  - scripts
---

# create_translations

Bulk-inserts translation records across every ServiceNow translation table from one `{lang: text}` map: `sys_translated` (field-level), `sys_translated_text` (catalog item title), `sys_choice` (dependent choice list), `sys_ui_message` (UI messages), and `sys_documentation` (field help). Handy scaffold when a catalog item or choice list needs to ship with all supported languages at once — note `zh` needs to be `zt` for Traditional Chinese in some tables.

```javascript
//Example from the app
var options = { 
es: 'Esto es una prueba',
fr: "’est un test",        
ru: 'Это проверка',
sl: 'To je preskus',        
uk: 'Це перевірка',
zh: '这是个测试',
ar: 'هذا اختبار',
de: 'Dies ist ein Test',    
id: 'Ini adalah tes',       
sr: 'Ovo je proba',
ms: 'Ini adalah satu ujian',
pl: 'To jest test',
bg: 'Това е тест',
it: 'Questo è un test',     
ro: 'Acesta este un test',  
sk: 'Toto je skúška',       
nl: 'Dit is een test',      
pt: 'Isso é um teste',      
vi: 'Đây là bài kiểm tra',  
hu: 'Ez egy próba',
cs: 'Tohle je test',        
en: 'This is a test' } 


  //zh needs to be zt
//For the Translations tables
//FIELDS
  Object.keys(options).forEach(function(lang){
      if(lang != 'en'){
            var translation = new GlideRecord('sys_translated');
            translation.initialize();
            translation.setValue('name', 'question');
            translation.language = lang;
            translation.value = options['en'];
            translation.label = options[lang];
            translation.element = 'question_text'; //or question_text || title || name
            translation.insert();
    }
});
var catalogItem = '';
//TITLES
Object.keys(options).forEach(function(lang){
          var translation = new GlideRecord('sys_translated_text');
          translation.initialize();
          translation.documentkey = catalogItem;
          translation.fieldname = 'short_description'; //short_description || name
          translation.language = lang;
          translation.value = options[lang];
          translation.tablename = 'sc_cat_item';
          translation.insert();
});

//For the Choice table list
var table = 'incident_task';
var element = 'u_subcategory';
var dependantValue = 'Workplace';
var sequence = '8';

Object.keys(options).forEach(function(lang){
  var translation = new GlideRecord('sys_choice');
  translation.initialize();
  translation.name = table;
  translation.dependent_value = dependantValue;
  translation.language = lang;
  translation.value = options['en'];
  translation.label = options[lang];
  translation.element = element;
  translation.sequence = sequence;
  translation.insert();
});


//For Message table
Object.keys(options).forEach(function(lang){
  var translation = new GlideRecord('sys_ui_message');
  translation.initialize();
  translation.key = options['en'];
  translation.language = lang;
  translation.message = options[lang];
  translation.insert();
});

var obj = {
  'Priority': 'prioridade',
  'state': 'estado'
  }
  

Object.keys(options).forEach(function(label){


//For Documentation table (aka for BO fields)
var documentation = new GlideRecord('sys_documentation');
    documentation.initialize();
    documentation.help = '';
    documentation.plural = '';
    documentation.url_target = '';
    documentation.hint = '';
    documentation.name = '';
    documentation.language = '';
    documentation.label = '';
    documentation.url = '';
    documentation.element = '';
    documentation.insert();

});
```

## Related

- [[Create translation for an existing choice]]
- [[Now Assist Q&A using Dynamic Translation]]
