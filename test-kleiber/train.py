import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
from data import get_mammals_dataset

# 1. Cargar datos
df = get_mammals_dataset()

# Omitimos al humano para que no altere la regla natural del modelo
df_wild = df[df['species'] != 'Humano (Teórico)']

# 2. Transformación Logarítmica (log10)
# log10(Y) = log10(a) + b * log10(M)
X_log = np.log10(df_wild[['mass_kg']])
y_hr_log = np.log10(df_wild['heart_rate_bpm'])
y_life_log = np.log10(df_wild['lifespan_years'])

# 3. Entrenar los modelos
model_hr = LinearRegression().fit(X_log, y_hr_log)
model_life = LinearRegression().fit(X_log, y_life_log)

# 4. Guardar los modelos entrenados
joblib.dump(model_hr, 'model_hr.pkl')
joblib.dump(model_life, 'model_life.pkl')

print("=== PENDIENTES APRENDIDAS VS TEORÍA ===")
print(f"Ritmo cardíaco (b):  {model_hr.coef_[0]:.4f}  |  Teórico Kleiber: -0.2500")
print(f"Longevidad (b):     {model_life.coef_[0]:.4f}  |  Teórico Kleiber:  0.2500\n")

# 5. Evaluación de la anomalía del Humano Real
human_mass_log = np.array([[np.log10(70.0)]])

predicted_hr = 10 ** model_hr.predict(human_mass_log)[0]
predicted_life = 10 ** model_life.predict(human_mass_log)[0]

print("=== PREDICCIÓN NATURALEZA PURA (HUMANO 70 kg) ===")
print(f"Ritmo cardíaco estimado: {predicted_hr:.1f} bpm")
print(f"Esperanza de vida estimada: {predicted_life:.1f} años")
print(f"Esperanza de vida real (con civilización): ~80.0 años")
print(f"Factor de desacople (Tecnología): x{80.0 / predicted_life:.2f}")