from flask import Flask
from offers import n_factory, flyingfolk, flyingmachines, fpv24


app = Flask(__name__)

@app.get('/<query>')
def search(query):
    return [
        n_factory.get_offer(query),
        flyingfolk.get_offer(query),
        flyingmachines.get_offer(query),
        fpv24.get_offer(query)
    ]

if __name__ == '__main__':
    app.run(debug=True, port=8080)
