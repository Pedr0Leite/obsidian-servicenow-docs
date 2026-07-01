---
aliases:
  - "Ler anexos excel via BG"
tags:
  - background-scripts
  - attachments
  - excel-parser
  - glide-record
  - random-scripts
---

# Ler anexos excel via BG

var parser = new sn_impex.GlideExcelParser();
var attachment = new GlideSysAttachment();
var attachmentStream = attachment.getContentStream('sys_id_attachment_aqui');
parser.parse(attachmentStream);

var headers = parser.getColumnHeaders();

var header1 = headers[0];
var header14 = headers[14];

while(parser.next()) {
var row = parser.getRow();
gs.print('EXCEL ' + row[header1] + ' ' + row[header14]);

```
    var pedido = row[header1].toString();
    var equip = row[header14].toString();

    var gr = new GlideRecord('u_alm_equipment');
    gr.addEncodedQuery('serial_number=' + equip);
    gr.query();

    if (gr.next()) {
            gs.print('SERIAL ' + gr.getValue('serial_number'));
            gs.print('P. COMPRA ' + gr.getValue('u_purchase_order'));

            var grP = new GlideRecord('u_pedido_venda');
            grP.addEncodedQuery('number=' + pedido);
            grP.query();

            if (grP.next()) {
                gs.print('P. VENDA ' + grP.getValue('number'));

                    var grEquip = new GlideRecord('u_equipamento_vinculado');
                    grEquip.addEncodedQuery('parent=' + grP.getUniqueValue());
                    grEquip.addEncodedQuery('short_descriptionSTARTSWITHVincular ativo para o pedido nº:');
                    grEquip.query();
                    while (grEquip.next()) {
                        gs.print('TASK VINCULO ' + grEquip.getDisplayValue());
                        gs.print('P. COMPRA NA TASK ' + grEquip.u_equipament);

                    }
            }
    }
    gs.print('');

```

}

## Related

- [[Random Scripts]]
- [[Fun with array methods!]]
- [[Create translation for an existing choice]]
- [[Confidential Attachments]]