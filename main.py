import time
import json
import threading
import MetaTrader5 as mt5

def run_account(acc):
    login = acc["login"]
    password = acc["password"]
    server = acc["server"]

    if not mt5.initialize(login=login, password=password, server=server):
        print(f"❌ Failed to connect account {login}")
        return

    print(f"✅ Connected account {login}")

    while True:
        account_info = mt5.account_info()
        if account_info:
            print(f"📊 Account {login} | Balance: {account_info.balance}")
        time.sleep(60)

# Load accounts
with open("accounts.json", "r") as f:
    accounts = json.load(f)

threads = []
for acc in accounts:
    t = threading.Thread(target=run_account, args=(acc,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

