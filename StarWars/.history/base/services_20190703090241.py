from pelicula.models import Film
from personaje.models import Personaje



class LoadData():

    @classmethod
    def execute(self):
        if not Film.objects.first():
            url = "https://swapi.co/api/films"
            response_peli = requests.get(url)
            json_peli = response_peli.json()

            for peli in json_peli['results']:
                Film(episode_id=peli['episode_id'], title=peli['title'], opening_crawl=peli['opening_crawl'],
                        director=peli['director'], producer=peli['producer'], release_date=peli['release_date'],
                        image='pelicula/img/'+str(peli['title'])+'.jpg', url_API=peli['url']).save()

        if not Personaje.objects.first():
            url_persona = "https://swapi.co/api/people/?search="
            personajes_list = []
            personaje_json = []

            personajes_list.append(requests.get(url_persona+'Yoda'))
            personajes_list.append(requests.get(url_persona+'R2 d2'))
            personajes_list.append(requests.get(url_persona+'bb8'))
            personajes_list.append(requests.get(url_persona+'luke'))
            personajes_list.append(requests.get(url_persona+'obi'))
            personajes_list.append(requests.get(url_persona+'Vader'))
            personajes_list.append(requests.get(url_persona + 'leia'))

            for api_json in personajes_list:
                personaje_json.append(api_json.json())

            for persona in personaje_json:
                obj = Personaje(nombre=persona["results"][0]['name'],
                            height=persona['results'][0]['height'],
                            mass=persona['results'][0]['mass'],
                            hair_color=persona['results'][0]['hair_color'],
                            eye_color=persona['results'][0]['eye_color'],
                            birth_year=persona['results'][0]['birth_year'],
                            gender=persona['results'][0]['gender'],
                            image='personaje/img/'+persona['results'][0]['name']+'.jpg',
                            url_API=persona['results'][0]['url']).save()
                obj.save()

                for peli in persona['results'][0]['films']:
                    obj.films.add(Film.objects.get(url_API=peli))