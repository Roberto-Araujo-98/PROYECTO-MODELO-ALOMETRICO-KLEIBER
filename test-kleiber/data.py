import pandas as pd

def get_mammals_dataset():
    data = {
        'species': [
            'Ratón', 'Rata', 'Cuy', 'Gato', 'Zorro', 'Perro', 'Oveja',
            'Cerdo', 'Humano (Teórico)', 'Caballo', 'Jirafa', 'Elefante', 'Ballena Azul'
        ],
        'mass_kg': [
            0.02, 0.3, 0.8, 4.0, 6.0, 20.0, 50.0,
            100.0, 70.0, 500.0, 1200.0, 4000.0, 100000.0
        ],
        'heart_rate_bpm': [
            600, 400, 280, 150, 120, 90, 75,
            60, 70, 38, 40, 30, 10
        ],
        'lifespan_years': [
            2.0, 3.0, 5.0, 15.0, 10.0, 12.0, 12.0,
            15.0, 27.0, 30.0, 25.0, 65.0, 90.0  # Humano ajustado a ~27 años salvajes
        ]
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = get_mammals_dataset()
    df.to_csv('mammals.csv', index=False)
    print("Dataset 'mammals.csv' generado con éxito. Muestra:")
    print(df.head())