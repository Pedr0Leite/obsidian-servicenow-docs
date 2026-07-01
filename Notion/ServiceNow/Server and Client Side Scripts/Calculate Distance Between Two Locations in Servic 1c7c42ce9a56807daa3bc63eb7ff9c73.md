---
aliases:
  - "Calculate Distance Between Two Locations in Servic"
tags:
  - script-include
  - glide-record
  - scripting
  - cmn-location
---

# Calculate Distance Between Two Locations in ServiceNow (without an API call!

I'm gonna keep this really quick --

If you need to calculate the distance between two Location records in the `cmn_location` table in ServiceNow, as long as both of those locations have latitude and longitude values, you can do so using the script below!

Usage examples at the bottom.

You can turn these functions into methods of a Script Include if you like; whatever boats your float, mate.

EDIT 3/26/25: Nevermind, I turned it into a Script Include for you. 😎

This is just for calculating raw distance; it's not for calculating actual driving distance or "drive time"/duration.

The main value for something like this is ruling things out. Like for example, if you're attempting to determine the optimal path from nodes A (starting point), B, and C, you could do GIS calls for all of that, but it would be expensive.

However, if you use the Haversine formula, you can identify that location B is 2 miles from A, whereas C is 50 miles from A. Therefore, you can assume that the routing will be A > B > C.

Adding more nodes further illustrates the point. You may be able to determine that A, B, C, and D are all within 5 miles of the starting point and each other, but location E is 10x that.

Therefore, you can optimize the location API queries and save yourself some spend.

Maybe.

Or use it however you want; I'm not your dad.

Unless I am. In this case, FINISH YOUR HOMEWORK!

var dc = new DistanceCalculator();
dc._exampleUsage();

var DistanceCalculator = Class.create();
DistanceCalculator.prototype = {
initialize : function(distanceUnits, roundDigits) {
this.distanceUnits = distanceUnits || 'km';
this.roundDigits = roundDigits || 0;
},

```
/**
 *
 * @param {String} originLocationID - The sys_id of the Location record for the origin point.
 * This should be the sys_id of a valid record in the cmn_location table.
 *
 * @param destinationLocationID - The sys_id of the Location record for the destination point.
 * This should be the sys_id of a valid record in the cmn_location table.
 *
 * @param {('km'|'miles'|'mile'|'mi'|'yards'|'yd'|'inches'|'in'|'feet'|'ft'|'meters'|'m'|'centimeters'|'cm'|'millimeters'|'mm'|'nautical miles'|'nm')} [distanceUnits='km']
 *     - The units of the distance. Default is 'km'.
 *
 * @param {number} [roundDigits=] - Number of decimal places to round the result to.
 * The default if this argument is not specified is to not round the result at all, and use the
 *  math engine's default. .
 * The maximum value for roundDigits is 15 (the maximum number of decimal places that
 *     JavaScript
 *  can accurately represent), but it is recommended to keep it below 10 to avoid floating
 *     point
 *  errors caused by the limitations of the weird Mozilla Rhino Java-based JavaScript engine.
 *
 * @returns {{origin: {name: string, latitude: number, longitude: number}, destination: {name:
 *     string, latitude: number, longitude: number}, distance: {value: number, units: string},
 *     has_errors: boolean, errors: *[]}} - An object containing the origin and destination
 *     location data, the distance between the two locations, and any errors that occurred
 *     during the calculation.
 */
distanceBetweenLocationsBySysID : function(originLocationID, destinationLocationID, distanceUnits, roundDigits) {

	distanceUnits = distanceUnits ? distanceUnits : this.distanceUnits;
	roundDigits = roundDigits ? roundDigits : this.roundDigits;

	var distanceNum = 0;
	var grLocation = new GlideRecord('cmn_location');
	var locationData = {
		'origin' : {
			'name' : '',
			'latitude' : 0,
			'longitude' : 0
		},
		'destination' : {
			'name' : '',
			'latitude' : 0,
			'longitude' : 0
		},
		'distance' : {
			'value' : 0,
			'units' : ''
		},
		'has_errors' : false,
		'errors' : []
	};

	grLocation.addQuery('sys_id', 'IN', [originLocationID, destinationLocationID]);
	grLocation.setLimit(2);
	grLocation.query();

	while (grLocation.next()) {
		if (grLocation.getUniqueValue() === originLocationID) {
			locationData.origin.name = grLocation.getValue('name');
			locationData.origin.latitude = Number(grLocation.getValue('latitude'));
			locationData.origin.longitude = Number(grLocation.getValue('longitude'));
		} else if (grLocation.getUniqueValue() === destinationLocationID) {
			locationData.destination.name = grLocation.getValue('name');
			locationData.destination.latitude = Number(grLocation.getValue('latitude'));
			locationData.destination.longitude = Number(grLocation.getValue('longitude'));
		}
	}

	if (
		!locationData.origin.latitude ||
		!locationData.origin.longitude ||
		!locationData.destination.latitude ||
		!locationData.destination.longitude
	) {
		locationData.has_errors = true;
		locationData.errors.push('One or both of the Location records are missing latitude and/or longitude values.');

		return locationData;
	}

	distanceNum = this.calculateDistanceBetweenCoords(
		locationData.origin.latitude,
		locationData.origin.longitude,
		locationData.destination.latitude,
		locationData.destination.longitude,
		distanceUnits,
		roundDigits
	);

	locationData.distance.value = distanceNum;
	locationData.distance.units = distanceUnits;

	return locationData;
},

/**
 * Calculates the distance between two GPS coordinates using the Haversine formula.
 *
 * Limitations include the fact that nature is inconvenient, that the Earth is not a perfect
 *  sphere but an oblate spheroid which is a very fun thing to type, that elevation changes are
 *  not accounted for in this calculation, and the formula is not designed to handle points
 * that
 *  are more than half the circumference of the Earth apart (how would that even be possible?)
 *
 * Result accuracy may be impacted by the limitations of floating point arithmetic in both Java
 *  and JavaScript, by the limitations of the Haversine formula itself, by severe differences
 * in
 *  elevation between the two points for which the distance is being calculated, and by the
 *  shape of the Earth itself.
 *
 * Stupid nature, always ruining math for everyone.
 *
 * @param {number} lat1 - Latitude of the first coordinate.
 *
 * @param {number} lon1 - Longitude of the first coordinate.
 *
 * @param {number} lat2 - Latitude of the second coordinate.
 *
 * @param {number} lon2 - Longitude of the second coordinate.
 *
 * @param {('km'|'miles'|'mile'|'mi'|'yards'|'yd'|'inches'|'in'|'feet'|'ft'|'meters'|'m'|'centimeters'|'cm'|'millimeters'|'mm'|'nautical miles'|'nm')} [distanceUnits='km']
 *     - The units of the distance. Default is 'km'.
 *
 * @param {number} [roundDigits=] - Number of decimal places to round the result to.
 * The default if this argument is not specified is to not round the result at all.
 * The maximum value for roundDigits is 15 (the maximum number of decimal places that
 *     JavaScript
 *  can accurately represent), but it is recommended to keep it below 10 to avoid floating
 *     point
 *  errors caused by the limitations of the weird Mozilla Rhino Java-based JavaScript engine.
 *
 * @returns {number} - The distance between the two coordinates in the specified units.
 *
 * @throws {Error} - If latitude and longitude values are not numbers or if invalid distance
 *     units are provided.
 *
 * @example
 * var lat1 = 45.58568758810709, lon1 = -122.47954663934604;
 * var lat2 = 45.605901771569044, lon2 = -122.56087319825683;
 * var distanceKM = calculateDistanceBetweenCoords(lat1, lon1, lat2, lon2, 'km', 3); // Returns
 *     6.715 var distanceMI = calculateDistanceBetweenCoords(lat1, lon1, lat2, lon2, 'mi', 3);
 *     // Returns 4.172 console.log('Distance: ' + distanceKM + ' km (' + distanceMI + ' mi)');
 */
calculateDistanceBetweenCoords : function(
	lat1,
	lon1,
	lat2,
	lon2,
	distanceUnits,
	roundDigits
) {

	distanceUnits = distanceUnits ? distanceUnits : this.distanceUnits;
	roundDigits = roundDigits ? roundDigits : this.roundDigits;

	var distance, roundMultiplier, latDistanceDegrees, lonDistanceDegrees, sqHalfChordLength,
		angularDistanceRads;
	var earthRadiusKM = 6371; // Radius of the Earth in kilometers

	if (typeof lat1 !== 'number' || typeof lon1 !== 'number' || typeof lat2 !== 'number' || typeof lon2 !== 'number') {
		throw new Error('Latitude and longitude values must be numbers.');
	}
	if (typeof distanceUnits !== 'undefined' && typeof distanceUnits !== 'string') {
		throw new Error(
			'Distance units must be a string containing one of the enumerated values: "km", ' +
			'"miles", "yards", "inches", "feet", "meters", "centimeters", "millimeters", ' +
			'or "nautical miles".'
		);
	}
	if (
		roundDigits && roundDigits !== 0 &&
		(typeof roundDigits !== 'number' || roundDigits < 0 || roundDigits > 15)
	) {
		throw new Error('roundDigits must be a number between 0 and 15, if specified.');
	}

	latDistanceDegrees = degreesToRadians(lat2 - lat1);
	lonDistanceDegrees = degreesToRadians(lon2 - lon1);

	/*
			~Meet the haversine formula~
		I wish that I'd known about it around nine hundred hours ago when I started working on this
		 calculation instead of sleeping.
		I mean, I could've literally just googled "how to do [the thing I'm doing]" and found *some*
		 version of this formula in 5 seconds, probably.
		But, no. Turns out, I'm a complete dingus, and I ended up completely reinventing it from
		 scratch. It was only when I was troubleshooting my code to figure out why it kept barfing
		 when one of the points was in the southern hemisphere that I finally stumbled upon the
		 haversine formula which is specifically designed to handle this exact situation, and I
		 was like, "Oh, that's what I'm trying to do... but better."
		Turns out that it also solves the exact problem I was having, and is way more elegant than
		 my solution was. ಠ_ಠ

		But hey, at least I learned something new - and now you get to as well.
		Unless you didn't read this comment.
		But you wouldn't just copy and paste code without reading the comments, would you?
		That would be a terrible idea.
		You could be copying and pasting anything.
		Like, this code could call a function that sends your social security number to North Korea.

		sendToNorthKorea(yourSocialSecurityNumber);

		See? You wouldn't want that.
		Anyway, here's the haversine formula.
		It does not send your social security number to North Korea.
		It calculates the distance between two points on the surface of a sphere.
		Why a sphere?
		Turns out, the Earth is a sphere; kinda.
		Who knew?
		Yeah, I know, elevation is a thing; but for short distances, elevation changes are mostly
		 negligible; and for long distances, the average elevation changes come close to either
		 cancelling out or being negligible at least as the emu flies.
		We're not calculating driving distance here, just straight-line distance (though not in a
		 Euclidian sense, because the Earth is a sphere(oid) - have I mentioned that?)

		The formula is based on the law of haversines, which relates the sides and angles of
		 triangles on the surface of a sphere.
		The formula is: a = sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlon/2)
		c = 2 * atan2( √a, √(1−a) )
		d = R * c

		Where:
		Δlat = lat2 - lat1
		Δlon = lon2 - lon1
		a is the square of half the chord length between the points
		c is the angular distance in radians
		d is the distance between the two points
		R is the earth's radius

		The atan2 function returns a value in the range of -π to π radians and is used to calculate
		 the angle between the x-axis and a specific point.

		Anyway, NOW you can safely copy and paste this code without understanding it.
		I sure as hell don't.
	*/
	sqHalfChordLength = Math.sin(latDistanceDegrees / 2) * Math.sin(latDistanceDegrees / 2) +
		Math.cos(degreesToRadians(lat1)) * Math.cos(degreesToRadians(lat2)) *
		Math.sin(lonDistanceDegrees / 2) * Math.sin(lonDistanceDegrees / 2);
	angularDistanceRads = 2 * Math.atan2(Math.sqrt(sqHalfChordLength), Math.sqrt(1 - sqHalfChordLength));

	distance = earthRadiusKM * angularDistanceRads;

	// Default to kilometers;
	distanceUnits = (typeof distanceUnits === 'string') ? distanceUnits.toLowerCase() : 'km';

	// Convert the distance to the specified units
	if (distanceUnits === 'mi' || distanceUnits === 'miles' || distanceUnits === 'mile') {
		distance = convertKMToMiles(distance);
	} else if (distanceUnits === 'yd' || distanceUnits === 'yards') {
		// Convert to miles, then to feet, then to yards, because miles are neatly divisible
		// into feet, and feet are neatly divisible into yards, but kilometers are not.
		distance = convertKMToMiles(distance) * 1760;
	} else if (distanceUnits === 'in' || distanceUnits === 'inches') {
		// Convert to miles, then to feet, then to inches, because miles are neatly divisible
		// into feet, and feet are neatly divisible into inches, but kilometers are not.
		distance = convertKMToMiles(distance) * 5280 * 12;
	} else if (distanceUnits === 'ft' || distanceUnits === 'feet') {
		// Convert to miles, then to feet, because miles are neatly divisible into feet, but
		//  kilometers are not.
		distance = convertKMToMiles(distance) * 5280;
	} else if (distanceUnits === 'm' || distanceUnits === 'meters') {
		distance *= 1000;
	} else if (distanceUnits === 'cm' || distanceUnits === 'centimeters') {
		distance *= 100000;
	} else if (distanceUnits === 'mm' || distanceUnits === 'millimeters') {
		distance *= 1000000;
	} else if (distanceUnits === 'nm' || distanceUnits === 'nautical miles') {
		distance *= 0.539957;
	} else if (distanceUnits !== 'km' && distanceUnits !== 'kilometers') {
		// Invalid distance units - throw an error.
		throw new Error(
			'Invalid distance units. Please specify one of the following: enumerated values for ' +
			'the distanceUnits parameter: \\n' +
			'"km", "miles", "yards", "inches", "feet", "meters", "centimeters", "millimeters", ' +
			'or "nautical miles".'
		);
	}

	if (roundDigits) {
		//round distance to specified number of decimal places, without adding additional
		// unnecessary leading or trailing zeros
		roundMultiplier = Math.pow(10, roundDigits);
		distance = Math.round(distance * roundMultiplier) / roundMultiplier;
	}

	/*
		Fun fact, SN's rounding is different from the standard rounding in JavaScript.
		It's probably a super lame Java-related issue, but check this out:

		//Example code:
		function doRoundingOkay(numToRound, roundDigits) {
		  var roundMultiplier = Math.pow(10, roundDigits);
		  var roundedResult = Math.round(numToRound * roundMultiplier) / roundMultiplier;
		  return roundedResult;
		}

		var numToRound = 1.234567;
		gs.debug('3 decimal places: ' + doRoundingOkay(numToRound, 3)); //1.235 - Cool
		gs.debug('10 decimal places: ' + doRoundingOkay(numToRound, 10)); //1.234567 - Good, since the original number had <10 digits of precision.
		gs.debug('18 decimal places: ' + doRoundingOkay(numToRound, 18)); //1.234567 - Okay, rad
		gs.debug('19 decimal places: ' + doRoundingOkay(numToRound, 19)); //0.9223372036854776 - wait wtf...
		gs.debug('35 decimal places: ' + doRoundingOkay(numToRound, 22)); //0.0009223372036854776 - ???
		gs.debug('35 decimal places: ' + doRoundingOkay(numToRound, 35)); //9.223372036854776e-17 - WHAT? HOWWW??

		//What if we change the number to round?
		gs.debug('19 decimal places, new number: ' + doRoundingOkay(654321.789, 19)); //0.9223372036854776 - BRO WTF HOW

		//What if we just round an integer - a straight-up, normal-ass integer that shouldn't need rounding at all.
		gs.debug('Integer rounded to 19 decimal places: ' + doRoundingOkay(123, 19)); //0.9223372036854776 - I AM CONFUSION!
	 */

	return distance;

	function degreesToRadians(degrees) {
		return degrees * (Math.PI / 180);
	}

	function convertKMToMiles(km) {
		return km / 1.60934;
	}
},

_exampleUsage: function() {
	var distanceCalculator = new DistanceCalculator('mi', 3);

	/*** CALCULATING DISTANCE USING SPECIFIED LAT/LON ***/

	var lat1 = 45.58568758810709, lon1 = -122.47954663934604;
	var lat2 = 45.605901771569044, lon2 = -122.56087319825683;

	var distanceKM = distanceCalculator.calculateDistanceBetweenCoords(
		lat1,
		lon1,
		lat2,
		lon2,
		'km', //Overrides the distance units specified in the constructor
	); //6.714963986312145

	var distanceMI = distanceCalculator.calculateDistanceBetweenCoords(
		lat1,
		lon1,
		lat2,
		lon2,
		null, //Uses the distance units specified in the constructor; same as if not specified.
		5 //Overrides the rounding specified in the constructor
	); //4.17249
                                                                                      // = 4.172
	gs.debug('Distance: ' + distanceKM + ' km (' + distanceMI + ' mi)');

	/*** CALCULATING DISTANCE USING LOCATION RECORDS ***/

	var distanceData;
	var grOriginLocation = new GlideRecord('cmn_location');
	var grDestinationLocation = new GlideRecord('cmn_location');

	grOriginLocation.get('sys_id', '25ab9c4d0a0a0bb300f7dabdc0ca7c1c');
	grDestinationLocation.get('sys_id', '25ab8f300a0a0bb300d99f69c3ac24cd');

	distanceData = distanceCalculator.distanceBetweenLocationsBySysID(
		grOriginLocation.getUniqueValue(),
		grDestinationLocation.getUniqueValue(),
		null,
		1
	);

	gs.debug(
		'The distance between "' + grOriginLocation.getDisplayValue() + '" and "' +
		grDestinationLocation.getDisplayValue() + '" is ' + distanceData.distance.value +
		' miles.'
	);
},

type : 'DistanceCalculator'

```

};

## Related

- [[Server and Client Side Scripts]]
- [[Script include Advance structure - Inheritance]]
- [[Scripted Extension Point]]