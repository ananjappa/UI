from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 3
clients = [
            "Toast",
            "Shake Shack",
            "Computer Science Department",
            "Teacher's College",
            "Starbucks",
            "Subsconsious",
            "Flat Top",
            "Joe's Coffee",
            "Max Caffe",
            "Nussbaum & Wu",
            "Taco Bell"
]

sales = [
        {
            "id": 3,
            "salesperson": "James D. Halpert",
            "client": "Shake Shack",
            "reams": 100
        },
        {
            "id": 2,
            "salesperson": "Stanley Hudson",
            "client": "Toast",
            "reams": 400
        },
        {
            "id": 1,
            "salesperson": "Michael G. Scott",
            "client": "Computer Science Department",
            "reams": 1000
        }
]


@app.route('/')
def welcome():
   return render_template('welcome.html')

@app.route('/infinity')
def log_sales():
   return render_template('log_sales.html', sales=sales, clients=clients)

@app.route('/save_sale', methods=['GET', 'POST'])
def save_sale():
    global sales
    global clients
    global current_id

    json_data = request.get_json()
    salesperson = json_data["salesperson"]
    client = json_data["client"]
    reams = json_data["reams"]

    # add new entry to array with
    # a new id and the name the user sent in JSON
    current_id += 1
    new_entry = {
        "id": current_id,
        "salesperson": salesperson,
        "client": client,
        "reams": reams
    }
    sales.insert(0, new_entry)
    if client not in clients:
        clients.insert(0,client)
    

    data = {'sales': sales, 'clients': clients}

    # send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data)

@app.route('/delete_sale', methods=['GET', 'POST'])
def delete_sale():
    global id
    global sales

    json_data = request.get_json()
    id = json_data["id"]

    for i, sale in enumerate(sales):
        if id == sale["id"]:
            del sales[i]


    # send back the WHOLE array of data, so the client can redisplay it
    return jsonify(sales=sales)



if __name__ == '__main__':
   app.run(debug = True)