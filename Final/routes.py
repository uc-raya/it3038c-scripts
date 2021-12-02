from flask import Flask, render_template, request 


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == "POST":
    
        adjective=request.form.get('adjective')
        verb=request.form.get('verb')
        adjective2=request.form.get('adjective2')
        pluralNoun=request.form.get('pluralNoun')
        food=request.form.get('food')
        pluralNoun=request.form.get('pluralNoun')
        adjective3=request.form.get('adjective3')
        animal=request.form.get('animal')
        
        return "Many think a lonely ghost of this " + adjective + " town has been haunting christmas shops and causing owners to " + verb + ". Recently, there has been a shortage of " + adjective2 + " Christmas trees. Many suspect that the ghost is behind this. It can only come out at night and some in the town say you if you leave out " + food + ", then it will leave you alone. After a while, the town noticed a smell of " + pluralNoun + " coming from a " + adjective3 + " house. When the town sheriff checked the house, he found a " + animal + ". He also found all of the stolen Christmas trees." 
       
  
    
    return render_template("welcome.html")



app.run(debug=True, port=5000, host='0.0.0.0')
