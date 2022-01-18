const mapDisplayKey = 'HroGGaVWiuC5LUReWH6uimeNZF4QEzIw';
const searchKey = 'EaP9PCgZntMQeqBZpeoG9DxbxVybLBGU';
const center = [37.617617, 55.755811];
const target = document.createElement('div');

var layer_id = 0;

let marker = new tt.Marker({ element: target, offset: [0, 27]});
let bestRoute;
let p_o_i;

const map = tt.map({
  key: mapDisplayKey,
  container: 'map',
  center: center,
  zoom: 9.5,
  style: {
        poi: 'poi_main',
        map: 'basic_night'
  },
  stylesVisibility: {
        poi: false
  }
});

var options = {
    idleTimePress: 500,
    minNumberOfCharacters: 5,
    searchOptions: {
        key:searchKey,
        language:"ru-RU",
        countrySet: "RUS",
        extendedPostalCodes: "None",
        idxSet: "Addr,PAD,Str",
        minFuzzyLevel: 2,
        maxFuzzyLevel: 2,
        resultSet: "category"
    },
    autocompleteOptions: {
        key:searchKey,
        language:"ru-RU",
        countrySet: "RUS",
        extendedPostalCodes: "None",
        resultSet: "category"
    },
    filterSearchResults: function (searchResult) {
        if (searchResult.address.municipality == "Москва") {
            return true;
        }
        else {
            return false;
        }
    },
    labels: {
        placeholder: 'Введите свой адрес',
        noResultsMessage: 'Нет результатов'
    }
}

var ttSearchBox = new tt.plugins.SearchBox(tt.services, options);
var searchBoxHTML = ttSearchBox.getSearchBoxHTML();
document.body.appendChild(searchBoxHTML);
map.addControl(ttSearchBox, 'top-left');
ttSearchBox.on('tomtom.searchbox.loadingstarted', function() {
    var req = ttSearchBox.getValue();
    if (req != '' && req.length >= 5) {
        options.searchOptions.query = "Москва, " + req;
        options.autocompleteOptions.query = "Москва, " + req;
        ttSearchBox.updateOptions(options);
    };
});

ttSearchBox.on('tomtom.searchbox.resultsfound', function(event) {
    var res1 = event.data.results.fuzzySearch.results;
    for (let i = 0; i < res1.length; i++) {
        console.log(res1[i]);
    };
});

function createPOI(name, coordinates) {
    return {
        name: name,
        coordinates: coordinates,
        icon: "<img src=static/images/pin.png style='width:55px; height:55px;'>"
    };
}

function displayPOI(coordinates) {
    p_o_i = createPOI('test', coordinates);
    target.innerHTML = p_o_i.icon;
}

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
}

function test(id,routeData){
    map.on('load', function layer() {
        map.addLayer(buildStyle(id , routeData, 'red', 5));
    })
}

function newLayer(id, routeData) {
    map.addLayer(buildStyle(id, routeData, 'red', 5));
}

ttSearchBox.on('tomtom.searchbox.resultselected', async function(event) {
    console.log('check');
    let formData = new FormData();
    formData.append("longitude", event.data.result['position']['lng']);
    formData.append("latitude", event.data.result['position']['lat']);
    let response = await fetch('/', {method: 'POST',
        body: formData});
    if (response.ok) {
        let result = await response.json();
        if (map.getLayer(layer_id) != 'undefined'){
            map.removeLayer(String(layer_id));
            layer_id += 1;
        }
        displayPOI([result['closest_longitude'], result['closest_latitude']]);
        marker.setLngLat(p_o_i.coordinates).addTo(map);
        newLayer(String(layer_id), result['geodata']);
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
    else {
        console.log(response.status);
    }
});