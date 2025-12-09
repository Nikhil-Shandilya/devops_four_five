from flask import Flask , render_template_string
app=Flask(__name__)
HTML=""""
<!DOCTYPE html>
<html>
    <head>
        <title> Event Registration new form scm echo line---- jenkin  del </title>
    </head>
    <body>
        <h1>Event Registration new form new branch</h1>
        <form>
            <p>
                <label>Name: </label> <br>
                <input type="text" required>
            </p>
                    <p>
                <label>email: </label> <br>
                <input type="email" required>
            </p>
            </p>
                    <p>
                <label>departmen2t: </label> <br>
                <input type="textl" required>
            </p>
            </p>
                    <p>
                <label>fathers name cl: </label> <br>
                <input type="textl" required>
            </p>
                        <p>
                <label>Telephone: </label> <br>
                <input type="tel" required>
            </p>
            <button type="submit">Register</button>
        </form>
    </body>
</html>
"""
@app.route("/")
def home():
    return render_template_string(HTML)
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
    