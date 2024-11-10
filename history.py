import sqlite3
import os
from datetime import datetime
import json

FILE = "output_file.json"

def update_json(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
def read_json():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)
def upadte_history():
    history_path = os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data\Default\History"

    if not os.path.exists(history_path):
        print("Файл истории не найден. Убедитесь, что Chrome закрыт.")
        exit()
    
    conn = sqlite3.connect(history_path)
    cursor = conn.cursor()
    query = """
    SELECT
        urls.url,
        urls.title
    FROM
        urls
    """

    cursor.execute(query)
    data = cursor.fetchall()

    data_loaded = read_json()
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            for url, title in data:
                if url.split('=')[0] == "https://music.youtube.com/watch?v":
                    adress = url.split('/')[3].split('=')[1].split('&')[0]
                    print(url)
                    if adress not in data_loaded:
                        data_loaded[adress] = {"title": title[:max(0,len(title) - 16)], "downloaded" : False}
            json.dump(data_loaded, f, ensure_ascii=False, indent=4)
    except Exception as exc:
        print(exc)
        update_json(data_loaded)
            
    # Закрываем соединение с базой данных
    conn.close()

    print(f"История успешно экспортирована в {FILE}")
    return(data_loaded)
