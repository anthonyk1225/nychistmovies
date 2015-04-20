$( document ).ready(function initialize() {
        var mapOptions = {
            zoom: 10,
            center: new google.maps.LatLng(40.74727,-73.9800645)
        }
        var map = new google.maps.Map(document.getElementById('map-canvas'),
        mapOptions);

        var image = "/static/locations/video.png"
        var filmLatLng = new google.maps.LatLng(40.7604000000000,-73.9758000000000);
        var beachMarker = new google.maps.Marker({
            position: filmLatLng,
            map: map,
            icon: image
        });
    // };
});
// google.maps.event.addDomListener(window, 'load', initialize);
