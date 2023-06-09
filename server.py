from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberry = request.form['strawberry'] 
    raspberry = request.form['raspberry'] 
    apple = request.form['apple'] 
    blackberry = request.form['blackberry'] 

    student_id = request.form['student_id']  
    last_name = request.form['last_name'] 
    first_name = request.form['first_name']
    print(request.form)

    return render_template("checkout.html",
    strawberry = strawberry,
    raspberry = raspberry,
    apple = apple,
    blackberry = blackberry,
    student_id = student_id,
    last_name = last_name,
    first_name = first_name
    )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    