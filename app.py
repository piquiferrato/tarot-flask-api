import random

from flask import Flask, jsonify
from deck import cards

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
  endpoints = [rule.rule for rule in app.url_map.iter_rules() 
  if rule.endpoint !='static']
  
  return jsonify(dict(api_endpoints=endpoints))

@app.route('/tarot/deck/', methods=['GET'])
def getDeck():
  return jsonify({"cards": cards})

@app.route('/tarot/deck/card/<int:card_number>/', methods=['GET'])
def getCard(card_number):
  for card in cards:
    if card['id'] == card_number:
      return jsonify({"card": card})
  
  return jsonify({'message': 'Card does not exist in this deck'})


@app.route('/tarot/deck/draft/', methods=['GET'])
def dealCards():
  draft = random.sample(cards, 3)
  return jsonify({'draft': draft})

@app.route('/tarot/deck/card/random/', methods=['GET'])
def getRandomCard():
  card = random.choice(cards)
  return jsonify({'card': card})

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)