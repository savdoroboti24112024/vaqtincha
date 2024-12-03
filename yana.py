import time
import requests
import random

# Telegram bot ma'lumotlari
API_TOKEN = "7634960446:AAE3k4oCVhTU3EtSv1ab9IrQLGoyCVyt2Kk"
CHAT_ID = "1114803079"  # Sizning chat ID

def send_telegram_message(message):
    """Telegram bot orqali xabar yuborish"""
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"Xabar yuborishda xatolik: {response.status_code}, {response.text}")

# Hisob ma'lumotlari (parolni to'g'ridan-to'g'ri kiritilgan)
initial_balance = 100  # Hisobdagi boshlang'ich mablag' 100$
balance = initial_balance  # Hozirgi balans
risk_factor = 0.1  # 1/10 qismi bilan kirish
leverage = 100  # Leverage miqdori (100x leverage)
daily_lot_size = 0  # Kunlik lot hajmi

def set_daily_lot_size():
    """Kunlik lot hajmini belgilash, leverage hisobga olinadi"""
    global daily_lot_size
    daily_lot_size = (initial_balance * risk_factor) / (1000 * leverage)  # Leverage'ni hisobga olish
    send_telegram_message(f"Kunlik lot hajmi: {daily_lot_size}")

def simulate_trading(period_days=365):
    global balance
    initial_balance = balance
    results = []  # Natijalarni saqlash uchun

    for day in range(1, period_days + 1):
        send_telegram_message(f"Kun {day} savdosi boshlanmoqda...")
        set_daily_lot_size()

        # Savdo faolligi uchun ishlatiladigan instrumentlar
        valid_symbols = ['XAUUSD', 'USDJPY']
        open_orders = {}

        for symbol in valid_symbols:
            # Simulyatsiya: tasodifiy bozor ma'lumotlari (bu yerda o'zgartirishingiz mumkin)
            previous_candle = random.uniform(1000, 2000)
            current_candle = random.uniform(1000, 2000)
            action = 'buy' if current_candle > previous_candle else 'sell'

            if action:
                # Simulyatsiya: Buyurtma yuborish (faqat xabar yuboriladi)
                order_result = f"{action} order placed for {symbol} with volume {daily_lot_size}"
                open_orders[symbol] = order_result

                # Savdolarni tekshirish
                for symbol, entry_price in open_orders.items():
                    # Simulyatsiya: foyda yoki zarar hisoblash (tasodifiy qiymatlar)
                    profit_or_loss = random.uniform(-50, 50)
                    
                    # Balansni yangilash
                    balance += profit_or_loss
                    send_telegram_message(f"Savdo yopildi. Foyda/Zarar: {profit_or_loss}, Yangi balans: {balance}")
                    
                    # Savdoni yopish
                    open_orders.pop(symbol)

        # Kun oxirida hisobot yuborish (kun davomida)
        message = f"Bugungi savdo yakunlari:\nBalans: {balance}$"
        send_telegram_message(message)
        results.append(balance)  # Har bir kunning yakuniy balansini saqlash

        # Kutilgan vaqt, savdolarni tekshirish va hisobot yuborish
        time.sleep(1)  # 1 daqiqa kutish (savdo tahlili va natijalarni yuborish uchun)

    # Yillik simulyatsiya yakunida umumiy hisobot yuborish
    final_balance = balance
    total_profit_loss = final_balance - initial_balance
    message = f"Yillik simulyatsiya yakunlari:\nBoshlang'ich balans: {initial_balance}$\nYakuni: {final_balance}$\nFoyda/Zarar: {total_profit_loss}$"
    send_telegram_message(message)

# Yillik simulyatsiya qilish (365 kun)
simulate_trading(period_days=365)
