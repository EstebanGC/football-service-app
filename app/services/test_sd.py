import soccerdata as sd
import sys

try:
    print("Iniciando prueba de SoccerData...")
    # Probamos el método que dice la documentación
    ligas = sd.ESPN.available_leagues()
    print(f"Ligas encontradas: {ligas}")
except Exception as e:
    print(f"Error detectado: {type(e).__name__} - {e}")
    # Si falla, intentamos la forma alternativa
    try:
        print("Intentando forma alternativa...")
        espn = sd.ESPN()
        print(f"Ligas via instancia: {espn.leagues}")
    except Exception as e2:
        print(f"Segundo error: {e2}")