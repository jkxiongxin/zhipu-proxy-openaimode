from flask import Flask, request, stream_with_context, jsonify
from flask_cors import CORS
from zhipuai import ZhipuAI
from flask import Response

app = Flask(__name__)
CORS(app) 
client = ZhipuAI(api_key="")
import json
@stream_with_context
@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    data = request.get_json()
    model = data.get('model')
    messages = data.get('messages')
    stream = data.get('stream')
    response = client.chat.completions.create(model=model, messages=messages, stream=stream)
    def generate():
        for chunk in response:
            json_string = chunk.model_dump_json() + '\n\n'
            yield json_string

    return Response(generate(), mimetype='text/event-stream')

@app.route('/v1/models', methods=['GET'])
def get_models():
    models = [{
		"id":       "glm-3-turbo",
		"object":   "model",
		"created":  1677610602,
		"owned_by": "zhipuai",
		"permission": 
			{
				"id":                   "modelperm-xa",
				"object":               "model_permission",
				"created":              1677610602,
				"allow_create_engine":  False,
				"allow_sampling":       True,
				"allow_logprobs":       True,
				"allow_search_indices": False,
				"allow_view":           True,
				"allow_fine_tuning":    False,
				"organization":         "*",
				"group":                "",
				"is_blocking":          False,
			},
		"root":   "glm-3-turbo",
		"parent": "",
	},
    {
		"id":       "glm-4",
		"object":   "model",
		"created":  1677610602,
		"owned_by": "zhipuai",
		"permission": 
			{
				"id":                   "modelperm-xa",
				"object":               "model_permission",
				"created":              1677610602,
				"allow_create_engine":  False,
				"allow_sampling":       True,
				"allow_logprobs":       True,
				"allow_search_indices": False,
				"allow_view":           True,
				"allow_fine_tuning":    False,
				"organization":         "*",
				"group":                "",
				"is_blocking":          False,
			},
		"root":   "glm-4",
		"parent": "",
	}]
    return jsonify({"data": models})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9095)