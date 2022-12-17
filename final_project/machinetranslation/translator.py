"""
IMPORTS for project
"""
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
import os
import json
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#from ibm_watson import LanguageTranslatorV3
#from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('siQMYfoh1CR0oBvb5Q54Q9CEwVEDwPE3XOALOfVKp4j4')
language_translator = LanguageTranslatorV3(
    version='2022-12-17',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')


# translating
def english_to_french(english_text, self):
    #write the code here
    translation = self.language_translator.translate(text=english_text,
            model_id='en-fr').get_result()
    french_text=translation['translation']['-->']['translation']
    return french_text

def french_to_english(french_text, self):
    #write the code here
    translation = self.language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text=translation['translation']['-->']['translation']
    return english_text
