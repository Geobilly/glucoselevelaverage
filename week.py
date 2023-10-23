from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate_weekly_average', methods=['POST'])
def calculate_weekly_average():
    data = request.get_json()
    if 'daily_averages' in data and isinstance(data['daily_averages'], dict) and len(data['daily_averages']) == 7:
        daily_averages = data['daily_averages']

        try:
            weekly_avg = sum(daily_averages.values()) / len(daily_averages)
            return jsonify({'weekly_average': weekly_avg}), 200
        except (ValueError, TypeError):
            return jsonify({'error': 'Invalid input! Please provide a dictionary with 7 numeric values.'}), 400
    else:
        return jsonify({'error': 'Invalid data format! Please provide a dictionary with 7 daily averages.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
