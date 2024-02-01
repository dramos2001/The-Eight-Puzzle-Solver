from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Initialize a 3x3 empty grid
initial_values = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

@app.route('/', methods=['GET', 'POST'])
def index():
    # print(request.method)
    # print(request.form)
    selected_algo = 'uniformCostSearch'  # default value
    
    if request.method == 'POST':
        #print(request.form)
        if 'submit' in request.form:
            # update algorithm based on user input
            selected_algo = request.form.get('flexRadioDefault', 'uniformCostSearch')
            # update values based on user input
            for i in range(3):
                for j in range(3):
                    key = f'box_{i}_{j}'
                    try:
                        # try to convert input to integer
                        value = int(request.form.get(key, 0))
                        initial_values[i][j] = value
                    except ValueError:
                        # if not valid int, keep current value
                        print("INVALID INPUT")
                        pass
                    
            # run another python file
            # subprocess.run(['python', 'main.py'])
        elif 'reset' in request.form:
            # reset button clicked, set all values to 0
            for i in range(3):
                for j in range(3):
                    initial_values[i][j] = 0
                
    # for testing purposes
    print(initial_values)
    print(selected_algo)
    
    return render_template('index.html', values=initial_values, selected_algo=selected_algo)


if __name__ == '__main__':
    app.run(debug=True)
