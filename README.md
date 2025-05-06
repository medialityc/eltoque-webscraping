# Feliz cumpleaños elToque, te pirateamos la API

> Api sencillita hecha con **FastApi**, que permite hacerle **web-scrapping**
> a las páginas de **elToque**.

## 😈 Página actual que se pone en 4

- [Preguntas y respuestas sobre la api de elToque](https://eltoque.com/preguntas-y-respuestas-sobre-la-api-de-eltoque).

## 🚀 Despliegues

- [Prueba en Render](https://feliz-cumpleannos-eltoque-te-pirateamos.onrender.com/docs).
- [Servers de Mdialityc]().

## 🛠️ Endpoints

- `GET /piratear-eltoque`: Te devuelve toda la info disponible de la página pirateada.
    - **Monedas**: Todas las monedas que manejan.
    - **Estadísticas**: Las tasas de cambios y bulto de cosas. `OJO`: El dato que muestran ellos es la mediana.
    - **Fecha**: La vigencia de los datos.

## ❤️ Healthcheck visual

- `GET /healthcheck`: Página que muestra el estado de salud del endpoint principal.

## 📖 Documentación

- `/docs`: Swagger de toda la vida.
- `/redoc`: Una documentación de Redocly.
- `/openapi.json`: La vida y obra de la API.
Añade una sección de instalación local al final de tu README siguiendo este ejemplo:

---

## 🖥️ Instalación y ejecución local

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/medialityc/eltoque-webscraping.git
   cd eltoque-webscraping
   ```

2. **Crea un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Arranca el servidor de desarrollo:**

   ```bash
   uvicorn main:app --reload
   ```

5. **Accede a la documentación interactiva:**

   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
