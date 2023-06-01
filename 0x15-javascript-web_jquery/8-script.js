$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  for (const film of data.results) {
    $('<li>').text(film.title).appendTo('ul#list_movies');
  }
});
