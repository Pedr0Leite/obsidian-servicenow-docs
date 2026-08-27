---
aliases:
  - "amountToString"
area: "Scripts"
source: custom
tags:
  - javascript
  - number-formatting
  - localization
  - scripting
  - scripts
---

# amountToString

Converts a numeric amount into its written-out word form (e.g. `123.35` → "cento e vinte e três euros e trinta e cinco cêntimos"), with both a Portuguese and an English implementation. Plain JavaScript — no ServiceNow API calls — useful for amount-in-words fields on financial forms/PDFs.

```javascript
    //PORTUGUESE
   // actual  conversion code starts here

   var ones = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove'];
   var dezenas = ['', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa'];
   var teens = ['','onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove'];
   var centenas = ['','c', 'duz', 'trez', 'quatroc', 'quinh', 'seisc', 'setec', 'oitoc', 'novec'];


   function PTconvert_millions(num) {
     if (num >= 1000000) {
        if(PTconvert_millions(Math.floor(num / 1000000)) == 'um'){
            return PTconvert_millions(Math.floor(num / 1000000)) + " milhão " + PTconvert_thousands(num % 1000000);

        }else{
            return PTconvert_millions(Math.floor(num / 1000000)) + " milhões " + PTconvert_thousands(num % 1000000);
        }

     } else {
       return PTconvert_thousands(num);
     }
   }

   function PTconvert_thousands(num) {
     if (num >= 1000) {
        if(PTconvert_hundreds(Math.floor(num / 1000)) == 'um'){
            return "mil " + PTconvert_hundreds(num % 1000);

        }else{
            return PTconvert_hundreds(Math.floor(num / 1000)) + " mil " + PTconvert_hundreds(num % 1000);

        }

     } else {
       return PTconvert_hundreds(num);
     }
   }

   function PTconvert_hundreds(num) {
    if(num == 100){
        return 'cem';
    } else if ( num > 99) {
        if(centenas[Math.floor(num / 100)] == 'c'){
            return centenas[Math.floor(num / 100)] + "ento " + PTconvert_dezenas(num % 100);

        }else{

            return centenas[Math.floor(num / 100)] + "entos " + PTconvert_dezenas(num % 100);

        }
     } else {
       return PTconvert_dezenas(num);
     }
   }

   function PTconvert_dezenas(num) {
     if (num < 10){
         return ones[num];

     } else if(num == 10){
        return dezenas[1];

    } else if(num > 10 && num < 20){
         return teens[num - 10];

     } else {
       return dezenas[Math.floor(num / 10)] + "" + ones[num % 10];
     }
   }

   function PTconvert(num) {
     if (num == 0) return "zero";
     else return PTconvert_millions(num);
   }

   function PTconvertDec(num){
    return PTconvert(num)
   }

   //testing code begins here

   function main(number) {

    var parts = number.toString().split(".");
    var integerPart = parts[0];
    var decimalPart = parts[1];

    if(parts.length == 1){
        return PTconvert(integerPart) + " euros";
    }else{
        return PTconvert(integerPart) + " euros e " + PTconvertDec(decimalPart) + " cêntimos";

    }

    }
//1.040.501
   console.log(main(123.35));
//1.040.501
//    console.log(main(10000000000));

//ENGLISH
// actual  conversion code starts here

var ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
var tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];
var teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'];

function convert_millions(num) {
  if (num >= 1000000) {
    return convert_millions(Math.floor(num / 1000000)) + " million " + convert_thousands(num % 1000000);
  } else {
    return convert_thousands(num);
  }
}

function convert_thousands(num) {
  if (num >= 1000) {
    return convert_hundreds(Math.floor(num / 1000)) + " thousand " + convert_hundreds(num % 1000);
  } else {
    return convert_hundreds(num);
  }
}

function convert_hundreds(num) {
  if (num > 99) {
    return ones[Math.floor(num / 100)] + " hundred " + convert_tens(num % 100);
  } else {
    return convert_tens(num);
  }
}

function convert_tens(num) {
  if (num < 10) return ones[num];
  else if (num >= 10 && num < 20) return teens[num - 10];
  else {
    return tens[Math.floor(num / 10)] + " " + ones[num % 10];
  }
}

function convert(num) {
  if (num == 0) return "zero";
  else return convert_millions(num);
}

//end of conversion code

//testing code begins here

function main() {
  var cases = [0, 1, 2, 7, 10, 11, 12, 13, 15, 19, 20, 21, 25, 29, 30, 35, 50, 55, 69, 70, 99, 100, 101, 119, 510, 900, 1000, 5001, 5019, 5555, 10000, 11000, 100000, 199001, 1000000, 1111111, 190000009];
  for (var i = 0; i < cases.length; i++) {
    console.log(cases[i] + ": " + convert(cases[i]));
  }
}

main();
```

## Related

- [[Fun with array methods!]]
- [[Random Scripts]]
