from requests import get

from StarWarsApp.models.pelicula import Pelicula as pelicula
from StarWarsApp.models.personaje import Personaje


class LoadData():

    @classmethod
    def execute(self):
        if not pelicula.objects.first():
            url = "https://swapi.co/api/peliculas"
            response_peli = get(url)
            json_peli = response_peli.json()

            for peli in json_peli['results']:
                pelicula(episode_id=peli['episode_id'], title=peli['title'], opening_crawl=peli['opening_crawl'],
                         director=peli['director'], producer=peli['producer'], release_date=peli['release_date'],
                         image='pelicula/img/'+str(peli['title'])+'.jpg', url_API=peli['url']).save()

        if not Personaje.objects.first():
            url_persona = "https://swapi.co/api/people/?search="
            personajes_list = []
            personaje_json = []

            personajes_list.append(get(url_persona+'Yoda'))
            personajes_list.append(get(url_persona+'R2 d2'))
            personajes_list.append(get(url_persona+'bb8'))
            personajes_list.append(get(url_persona+'luke'))
            personajes_list.append(get(url_persona+'obi'))
            personajes_list.append(get(url_persona+'Vader'))
            personajes_list.append(get(url_persona + 'leia'))

            for api_json in personajes_list:
                personaje_json.append(api_json.json())

            for persona in personaje_json:
                obj = Personaje(nombre=persona['name'],
                                height=persona['height'],
                                mass=persona['mass'],
                                hair_color=persona['hair_color'],
                                eye_color=persona['eye_color'],
                                birth_year=persona['birth_year'],
                                gender=persona['gender'],
                                image='personaje/img/'+persona['name']+'.jpg',
                                url_API=persona['url'])
                obj.save()

                for peli in persona['peliculas']:
                    obj.peliculas.add(pelicula.objects.get(url_API=peli))
