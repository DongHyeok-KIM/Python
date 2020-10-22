from flask import Flask
from flask import render_template, request, jsonify
from model.ai_service import AiService
#from model.blood import Model
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kimch',methods=["post"])
def cabbage():
    ai = AiService()
    result = ai.service()
    render_params = {}
    render_params['result'] = result
    return render_template('index.html',**render_params)



    '''
    @app.route('/blood',methods=['POST'])
    def blood():
        weight = request.form['weight']
        age = request.form['age']
        print('넘어온 몸무게 : {}, 나이 : {}'.format(weight, age))
        model = Model('model/data/data')
        raw_data = model.create_raw_data()
        render_params= {}
        value = model.create_model(raw_data,weight, age)
        print('AI가 예측한 혈중농도 {}'.format(value))
        render_params['result'] = value
        return render_template('index.html', **render_params)
    
    '''


if __name__ == '__main__':
    app.debug = True
    app.run()
