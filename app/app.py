from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import random
import pickle
import os

app = Flask(__name__)

# Load the dataset
data = pd.read_csv('demodata.csv')

# Load the models
model_paths = ['/Users/skyleraliya/Recommendation_of_medicine_by_drug_reviews_NLP/app/logistic_regression_model.pkl']
models = [pickle.load(open(model_path, 'rb')) for model_path in model_paths]

@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, ''), 'index.html')

@app.route('/compare', methods=['GET'])
def compare_models():
    try:
        # Get a random sample from the dataset
        sample_index = random.randint(0, len(data) - 1)
        sample_text = data.iloc[sample_index]['text']

        # Get predictions from all models
        results = {}
        for i, model in enumerate(models):
            prediction = model.predict([sample_text])[0]
            results[f'model_{i+1}'] = prediction

        return jsonify({
            'sample_text': sample_text,
            'results': results
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/compare/<int:sample_index>', methods=['GET'])
def compare_models_with_index(sample_index):
    try:
        if sample_index < 0 or sample_index >= len(data):
            return jsonify({'error': 'Invalid sample index'}), 400

        sample_text = data.iloc[sample_index]['text']

        # Get predictions from all models
        results = {}
        for i, model in enumerate(models):
            prediction = model.predict([sample_text])[0]
            results[f'model_{i+1}'] = prediction

        return jsonify({
            'sample_text': sample_text,
            'results': results
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)