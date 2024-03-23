import streamlit as st
from env import API_KEY
import openai


client = OpenAI(api_key=API_KEY)


st.title('Corrector Gramatical 📝')


st.write(
    "¡Bienvenido al Corrector Gramatical! Esta aplicación te permite corregir tus textos gramaticalmente. "
    "Solo tienes que escribir tu texto en la caja de texto a continuación y hacer clic en el botón 'Corregir'."
)


texto_usuario = st.text_area("Ingresa tu texto aquí:")


def corregir_gramatica(texto_a_corregir):
    prompt = f"Corrige la siguiente frase gramaticalmente:\n{texto_a_corregir}\nCorrección:"

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {
        "role": "user",
        "content": prompt
    }
    ],
        max_tokens=150
    )



    texto_corregido = response.choices[0].text.strip()
    return texto_corregido


if __name__ == "__main__":
    texto_original = "Hoy hace mucho calor y me gustaria ir a la playa."
    texto_corregido = corregir_gramatica(texto_original)
    
    print("Texto original:", texto_original)
    print("Texto corregido:", texto_corregido)

st.write(
    "Nota: Este corrector gramatical utiliza la API de OpenAI. Ten en cuenta que los resultados pueden variar "
    "y es posible que no todas las correcciones sean perfectas. ¡Diviértete corrigiendo tus textos!"
)
