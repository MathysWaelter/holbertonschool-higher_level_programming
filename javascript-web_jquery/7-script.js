#!/usr/bin/node
$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function(sw) {
    $('#character').html(sw['name'])
});