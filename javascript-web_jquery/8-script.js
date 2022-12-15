$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
  var movies = data['results'];
  var list = $('<ul>').attr('id', 'list_movies');
  
  for (var i = 0; i < movies.length; i++) {
    var movie = movies[i];
    var item = $('<li>').text(movie['title']);
    list.append(item);
  }
  
  $('body').append(list);
});