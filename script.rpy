
#Здравствуйте, а что вы тут забыли?
# Определение персонажей игры.

define v = Character('Вован', color="#f50000")
define who = Character('???', color="#55e655")
define el = Character('Таня', color="#c710e8")
define al = Character('Алла', color="#f334e3")

# Игра начинается здесь:
label start:
    play music "audio/Zacheni.ogg"
    image black = "#000000"
    with dissolve
    "Все персонажи вымышлены, совпадения случайны"
    scene bg zdanie
    with dissolve


    show vova sp at center with move

    v "Вот я и здесь. Крупная компания Тяндекс."

    scene bg admin
    with dissolve
    show vova sp at center with move
    v "Я внутри)
    "
    v "Я пришел сюда, потому что уже окончил третий курс, и мне пора искать настоящую работу." 

    v "Работу веб-разработчика!"

    v "Я отправил свою анкету пару недель назад и меня наконец-то пригласили на собеседование."

    show vova at right 
    with move
    
    who "Эй, молодой человек, постойте!!!"

    v "Э, че?"

    show tanechka sp at left 
    with move

    el "Здравствуй, ты Вован?"

    el "Шуруй за мной на собеседование"

    v "Ok"

    scene bg cab
    with dissolve

    show tanechka sp at right

    show vova sp at left

    el "Итак, ты готов ответить на несколько вопросов?"

    v "Я готов с рождения"

    el "Ну начнём"

    jump sobes

    return
label sobes:
    menu:
        el "Какой язык может компилировать движок браузера?"
        "Python":
            show tanechka sad
            el "Подумай ещё)"
            jump sobesRes
        "JavaScript":
            show tanechka hap
            el "Ничего себе ты умный, ну ладно, следующий вопрос"
            jump sobes2
        "Java":
            show tanechka sad
            el "Подумай ещё)"
            jump sobesRes
        "TypeScript":
            show tanechka sad
            el "Подумай ещё)"
            jump sobesRes

label sobesRes:
    show tanechka sp
    menu:
        el "Что? хочешь еще раз проверить свои знания?"
        "Да":
            jump sobes
        "Нет":
            el "Ну и досвидания"

            return
label sobes2:
    show tanechka sp
    menu:
        el "Что из приведённого не является тегом html?"
        "<div>":
            show tanechka sad
            el "Подумай ещё)"
            jump sobesRes
        "<image>": 
            show tanechka hap
            el "Ну да, тут скорее надо <img />"
            el "Итак, внмание, последняя теоритическая задача!"
            jump sobes3
        "<span>":
            show tanechka sad
            el "Подумай ещё)"
            jump sobesRes
        "<mark>":
            show tanechka sad
            el "Подумай ещё)"
            jump sobesRes
label sobes3:
    show tanechka sp
    el "Чему равен typeof null в режиме use strict?" 
    $ popa = renpy.input("Чему равен typeof null в режиме use strict?", length=32)
    python:
        if popa == "object" or popa == "Object" or popa == "OBJECT":
            renpy.jump("sobesEnd1")
        else:
            renpy.jump("sobesEnd2")
label sobesEnd1:
    show tanechka hap
    el "Ну ничеси ты умный, даже я этого не знаю"
    
    el "Ну, что могу сказать"
    
    jump allow
label sobesEnd2:
    show tanechka sad
    el "Ну лан, я честно тоже не знаю"
    show tanechka sp
    el "Ну что могу сказать"

    jump allow

label allow:
    show tanechka hap
    el "Поздравляем, вы прошли собеседование!"
    el "Алла, подойте сюда пожайлуста"

    image black = "#000000"
    with dissolve

    

    scene bg dveri
    with fade
    "В дверях появилась девушка неземной красоты"
    show alla sp

    al "Дратути, чем помочь?"

    scene bg cab

    show tanechka sp at right

    show vova sp at center

    show alla sp at left

    el "можешь показать Вовану офис?"

    al "Да, кнш"

    al "Пошли, Вован)"
    scene black
    with dissolve
    "далее Вован будет получать задания, выполнять их и знакомится с работницами Тяндекса"
    "ПРОДОЛЖЕНИЕ СЛЕДУЕТ"
    
        
