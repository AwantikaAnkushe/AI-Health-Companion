from fastapi import FastAPI

app = FastAPI(title='AI Health Companion API')

@app.get('/health')
def health_check():
    return {'status': 'ok', 'message': 'AI service is running'}

@app.post('/predict')
def predict(symptoms: list[str]):
    return {
        'possible_conditions': ['Common Cold', 'Viral Infection'],
        'advice': 'Rest, hydrate, and monitor symptoms. This is not medical advice. Please consult a healthcare professional.'
    }
