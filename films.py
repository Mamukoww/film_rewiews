films = {
    1:{
        "name": "Звёздные войны. Эпизод IV: Новая надежда",
        "release_date": "25 мая 1977 года",
        "image": "https://upload.wikimedia.org/wikipedia/ru/8/87/StarWarsMoviePoster1977.jpg"
    },
    2:{
        "name": "Назад в будущее",
        "release_date": "3 июля 1985 года",
        "image": "https://upload.wikimedia.org/wikipedia/ru/9/90/BTTF_DVD_rus.jpg"
    },
    3:{
            "name": "ВАЛЛ-И",
            "release_date": "27 июня 2008 года",
            "image": "https://upload.wikimedia.org/wikipedia/ru/thumb/c/c4/WALL-E_poster.png/266px-WALL-E_poster.png"
        }
}



def find_by_name(name: str):
    result = {}

    for index, film in films.items():
        if name.lower() in film["name"].lower():
            result[index] = film

    return result