import sys
from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
app = Flask(__name__)
CORS(app)
sys.set_int_max_str_digits(1000000)
#put hashing print over here
@app.route('/submit', methods=['POST'])

def submit_data():
    data = request.get_json()
    u_and_p = [data['name'], data['message']]
    e1  = u_and_p[0]
    equation1 = e1
    e2 = u_and_p[1]
    equation2 = e2
    j = 0
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
        return jsonify({"message": "https://surfdoge.pro", "url":"backup"}), 200
    elif c == e:
        return jsonify({"message": "https://surfdoge.pro", "url":"backup"}), 200
    elif c == f:
        return jsonify({"message": "https://tinf0il.tech", "url":"backup"}), 200
    elif c == g:
        return jsonify({"message": "https://architecture.hillbrick.net/", "url":"backup"}), 200
    elif c == f:
        return jsonify({"message": "https://basketrandomonline.github.io/play/minecraft-1.8.8/", "url":"backup"}), 200
    elif user1 == c:
        return jsonify({"message": "https://utopia.web" }), 200
    elif c == h:
        return jsonify({"message": "https://help.goguardian.online/ ", "url":"backup" }), 200
    else:
        try:
            import cal as c
            print("Recieved")
            if equation1 != "" and equation2 == "":
                return jsonify({"message": str(c.calculator(equation1))}), 200
            elif equation1 == "" and equation2 !="":
                return jsonify({"message": str(c.calculator(equation2))}), 200
            elif equation1 != "" and equation2 !="":
                return jsonify({"message": str(c.solve_linear_equations(equation1, equation2))}), 200
        except Exception as e:
            print("Recieved")
            return jsonify({"message":f"Error evaluating expression, please check that you entered everything correctly. {repr(e)}"}), 200



@app.route('/store', methods=['POST'])
def store_data():
    data = request.get_json()
    import hashing as h
    with open("data.txt", "w") as file:
        file.write(f"{h.hashedinfo(data['name'], data['message'])} {data['url']}")
    return jsonify({"message": "stored"}), 200

# This block is for running your Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



