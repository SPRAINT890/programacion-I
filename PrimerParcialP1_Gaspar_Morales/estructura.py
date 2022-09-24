#mat_peliculas
[['Godfather I and II', 1974, 1, 2, 3], 
 ['Star Wars A New Hope', 1977, 4, 5, 6], 
 ['Star Trek Motion Picture', 1979, 7, 8], 
 ['The Irishman', 2019, 2, 3]]

#mat_actores
[['Marlon', 'Brando', 80, 12, False], 
 ['Al', 'Pacino', 82, 7, True], 
 ['Robert', 'DeNiro', 79, 9, True], 
 ['Mark', 'Hamill', 70, 5, True], 
 ['Harrison', 'Ford', 80, 10, True], 
 ['Carrie', 'Fisher', 60, 4, False], 
 ['William', 'Shatner', 91, 7, True], 
 ['Leonard', 'Nimoy', 84, 11, False]]

#apellidos_actores
['Kelley', 'Stiller', 'Downey']
actores = []
peliculas = []


verificacion_desvinculo_1 = [ "Al", "Pacino", 82, 7, True ] not in actores
verificacion_desvinculo_2 = [ "Harrison", "Ford", 80, 10, True ] not in actores
verificacion_desvinculo_3 = len(peliculas) == 4 and len(actores) == 4
verificacion_desvinculo_4 = ([ "Godfather I and II", 1974, 1, 2] in peliculas) and ([ "Star Wars A New Hope", 1977, 3, 4] in peliculas)