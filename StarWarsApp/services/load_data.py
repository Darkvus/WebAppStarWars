from requests import get
from django.db import Error
from StarWarsApp.models.pelicula import Pelicula as pelicula
from StarWarsApp.models.personaje import Personaje
from StarWarsApp.helper.exception import LoadDataException


class LoadData():

    @classmethod
    def execute(self):
        try:
            json_peli = self.peticionJson("https://swapi.co/api/films")
        except Exception:
            raise LoadDataException(" Api temporalmente fuera de servicio")
        try:
            for peli in json_peli['results']:
                try:
                    _, _ = pelicula.objects.get_or_create(episode_id=peli['episode_id'], title=peli['title'], opening_crawl=peli['opening_crawl'],
                                                          director=peli['director'], producer=peli[
                        'producer'], release_date=peli['release_date'],
                        image='pelicula/img/'+str(peli['title'])+'.jpg', url_API=peli['url'])

                except Exception:
                    raise LoadDataException(
                        "Redundacia de datos sobre peliculas")

        except Error:
            raise LoadDataException("Error con la carga de las peliculas")

        try:
            personaje_json = []
            for i in range(1, 10):
                personaje_json.append(self.peticionJson(
                    "https://swapi.co/api/people/?format=json&page="+str(i)))

        except Exception:
            raise LoadDataException(" Api temporalmente fuera de servicio")

        try:
            if Personaje.objects.all().count() != 0:
                Personaje.objects.all().delete()
                for page in personaje_json:
                        for persona in page['results']:
                            try:
                                obj = Personaje(nombre=persona['name'],
                                                height=persona['height'],
                                                mass=persona['mass'],
                                                hair_color=persona['hair_color'],
                                                eye_color=persona['eye_color'],
                                                birth_year=persona['birth_year'],
                                                gender=persona['gender'],
                                                image='personaje/img/' +
                                                persona['name'] +
                                                '.jpg',
                                                url_API=persona['url']
                                                )
                                obj.save()
                                for peli in persona['films']:
                                    obj.peliculas.add(
                                        pelicula.objects.get(url_API=peli))
                            except Exception:
                                raise LoadDataException(
                                    "Fallo al actualizar datos sobre personajes")
            else:
                for page in personaje_json:
                    for persona in page['results']:
                        try:
                            obj = Personaje(nombre=persona['name'],
                                            height=persona['height'],
                                            mass=persona['mass'],
                                            hair_color=persona['hair_color'],
                                            eye_color=persona['eye_color'],
                                            birth_year=persona['birth_year'],
                                            gender=persona['gender'],
                                            image='personaje/img/' +
                                            persona['name'] +
                                            '.jpg',
                                            url_API=persona['url']
                                            )
                            obj.save()
                            for peli in persona['films']:
                                obj.peliculas.add(
                                    pelicula.objects.get(url_API=peli))
                        except Exception:
                            raise LoadDataException(
                                " Fallo al cargar datos sobre personajes")
        except Error:
            raise LoadDataException(" Error con la carga de personajes")

    def peticionJson(url):
        response_json = get(url).json()
        return response_json
