#!/usr/bin/node
$.getJSON('https://stefanbohacek.com/hellosalut/?lang=fr', function(sw) {
    $('#hello').html(sw['hello'])
});