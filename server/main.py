
from flask import Flask, jsonify, request
import animal_service


app = Flask(__name__)

@app.route('/animals/last-reserve')
def animal_last_reserve():

        search_type = 'id' if request.args.get('id') else 'name'
        search_value = request.args.get(search_type)
        print(search_type,search_value)
        details = animal_service.find_last_reserve(search_type, search_value)
        print(details)
        return jsonify({
             "animal_id": details[0],
             "collar_code": details[1],
             "species": details[2],
             "nickname": details[3],
             "reserve_name": details[4],
             "region": details[5],
             "description": details[6]
                    })





if "name == __main__":
    app.run(debug=True, port=3000)
