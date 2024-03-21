import requests  # You'll likely need this library

def emotion_detector(text_to_analyze):
   url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   payload = {"raw_document": {"text": text_to_analyze}}

   response = requests.post(url, headers=headers, json=payload)

   if response.status_code == 200:
       return response.json()['text']  # Adjust the path within the response if needed
   else:
       return None  # Or handle the error differently


