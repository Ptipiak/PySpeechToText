import logging
import azure.cognitiveservices.speech as speechsdk
import requests

log = logging.getLogger("simpleExample")

class ApiRequester():

    def __init__(self, speech_key, service_region):
        log.info("API Requester initialized")
        self.speech_config = self.getConfig(speech_key, service_region)

    def getConfig(self, speech_key, service_region):
        return speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    
    def getAudioInput(self, file_path):
        return speechsdk.AudioConfig(filename=file_path)

    def getAudioRecognizer (self, speech_config, audio_input):
        return speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    def getRecognizer(self, file_path, speech_config=None):
        if speech_config is None: speech_config = self.speech_config
        return self.getAudioRecognizer(speech_config,self.getAudioInput(file_path))        

    def requestUri(self, uri):                
        respons = requests.get(uri)
        log.debug(respons.content)
        log.info(respons.headers)