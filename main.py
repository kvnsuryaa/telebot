import requests as requests

class BotHandle:
    def __init__(self, token):
        self.apiUrl = "https://api.telegram.org/bot{}/".format(token)

    def getChatId(self, update):
        chat_id = update['message']['chat']['id']
        return chat_id

    def getMessageText(self, update):
        text = update['message']['text']
        return text

    def lastUpdates(self):
        response = requests.get(self.apiUrl+'getUpdates')
        response = response.json()
        res = response['result']
        total_chat = len(res) - 1
        return res[total_chat]

    def getUsername(self, update):
        first_name = update['message']['from']['first_name']
        last_name = update['message']['from']['last_name']
        username = first_name + ' ' + last_name
        return username

    def sendMessage(self, chat_id, text):
        params = {"chat_id":chat_id, "text": text}
        print(params)
        response = requests.post(self.apiUrl+'sendMessage', data=params)
        return response

token = '1097165179:AAHAanw3-WxV2MxRuKGSSUkuuS2lyJUPcEw'

teleBot = BotHandle(token)

def main():
    print("Launching....")

    updateID = teleBot.lastUpdates()["update_id"]
    print("Chats Log")
    print('===========================')

    lists = "1. My Github\n2. My Project"

    while True:
        update = teleBot.lastUpdates()
        # print(update)

        if updateID == update["update_id"]:

            # Bot Condition
            texts = teleBot.getMessageText(update).lower()
            if texts == 'hi' or texts == 'hello' or texts == '/start':
                teleBot.sendMessage(teleBot.getChatId(update), 'Hello '+teleBot.getUsername(update)+', Welcome to Trickasbot \nChoose:\n\n'+lists)
            elif texts == '1' or texts == 'github':
                teleBot.sendMessage(teleBot.getChatId(update), 'Here you go \n\nhttps://github.com/Trickascp')
            elif texts == '2' or texts == 'project':
                apiGit = 'https://api.github.com/users/trickascp/repos'
                response = requests.get(apiGit)
                slices = slice(0, 5)
                datas = response.json()[slices]
                listP = ''
                num = 0
                for d in datas:
                    num += 1
                    listP += str(num) + '. ' + d['name'] + '\n'
                teleBot.sendMessage(teleBot.getChatId(update), 'Here you go\n\n' + listP)
            elif texts == 'thanks' or texts == 'ty':
                teleBot.sendMessage(teleBot.getChatId(update), "You're welcome :)")
            else:
                teleBot.sendMessage(teleBot.getChatId(update), 'No Command like that here :(')
            updateID += 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()


