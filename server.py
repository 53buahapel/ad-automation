from flask import Flask, request, jsonify
import requests
import os
import dotenv
import sys
dotenv.load_dotenv()

HOST = f"{os.getenv('HOST')}"
TOKEN = f"{os.getenv('TOKEN')}"

SUBMITTER_URL = f"https://{HOST}/api/flag"

app = Flask(__name__)

if not TOKEN:
  print("[-] Token not found")
  sys.exit(1)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()['flag']
    
    res = requests.post(SUBMITTER_URL, json={'flags': data}, headers={'Authorization': f'Bearer {TOKEN}'})
    
    print("[+] Response:", res.json())
    
    return jsonify(res.json())
    

if __name__ == '__main__':
  app.run(debug=False, host='localhost', port=3000)