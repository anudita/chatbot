import openai
from tkinter import *
from tkinter import ttk

# set api key
openai.api_key = "<API_KEY>"

root = Tk()
root.title('CHATBOT')

# method to send end users question,get an answer from the bot and print it on text box


def getResponse():
    # set end user's username colour to orange
    chatbox.tag_config('sender', foreground="orange")
    # set bot's username colour to green
    chatbox.tag_config('bot', foreground="green")
    message = sender_message.get()  # fetching message sent by user in Entry box
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message},
        ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    # Add message and response in text box on screen
    chatbox.insert(END, 'Me >> ', 'sender')
    chatbox.insert(END, message + '\n\n')
    chatbox.insert(END, 'BOT >> ', 'bot')
    chatbox.insert(END,  result + '\n\n')
    # Remove text from Entry box after send is clicked
    sender_message.delete(0, END)


Label(root, text="----- JARVIS -----").grid(
    column=2, row=1, rowspan=2)
chatbox = Text(root, height=30, width=100)  # create text box
chatbox.grid(column=1, row=3, columnspan=2)  # add text box on chat window
sender_message = Entry()  # Add entry box for user to ask a question
sender_message.grid(
    column=1, row=4, columnspan=2, sticky=W, ipadx=200)  # add entry box on chat window
send_button = Button(root, command=getResponse, text="SEND>>").grid(
    column=2, row=4, sticky=E)  # add send button and call getResponse method once the button is pressed
Button(root, text="Quit", command=root.destroy).grid(
    column=2, row=6, ipadx=324, sticky=SE)  # add a button to exit
root.mainloop()
