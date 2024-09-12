import requests
import multiprocessing
import time
import os
import sys
from dotenv import load_dotenv
load_dotenv()

HOST = f"{os.getenv('HOST')}"
TOKEN = f"{os.getenv('TOKEN')}"

ATTDEF_SERVER = f"https://{HOST}/api/v2/"
CHALL_ID = '1'        # Change this to the challenge ID
CHALL_PORT = 0000     # Change this to the challenge port

if not TOKEN:
  print("[-] Token not found")
  sys.exit(1)

def exploit(target_ip, port):
  try:


    flag = ""
    if not flag:
      raise Exception("Flag not found")
    
    return flag
  except Exception as e:
    print(f"[-] Error: {e} ({target_ip})")

def process_exploit(target_ip, port):
  try:
    print(f"[+] Target IP: {target_ip}")
      
    flag = exploit(target_ip, CHALL_PORT)
    
    if not flag:
      print(f"[-] Exploit failed ({target_ip})")
      return
      
    print(f"[+] Flag: {flag}")
      
    requests.post('http://localhost:3000/submit', json={'flag': [flag]})
  except Exception as e:
    print(f"[-] Error: {e}")

def main():
  target_ip_list = requests.get(ATTDEF_SERVER + "services", headers={'Authorization': f'Bearer {TOKEN}'}).json()['data'][CHALL_ID]

  # target_ip_list = {
  #   "1": "10.10.0.1",
  #   "2": "10.10.0.2",
  # }
  
  timer = 0
    
  while True:
    if timer > 0:
      print(f"[+] Next Exploit in: {timer} seconds", end="\r")
      timer -= 1
      time.sleep(1)
      continue
    
    for target_id, target_ip in target_ip_list.items():
      process = multiprocessing.Process(target=process_exploit, args=(target_ip, CHALL_PORT))
      process.start()

    timer = 300 # Tick in seconds

if __name__ == "__main__":
  main()