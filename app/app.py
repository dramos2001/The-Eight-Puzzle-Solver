from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize a 3x3 empty grid
initial_values = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'reset' in request.form:
            # reset button clicked, set all values to 0
            for i in range(3):
                for j in range(3):
                    initial_values[i][j] = 0
        else:
            # update values based on user input
            for i in range(3):
                for j in range(3):
                    key = f'box_{i}_{j}'
                    try:
                        # try to convert input to integer
                        value = int(request.form[key])
                        initial_values[i][j] = value
                    except ValueError:
                        # if not a valid int, keep current value
                        pass
                
    return render_template('index.html', values=initial_values)

# @app.route('/update_cell', methods=['POST'])
# def update_cell():
#     data = request.get_json()
#     row = data['row']
#     col = data['col']
#     number = data['number']
    
#     # update grid with entered number
#     initial_grid[row][col] = number
    
#     return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
