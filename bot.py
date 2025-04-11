import telebot
from config import token
print(token)

bot = telebot.TeleBot(token)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['s_gen'])
def send_s(message):
    bot.reply_to(message, f"Здорова, брат! Я бот. Как сам?")
    bot.reply_to(message, f"сочинение не меньше 200 слов на тему <s>:")
    bot.reply_to(message, f"Summer Vacation Experience: This summer, I had the opportunity to take a break from school and enjoy my vacation to the fullest. I decided to spend most of my time resting at home and spending quality moments with my family. One of the highlights of my summer was embarking on a road trip with my family, which turned out to be an unforgettable experience. During our journey, we traveled to several cities and visited a variety of tourist attractions. We explored amusement parks, national parks, and museums, each offering unique experiences and memories. It was a great opportunity to have fun and create lasting memories with my loved ones. In addition to the road trip, I also spent a significant amount of time outdoors, engaging in various activities. I went swimming in the pool, played football with my friends, and even had my first camping experience. The fresh air and physical activities were a welcome break from the school year, rejuvenating my body and mind. Despite all the fun and excitement, I also made sure to use my summer vacation productively. I spent a few hours each day reviewing my notes and completing assignments, ensuring I would be well-prepared for the upcoming school year. This balance between relaxation and productivity allowed me to make the most of my summer break. To sum it up, my summer vacation was a perfect blend of relaxation and productivity. I am grateful for the opportunity to take a break from school and spend time with my family. As I look forward to the new academic year, I feel refreshed and ready to tackle new challenges with enthusiasm and vigor.")


@bot.message_handler(content_types=['text', 'photo', 'sticker', 'audio'])
def handle_message1(message):
  
  # Ответ на текстовое сообщение
  if message.text == 'Привет':
      bot.send_message(message.chat.id, 'Привет! Как дела?')
  
  # Ответ на изображение
  if message.photo:
      bot.send_message(message.chat.id, 'Вы отправили изображение.')
  
  # Ответ на стикер
  if message.sticker:
      bot.send_message(message.chat.id, 'Вы отправили стикер.')

  if message.audio:
      bot.send_message(message.chat.id, 'Крутое аудио.')



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == "$@Сыграем_в_города":
        Comp_gorod = ["А:", "Армавир", "Анапа",
                      "Б:", "Брянск", "Белгород",
                      "В:", "Владимир", "Волгоград",
                      "Г:", "Грозный", "Гатчина",
                      "Д:", "Дмитров", "Дербент",
                      "Е:", "Екатеринбург", "Ейск"]
        ert = 0
        if ert == 0:
            bot.send_message(message, "В разработке!!!")
    else:
        bot.reply_to(message, message.text)


bot.infinity_polling()










