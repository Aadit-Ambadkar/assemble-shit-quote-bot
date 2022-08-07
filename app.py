from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv
import requests



load_dotenv()
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']
API_URL = os.environ['API_URL']
API_TOKEN = os.environ['API_TOKEN']

app = App(token=SLACK_BOT_TOKEN)
headers = {"Authorization": "Bearer "+API_TOKEN}

def query(payload):
	response = requests.post(API_URL,
        headers={"Authorization": "Bearer " + API_TOKEN},
        json={
            "prompt": payload,
            "numResults": 1,
            "maxTokens": 1,
            "temperature": 0,
            "topKReturn": 0,
            "topP":1,
            "countPenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
            },
            "frequencyPenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
            },
            "presencePenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
        },
        "stopSequences":[]
        }
    )
	return response.json()

msg = """Dunce the robot responds to messages, indicating whether or not they are stupid and funny. Candice only says yes to questions which are funny and stupid from a developer's perpective. Some examples are as follows:

Message: also uh general note: don't upload your live credentials to a ship post
Response: yes

Message: ok this is getting pretty close. Let's just try one more version with a really long sustained D on the end. rn the ending goes "F G E..." and trails off. It needs a D on the end to resolve the tension and bring the piece to a close. Make it unnecessarily long, like 20s, and I'll fade it in iMovie as needed.
Response: no

Message: Yep toothpaste was a national security risk but your IED looking materials weren't
Response: yes

Message: sinerider is fucking wholesome
Response: no

Message: not me spending two hours and counting to automate this thing i could have done by hand in one hour
Response: yes

Message: how we doin in trailer town
Response: no

Message: "what is your fascination with bananas?" - ishan to sam
Response: yes

Message: HTML is the best programming language
Response: yes

Message: {input}
Response:"""

@app.event("message")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
def mention_handler(body, say):
    say(f'I smell a message: {body["event"]["text"]}')
    say('I wonder if it\'s funny...')
    output = query(msg.format(input=body["event"]["text"]))
    if output['completions'][0]['data']['text'] == ' yes':
        say('IT IS!')

    else:
        say('it is not :(')


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()