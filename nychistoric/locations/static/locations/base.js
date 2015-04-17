$(document).ready(function(){
        var mapCanvas = document.getElementById('map-canvas');
        var mapOptions = {
            center: new google.maps.LatLng(40.722445296, -73.97865056),
            zoom: 16,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        var map = new google.maps.Map(mapCanvas, mapOptions);
        var marker = new google.maps.Marker({
        position: (myLatlng),
        map: map,
        title:"Hello World!"
        });
        google.maps.event.addDomListener(window, 'load');
        marker.setMap(map);
});