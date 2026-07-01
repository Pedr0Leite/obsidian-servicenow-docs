---
aliases:
  - "The Secrets of GlideDateTime"
tags:
  - glide-date-time
  - scripting
  - date-formatting
  - glide-schedule
---

# The Secrets of GlideDateTime

Working with Dates in ServiceNow can be quite challenging.

In this Blog Series, I will list some of the common mistakes and provide some secrets to using GlideDateTime that you might not be aware of.

### **Topics**

### [**Date Formatting**](https://www.servicenow.com/community/in-other-news/the-secrets-of-glidedatetime/ba-p/2290801#dateFormatting)

### [**Scheduled Tasks using Date GlideDate**](https://www.servicenow.com/community/in-other-news/the-secrets-of-glidedatetime/ba-p/2290801#scheduledTasks)

### [**Calculating Business Duration In Schedule**](https://www.servicenow.com/community/in-other-news/the-secrets-of-glidedatetime/ba-p/2290801#calcBusinessDuration)

### **Date Formatting**

Date formatting is actually incredibly easy in ServiceNow. I have seen lots of posts with complex code to format dates into day names, month names and everything in between - often with 10's of 100's of lines of code. But it doesn't have to be this hard! It is actually very easy. You can do all your formatting using one function, provided OOTB!

[GlideDateTime](https://developer.servicenow.com/app.do#!/api_doc?v=jakarta&id=r_ScopedGlideDateTimeSetDisplayValue_String_value_String_%E2%80%A6)

**Example**

```jsx
var gdt = new GlideDateTime("2011-02-02 12:00:00");
gdt.setDisplayValue("20-5-2011 12:00:00", "dd-MM-yyyy HH:mm:ss"); //uses current user session time zone (US/Pacific)
gs.print(gdt.getValue());
```

setDisplayValue() uses the [SimpleDateFormat](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) (Java Platform SE 7 ) , which is fully documented!

### **Get current date in any format (GMT)**

**Current Date/Time:** 16th September 2020, 08:26:22 AM (AWST +8)

```jsx
var gDate = new GlideDate();
var formattedDate = (gDate.getByFormat('yyyy-MM-dd HH:mm:ss'));
gs.print(formattedDate);
```

```markup
2020-09-16 00:26:22
```

### **Get current date in any format (Local)**

**Current Date/Time:** 16th September 2020, 08:26:22 AM (AWST +8)

```jsx
var gdt = new GlideDateTime();
var gd = new GlideDate();
gd.setValue(gdt.localTime);
gs.print(gd.getByFormat("yyyy-MM-dd HH:mm:ss"));
```

```markup
2020-09-16 08:26:22
```

### **Get the hour of a given date (Local)**

**Current Date/Time:** 16th September 2020, 08:26:22 AM (AWST +8)

```jsx
var gdt = new GlideDateTime(); // datetime of your choosing in here
var gd = new GlideDate();
gd.setValue(gdt.localTime);
var hour = parseInt(gd.getByFormat("HH"));
gs.print(hour)
```

```markup
8
```

### **Converting Formats**

**Incoming Format:** 20171216 01:23:45

**Simple Format:** yyyyMMdd HH:mm:ss

```jsx
var date = '20171216 01:23:45';
var simpleDateFormat = 'yyyyMMdd HH:mm:ss';
var gdt = new GlideDateTime();
gdt.setDisplayValue(date,simpleDateFormat);
gs.print(gdt.getDisplayValue());
```

```markup
16-12-2017 01:23:45
```

### **Converting Day and Month Names with AM/PM**

**Incoming Format:** Friday, August 18, 2017 8:00 AM

**Simple Format:** E, MMMM dd, yyyy K:mm a

```jsx
var newDate = 'Friday, August 18, 2017 8:00 AM';
var gdt = new GlideDateTime();
gdt.setDisplayValue(newDate, "E, MMMM dd, yyyy K:mm a");
var dateTimeForField = gdt.getDisplayValue();
gs.print(dateTimeForField);
```

```markup
2017-08-18 08:00:00
```

### **Getting the Name and Day of Month**

**Incoming Format:** new GlideDateTime();

**Simple Format:** EEEE dd MMMMM

```jsx
var gDate = new GlideDateTime().getDate();
gs.print(gDate.getByFormat('EEEE dd MMMMM'));
```

```markup
Thursday 14 December
```

### **Add days to any format**

**Incoming Format:** 10 Jul 2018 12:30:00

**Simple Format:** EEEE dd MMMMM

```jsx
var date = '10 Jul 2018 12:30:00';
var simpleDateFormat = 'dd MMMM yyyy HH:mm:ss'; // Simple Date Time format
var gdt = new GlideDateTime();
gdt.setDisplayValue(date,simpleDateFormat); //Set time using current TZ
gs.addInfoMessage(gdt.getDisplayValue()); // Output time in current TZ
```

```markup
2018-07-10 12:30:00 PM
```

Once your GlideDateTime object has the correct time, you can manipulate it as you need.

```jsx
gdt.addDays(7);
gs.addInfoMessage(gdt.getDisplayValue());
```

```markup
2018-07-17 12:30:00 PM
```

And back again to your original format, with the added 7 days

```jsx
var gd = gdt.getLocalDate();
var gt = gdt.getLocalTime();
```

gs.addInfoMessage(gd.getByFormat('dd MMM yyyy') + gt.getByFormat(' HH:mm:ss'));

```markup
17 Jul 2018 12:30:00
```

### **Scheduled Tasks using Date GlideDate**

It is a fairly common requirement - generate a task every day of the week, excluding the weekend. If you do a quick search for this, you will see lots of versions of the code below which uses Date():

```jsx
(function doNotUseThisCode() {
	var now = new Date();
	var day = now.getDay();
	var result = false;
	if(day != 0 && day != 6) {
		result = true;
	}
	return result;
})();
```

Please do not use this code!

**It is wrong!**

If you run the code below (run from a Perth Instance in Australia)

```jsx
gs.addInfoMessage(new Date().toString());
gs.addInfoMessage(new GlideDateTime().getDisplayValue());
```

You get the following output:

```markup
Tue Jan 02 2018 05:38:49 GMT-0800 (PST)
02-01-2018 21:38:49
```

What is going on here?

The output of Date().toString() is not using your TimeZone!

now.getDay() is getting the day in PST!

I am from Perth, Australia (GMT +

![:smiling_face_with_sunglasses:](https://www.servicenow.com/community/s/html/@F3C66D603EE9BB084475D0CBC0E5EF97/emoticons/1f60e.png)

which means that my Task will spawn on Saturday and not on Monday because it is still Friday and Sunday retrospectively in PST.And you can bet that is what happened when the code went into Production...

![:confused_face:](https://www.servicenow.com/community/s/html/@12E8E9F937AE499E5A660BBA71BBF4AF/emoticons/1f615.png)

Let's utilize what we learned from Date Formatting for a more readable and TimeZone agnostic solution using GlideDate instead:

```jsx
(function isWeekday() {

	var isWeekday;
	var gDate = new GlideDate(); //Uses your Timezone!
	var day = gDate.getByFormat('EEEE') + ""; // Gets name of day, retruns Java object
	switch(day) {
		case "Saturday":
		case "Sunday":
			isWeekday = false;
		break;
		default:
			isWeekday = true;
	}

	return isWeekday;

})();
```

### **Calculating Business Duration In Schedule**

There are a few different ways to do this, either through the SLA API or GlideSchedule.

GlideSchedule seems to be the cleanest way:

```jsx
function getBusinessDuration(scheduleID, gdtStart,gdtEnd) {
    var sched = new GlideSchedule(scheduleID);
   return sched.duration(gdtStart, gdtEnd).getDurationValue();
}
```

Let's assume our Schedule has a business day of 11 hours, Monday to Friday.

We would, therefore, expect the duration of a calendar week in business hours to be 55.

```jsx
var oneWeekAgo = new GlideDateTime();
oneWeekAgo.addDays("-7");

getBusinessDuration(
  'c2f96f156fc1750029ca5e0d5d3ee427',
  oneWeekAgo,
  new GlideDateTime()
);
```

```markup
2 07:00:00
```

There are 24 hours in each day.

2 days = 48 hours

48 + 7 = 55 hours

## Related

- [[Server and Client Side Scripts]]
- [[Script include Advance structure - Inheritance]]
- [[SLA]]