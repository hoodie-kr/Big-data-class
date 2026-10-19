import os
import requests
from dotenv import load_dotenv

# 같은 폴더에 있는 .env 파일의 내용을 환경 변수로 로드합니다.
load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


def send_telegram(text: str):
    """텔레그램 봇으로 메시지를 한 통 보냅니다."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    res = requests.post(
        url,
        data={"chat_id": TELEGRAM_CHAT_ID, "text": text},
        timeout=10,
    )
    res.raise_for_status()
    return res.json()