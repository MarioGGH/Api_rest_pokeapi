from flask import Flask, render_template, request, redirect, url_for
import requests
import os
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)

API_URL = os.getenv('API_URL')
GEN1_LIMIT = 151

GENS = {
    "1": "Kanto",
    "2": "Johto",
    "3": "Hoenn",
    "4": "Sinnoh",
    "5": "Unova",
    "6": "Kalos",
    "7": "Alola",
    "8": "Galar",
    "9": "Paldea"
}

# Función para obtener la pokédex de una generación específica
def obtener_pokedex_por_generacion(gen_id):
    url = f"https://pokeapi.co/api/v2/generation/{gen_id}"
    r = requests.get(url)

    if r.status_code != 200:
        return []

    data = r.json()

    pokemons = []
    for p in data["pokemon_species"]:
        nombre = p["name"]
        # extraer ID desde la URL
        numero = int(p["url"].split("/")[-2])
        pokemons.append({
            "name": nombre,
            "id": numero
        })

    pokemons.sort(key=lambda x: x["id"])
    return pokemons

# Función para obtener la pokédex de la primera generación (151 Pokémon)
def obtener_pokedex_gen1():
    r = requests.get(f"{API_URL}?limit={GEN1_LIMIT}&offset=0")
    if r.status_code == 200:
        return r.json()["results"]
    return []

# Función para obtener los detalles de un Pokémon por su número
def obtener_pokemon(numero):
    r = requests.get(f"{API_URL}/{numero}")
    if r.status_code == 200:
        return r.json()
    return None

# Rutas de la aplicación
@app.route("/")
def index():
    gen = request.args.get("gen", "1")  
    pokedex = obtener_pokedex_por_generacion(gen)

    return render_template(
        "index.html",
        pokedex=pokedex,
        gen_actual=gen,
        gens=GENS
    )
# Ruta para manejar la búsqueda de Pokémon por nombre o número
@app.route("/buscar", methods=["POST"])
def buscar():
    query = request.form.get("query").lower()
    gen = request.form.get("gen", "1")

    pokedex = obtener_pokedex_por_generacion(gen)

    if query.isdigit():
        num = int(query)
        for p in pokedex:
            if p["id"] == num:
                return redirect(url_for("pokemon", numero=num))
    else:
        for p in pokedex:
            if p["name"] == query:
                return redirect(url_for("pokemon", numero=p["id"]))

    return redirect(url_for("index", gen=gen))

# Ruta para mostrar los detalles de un Pokémon específico
@app.route("/pokemon/<int:numero>")
def pokemon(numero):
    data = obtener_pokemon(numero)
    if not data:
        return redirect(url_for("index"))

    anterior = numero - 1 if numero > 1 else None
    siguiente = numero + 1

    return render_template(
        "pokemon.html",
        pokemon=data,
        anterior=anterior,
        siguiente=siguiente
    )


if __name__ == "__main__":
    app.run(debug=True)
