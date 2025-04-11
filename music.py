import random

music_database = {
    "рок": [
        "Måneskin - HONEY (ARE U COMING?)",
        "The Rolling Stones - Angry",
        "Royal Blood - Pull Me Through",
        "Foo Fighters - Under You",
        "Green Day - One Eyed Bastard",
        "Bring Me The Horizon - Kool-Aid",
        "Arctic Monkeys - Body Paint",
        "The Killers - Your Side of Town",
        "Queens of the Stone Age - Paper Machete",
        "Sleep Token - The Summoning",
        "Imagine Dragons - Eyes Closed",
        "Ghost - Spillways",
        "Bad Omens - THE DEATH OF PEACE OF MIND",
        "Paramore - This Is Why",
        "Nothing But Thieves - Overcome"
],
    "фонк": [
        "BLESSED MANE - Death is No More",
        "Dj Ikeraus - TURU R9, Vol. 2",
        "SXCREDMANE - byebye.wav, Slowed",
        "2KE, TREN - HIIT 2, SLOWED",
        "FAKEREALITY - MORTAL FIGHING",
        "KUTE - RAVE DRILL",
        "DJ Y2K - PHONK DEMON",
        "SXMPRA - COWBELL WARRIOR",
        "KORDHELL - MURDER IN MY MIND",
        "PLAZMA - TOKYO DRIFT",
        "MC ORSEN - 7 MEN",
        "DVRST - CLOSE EYES",
        "PHONKIE - MEMPHIS DEMONS",
        "LXST CXNTURY - UNFAIR"
    ],
    "хип-хоп": [
        "Eminem - Lose Yourself",
        "Kendrick Lamar - HUMBLE.",
        "Travis Scott - SICKO MODE",
        "Drake - God's Plan",
        "50 Cent - In Da Club",
        "J. Cole - No Role Modelz",
        "Nas - NY State of Mind",
        "OutKast - Ms. Jackson",
        "Wu-Tang Clan - C.R.E.A.M.",
        "Migos - Bad and Boujee",
        "Lil Wayne - A Milli",
        "Tupac - Changes",
        "The Notorious B.I.G. - Juicy",
        "Tyler, The Creator - EARFQUAKE",
        "Mac Miller - Self Care"
    ],
    "классика": [
        "Чайковский - Лебединое озеро",
        "Рахманинов - Концерт для фортепиано №2",
        "Мусоргский - Картинки с выставки",
        "Шостакович - Симфония №7",
        "Римский-Корсаков - Шехеразада",
        "Прокофьев - Война и мир",
        "Глинка - Жизнь за царя",
        "Скрябин - Поэма экстаза",
        "Стравинский - Весна священная",
        "Бородин - Князь Игорь",
        "Шнитке - Кончерто гроссо",
        "Глазунов - Времена года",
        "Лядов - Волшебное озеро",
        "Танеев - Симфония №4",
        "Калинников - Симфония №1"
    ]
}

def get_music_recommendation(genre=None):
            if genre and genre in music_database:
                return random.choice(music_database[genre])
            else:
                all_tracks = [track for genre_tracks in music_database.values() for track in genre_tracks]
                return random.choice(all_tracks)

def get_available_genres():
        return list(music_database.keys())