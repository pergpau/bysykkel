from bysykkelviser import Bysykkelviser
from flask import Flask, jsonify, request

app = Flask(__name__)
sykkelapp = Bysykkelviser()

@app.route("/api/stations", methods=['GET'])
def show_stations():
    query = request.args.get('q')
    if not query:
        query = ""
    results = sykkelapp.get_search_results(query)

    if len(results) == 0:
        return jsonify({"error": "Ingen stasjoner med navn '" + query + "' funnet."})

    return jsonify(results)


@app.route("/api/stations/<int:station_id>", methods=['GET'])
def show_station_by_id(station_id):
    station_id = str(station_id)
    results = sykkelapp.get_station_from_id(station_id)

    if len(results) == 0:
        return jsonify({"error": "Ingen stasjon med ID: '" + station_id + "' funnet." })
 
    return jsonify(results)


@app.errorhandler(404) 
def page_not_found(error):
    return jsonify({"error":"404 - Ugyldig URI. Sjekk API-instruks på https://github.com/pergpau/bysykkel"})


@app.errorhandler(405) 
def invalid_method(error):
    return jsonify({"error":"405 - Ugyldig metode. Sjekk API-instruks på https://github.com/pergpau/bysykkel"})

if __name__ == '__main__':
    app.run()