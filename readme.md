# Discord Nuke Bot
一個簡單的discord炸群機器人
## 使用方法
1.pip install discord(如果還沒安裝python請去安裝)

2.將設定填入bot.py的這段中
```py
prefix = "!"
channel_name = "nuked"
role_name = "nuked"
server_name = "Nuked Server"
webhook_name = "Nuke bot"
message = "boom"
token = "your discord bot token"
```
其他不改也沒關係，但一定要填入token

3.執行bot.py

在伺服器輸入!nuke即可炸群(請確認機器人是否有管理者權限)

如果不確定是否有管理者權限可以輸入!check來確認
