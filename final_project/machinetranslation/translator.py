import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# load_dotenv()

# apikey = os.environ['Jke6XZ7cNBND6zVuKAoHLX2xgl0OzHNNByEgZ_zOi0I8']
# url = os.environ['https://api.us-south.language-translator.watson.cloud.ibm.com/instances/08c7ace4-dd1e-4cfa-bc9f-32ddb90b8f8d']


# Instance of IBM language
authenticator = IAMAuthenticator('Jke6XZ7cNBND6zVuKAoHLX2xgl0OzHNNByEgZ_zOi0I8')
language_translator = LanguageTranslatorV3(
    version='2022-30-22',
    authenticator=authenticator
)

language_translator.set_service_url("https://api.us-south.language-translator.watson.cloud.ibm.com/instances/08c7ace4-dd1e-4cfa-bc9f-32ddb90b8f8d")


# Function: englishToFrench
def english_to_french(english_text):
    translation = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text
    
# Function: frenchToEnglish
def french_to_english(french_text):
    translation = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text
