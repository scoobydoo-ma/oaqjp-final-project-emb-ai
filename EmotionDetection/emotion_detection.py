import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        all_emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = all_emotions['anger']
        disgust_score = all_emotions['disgust']
        fear_score = all_emotions['fear']
        joy_score = all_emotions['joy']
        sadness_score = all_emotions['sadness']
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion

    elif response.status_code == 400:
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return emotions