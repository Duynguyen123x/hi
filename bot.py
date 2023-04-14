import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Thiết lập token của bot Telegram của bạn tại đây
TOKEN = '5607905930:AAHF1pyoLdikzdippsWTsrnKzjBe0A4ezxo'

# Định nghĩa trạng thái chờ đợi người chơi
class GameState:
    WAITING_FOR_PLAYERS = 0
    WAITING_FOR_GUESS = 1

# Thiết lập trạng thái ban đầu cho trò chơi
state = GameState.WAITING_FOR_PLAYERS

# Lưu trữ thông tin người chơi và câu hỏi hiện tại
player = None
current_question = None

def start(update, context):
    # Kiểm tra xem trò chơi đang chờ đợi người chơi mới hay không
    global state
    global player
    global current_question
    if state == GameState.WAITING_FOR_PLAYERS:
        update.message.reply_text("Bắt đầu trò chơi đoán số! Tôi đã chọn một số từ 1 đến 100. Hãy đoán xem đó là số gì.")
        player = update.message.from_user
        state = GameState.WAITING_FOR_GUESS
        current_question = random.randint(1, 100)
    else:
        update.message.reply_text("Hiện tại trò chơi đang diễn ra.")

def guess(update, context):
    # Kiểm tra xem trò chơi đang trong trạng thái cho phép đoán hay không
    global state
    global player
    global current_question
    if state == GameState.WAITING_FOR_GUESS:
        guess = int(context.args[0])
        if guess == current_question:
            update.message.reply_text(f"Chính xác! Số {current_question} là số tôi đã chọn.")
            # Thiết lập lại trạng thái ban đầu cho trò chơi và thông tin người chơi/câu hỏi hiện tại
            state = GameState.WAITING_FOR_PLAYERS
            player = None
            current_question = None
        elif guess < current_question:
            update.message.reply_text("Không chính xác. Số bạn đoán nhỏ hơn số tôi đã chọn.")
        else:
            update.message.reply_text("Không chính xác. Số bạn đoán lớn hơn số tôi đã chọn.")
    else:
        update.message.reply_text("Hiện tại không thể đoán số.")

# Khởi tạo bot và thiết lập các command handlers
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('guess', guess))

# Khởi chạy bot
updater.start_polling()
updater.idle()
