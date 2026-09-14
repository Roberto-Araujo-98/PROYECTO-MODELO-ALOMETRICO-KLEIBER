import numpy as np
import joblib

# 1. Cargar el modelo guardado previamente
model_life = joblib.load('model_life.pkl')

def predict_lifespan(mass_kg):
    # Transformar a escala logarítmica
    mass_log = np.array([[np.log10(mass_kg)]])
    
    # Hacer predicción en espacio logarítmico y convertir de vuelta
    predicted_log = model_life.predict(mass_log)[0]
    return 10 ** predicted_log

# 2. Prueba con distintos pesos
pesos_prueba = [0.05, 10.0, 70.0, 800.0]

print("=== PREDICCIONES CON MODELO CARGADO (SIN ENTRENAR DE NUEVO) ===")
for peso in pesos_prueba:
    anios = predict_lifespan(peso)
    print(f"Masa: {peso:6.2f} kg  ->  Esperanza de vida natural: {anios:5.1f} años")