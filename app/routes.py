from flask import request
from app import app
from app.LLMResponse import LLMConnector


@app.route('/')
@app.route('/index',methods=['GET'])
def index():
    scenario = request.args.get("message")
    llm = LLMConnector(scenario=scenario)
    response = {
        "status":"success",
        "message":llm.LLMResponseGenerator()
    }
    return response