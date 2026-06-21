import sqlite3
import json

def init_db():
    conn = sqlite3.connect('gic_data.db')
    cursor = conn.cursor()
    # Hapus tabel lama agar data tidak bentrok saat restart
    cursor.execute('DROP TABLE IF EXISTS chain') 
    cursor.execute('''CREATE TABLE IF NOT EXISTS chain 
                      (id INTEGER PRIMARY KEY, data TEXT, hash TEXT, signatures TEXT)''')
    conn.commit()
    conn.close()

def save_block(block):
    conn = sqlite3.connect('gic_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chain VALUES (?, ?, ?, ?)", 
                   (block.index, json.dumps(block.data), block.hash, json.dumps(block.signatures)))
    conn.commit()
    conn.close()

def load_chain():
    conn = sqlite3.connect('gic_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chain")
    rows = cursor.fetchall()
    conn.close()
    return rows # Ini akan kita olah kembali jadi objek Block di main.py