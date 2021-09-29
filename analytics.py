def create_events(request, intent_name):
    events = []
    events.append(create_event_scene(request, intent_name))
    events.append(create_event_intent(request, intent_name))
    if intent_name == "fallback":
        events.append(create_event_fallback(request))
    return events


def create_event_scene(request, intent_name):
    # scene = request["state"]["session"]["scene"]
    scene = "test scene"
    return {
        "name": "Scenes",
        "value": {
            scene: {
                intent_name: unpack_request(request)
            }
        }
    }


def create_event_intent(request, intent_name):
    # scene = request["state"]["session"]["scene"]
    scene = "test scene"
    return {
        "name": "Intents",
        "value": {
            intent_name: {
                scene: unpack_request(request)
            }
        }
    }


def create_event_fallback(request):
    original_utterance = request["request"]["original_utterance"]
    tokens = request["request"]["nlu"]["tokens"]
    return {
        "name": "Fallback",
        "value": {
            original_utterance: tokens
        }
    }


def unpack_request(request):
    command = request["request"]["command"]
    original_utterance = request["request"]["original_utterance"]
    nlu = request["request"]["nlu"]
    tokens = nlu["tokens"]
    return {
        "original to command": {
            original_utterance: command
        },
        "command to original": {
            command: original_utterance
        },
        "command to tokens": {
            command: tokens
        },
        "tokens": tokens
    }
