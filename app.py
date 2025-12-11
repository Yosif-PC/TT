from flask import Flask, render_template, request,jsonify
#import os
app = Flask(__name__)

# Simple in-memory storage for recent submissions (not persistent)
submissions = []


@app.route('/', methods=['get'])
def home():
    """Serve the main Home page."""
    return render_template('Home.html')

TotalOrder = []


@app.route('/Accept_Orders', methods=['GET', 'POST'])
def Accept_Orders():
    

    folder_path = "Accept_Orders"

    # الحصول على أسماء الملفات بدون الامتداد
    #Order_List = [os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith(".txt")]

    return render_template('Accept_Orders.html',Order_List=Order_List)


def Order_load(place,num):
    loaded_matrix=[]
    with open(f"{place}/{num}.txt", "r") as f:
        for line in f:
            loaded_matrix.append(line.strip().split(","))
    return loaded_matrix




@app.route('/Accept_Orders/<num>')
def order(num):
    return render_template('Accept_Orders_View.html',TotalOrder=Order_load('Accept_Orders',num))


@app.route('/Archive', methods=['post'])
def Archive():
    return render_template('Archive.html')


@app.route('/Clients', methods=['post'])
def Clients():
    return render_template('Clients.html')


@app.route('/Cooking', methods=['post'])
def Cooking():
    return render_template('Cooking.html')


@app.route('/Delivery', methods=['post'])
def Delivery():
    return render_template('Delivery.html')

Clients_List=["يوسف","أحمد","محمد","سعيد","خالد","علي","يوسف","أحمد","محمد","سعيد","خالد","علي"]
Products_List=["بيتزا","برجر","سلطة","مشروب","حلويات"]
prices_List=[50,30,20,10,15]

@app.route('/New_Order',methods=['GET', 'POST'])
def New_Order():

    return render_template('New_Order.html',Clients=Clients_List,Products=Products_List)


@app.route('/receive_NewOrderData', methods=['POST'])
def receive_NewOrderData():
    global TotalOrder
    data = request.get_json()
    TotalOrder=data['TotalOrder']
    print("📋 تم استلام مصفوفة النتائج:")
    print(TotalOrder)  # ستكون قائمة أرقام فقط [5,17,12,...]

    with open(f"Accept_Orders/( {TotalOrder[0][0]} ) {TotalOrder[0][1]}.txt", "w") as f:
        for row in TotalOrder:
            f.write(",".join(map(str, row)) + "\n")
            print(12)
    return jsonify(message="تم استلام المصفوفة بنجاح ✅")



@app.route('/process_array', methods=['POST'])
def process_array():
    arr = request.json['Choice_P']  # استقبال المصفوفة
    return jsonify({'result': prices_List[Products_List.index(arr)]})  # إرجاع النتيجة كـ JSON






@app.route('/Pended_Orders', methods=['post'])
def pended_Orders():
    return render_template('Pended_Orders.html')


@app.route('/Products', methods=['post'])
def Products():
    return render_template('Products.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

#<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Yosif-PC/MY_CSS@main/style.css">