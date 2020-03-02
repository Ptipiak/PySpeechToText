from azure.cognitiveservices.speech import speech as speechsdk
from api.apiRequester import ApiRequester

# IMPORT
from os import path, sys
import logging, logging.config

# GLOBAL LOGGER OR VARIABLES
ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
logging.config.fileConfig(path.join(ROOT_DIR ,'logs/loggings.conf'))

log = logging.getLogger("root")


if __name__ == "__main__":
                 
    audio_file = path.join(ROOT_DIR, 'ressources/test_audio_fr.wav')
    result = None

    log.debug('Audio file: ' + audio_file)
    log.debug('Key: ' + sys.argv[1])

    api = ApiRequester(sys.argv[1], 'francecentral')
    speech_recognizer = api.getRecognizer(audio_file)

    result = speech_recognizer.recognize_once()

    if result is None:         
        log.info("Exited without any call to the API")
        sys.exit()

    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        log.info("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        log.warn("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        log.error("Speech Recognition canceled: {}".format(cancellation_details.reason))        
        log.error("Error details: {}".format(cancellation_details.error_details))