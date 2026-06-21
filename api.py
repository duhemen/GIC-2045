from flask import Flask, jsonify, request
from blockchain import GoldenIndonesiaChain

app = Flask(__name__)
gic = GoldenIndonesiaChain()

# Endpoint untuk melihat seluruh rantai visi
@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in gic.chain:
        chain_data.append({
            "index": block.index,
            "data": block.data,
            "hash": block.hash,
            "previous_hash": block.previous_hash
        })
    return jsonify(chain_data)

# Endpoint untuk menambah pencapaian baru ke rantai
@app.route('/add_milestone', methods=['POST'])
def add_milestone():
    data = request.get_json()
    gic.add_block(data)
    return jsonify({"message": "Data Visi berhasil dikunci di rantai!", "status": "success"}), 201

if __name__ == '__main__':
    app.run(port=5000)