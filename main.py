import sys
from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
app = Flask(__name__)
CORS(app)
#put hashing print over here

# db = SQLAlchemy()
#username module

@app.route('/submit', methods=['POST'])

def submit_data():
    data = request.get_json()
    u_and_p = [data['name'], data['message']]
    import hashing as h
    c = h.hashedinfo(u_and_p[0], u_and_p[1])
    print("Received data:", data)
    response = {"message": "some data"}
    print(data)
    d = ["a226abda121d6a22bbb9d858a94c9ce1","55be20677b1caac1b4d53058800b06ef"]
    e = ['e2884f8636953a76dc7833ec63f081f3', 'eeaf08b96e493abb74af595db835f36c'] #ilovedogs, 1oi6bm
    f = ['3ed6d0fac7dcd33714fed5c9d3b0076f', '38659adc997e4898eb812b2de57e5297'] #tinf0il, tinfoil
    g = ['7d128fea364420e74c62bff0fa777a36', 'afc5d26d56f3993ecb8266d96a50c4fd'] #spacestation123, b98z'
    f = ['80c165da28ef540ec718180695b41916', '10d18a6f7fd9865c6c23499dab51b445'] #minecraft, shovel
    h = ['000a3352aa1b21a30f2569ad399d322a', '9d3cd00c6511b76f9af5dc8e32548677'] #somebody, at the cheese

    #user registered usernames and passwords here(they stay a secret)
    user1 = ['fe5e4de02ea301f33e0a1d6d641fa00d', '22b4b30d83b55ed336059f7051446503']

    if c == d:
        return jsonify({"message": "https://surfdoge.pro"}), 200
    elif c == e:
        return jsonify({"message": "https://surfdoge.pro"}), 200
    elif c == f:
        return jsonify({"message": "https://tinf0il.tech"}), 200
    elif c == g:
        return jsonify({"message": "https://architecture.hillbrick.net/"}), 200
    elif c == f:
        return jsonify({"message": "https://basketrandomonline.github.io/play/minecraft-1.8.8/"}), 200
    elif user1 == c:
        return jsonify({"message": "https://utopia.web" }), 200
    elif c == h:
        return jsonify({"message": "https://help.goguardian.online/ " }), 200
    else:
        return jsonify({"message": "do normal"}), 200




# This block is for running your Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
