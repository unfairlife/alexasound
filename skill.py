import logging
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.ui import PlayBehavior
from ask_sdk_model import Response

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class PlaySoundIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("PlaySoundIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "Playing a sound on your Alexa device."

        handler_input.response_builder.speak(speak_output).add_audio_player_play_directive(
            play_behavior=PlayBehavior.REPLACE_ALL,
            audio_item={"stream": {"url": "https://s3.amazonaws.com/your-s3-bucket/your-sound-file.mp3",
                                   "token": "sound"}}
        )

        return handler_input.response_builder.response

sb.add_request_handler(PlaySoundIntentHandler())

def lambda_handler(event, context):
    return sb.lambda_handler()
