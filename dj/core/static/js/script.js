
function initMap(geoLocation){
    var myOptions = {
        center: geoLocation,
        zoom: 8,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map_canvas"),
        myOptions);
}

function initAddrComplete(geoLocation){
    autocomplete = new google.maps.places.Autocomplete(
        $('#id_address')[0], { types: ['geocode'] });
    autocomplete.setBounds(
        new google.maps.LatLngBounds(geoLocation, geoLocation));
}
// Bias the autocomplete object to the user's geographical location,
// as supplied by the browser's 'navigator.geolocation' object.
function getUserLocation(callback) {
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(function(position) {
            callback(new google.maps.LatLng(
                position.coords.latitude, position.coords.longitude));
        });
    } else callback(new google.maps.LatLng(-33.8902, 151.1759));
}

function setCoordinates(){
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({'address': $('#id_address').val()},function(results, status){
        if (status == google.maps.GeocoderStatus.OK){
            var coordinates = results[0].geometry.location;
            $('#id_coordinates').val(coordinates.lat()+','+ coordinates.lng());
            map.setCenter(coordinates);
            mark(coordinates);
        } else {
            alert('Address not found.');
            $('#id_cordinates').val('');
        };
    });
}

function getCoordinates(){
    strpos = $('#id_coordinates').val().split(',');
    return new google.maps.LatLng(parseFloat(strpos[0]), parseFloat(strpos[1]));
}

function mark(position){
    var marker = new google.maps.Marker({
        map: map,
        position: position
    })
}
