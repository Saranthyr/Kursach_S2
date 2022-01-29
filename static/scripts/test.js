const mapDisplayKey = 'HroGGaVWiuC5LUReWH6uimeNZF4QEzIw';
const center = [37.617617, 55.755811];
const target = document.createElement('div');
const type = document.getElementById("type");
const net = document.getElementById("net");
const mode = document.getElementById("legs-car");
const theme = document.getElementById("theme");

var layer_id = 0;
let long;
let lat;
let marker = new tt.Marker({ element: target, offset: [0, 27]});
let bestRoute;
let p_o_i;

let saved_response;

const map = tt.map({
  key: mapDisplayKey,
  container: 'map',
  center: center,
  zoom: 9.5,
  style: {
        poi: 'poi_main',
        map: 'basic_main'
  },
  stylesVisibility: {
        poi: false
  }
});

var popup = new tt.Popup();
var geolocateControl = new tt.GeolocateControl({
    positionOptions:{
        enableHighAccuracy: true
    }
});
map.addControl(geolocateControl, 'top-left');

function createPOI(name, coordinates) {
    return {
        name: name,
        coordinates: coordinates,
        icon: "<img src=static/images/"+ theme.value + ".png style='width:25px; height:25px;'>"
    };
};

function displayPOI(coordinates) {
    p_o_i = createPOI('test', coordinates);
    target.innerHTML = p_o_i.icon;
};

function buildStyle(id, data, color, width) {
    return {
        'id': id,
        'type': 'line',
        'source': {
            'type': 'geojson',
            'data': data
        },
        'paint': {
            'line-color': color,
            'line-width': width
        },
        'layout': {
            'line-cap': 'round',
            'line-join': 'round'
        }
    }
};

function test(id,routeData){
    map.on('load', function layer() {
        map.addLayer(buildStyle(id , routeData, 'red', 5));
    })
};

function newLayer(id, routeData) {
    map.addLayer(buildStyle(id, routeData, 'red', 5));
};

geolocateControl.on('geolocate', async function(event){
    let formData = new FormData();
    long = event.coords['longitude'];
    lat = event.coords['latitude'];
    formData.append("longitude", event.coords['longitude']);
    formData.append("latitude", event.coords['latitude']);
    formData.append("table", type.value);
    formData.append("mode", mode.value);
    if (net.checked == true) {
        formData.append("net", "True")
    }
    let response = await fetch('/', {method: 'POST',
        body: formData});
    if (response.status == 200) {
        let result = await response.json();
        saved_response = result;
        displayPOI([result['closest_longitude'], result['closest_latitude']]);
        marker.setLngLat(p_o_i.coordinates).addTo(map);
        let html_content = "<h1>"+result['place_name']+"</h1><h2>"+result['address']+"</h2><p>"+result['phone']+"</p><p>Мест: "+result['seats']+"</p>"
        popup.setHTML(html_content);
        marker.setPopup(popup);
        if (map.getLayer(layer_id) !== undefined) {
            map.removeLayer(String(layer_id));
            map.removeSource(String(layer_id));
            newLayer(String(layer_id), result['geodata']);
        }
        else {
            newLayer(String(layer_id), result['geodata']);
        }
        let zoom;
        if (result['geodata']['features'][0]['properties']['summary']['lengthInMeters'] < 1000) {
            zoom = 16;
        }
        else {
            zoom = 15;
        }
        map.jumpTo({'center': [result['longitude'], result['latitude']],
        'zoom' : zoom});
    };
    if (response.status == 230) {
            let result = await response.json();
            if (map.getLayer(layer_id) !== undefined) {
                map.removeLayer(String(layer_id));
                map.removeSource(String(layer_id));
                marker.remove();
            }
            alert(result['message']);
        }
});

type.addEventListener('change', async function(event){
    if (long !== undefined && lat !== undefined){
        let formData = new FormData();
        formData.append("longitude", long);
        formData.append("latitude", lat);
        formData.append("table", type.value);
        formData.append("mode", mode.value);
        if (net.checked == true) {
            formData.append("net", "True")
        }
        let response = await fetch('/', {method: 'POST',
            body: formData});
        if (response.status == 200) {
            let result = await response.json();
            saved_response = result;
            displayPOI([result['closest_longitude'], result['closest_latitude']]);
            marker.setLngLat(p_o_i.coordinates).addTo(map);
            let html_content = "<h1>"+result['place_name']+"</h1><h2>"+result['address']+"</h2><p>"+result['phone']+"</p><p>Мест: "+result['seats']+"</p>"
            popup.setHTML(html_content);
            if (map.getLayer(layer_id) !== undefined) {
                map.removeLayer(String(layer_id));
                map.removeSource(String(layer_id));
                newLayer(String(layer_id), result['geodata']);
            }
            else {
                newLayer(String(layer_id), result['geodata']);
            }
            let zoom;
            if (result['geodata']['features'][0]['properties']['summary']['lengthInMeters'] < 1000) {
                zoom = 16;
            }
            else {
                zoom = 15;
            }
            map.jumpTo({'center': [result['longitude'], result['latitude']],
                'zoom' : zoom});
        }
        if (response.status == 230) {
            let result = await response.json();
            if (map.getLayer(layer_id) !== undefined) {
                map.removeLayer(String(layer_id));
                map.removeSource(String(layer_id));
                marker.remove();
            }
            alert(result['message']);
        }
    }
    else {
        return false
    }
});

mode.addEventListener('change', async function(event){
    if (long !== undefined && lat !== undefined){
        let formData = new FormData();
        formData.append("longitude", long);
        formData.append("latitude", lat);
        formData.append("table", type.value);
        formData.append("mode", mode.value);
        if (net.checked == true) {
            formData.append("net", "True")
        }
        let response = await fetch('/', {method: 'POST',
            body: formData});
        if (response.status == 200) {
            let result = await response.json();
            saved_response = result;
            displayPOI([result['closest_longitude'], result['closest_latitude']]);
            marker.setLngLat(p_o_i.coordinates).addTo(map);
            let html_content = "<h1>"+result['place_name']+"</h1><h2>"+result['address']+"</h2><p>"+result['phone']+"</p><p>Мест: "+result['seats']+"</p>"
            popup.setHTML(html_content);
            if (map.getLayer(layer_id) !== undefined) {
                map.removeLayer(String(layer_id));
                map.removeSource(String(layer_id));
                newLayer(String(layer_id), result['geodata']);
            }
            else {
                newLayer(String(layer_id), result['geodata']);
            }
            let zoom;
            if (result['geodata']['features'][0]['properties']['summary']['lengthInMeters'] < 1000) {
                zoom = 16;
            }
            else {
                zoom = 15;
            }
            map.jumpTo({'center': [result['longitude'], result['latitude']],
                'zoom' : zoom});
        };
        if (response.status == 230) {
            let result = await response.json();
            if (map.getLayer(layer_id) !== undefined) {
                map.removeLayer(String(layer_id));
                map.removeSource(String(layer_id));
                marker.remove();
            }
            alert(result['message']);
        }
    }
    else {
        return false
    }
});

net.addEventListener('change', async function(event){
    if (long !== undefined && lat !== undefined){
        let formData = new FormData();
        formData.append("longitude", long);
        formData.append("latitude", lat);
        formData.append("table", type.value);
        formData.append("mode", mode.value);
        if (net.checked == true) {
            formData.append("net", "True")
        }
        let response = await fetch('/', {method: 'POST',
            body: formData});
        if (response.status == 200) {
            let result = await response.json();
            saved_response = result;
            displayPOI([result['closest_longitude'], result['closest_latitude']]);
            marker.setLngLat(p_o_i.coordinates).addTo(map);
            let html_content = "<h1>"+result['place_name']+"</h1><h2>"+result['address']+"</h2><p>"+result['phone']+"</p><p>Мест: "+result['seats']+"</p>"
            popup.setHTML(html_content);
            if (map.getLayer(layer_id) !== undefined) {
                map.removeLayer(String(layer_id));
                map.removeSource(String(layer_id));
                newLayer(String(layer_id), result['geodata']);
            }
            else {
                newLayer(String(layer_id), result['geodata']);
            }
            let zoom;
            if (result['geodata']['features'][0]['properties']['summary']['lengthInMeters'] < 1000) {
                zoom = 16;
            }
            else {
                zoom = 15;
            }
            map.jumpTo({'center': [result['longitude'], result['latitude']],
                'zoom' : zoom});
        };
        if (response.status == 230) {
            let result = await response.json();
            if (map.getLayer(layer_id) !== undefined) {
                map.removeLayer(String(layer_id));
                map.removeSource(String(layer_id));
                marker.remove();
            }
            alert(result['message']);
        }
    }
    else {
        return false
    }
});

theme.addEventListener('change', async function(event){
    map.setStyle({poi: 'poi_main', map: theme.value});
    map.on('idle', function() {
        if (saved_response !== undefined){
            displayPOI([saved_response['closest_longitude'], saved_response['closest_latitude']]);
            marker.setLngLat(p_o_i.coordinates).addTo(map);
            let html_content = "<h1>"+saved_response['place_name']+"</h1><h2>"+saved_response['address']+"</h2><p>"+saved_response['phone']+"</p><p>Мест: "+saved_response['seats']+"</p>"
            popup.setHTML(html_content);
            if (map.getLayer(layer_id) !== undefined) {
                map.removeSource(String(layer_id));
                newLayer(String(layer_id), saved_response['geodata']);
            }
            else {
                newLayer(String(layer_id), saved_response['geodata']);
            }
            let zoom;
            if (saved_response['geodata']['features'][0]['properties']['summary']['lengthInMeters'] < 1000) {
                zoom = 16;
            }
            else {
                zoom = 15;
            }
            map.jumpTo({'center': [saved_response['longitude'], saved_response['latitude']],
            'zoom' : zoom});
        }
        else{
            return 0;
        }
    });
});