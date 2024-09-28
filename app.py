from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        @app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Process the input data here
        # Your logic for calculating grades
        # Return results to the template
        try:
            # Get input values
            absences = int(request.form['absences'])
            prelim_grade = float(request.form['prelim_grade'])
            quizzes_grade = float(request.form['quizzes_grade'])
            requirements_grade = float(request.form['requirements_grade'])
            recitation_grade = float(request.form['recitation_grade'])

            # Check for absence failure
            if absences >= 4:
                result = "FAILED due to too many absences."
            else:
                # Calculate attendance
                attendance_grade = 100 - (10 * absences)

                # Class standing calculation
                class_standing = (0.4 * quizzes_grade +
                                  0.3 * requirements_grade +
                                  0.3 * recitation_grade)

                # Prelim grade calculation
                prelim_calculated = (0.6 * prelim_grade +
                                     0.1 * attendance_grade +
                                     0.3 * class_standing)

                # Prepare results
                result = f"Prelim Grade: {prelim_calculated:.2f}\n"
                for target in [75, 90]:
                    result += f"\nTo achieve {target}% overall grade:\n"
                    for final_grade in [0, 50, 75, 100]:
                        midterm_grade = (target - 0.2 * prelim_calculated - 0.5 * final_grade) / 0.3
                        if 0 <= midterm_grade <= 100:
                            result += f" - Midterm Grade: {midterm_grade:.2f} when Final Grade is {final_grade}\n"

        except Exception as e:
            result = f"Error: {str(e)}"
    
    return render_template('index.html', result=result)
<form id="myForm">
    <input type="text" name="inputData" required>
    <button type="submit">Submit</button>
</form>

if __name__ == '__main__':
    app.run(debug=True)
