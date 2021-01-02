########  imports  ##########
import psycopg2, socket
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

HEADER = 64
PORT = 5050
SERVER = "172.29.0.86"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

premium_tax = 1.45
green_tax = 1.6

def send_msg(msg, client):
    #Encode msg and header
    encoded_msg = msg.encode(FORMAT)
    msg_length = len(encoded_msg)
    encoded_header = str(msg_length).encode(FORMAT)
    encoded_header += b' '*(HEADER-len(encoded_header))
    #Send msgs to server
    client.send(encoded_header)
    client.send(encoded_msg)

def get_pricesDB(id):
    conn = None

    try:
        conn = psycopg2.connect(
            host="db.fe.up.pt",
            database="up201504961",
            user="up201504961",
            password="32FiuJr2X")

        cur = conn.cursor()
        cur.execute("SELECT priceper_kwh FROM seai.charger WHERE charger_id="+str(id))
        row = cur.fetchone()
        
        value = row[0]

        cur.close()

        return value

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def get_finalPrice(id):
    conn = None

    try:
        conn = psycopg2.connect(
            host="db.fe.up.pt",
            database="up201504961",
            user="up201504961",
            password="32FiuJr2X")

        cur = conn.cursor()
        cur.execute("SELECT total_cost FROM seai.charging WHERE charger_id="+str(id))
        row = cur.fetchone()
        
        value = row[0]

        cur.close()

        return value

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def check_interrupt(id):
    conn = None

    try:
        conn = psycopg2.connect(
            host="db.fe.up.pt",
            database="up201504961",
            user="up201504961",
            password="32FiuJr2X")

        cur = conn.cursor()
        cur.execute("SELECT operator_interr FROM seai.charger WHERE charger_id="+str(id))
        row = cur.fetchone()
        
        value = row[0]

        cur.close()

        return value

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def check_connection(id):
    conn = None

    try:
        conn = psycopg2.connect(
            host="db.fe.up.pt",
            database="up201504961",
            user="up201504961",
            password="32FiuJr2X")

        cur = conn.cursor()
        cur.execute("SELECT new_connection FROM seai.charger WHERE charger_id="+str(id))
        row = cur.fetchone()
        
        value = row[0]

        cur.close()

        return value

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def check_finish(id):
    conn = None

    try:
        conn = psycopg2.connect(
            host="db.fe.up.pt",
            database="up201504961",
            user="up201504961",
            password="32FiuJr2X")

        cur = conn.cursor()
        cur.execute("SELECT stoping_time FROM seai.charging WHERE charger_id="+str(id))
        row = cur.fetchone()
        
        value = row[0]

        cur.close()

        return value

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


def check_occupation(id):
    conn = None

    try:
        conn = psycopg2.connect(
            host="db.fe.up.pt",
            database="up201504961",
            user="up201504961",
            password="32FiuJr2X")

        cur = conn.cursor()
        cur.execute("SELECT state_occupation FROM seai.charger WHERE charger_id="+str(id))
        row = cur.fetchone()
        
        value = row[0]

        cur.close()

        return value

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def checkparkingslots():
    conn = None

    try:
        conn = psycopg2.connect(
            host="db.fe.up.pt",
            database="up201504961",
            user="up201504961",
            password="32FiuJr2X")

        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM seai.charger WHERE state_occupation=FALSE")
        row = cur.fetchone()
        
        value = row[0]

        cur.close()

        return value

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def checkpremium(id):
    conn = None

    try:
        conn = psycopg2.connect(
            host="db.fe.up.pt",
            database="up201504961",
            user="up201504961",
            password="32FiuJr2X")

        cur = conn.cursor()
        cur.execute("SELECT fc_availability FROM seai.charger WHERE charger_id="+str(id))
        row = cur.fetchone()
        
        value = row[0]

        cur.close()

        return value

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def checkgreen(id):
    conn = None

    try:
        conn = psycopg2.connect(
            host="db.fe.up.pt",
            database="up201504961",
            user="up201504961",
            password="32FiuJr2X")

        cur = conn.cursor()
        cur.execute("SELECT green_power FROM seai.charger WHERE charger_id="+str(id))
        row = cur.fetchone()
        
        value = row[0]

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

@app.route('/prices/<int:id>', methods=['GET'])
def priceloader(id):
    #GET request
    if request.method == 'GET':
        
        x = float(get_pricesDB(id))
        message = {'normal':str("{:.2f}".format(x))+' €/kWh', 
                   'premium':str("{:.2f}".format(x*premium_tax))+' €/kWh',
                   'green':str("{:.2f}".format(x*green_tax))+' €/kWh'}
        return jsonify(message)  # serialize and use JSON headers


@app.route('/pricesAPP/<int:id>', methods=['GET'])
def priceloaderAPP(id):
    #GET request
    if request.method == 'GET':
        
        x = float(get_pricesDB(id))
        
        message = {'normal':x,'premium':x*premium_tax,'green':x*green_tax}

        return jsonify(message)  # serialize and use JSON headers


@app.route('/finalprice/<int:id>', methods=['GET'])
def finalpriceloader(id):
    #GET request
    if request.method == 'GET':
        
        x = float(get_finalPrice(id))
        message = {'total':str("{:.2f}".format(x))+' €'}
        return jsonify(message)  # serialize and use JSON headers


@app.route('/finalpriceAPP/<int:id>', methods=['GET'])
def finalpriceloaderAPP(id):
    #GET request
    if request.method == 'GET':
        
        x = float(get_finalPrice(id))
        message = {'total':x}
        return jsonify(message)  # serialize and use JSON headers


@app.route('/normal/<int:id>', methods=['GET'])
def normalstart(id):
    #GET request
    if request.method == 'GET':
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        # Send a message to the SERVER
        send_msg("ID: "+str(id)+"; State: 1;", client)
        send_msg(DISCONNECT_MESSAGE, client)

        return jsonify("Normal start sent successfully!")


@app.route('/premium/<int:id>', methods=['GET'])
def premiumstart(id):
    #GET request
    if request.method == 'GET':
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        send_msg("ID: "+str(id)+"; State: 2;", client)
        send_msg(DISCONNECT_MESSAGE, client)

        return jsonify("Premium start sent successfully!")


@app.route('/green/<int:id>', methods=['GET'])
def greenstart(id):
    #GET request
    if request.method == 'GET':
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        # Send a message to the SERVER
        send_msg("ID: "+str(id)+"; State: 3;", client)
        send_msg(DISCONNECT_MESSAGE, client)

        return jsonify("Green start sent successfully!")


@app.route('/stop/<int:id>', methods=['GET'])
def stop(id):
    #GET request
    if request.method == 'GET':
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)

        send_msg("ID: "+str(id)+"; State: -1;", client)
        send_msg(DISCONNECT_MESSAGE, client)

        return jsonify("Stop sent successfully!")


@app.route('/interrupt/<int:id>', methods=['GET'])
def interrupter(id):
    #GET request
    if request.method == 'GET':
        
        x = check_interrupt(id)
        message = {'flag':x}
        return jsonify(message)  # serialize and use JSON headers


@app.route('/connection/<int:id>', methods=['GET'])
def connector(id):
    #GET request
    if request.method == 'GET':
        
        x = check_connection(id)
        message = {'flag':x}
        return jsonify(message)  # serialize and use JSON headers


@app.route('/finish/<int:id>', methods=['GET'])
def finisher(id):
    #GET request
    if request.method == 'GET':
        
        x = check_finish(id)

        if x != None:
            x = 1
        else: 
            x = 0

        message = {'flag':x}
        return jsonify(message)  # serialize and use JSON headers


@app.route('/checkslots/', methods=['GET'])
def slotchecker():
    #GET request
    if request.method == 'GET':

        x = int(checkparkingslots())
        message = {'slots':x}
        return jsonify(message)  # serialize and use JSON headers


@app.route('/readytocharge/<int:id>', methods=['GET'])
def initializer(id):
    #GET request
    if request.method == 'GET':

        x = check_connection(id)
        y = check_occupation(id)
        message = {'flag':x&(not(y))}
        return jsonify(message)  # serialize and use JSON headers


@app.route('/premiumavailable/<int:id>', methods=['GET'])
def premiumchecker(id):
    #GET request
    if request.method == 'GET':

        x = checkpremium(id)

        if bool(x) == True: 
            x = 1
        elif bool(x) == False: 
            x = 0

        message = {'flag':x}
        return jsonify(message)  # serialize and use JSON headers


@app.route('/greenavailable/<int:id>', methods=['GET'])
def greenchecker(id):
    #GET request
    if request.method == 'GET':

        x = checkgreen(id)

        if bool(x) == True: 
            x = 1
        elif bool(x) == False: 
            x = 0

        message = {'flag':x}
        return jsonify(message)  # serialize and use JSON headers
        

#########  run app  #########
CORS(app)
app.run(debug=True)    