import json
import re

file = open('cinemaATP.json',encoding='utf-8')

data = json.load(file)

movies = {}
actors = {}

movieID = 1
actorID = 1

for item in data :

     movies[item['title']] = {
         'atores' : set(x for x in item['cast']),
         'ano' : item['year'],
         'genero' : set(x for x in item['genres']),
         'ID' : movieID
     }
     movieID += 1

     for actor in item['cast'] :
         if actor not in actors :
             actors[actor] = {
                 'filmes' : [],
                 'ID' : actorID
             }
             actors[actor]['filmes'].append(item['title'])
             actorID += 1
         else :
             actors[actor]['filmes'].append(item['title'])

movies = dict(sorted(movies.items(), key = lambda x : x[0]))
actors = dict(sorted(actors.items(), key = lambda x : x[0]))

def genHomePage() :
    homePage_path = "./html/index.html"
    homePage = open(homePage_path,"w")
    homePage.write("<!DOCTYPE html>\n")

    homePage.write("<html lang=\"en\">\n")

    homePage.write("\t<head>\n")

    homePage.write("\t\t<title>TPC2 - List of Movies and Actors</title>\n")
    homePage.write("\t\t<meta charset=\"UTF-8\">")
    homePage.write("\t\t<link rel=\"stylesheet\" href=\"https://www.w3schools.com/w3css/4/w3.css\">")

    homePage.write("\t</head>\n")

    homePage.write("\t<body>\n")

    homePage.write("\t\t<h1><a href=\"http://localhost:7777/filmes\">Movies</a></h1>")
    homePage.write("\t\t<h1><a href=\"http://localhost:7777/atores\">Actors</a></h1>")

    homePage.write("\t</body>\n")

    homePage.write("</html>\n")

def genMoviesPage() : 
    moviesPage_path = "./html/filmes.html"
    moviesPage = open(moviesPage_path,"w")
    moviesPage.write("<!DOCTYPE html>\n")

    moviesPage.write("<html lang=\"en\">\n")

    moviesPage.write("\t<head>\n")

    moviesPage.write("\t\t<title>Movies</title>\n")
    moviesPage.write("\t\t<meta charset=\"UTF-8\">")
    moviesPage.write("\t\t<link rel=\"stylesheet\" href=\"https://www.w3schools.com/w3css/4/w3.css\">")

    moviesPage.write("\t</head>\n")

    moviesPage.write("\t<body>\n")

    moviesPage.write("\t\t<div class=\"w3-bar w3-center\">\n")
    moviesPage.write("\t\t\t<h1>Movies</h1>\n")
    moviesPage.write("\t\t</div>\n")

    moviesPage.write("\t\t<div class=\"w3-container w3-margin-left w3-text-red\">\n")
    moviesPage.write("\t\t\t<p><a href=\"http://localhost:7777\"><u>Back</u></a><p>\n")
    moviesPage.write("\t\t</div>")

    moviesPage.write("\t\t<div class=\"w3-container w3-margin-left\">\n")
    moviesPage.write("\t\t\t<ol>\n")

    for item,values in movies.items() :
        moviesPage.write("\t\t\t<li><a href=\"http://localhost:7777/filmes/f" + {values['ID']} + "\">" + {item} + "</a></li>")

    moviesPage.write("\t\t\t<\ol>\n")

    moviesPage.write("\t</body>\n")

    moviesPage.write("</html>\n")

def genEachMoviePage() :
    for item,values in movies.items() :

        fileName = "./html/f" + {values['ID']} + ".html"
        f = open(fileName,"w")
        
        f.write("<!DOCTYPE html>\n")

        f.write("<html lang=\"en\">\n")

        f.write("\t<head>\n")

        f.write("\t\t<title>Movies - " + {item} + "</title>\n")
        f.write("\t\t<meta charset=\"UTF-8\">")
        f.write("\t\t<link rel=\"stylesheet\" href=\"https://www.w3schools.com/w3css/4/w3.css\">")

        f.write("\t</head>\n")

        f.write("\t<body>\n")

        f.write("\t\t<div class=\"w3-bar w3-center\">\n")
        f.write("\t\t\t<h1>" + {item} + "</h1>\n")
        f.write("\t\t</div>")

        f.write("\t\t<div class=\"w3-container w3-margin-left\">\n")
        f.write("\t\t\t<h3>Debut: " + {values['ano']} + "</h3>\n")
        f.write("\t\t\t<h4>Cast:</h4>\n")
        f.write("\t\t\t<ul>\n")

        for actor in values['atores'] : 
            f.write("\t\t\t\t<li><a href=\"http://localhost:7777/atores/a" + {actors[actor]['ID']} + "\">" + {actor} + "</a></li>\n")

        f.write("\t\t\t</ul>\n")
        f.write("\t\t\t<h4>Genre:</h4>\n")
        f.write("\t\t\t<ul>\n")

        for gen in values['genero'] :
            f.write("\t\t\t\t<li>" + gen + "</li>\n")

        f.write("\t\t\t</ul>\n")
        f.write("\n\n</div>")

        f.write("\t\t<div class=\"w3-container w3-margin-left w3-text-red\">\n")
        f.write("\t\t\t<p><a href=\"http://localhost:7777/filmes\"><u>Back</u></a><p>\n")
        f.write("\t\t</div>")

        f.write("\t</body>\n")

        f.write("</html>\n")