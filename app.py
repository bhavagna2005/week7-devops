from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        name = request.form["name"]
        student_id = request.form["student_id"]
        email = request.form["email"]

        return f"""
        <h2>Registration Successful!</h2>
        <p>Name: {name}</p>
        <p>Student ID: {student_id}</p>
        <p>Email: {email}</p>
        <br>
        <a href="/">Go Back</a>
        """

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)