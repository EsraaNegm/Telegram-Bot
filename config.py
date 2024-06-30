######################## TELEGRAM BOT TOKEN ########################
BOT_TOKEN = "7012939808:AAH9QNLi05Sm4FfqTjv7JF-QBJpkimHhVak" # @asknu_bot
# BOT_TOKEN = "7087373040:AAH89WABcLjVqXP-4DEbki7FUOhFXgvrOwI" # @essawey_bot

######################## ELEVEN_API_KEY ########################
ELEVEN_API_KEY="sk_d12822bb7827756e3c8e30e63a829a93f46ed0407bff0a8d"

######################## FEEDBACK MAPS ########################
feedback_map = {
    'very long' : 'Very long, Make answer shorter',
    'very short': 'Very short, Make answer very detailed in more lines',
    'inaccurate': 'You are not correct',
    'irrelevant': 'Irrelevant, Please focus on my question or write an answer related to my question'
}

######################## ARABIC PRINTING SUPPORT ########################
import arabic_reshaper
from bidi.algorithm import get_display

def print_ar(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    print(bidi_text)

