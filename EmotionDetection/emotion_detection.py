import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        #return max(d, key=d.get), min(d, key=d.get)
        dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)

        return {
                    'anger': emotion_predictions['anger'],
                    'disgust': emotion_predictions['disgust'],
                    'fear': emotion_predictions['fear'],
                    'joy': emotion_predictions['joy'],
                    'sadness': emotion_predictions['sadness'],
                    'dominant_emotion': dominant_emotion
                }
    else:
        return {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                }