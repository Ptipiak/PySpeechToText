import sys, logging, logging.config, requests
import azure.cognitiveservices.speech as speechsdk
from os import path

ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
logging.config.fileConfig(path.join(ROOT_DIR ,'logs/loggings.conf'))
log = logging.getLogger("simpleExample")

class ApiRequester():

    def __init__(self, speech_key, service_region):
        log.info("API Requester initialized")
        self.speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)              
    
    def getAudioInput(self, file_path):
        return speechsdk.AudioConfig(filename=file_path)

    def getAudioRecognizer (self, speech_config, audio_input):
        return speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    def preparereRecognition(self, file_path, speech_config=None):
        if speech_config is None: speech_config = self.speech_config
        return self.getAudioRecognizer(speech_config,self.getAudioInput(file_path))        

    def requestUri(self, uri):                
        respons = requests.get(uri)
        log.debug(respons.content)
        log.info(respons.headers)

    

if __name__ == "__main__":
                 
    audio_file = path.join(ROOT_DIR, 'ressources/test_file_en.wav')
    result = None

    log.debug(audio_file)

    api = ApiRequester(sys.argv[0], "francecentral")    
    speech_recognizer = api.preparereRecognition(audio_file)

    result = speech_recognizer.recognize_once()

    if result is None:         
        log.info("Exited without any call to the API")
        sys.exit()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        log.info("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        log.info("No speech could be recognized: {}".format(result.no_match_details))
    
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        log.error("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        log.error("Error details: {}".format(cancellation_details.error_details))
        log.error("Error details: {}".format(cancellation_details.err))

    



    
