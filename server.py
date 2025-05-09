"""
Módulo principal de Flask para el despliegue de la aplicación de detección de emociones.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Renderiza la página principal con el formulario de entrada.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def analyze_emotion():
    """
    Analiza el texto proporcionado y devuelve una respuesta formateada
    con las puntuaciones de emociones y la emoción dominante.
    """
    text_to_analyze = request.args.get("text")
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"

    response = (
        f"Para la declaración dada, la respuesta del sistema es "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} y "
        f"'sadness': {result['sadness']}. "
        f"La emoción dominante es {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run()
