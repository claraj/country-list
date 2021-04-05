from flask import Flask, request, jsonify, abort
import requests 

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

world_bank_url = 'http://api.worldbank.org/v2/country?format=json&per_page=400'
response = requests.get(world_bank_url).json()
countries_regions = response[1]
countries = [ country for country in countries_regions if country['capitalCity'] ]


@app.route('/api/country', methods=['GET'])
def country_list():
    return jsonify(countries)


@app.errorhandler(404)
def not_found(e):
    return jsonify(error='Not found'), 404

