# Escuela EPI — aplicación Streamlit

Publica el HTML original de la Escuela de Feminismo de Datos e Indicadores Cotidianos de Paz sin modificar su diseño ni sus interacciones.

## Archivos

- `app.py`: página de Streamlit que presenta la herramienta.
- `static/escuela.html`: HTML original (sin cambios).
- `.streamlit/config.toml`: habilita la publicación de archivos estáticos.
- `requirements.txt`: versión mínima de Streamlit.

## Publicación gratuita con Streamlit Community Cloud

1. Descomprime el ZIP y crea un repositorio en GitHub.
2. Sube **el contenido de esta carpeta** a la raíz del repositorio. Es importante incluir la carpeta oculta `.streamlit`.
3. En https://share.streamlit.io, selecciona «Create app», tu repositorio y `app.py` como archivo principal.
4. Publica y abre el enlace terminado en `.streamlit.app`.

La aplicación integra el HTML dentro de un iframe de altura fija. Para disfrutar la navegación sin doble barra de desplazamiento, usa el enlace «Abrir herramienta en una pestaña completa» situado encima del iframe.

## Enlace directo al HTML

Cuando la aplicación esté publicada, también puedes compartir:

`https://TU-APP.streamlit.app/app/static/escuela.html`

Es una página completa con el aspecto original y sin barras de Streamlit. **No** cambies la ruta `/app/static/` salvo que adaptes el archivo `app.py`.

## Ejecución local

```bash
pip install -r requirements.txt
streamlit run app.py
```

Abre http://localhost:8501 y, para la página completa, http://localhost:8501/app/static/escuela.html.

## Consideraciones

- El contenido es estático y no guarda información ni progreso de las personas visitantes.
- Para actualizar textos, datos o piezas, edita y reemplaza `static/escuela.html` en GitHub.
- El HTML carga fuentes desde Google Fonts y contiene enlaces a páginas externas; requieren internet.
- Usa solamente HTML de confianza porque `st.iframe` permite ejecutar su JavaScript.
- Como alternativa, si no necesitas Python, puedes publicar directamente el HTML como `index.html` con GitHub Pages.
