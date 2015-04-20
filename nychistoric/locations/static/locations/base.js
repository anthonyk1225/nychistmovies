$( document ).ready(function() {
        var mapOptions = {
            zoom: 16,
            center: new google.maps.LatLng(40.7517291,-73.9794923)
        }
        var map = new google.maps.Map(document.getElementById('map-canvas'),
        mapOptions);
        $.getJSON("/nycfilms/coords/", function(data){
                            console.log(data['coords'])

            for (i=0;i<data['coords'].length; i++){
                var image = "/static/locations/video.png"
                var filmLatLng = new google.maps.LatLng(data['coords'][i][0],data['coords'][i][1]);
                var vidMarker = new google.maps.Marker({
                    position: filmLatLng,
                    map: map,
                    icon: image,
                    title: data['coords'][i][2]
            });
        }
        })
});
