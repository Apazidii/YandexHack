import coordinates
import events
from Kostya.phrase import get_phrase


def write_text(text, buttons=None, state=None, geo=None, bridge=None):
    response = {
        'text': text
    }
    if buttons:
        response['buttons'] = buttons
    main_response = {
        'response': response,
        'version': '1.0',
    }
    if state:
        main_response['session_state'] = state
    if (geo) or (bridge):
        main_response['application_state'] = {
            'geo': geo,
            'bridge': bridge
        }
    return main_response


def handler(event, context):
    intens = event['request'].get('nlu', {}).get('intents')
    state = event.get('state').get('session', {}).get('screen')
    if event['session']['new']:
        return def_start(event)
    elif 'tell_about_bridge' in intens:
        return def_bridge_event(event)
    elif 'i_am_here' in intens:
        return def_i_am_here_event(event)
    elif 'tell_about_nearest_bridge' in intens:
        return def_nearest_bridge_event(event)
    elif (('i_need_all_bridges' in intens) or ('i_dont_know' in intens)) and (state == 'all_bridges_state'):
        return def_all_bridges_list(event)
    elif ('i_need_all_bridges' in intens) or ('i_dont_know' in intens):
        return def_all_bridges_state(event)
    elif 'i_need_more_beauty' in intens:
        return def_beauty(event)
    elif 'tell_about_open_bridge' in intens:
        return def_open_bridge_event(event)
    elif 'tell_about_close_bridge' in intens:
        return def_close_bridge_event(event)
    elif 'i_need_help' in intens:
        return def_i_need_help(event)
    elif (state == 'yes_or_not') and ('yep_i_am_ready_for_everything' in intens):
        return def_bridge_from_state(event)
    elif (state == 'yes_or_not') and ('no' in intens):
        return def_end_scene(event)
    elif state == 'i_need_your_adress':
        return write_text("Я не нашла такое место в Петербурге, пожалуйста уточните адрес")
    else:
        # return write_text('спроси что полегче')
        return events.send_response(event, 'спроси что полегче', "fallback")


def def_beauty(event):
    return write_text(
        "Cамыми популярными разводными мостами Петербурга по версии МОСТОТРЕСТА считаются: Дворцовый, Тучков, Александра Невского, Биржевой, Благовещенский",
        buttons=[
            button("Дворцовый мост", suggest=True),
            button("Тучков мост", suggest=True),
            button("мост Александра Невского", suggest=True),
            button("Биржевой мост", suggest=True),
            button("Благовещенский мост", suggest=True),
        ])


def def_all_bridges_state(event):
    return write_text(
        'Прямо сейчас в Петербурге N_OPEN мостов наведено, N_CLOSED мостов разведено. Могу озвучить список наведенных, разведенных, или всех мостов. Также могу рассказать про ближайший к вам мост.',
        buttons=[
            button('Наведённые мосты', suggest=True),
            button('Разведённые мосты', suggest=True),
            button('Все мосты', suggest=True),
            button('Ближайший мост', suggest=True),
        ],
        state={
            'screen': 'all_bridges_state',
        })


def def_end_scene(event):
    return write_text(
        "Для выхода из навыка скажите хватит. Если вас интересует другой разводной мост скажите его название", buttons=[
            button("Ближайший мост", suggest=True),
            # проверка спрашивал ли он про дворцовый или тучков мост если да то заменить названия
            button("Дворцовый мост", suggest=True),
            button("Тучков мост", suggest=True),
            button("Я не знаю названий", suggest=True),
        ])


def def_all_bridges_list(event):
    return write_text(
        'Дворцовый мост, Тучков мост, мост Александра Невского, Биржевой мост, Благовещенский мост, Троицкий мост, Володарский мост, Большеохтинский мост, Литейный мост, Кантемировский мост, Гренадерский мост, Сампсониевский мост. Какой мост вас интересует?',
        buttons=[
            button("Дворцовый мост", suggest=True),
            button("Тучков мост", suggest=True),
            button("мост Александра Невского", suggest=True),
            button("Биржевой мост", suggest=True),
            button("Благовещенский мост", suggest=True),
            button("Троицкий мост", suggest=True),
            button("Володарский мост", suggest=True),
            button("Большеохтинский мост", suggest=True),
            button("Литейный мост", suggest=True),
            button("Кантемировский мост", suggest=True),
            button("Гренадерский мост", suggest=True),
            button("Сампсониевский мост", suggest=True),
        ])


def def_start(event):
    return write_text('Привет, я помогу узнать график разведения мостов, какой мост вас интересует?', buttons=[
        button("Ближайший мост", suggest=True),
        button("Дворцовый мост", suggest=True),
        button("Тучков мост", suggest=True),
        button("Я не знаю названий", suggest=True),
    ])


def def_nearest_bridge_event(event):
    address = event.get('state').get('application', {}).get('geo')
    if address:
        return write_text('Назовите свой адрес', buttons=[button(address, suggest=True)],
                          state={'screen': 'i_need_your_adress'})
    else:
        return write_text('Назовите свой адрес', state={'screen': 'i_need_your_adress'})


def def_open_bridge_event(event):
    return write_text('скоро я смогу расказать про открытые мосты')


def def_close_bridge_event(event):
    return write_text('скоро я смогу расказать про закрытые мосты')


def def_i_need_help(event):
    return write_text(
        'Я помогу вам узнать о графике разведения мостов в Петербурге. Чтобы узнать график конкретного моста, скажите его название. Чтобы узнать график ближайшего к вам моста, скажите ближайший мост, а затем адрес своего местоположения.Вы можете запросить список разводных мостов. Для этого скажите наведенные мосты, разведенные мост или все мосты.Если хотите узнать, какие мосты самые красивые и на разведение каких мостов стоит взглянуть — попросите меня порекомендовать красивые мосты.Информацию о графике разводок беру у СПб ГБУ «Мостотрест». Спасибо им!',
        buttons=[
            button("Ближайший", suggest=True),
            button("Наведенные сейчас", suggest=True),
            button("Самые популярные", suggest=True),
            button("Разведенные сейчас", suggest=True),
            button("Список всех мостов", suggest=True),
            button("Хватит", suggest=True),
        ])


def def_i_am_here_event(event):
    intent = event['request']['nlu']['intents']['i_am_here']
    adress = intent['slots']['geo']['value']
    text = ""
    for i in adress:
        text += adress[i]
    user_pos = coordinates.get_geocode(text)[0]
    nearest_bridge = coordinates.get_nearest_bridge(user_pos)
    phrase, condition = get_phrase(nearest_bridge.name)
    # condition = 1 для теста на разведённый мост
    if condition == 0:
        return write_text(
            phrase + ". Для выхода из навыка скажите хватит. Если вас интересует другой разводной мост скажите его название",
            buttons=[
                button("Ближайший мост", suggest=True),
                # проверка спрашивал ли он про дворцовый или тучков мост если да то заменить названия
                button("Дворцовый мост", suggest=True),
                button("Тучков мост", suggest=True),
                button("Я не знаю названий", suggest=True),
            ], geo=text)
    elif condition == 1:
        return write_text(
            "Ближайший к вам мост — " + nearest_bridge.name + " , сейчас разведен, будет наведен в $TIME. Ближайший к вам наведенный мост — $NEAREST_OPEN_BRIDGE_NAME. Рассказать про него подробнее?",
            buttons=[
                button("да рассказать", suggest=True),
                # проверка спрашивал ли он про дворцовый или тучков мост если да то заменить названия
                button("нет", suggest=True),
            ], state={'screen': "yes_or_not"}, geo=text, bridge=nearest_bridge.name)


def def_bridge_from_state(event):
    bridge = event.get('state').get('application', {}).get('bridge')
    phrase, condition = get_phrase(bridge)
    return (write_text(
        phrase + ". Для выхода из навыка скажите хватит. Если вас интересует другой разводной мост скажите его название",
        buttons=[
            button("Ближайший мост", suggest=True),
            # проверка спрашивал ли он про дворцовый или тучков мост если да то заменить названия
            button("Дворцовый мост", suggest=True),
            button("Тучков мост", suggest=True),
            button("Я не знаю названий", suggest=True),
        ]))


def def_bridge_event(event):
    intent = event['request']['nlu']['intents']['tell_about_bridge']
    bridge = intent['slots']['bridge']['value']
    phrase, condition = get_phrase(bridge)
    return write_text(
        phrase + ". Для выхода из навыка скажите хватит. Если вас интересует другой разводной мост скажите его название",
        buttons=[
            button("Ближайший мост", suggest=True),
            # проверка спрашивал ли он про дворцовый или тучков мост если да то заменить названия
            button("Дворцовый мост", suggest=True),
            button("Тучков мост", suggest=True),
            button("Я не знаю названий", suggest=True),
        ])


def button(text, suggest=False):
    button = {
        'title': text,
        'hide': suggest,
    }
    return button