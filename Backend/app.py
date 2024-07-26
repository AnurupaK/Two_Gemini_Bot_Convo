
from flask import Flask, request, jsonify, render_template
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI_Service')))

from gemini_response import update_models, get_gemo_response, get_gemi_response, reset_chat_session, conversation_history

# Creating Flask app instance
app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')

# Frontend integration
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint for generating responses
@app.route('/api/sendPrompt', methods=['POST'])
def send_prompt():
    data = request.get_json()
    gemo_instruction = data.get('gemoSelectedPrompt')
    gemi_instruction = data.get('gemiSelectedPrompt')
    message = data.get('message')

    # Debugging statements to check the values
    print(f"gemo_instruction: {gemo_instruction}")
    print(f"gemi_instruction: {gemi_instruction}")

    if gemo_instruction is None or gemi_instruction is None:
        return jsonify({'error': 'Invalid input'}), 400

    # Update models with new prompts
    update_models(gemo_instruction, gemi_instruction)
    
    message = 'Sent successfully'
    print(f"message: {message}")
    
    return jsonify({'message': message})

@app.route('/api/get_response_fromBots', methods=['POST'])
def BotResponse():
    global conversation_history
    print("CONVERSATION HISTORY", conversation_history)
    gemi_response = ""
    gemo_response = ""
    
    if conversation_history:
        gemi_response = get_gemi_response(conversation_history[-1])
        gemo_response = get_gemo_response(gemi_response)
        conversation_history.append(gemo_response)
    
    return jsonify({'gemi': gemi_response, 'gemo': gemo_response})

reset_chat_session()

if __name__ == '__main__':
    app.run(debug=True)
