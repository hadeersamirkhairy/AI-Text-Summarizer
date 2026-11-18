from flask import Flask, request, render_template
from ai_service import summarize_text

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/summarize", methods=["POST"])
def summarize():
    user_text = request.form.get("text", "")

    if not user_text.strip():
        return "Please enter some text!", 400

    try:
        summary = summarize_text(user_text)

    except Exception:
        app.logger.exception("AI summarization failed")
        return "Unable to generate summary. Please try again.", 502
    return render_template("result.html", summary=summary)



if __name__ == "__main__":
    app.run(debug=False)
