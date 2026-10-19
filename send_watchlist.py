import csv
import requests
from telebot import send_telegram


def format_rate_badge(rate: float) -> str:
    """등락률에 따라 🔺 🔻 표시를 붙여 줍니다.
    ※ 3장에서 만든 format_rate_badge()가 있으면 이 함수를 지우고
       from notify_stock_price import format_rate_badge 로 바꿔 쓰세요."""
    if rate > 0:
        return f"🔺 +{rate:.2f}%"
    elif rate < 0:
        return f"🔻 {rate:.2f}%"
    return f"▬ {rate:.2f}%"


def load_watchlist(path="watchlist.csv"):
    """종목 목록은 코드가 아니라 watchlist.csv에서 읽습니다."""
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def get_price(code: str):
    """네이버 증권 모바일 API로 현재가와 등락률을 가져옵니다."""
    url = f"https://m.stock.naver.com/api/stock/{code}/basic"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    res.raise_for_status()
    data = res.json()
    price = int(data["closePrice"].replace(",", ""))
    rate = float(data["fluctuationsRatio"])
    return price, rate


def build_message(stocks) -> str:
    lines = ["📊 내 관심종목 현재가", ""]               # 헤더 한 줄
    for s in stocks:
        code = s["code"].zfill(6)
        name = s.get("name") or code
        price, rate = get_price(code)
        lines.append(f"✅ {name} ({code})")              # 종목마다 첫째 줄
        lines.append(f"  {price:,}원 {format_rate_badge(rate)}")  # 둘째 줄
    return "\n".join(lines)


if __name__ == "__main__":
    stocks = load_watchlist()
    message = build_message(stocks)
    send_telegram(message)   # 터미널 출력 없이 폰 텔레그램으로만 한 통 전송