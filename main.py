from js import document
from pyscript import display

#Computing the average using codes from the practice lesson
def compute_average(e):
    grade1 = float(document.getElementById("g1").value)
    grade2 = float(document.getElementById("g2").value)   
    average = (grade1 + grade2) / 2
    display(f"Average: {average:.2f}", target="comp_avg")

# to verify if you passed or failed
    if average >= 90:
        message = "Passed :)"
    elif average >= 80:
        message = "Passed but can do better!" # a reminder to do better
    else:
        message = "Failed :O"
    display(message, target="result_output")

# to clear the input fields and their output
def clear_fields(event=None):
    document.getElementById("g1").value = ""
    document.getElementById("g2").value = ""
    document.getElementById("comp_avg").innerText = ""
    document.getElementById("result_output").innerText = ""