from flask import Flask, jsonify, request
from flask_cors import CORS
import main

app = Flask(__name__)
CORS(app)

@app.route('/summoner', methods=['GET'])
def get_summoner():
    summoner_name = request.args.get('summoner_name')
    region = request.args.get('region')
    api_key = request.args.get('api_key')
    summoner_info = main.get_summoner_info(summoner_name, region, api_key)
    return jsonify(summoner_info)

if __name__ == '__main__':
    app.run(debug=True)
