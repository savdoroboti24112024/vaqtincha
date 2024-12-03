# Telegram Trading Bot Simulyatsiyasi

Bu loyiha Python kodini ishlatib, Telegram bot orqali savdo simulyatsiyasini amalga oshiradi. Ushbu bot har kuni savdo faoliyatini simulyatsiya qiladi, foyda va zararlarni hisoblaydi va har bir kunning yakunlari haqida xabar yuboradi.

## Foydalanish

1. **Telegram bot tokenini va chat ID ni o'zgartirish:**
   - `API_TOKEN` va `CHAT_ID` o'zgaruvchilarini Telegram'da o'zingizning botingiz va chat IDingizga to'g'ri moslang.
   
2. **Loyihani ishga tushurish:**
   - Loyihani ishga tushirishdan oldin `requirements.txt` faylini o'rnatishingiz kerak:
     ```bash
     pip install -r requirements.txt
     ```

3. **Kodning ishlashini tekshirish:**
   - Kodni `python your_script.py` orqali ishga tushiring.

## Loyiha Tavsifi

Bu Python skript har kuni savdo simulyatsiyasini amalga oshiradi va Telegram orqali foyda yoki zarar haqida xabar yuboradi. Har bir savdo instrumenti uchun tasodifiy narxlar yaratilib, savdo amalga oshiriladi.

## Foydalanish Shartlari

- Ushbu skriptni faqat shaxsiy maqsadlarda va o'rganish maqsadida ishlatish tavsiya etiladi.
- MetaTrader 5 yoki boshqa real bozor tizimlaridan foydalanish uchun kodni sozlash kerak bo'ladi.
