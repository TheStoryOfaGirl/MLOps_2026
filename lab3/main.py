# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pickle
import numpy as np

app = FastAPI(title="Iris Classifier API", description="API для классификации ирисов")

# Загружаем модель
try:
    with open('knn_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Модель успешно загружена")
except FileNotFoundError:
    print("Ошибка: файл 'knn_model.pkl' не найден")
    raise

# Классы ирисов
IRIS_CLASSES = {
    0: "setosa",
    1: "versicolor", 
    2: "virginica"
}

# Модель данных для валидации входных параметров
class IrisFeaturesRequest(BaseModel):
    sepal_length: float = Field(..., ge=0, le=10, description="Длина чашелистика (см)")
    sepal_width: float = Field(..., ge=0, le=10, description="Ширина чашелистика (см)")
    petal_length: float = Field(..., ge=0, le=10, description="Длина лепестка (см)")
    petal_width: float = Field(..., ge=0, le=10, description="Ширина лепестка (см)")

# Модель ответа
class PredictionResponse(BaseModel):
    class_id: int
    class_name: str
    features: IrisFeaturesRequest
    message: str = "Классификация выполнена успешно"

@app.post("/predict", response_model=PredictionResponse)
async def predict_iris(features: IrisFeaturesRequest):
    """
    Классифицирует ирис на основе входных параметров.
    
    - **sepal_length**: длина чашелистика (см)
    - **sepal_width**: ширина чашелистика (см)  
    - **petal_length**: длина лепестка (см)
    - **petal_width**: ширина лепестка (см)
    """
    try:
        # Преобразуем входные данные в numpy массив
        input_data = np.array([[
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width
        ]])
        
        # Предсказываем класс
        prediction = model.predict(input_data)[0]
        
        # Получаем название класса
        class_name = IRIS_CLASSES.get(prediction, "unknown")
        
        return PredictionResponse(
            class_id=int(prediction),
            class_name=class_name,
            features=features
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при классификации: {str(e)}")