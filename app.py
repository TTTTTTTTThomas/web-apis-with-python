from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    """
    TODO: Render the home page provided under templates/index.html in the repository
    """
    return render_template("index.html")

@app.get("/search")
def search():
    """
    1. Capture the word that is being searched
    2. Search for the word on Google and display results
    3. If 'I'm Feeling Lucky' is pressed, redirect to the first result
    """
    query = request.args.get("q")
    btn = request.args.get("btn")

    if btn == "lucky":
        # Redirect to Google's "I'm Feeling Lucky"
        return redirect(f"https://www.google.com/search?q={query}&btnI=1")
    else:
        # Normal search
        return redirect(f"https://www.google.com/search?q={query}")

if __name__ == "__main__":
    app.run()