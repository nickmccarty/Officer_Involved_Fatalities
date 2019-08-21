// Creating map object
var myMap = L.map("map", {
  center: [38.4, -95.5],
  zoom: 5
});

var API_KEY = process.env.API_KEY;
var API_KEY2 = process.env.API_KEY2;

// Adding tile layer to the map
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

// Store API query variables
var dataURL = "https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv";
// var date = "?requested_datetime between'2016-01-10T12:00:00.000' and '2017-01-01T14:00:00.000'";
// var complaint = "?service_details=Needles";
// var limit = "&limit=10000";
var googleGeocodingURL = "https://maps.googleapis.com/maps/api/geocode/json?address=";

// Grab the data with d3
d3.csv(dataURL, function(data) {
  // data.forEach(function(d) {
  //   d.name = +d.name;
  //   d.date = +d.date;
  //   d.manner_of_death = +d.manner_of_death;
  //   d.armed = +d.armed;
  //   d.age = +d.age;
  //   d.gender = +d.gender;
  //   d.race = +d.race;
  //   d.city = +d.city;
  //   d.state = +d.state;
  //   d.signs_of_mental_illness = +d.signs_of_mental_illness;
  //   d.threat_level = + d.threat_level;
  //   d.flee = +d.flee;
  //   d.body_camera = +d.body_camera;
  // });
  console.log(data);
});

var city = "Los Angeles";
var state = "CA";
var googleGeocodingKey = "&key="+API_KEY2;

// Assemble API query URL
var url = googleGeocodingURL+city+state+googleGeocodingKey;

d3.json(url, function(data) {

  console.log(data)

});



  // // Create a new marker cluster group
  // var markers = L.markerClusterGroup();

  // // Loop through data
  // for (var i = 0; i < response.length; i++) {

  //   // Set the data location property to a variable
  //   var latitude = response[i].lat;
  //   var longitude = response[i].long;
  //   var descriptor = response[i].service_subtype;


  //   // Check for location property
  //   if (location) {

  //     // Add a new marker to the cluster group and bind a pop-up
  //     markers.addLayer(L.marker([latitude, longitude])
  //       .bindPopup(descriptor));
  //   }

  // }

  // // Add our marker cluster layer to the map
  // myMap.addLayer(markers);
