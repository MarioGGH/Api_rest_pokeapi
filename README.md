# API REST PokeAPI

API REST desarrollada para consumir información pública de la *PokéAPI (Pokémon API)* y exponerla en un backend propio con funcionalidades personalizadas.

---

## 📌 Descripción

Esta aplicación es un servicio backend que consume la **PokéAPI**, una API REST pública que proporciona datos detallados del universo Pokémon, como nombres, habilidades, tipos, estadísticas, sprites y más. :contentReference[oaicite:1]{index=1}

El propósito del proyecto es demostrar la creación de un servidor REST propio que realiza peticiones a una API externa, procesa la respuesta y expone endpoints propios que pueden ser reutilizados por clientes o aplicaciones frontend.

---

## 🛠️ Tecnologías Utilizadas

- **Python** – Lenguaje de programación principal  
- **Web.py** – Framework minimalista para manejo de rutas y servidor web  
- **PokéAPI** – API pública de datos Pokémon (consumida) :contentReference[oaicite:2]{index=2}  
- **JSON** – Formato de intercambio de datos  
- **Git** – Control de versiones  
- **HTML / CSS / JavaScript** – Estructura mínima de presentación (si aplica)

---

## 🚀 Instalación

Antes de correr la API, asegúrate de tener Python instalado en tu entorno.

1. Clonar el repositorio:

```bash
git clone https://github.com/MarioGGH/Api_rest_pokeapi.git
cd Api_rest_pokeapi
python -m venv venv
```
2. Crear y activar entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # macOS/Linux
```
3. Instalar dependencias:
```bash
pip install -r requirements.txt
```
4. Ejecutar el servidor:
```bash
python app.py
```
