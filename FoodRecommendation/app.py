from flask import Flask, request, jsonify, render_template
from openai import OpenAI
app = Flask(__name__)
client = OpenAI(api_key="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")

@app.route("/", methods=['GET', 'POST'])
def index() -> str:
    if request.method == 'POST':

        weight = str(request.form['weight'])
        height = str(request.form['height'])
        dietary_goals = str(request.form['dietary_goals'])
        restrictions = str(request.form['restrictions'])
        meal_type = str(request.form['meal_type'])

        req = call_api(weight, height, dietary_goals, restrictions, meal_type)
        return render_template("testing.html", req=req)
    return render_template("testing.html")

def call_api(weight: str, height: str, dietary_goals: str, restrictions: str, meal_type: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "Act as a recipe/food guide. Keep answers 50 words or less. Don't give a greeting response or ending response AT ALL!"},
        {"role": "user", "content": f"I want you to give a recipe recommendation to a person who has a weight of {weight}, a height of {height} inches, a person with dietary goals of {dietary_goals} and a person who is {restrictions}. Give a recipe for a {meal_type} that is suited for this person. Only give out the recipe name, calories, and ingredients. DO NOT GIVE OUT INSTRUCTIONS!"}
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    app.run(debug=True, port=5000)