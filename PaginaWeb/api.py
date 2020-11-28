########  imports  ##########
import psycopg2, socket
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

HEADER = 64
PORT = 5050
SERVER = "172.29.0.30"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

premium_tax = 1.45

def send_msg(msg, client):
    #Encode msg and header
    encoded_msg = msg.encode(FORMAT)
    msg_length = len(encoded_msg)
    encoded_header = str(msg_length).encode(FORMAT)
    encoded_header += b' '*(HEADER-len(encoded_header))
    #Send msgs to server
    client.send(encoded_header)
    client.send(encoded_msg)

def get_pricesDB():
    conn = None

    try:
        conn = psycopg2.connect(
            host="db.fe.up.pt",
            database="up201504961",
            user="up201504961",
            password="32FiuJr2X")

        cur = conn.cursor()
        cur.execute("SELECT id FROM seai.historic")
        row = cur.fetchone()
        
        #i = 0

        #while row is not None:
        value = row[0]
        #    i += 1
        #    row = cur.fetchone()

        cur.close()

        return value

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

app = Flask(__name__)

#############################
#         API setup         #
#############################

@app.route('/prices', methods=['GET'])
def priceloader():
    #GET request
    if request.method == 'GET':
        
        x = get_pricesDB()
        message = {'normal':str("{:.2f}".format(x))+' €/hora', 'premium':str("{:.2f}".format(x*premium_tax))+' €/hora'}
        return jsonify(message)  # serialize and use JSON headers


@app.route('/normal', methods=['GET'])
def normalstart():
    #GET request
    if request.method == 'GET':
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        # Send a message to the SERVER
        send_msg("ID: 202010; State: 1;", client)
        send_msg(DISCONNECT_MESSAGE, client)

        return jsonify("Normal start sent successfully!")


@app.route('/premium', methods=['GET'])
def premiumstart():
    #GET request
    if request.method == 'GET':
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        send_msg("ID: 202010; State: 2;", client)
        send_msg(DISCONNECT_MESSAGE, client)

        return jsonify("Premium start sent successfully!")


@app.route('/stop', methods=['GET'])
def stop():
    #GET request
    if request.method == 'GET':
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        send_msg("ID: 202010; State: -1;", client)
        send_msg(DISCONNECT_MESSAGE, client)

        return jsonify("Stop sent successfully!")

#########  run app  #########
CORS(app)
app.run(debug=True)    