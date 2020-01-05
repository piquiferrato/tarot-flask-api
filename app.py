import random

from flask import Flask, jsonify

app = Flask(__name__)

from deck import cards

@app.route('/')
def ping():
  return "Welcome"

@app.route('/tarot/deck', methods=['GET'])
def getDeck():
  return jsonify({"cards": cards})

@app.route('/tarot/deck/card/<int:card_number>', methods=['GET'])
def getCard(card_number):
  for card in cards:
    if card['id'] == card_number:
      return jsonify({"card": card})
  
  return jsonify({'message': 'Card does not exist in this deck'})


@app.route('/tarot/deck/draft', methods=['GET'])
def dealCards():
  draft = random.sample(cards, 3)
  return jsonify({'draft': draft})


if __name__ == '__main__':
  app.run(debug=True, port=4000)