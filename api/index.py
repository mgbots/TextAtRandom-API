from flask import Flask, jsonify, request
import random
import string
import time

app = Flask(__name__)

fun_facts = [
    "Honey never spoils.",
    "The first alarm clock could only ring at 4 a.m.",
    "Octopuses have three hearts.",
    "A group of flamingos is called a 'flamboyance.'",
    "Bananas are berries, but strawberries aren't.",
    "Cleopatra lived closer in time to the moon landing than to the construction of the Great Pyramid.",
    "Humans share 60% of their DNA with bananas.",
    "A day on Venus is longer than a year on Venus.",
    "Sharks have been around longer than trees.",
    "Wombat poop is cube-shaped.",
    "The shortest war in history lasted just 38 to 45 minutes.",
    "There are more stars in the universe than grains of sand on all the Earth’s beaches.",
    "Butterflies taste with their feet.",
    "A jiffy is an actual unit of time: 1/100th of a second.",
    "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
    "The inventor of the Pringles can is now buried in one.",
    "Some cats have a condition called heterochromia, where each eye is a different color.",
    "A bolt of lightning contains enough energy to toast 100,000 slices of bread.",
    "The shortest complete sentence in the English language is 'I am.'",
    "You can't hum while holding your nose closed."
]

lorem_ipsum_words = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit", "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam", "quis", "nostrud", "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea", "commodo", "consequat", "duis", "aute", "irure", "dolor", "in", "reprehenderit", "in", "voluptate", "velit", "esse", "cillum", "dolore", "eu", "fugiat", "nulla", "pariatur"
]

MASTER_KEY = "CHOOSEASECURESTRING"

tokens = {
    "REPLACE THIS": {"limit": 20, "interval": 60},  
    "REPLACE THIS": {"limit": 20, "interval": 60}, 
    "REPLACE THIS": {"limit": 20, "interval": 3600},  
}

rate_limits = {}

def rate_limit_check(api_key):
    if api_key != MASTER_KEY:
        if api_key not in rate_limits:
            rate_limits[api_key] = {'count': 0, 'start_time': time.time()}
        
        rate_limit = tokens.get(api_key, {"limit": 0, "interval": 0})
        count = rate_limits[api_key]['count']
        start_time = rate_limits[api_key]['start_time']
        
        if time.time() - start_time > rate_limit['interval']:
            rate_limits[api_key] = {'count': 1, 'start_time': time.time()}
        else:
            if count >= rate_limit['limit']:
                return jsonify({
                    "error": "Rate limit exceeded",
                    "developer": "Rate limits can be a bummer! However, you can remove all rate limits for yourself if you host it here redirect.magicgamer.xyz"
                }), 429
            rate_limits[api_key]['count'] += 1
    return None, None

@app.route('/api/funfact', methods=['GET'])
def get_fun_fact():
    api_key = request.headers.get("X-API-KEY")
    if not api_key:
        return jsonify({"error": "API key missing"}), 401

    if api_key != MASTER_KEY and api_key not in tokens:
        return jsonify({"error": "Invalid API key"}), 401

    error, status_code = rate_limit_check(api_key)
    if error:
        return error, status_code

    fact = random.choice(fun_facts)
    return jsonify({
        'fun_fact': fact,
        'developer': "Created by MG Bots 🪄, host your own at redirect.magicgamer.xyz/randomapi"
    })

@app.route('/api/randomstring', methods=['GET'])
def get_random_string():
    api_key = request.headers.get("X-API-KEY")
    if not api_key:
        return jsonify({"error": "API key missing"}), 401

    if api_key != MASTER_KEY and api_key not in tokens:
        return jsonify({"error": "Invalid API key"}), 401

    error, status_code = rate_limit_check(api_key)
    if error:
        return error, status_code

    length = request.args.get('length')
    if not length or not length.isdigit():
        return jsonify({"error": "Length parameter is required and must be an integer"}), 400
    length = int(length)

    def get_bool_param(param_name, default_value):
        param_value = request.args.get(param_name, str(default_value)).lower()
        if param_value in ['true', 'false']:
            return param_value == 'true'
        return None

    params = ['uppercase', 'lowercase', 'numbers', 'special_chars', 'random_case']
    bool_params = {}

    for param in params:
        bool_value = get_bool_param(param, False)
        if bool_value is None:
            return jsonify({"error": f"Invalid value for parameter {param}. Must be 'true' or 'false'"}), 400
        bool_params[param] = bool_value

    if bool_params['random_case']:
        bool_params['uppercase'] = True
        bool_params['lowercase'] = True

    if not (bool_params['uppercase'] or bool_params['lowercase'] or bool_params['numbers'] or bool_params['special_chars']):
        return jsonify({"error": "No character sets selected"}), 400

    characters = ''
    if bool_params['uppercase']:
        characters += string.ascii_uppercase
    if bool_params['lowercase']:
        characters += string.ascii_lowercase
    if bool_params['numbers']:
        characters += string.digits
    if bool_params['special_chars']:
        characters += string.punctuation

    random_string = ''.join(random.choice(characters) for _ in range(length))
    return jsonify({
        'random_string': random_string,
        'developer': "Created by MG Bots 🪄, host your own at redirect.magicgamer.xyz/randomapi"
    })

@app.route('/api/loremipsum', methods=['GET'])
def get_lorem_ipsum():
    api_key = request.headers.get("X-API-KEY")
    if not api_key:
        return jsonify({"error": "API key missing"}), 401

    if api_key != MASTER_KEY and api_key not in tokens:
        return jsonify({"error": "Invalid API key"}), 401

    error, status_code = rate_limit_check(api_key)
    if error:
        return error, status_code

    words = request.args.get('words', default=50, type=int)
    if words <= 0:
        return jsonify({"error": "Number of words must be greater than 0"}), 400

    lorem_ipsum_text = ' '.join(random.choice(lorem_ipsum_words) for _ in range(words))
    return jsonify({
        'lorem_ipsum': lorem_ipsum_text,
        'developer': "Created by MG Bots 🪄, host your own at redirect.magicgamer.xyz/randomapi"
    })

@app.route('/api/choosetext', methods=['POST'])
def choose_text():
    api_key = request.headers.get("X-API-KEY")
    if not api_key:
        return jsonify({"error": "API key missing"}), 401

    if api_key != MASTER_KEY and api_key not in tokens:
        return jsonify({"error": "Invalid API key"}), 401

    error, status_code = rate_limit_check(api_key)
    if error:
        return error, status_code

    data = request.json
    if not data or 'choices' not in data:
        return jsonify({"error": "Choices parameter is required"}), 400

    choices_string = data['choices']
    if not choices_string:
        return jsonify({"error": "Choices parameter cannot be empty"}), 400

    choices = choices_string.split('(/)')
    
    if len(choices) < 2:
        return jsonify({"error": "At least 2 choices are required"}), 400
    if len(choices) > 30:
        return jsonify({"error": "A maximum of 30 choices are allowed"}), 400

    selected_choice = random.choice(choices)
    return jsonify({
        'selected_choice': selected_choice,
        'developer': "Created by MG Bots 🪄, host your own at redirect.magicgamer.xyz/randomapi"
    })

if __name__ == "__main__":
    app.run()