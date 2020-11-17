import os
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.models import messages

# file=open('info.json','r')
# info=json.load(file)



# CHANNEL_ACCESS_TOKEN=info['CHANNEL_ACCESS_TOKEN']
CHANNEL_ACCESS_TOKEN=os.environ['CHANNEL_ACCESS_TOKEN']
line_bot_api=LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID=os.environ['USER_ID']
    messages=TextSendMessage(text='おはようございます！今日も一日頑張りましょう！！')
    line_bot_api.push_message(USER_ID,messages=messages)

if __name__=='__main__':
    main()
