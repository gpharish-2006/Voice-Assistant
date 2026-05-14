from assistant.ml_model import predict_intent
from assistant.actions import perform_action


def process_command(text):

    intent = predict_intent(text)

    print("Intent:", intent)

    response = perform_action(intent, text)

    return response