---
aliases:
  - "Prompt Guideance"
area: "Knowledge Base Articles"
source: notion-export
tags:
  - knowledge-base
  - ai
  - genai
  - prompt-engineering
---

# Prompt Guideance

When I first started testing GenAI, I asked it to grade something from 1 to 10. The responses I got included 2, 3, 5… and even 15!? That one really threw me off. Turns out, the issue was that I wasn't being clear enough in my prompt.

When ServiceNow released its Prompting Guidance, it all made sense to me—especially after my own missteps trying to get GenAI to respond the way I expected. Below are ServiceNow’s principles for prompt guidance:

The LLM is smart, but it is NOT a mind reader - **learn to ‘speak’ the language to get better results:**

1. Write clear, specific, and concise prompt
2. Specify triggers and conditions
3. Specify the expected outcome and context
4. Include necessary details like task requirements, specific function names, and any constraints
5. Specify timeframes and date ranges
6. Prompt for one component part at a time
7. Always validate the response returned by the LLM is correct

Weak vs. Strong prompts

[MichaelFry1_0-1749732214676.png](https://www.servicenow.com/community/image/serverpage/image-id/448308iFF093DE177285948/image-size/medium?v=v2&px=400)

More examples…

| Weak | Strong |
| --- | --- |
| // close child records when the process ends | // close all child Task records when the parent Task is closed |
| // get the count of user cases | // get the count of currently open Cases for the current user with an AJAX call |
| // create a related list to show the records opened by this user
 | // create a related list on the Incident record to show all Incidents opened by the same caller
 |
| // pull all the related customer information when an Incident is created
 | // create a JavaScript function that uses a GlideRecord query to build an array of Customer sys_id values, and call the function from the condition builder in the Incident table
 |
| // replace social security numbers with #
 | //check the short description and description in the current record for any social security numbers, and replace the SSN information with '###'
 |
| //check for open cases that have not been updated in 3 months
 | //check for open HR cases that have not been updated in 3 months
 |

The bottom line, with a little bit of trial and error, you will learn how to write your strong prompts.

Thanks for reading.

## Related

- [[AI]]
- [[Knowledge Base Articles]]
- [[GenAI]]
- [[Now Assist]]