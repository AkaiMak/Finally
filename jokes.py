import random

jokes_database = [
    "— Доктор, я бессмертен! — Ну это пока не диагноз...",
    "Оптимист верит, что мы живём в лучшем из миров. Пессимист уверен, что мы в нём и останемся.",
    "— Почему вы носите чёрное? — Я в трауре по своей жизни.",
    "— Как называется фильм ужасов про диетологов? — 'Клетчатка 3D'.",
    "— Дорогой, ты бы хотел, чтобы я выглядела на 18? — Нет, я бы хотел, чтобы тебе было 18.",
    "— Почему скелеты такие весёлые? — Потому что им уже нечего терять.",
    "— Доктор, я чувствую себя как чайник! — Это ещё не диагноз, но уже кипение.",
    "— Почему призраки плохие любовники? — Потому что они исчезают сразу после первого поцелуя.",
    "— Как называется фильм про слепого массажиста? — 'Руки-базуки'.",
    "— Почему грабители банков не берут с собой календари? — Потому что у них и так много дней.",
    "— Что сказал врач пациенту после успешной ампутации? — 'Ну вот, теперь вы наконец встали на ноги!'",
    "— Почему утопленники всегда такие спокойные? — Потому что они уже прошли через самое трудное.",
    "— Как называется группа поддержки для неудачников? — 'Анонимные оптимисты'.",
    "— Почему вампиры не пользуются соцсетями? — Потому что у них нет отражения в жизни.",
    "— Летят в самолёте американец, немец и русский. Самолёт начинает падать, и обнаруживается,",
    " что у них только два парашюта. Американец: дайте мне парашют! Мне нужно кормить семью!,",
    " Русский даёт ему рюкзак, американец прыгает. Немец: прыгай ты, я уже многое повидал. Русский: а ты? У нас же два парашюта. Немец: а с чем тогда американец прыгнул? Русский: ну ему же кормить семью надо, я и дал ему рюкзак с продуктами!",
    "_ Штирлиц толкнул дверь. Дверь не открылась. Штирлиц толкнул сильнее. Дверь даже не шелохнулась. Штирлиц ударил ногой. С тем же успехом. — Штирлиц разбежался и бросился на дверь всем телом. Дверь не поддавалась. Закрыто — догадался Штирлиц.",
    "_ Спорят американец, немец и русский, чья нация быстрее строит. Американец: - Мы начнем строить мост 1 января и 31 декабря по нему поедет первая машина. Немец: - А мы начнем строить больничный комплекс 1 января и 31 января уже сможем принимать первых больных. Русский: - Ерунда! Вот мы в понедельник в 9 утра начнем строить пивзавод и в 10 все уже пьяные.",
]

def get_random_joke():
    return random.choice(jokes_database)