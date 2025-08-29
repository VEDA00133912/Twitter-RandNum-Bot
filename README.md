# Twitter-RandNum-Bot
Twitterに **1〜140桁のランダムな数字** を定期的に投稿するBOTです。  

---

## 🚀 機能
- 起動時にランダム数字を 1 回ツイート
- その後**90 分ごと** に自動投稿（1日16回）
- Freeプランのを使ってるから90分ごとにしてるだけなので、上位プランになったら好きに変えてください

---

## 📦 必須
- Python >=3.9
- X Developer Platformアプリ
  - **Read and Write 権限**
  - **Access Token & Secret**
  - **API Key & Secret**
  - **Bearer Token**
- package
  - tweepy
  - python-dotenv
  - schedule


---

## 🔑 環境変数 (.env)
以下の値を `.env` に設定してください
```
BEARER_TOKEN=xxxxxxxxxxxxxxxx
API_KEY=xxxxxxxxxxxxxxxx
API_KEY_SECRET=xxxxxxxxxxxxxxxx
ACCESS_TOKEN=xxxxxxxxxxxxxxxx
ACCESS_TOKEN_SECRET=xxxxxxxxxxxxxxxx
```

---

## 🖥️ 実行

```bash
git clone https://github.com/VEDA00133912/Twitter-RandNum-Bot
pip install -r requirements.txt
python main.py
```

