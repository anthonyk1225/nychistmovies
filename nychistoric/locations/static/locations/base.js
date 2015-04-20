$( document ).ready(function() {
        navigator.geolocation.getCurrentPosition(function(position){
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;    
        var mapOptions = {
            zoom: 16,
            center: new google.maps.LatLng(latitude,longitude)
        }
        var map = new google.maps.Map(document.getElementById('map-canvas'),
        mapOptions);

            $.getJSON("/nycfilms/coords/", function(data){
            for (i=0;i<data['coords'].length; i++){
                var image = "/static/locations/video.png"
                var filmLatLng = new google.maps.LatLng(data['coords'][i][0],data['coords'][i][1]);
                var beachMarker = new google.maps.Marker({
                    position: filmLatLng,
                    map: map,
                    icon: image,
                    title: data['coords'][i][2]
            });
        }
        })
    });
});
