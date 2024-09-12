import requests
import multiprocessing
import time
import os
from dotenv import load_dotenv

load_dotenv()
SUBMITTER_SERVER = f"{os.getenv('SUBMITTER_SERVER')}"
ATTDEF_SERVER = f"{os.getenv('ATTDEF_SERVER')}"
TOKEN = f"{os.getenv('TOKEN')}"

if not TOKEN:
  print("[-] Token not found")
  exit()

CHALL_ID = '1'
CHALL_PORT = 10004

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
      
    requests.post(SUBMITTER_SERVER, json={'flag': [flag]}, headers={'Authorization': f'Bearer {TOKEN}'})
  except Exception as e:
    print(f"[-] Error: {e}")

def main():
  # target_ip_list = requests.get(ATTDEF_SERVER + "services", headers={'Authorization': f'Bearer {TOKEN}'}).json()['data'][CHALL_ID]

  target_ip_list = {
    "1": "10.10.0.1",
    "2": "10.10.0.2",
  }
  
  timer = 0 # in seconds (TICK)
    
  while True:
    if timer > 0:
      print(f"[+] Next Exploit in: {timer} seconds", end="\r")
      timer -= 1
      time.sleep(1)
      continue
    
    for target_id, target_ip in target_ip_list.items():
      process = multiprocessing.Process(target=process_exploit, args=(target_ip, CHALL_PORT))
      process.start()

    timer = 300

if __name__ == "__main__":
  main()