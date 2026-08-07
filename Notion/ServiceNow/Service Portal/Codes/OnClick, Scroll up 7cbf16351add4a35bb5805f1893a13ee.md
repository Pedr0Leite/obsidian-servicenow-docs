---
aliases:
  - "OnClick, Scroll up"
area: "Service Portal"
source: notion-export
tags:
  - service-portal
  - javascript
  - jquery
  - ui-scripts
  - snippets
---

# OnClick, Scroll up

OPTION I

```jsx
 $(document).ready(function() {
				//scroll up
    	 var lastScrollTop = 0;
     	 $(window).scroll(function() {
     	     var st = $(this).scrollTop();

     	     if (st < lastScrollTop) {
     	        $('html, body').scrollTop(0);
     	     }

     	     lastScrollTop = st;
     	 });

         $timeout(function() {
             $('.pointer').click(function() {
             //scroll down
                 var bottomOfPagePosition = $(document).height();
                 $('html, body').animate({
                    scrollTop: bottomOfPagePosition
                 }, 'fast');
                 return false; // Prevent default behavior of the click event
             });
         }, 500);
     });
```

OPTION II

```jsx
    $(document).ready(function() {
        $timeout(function() {
            $('.pointer').click(function() {
                $timeout(function() {
                    var element = document.getElementById("sc_category_page");
                    if (element)
                        element.scrollIntoView();
                    return false; // Prevent default behavior of the click event
                }, 250)
            });
        }, 500);
    });
```

## Related
- [[Engagement Messenger]]

- [[Codes]]
- [[ServiceNow – Service Portal]]