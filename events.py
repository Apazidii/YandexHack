import analytics

def send_response(request, response_msg, intent_name):
    return {
    'response': {
        'text': response_msg,
    },
    "analytics": {
        "events": analytics.create_events(request, intent_name)
    },
    'version': '1.0',
}


# def faile_to_recognize(request, response_msg):
#     return {
#         'response': {
#             'text': response_msg,
#         },
#         "analytics": {
#             "events": {
#                 ""
#             }
#         },
#         'version': '1.0',
#     }