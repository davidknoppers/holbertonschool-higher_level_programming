$.get('http://swapi.co/api/films?format=json', function (data) {
  for (let i in data.results) {
    $('UL#list_movies').append('<LI>' + data.results[i].title + '</LI>');
  }
});
