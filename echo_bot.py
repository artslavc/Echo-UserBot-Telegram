from pyrogram import Client, filters

API_ID015 = ""
API_HASH015 = ""

TARGET_USER_ID = "@username"

app = Client("my_bot", api_id=API_ID015, api_hash=API_HASH015)


@app.on_message(filters.user(TARGET_USER_ID))
def echo(client, message):
    try:
        if message.sticker:  # Если сообщение - стикер
            client.send_sticker(chat_id=message.chat.id, sticker=message.sticker.file_id)
        elif '\"' in message.text:
            client.send_message(chat_id=message.chat.id, text="Почти")
        else:
            client.send_message(chat_id=message.chat.id, text=message.text)
    except Exception as e:
         print(f"Произошла ошибка при обработке сообщения: {e}")



if __name__ == "__main__":
    print("Эхо-бот запущен...\"")
    app.run()
