const apiKey = '{{ api_key }}';
const center = [{{ longitude }}, {{ latitude }}];

let bestRoute;
let p_o_i;

const map = tt.map({
  key: apiKey,
  container: 'map',
  center: center,
  zoom: 13,
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
        key:apiKey,
        language:"ru-RU",
        countrySet: "RU",
        idxSet: "Str",
        resultSet: "category"
    },
    autocompleteOptions: {
        key:apiKey,
        language:"ru-RU",
        countrySet: "RU",
        resultSet: "category"
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
    if (!req.includes("Москва, ") && req.length >= 5) {
        ttSearchBox.setValue("Москва, " + req);
    };
});

function createPOI(name, coordinates) {
    return {
        name: name,
        coordinates: coordinates,
        icon: "<img src=static/images/pin.png style='width:55px; height:55px;'>"
    };
}

function displayPOI() {
    p_o_i = createPOI('test', [{{ closest_long }}, {{ closest_lat }}]);
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

function test(routeData){;
    map.on('load', function layer() {
        map.addLayer(buildStyle('0', routeData, 'red', 5));
    })
}

displayPOI();
const target = document.createElement('div');
target.innerHTML = p_o_i.icon;
new tt.Marker({ element: target, offest: [0, 27]}).setLngLat(p_o_i.coordinates).addTo(map);
test({{ route | safe}});