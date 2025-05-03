import pyautogui
from time import sleep
import pyperclip
from openai import OpenAI

pyautogui.click(814, 783)  # Go to Whatsapp


def check_is_it_receiver(chatList, receiver):
    if (chatList[-1].startswith(f"{receiver}:")):
        return True
    return False


sender = "" # Sender Name
receiver = "" # Receiver Name

while True:
    pyautogui.rightClick(1279, 496)  # In the corner rihgt click to get menu
    pyautogui.moveTo(1249, 505)  # move slightly left and bottom
    pyautogui.doubleClick()  # Double click to firstly focus then select
    pyautogui.hotkey('ctrl', 'a')  # Select all chat
    pyautogui.hotkey('ctrl', 'c')  # Copy the chat

    # Convert to list based on open square bracket then flter and remove any empty value
    chat_history = list(filter(None, pyperclip.paste().split("[")))

    # remove date: 20-04-2025 07:36] then remove /r and append into the list
    chatList = [x[x.index("]")+2:].replace("\r", "") for x in chat_history]

    if (check_is_it_receiver(chatList, receiver)):  # If last message was by receiver
        final_conversation = "\n".join(chatList)  # Converting to string
        api_key="Your Open AI API Key"
        client = OpenAI(api_key=api_key)
        ai = client.responses.create(
            model="gpt-4o",
            instructions=f"You are {sender}, you will be given chat history between you and someone else, You have to response your reply. Conditions you have to follow:\n- Same tone as human\n- Don't throw much emojis\n- Stay concise\n- Give only message\nGive reply in same language and tone\nDon't write '{sender}:'",
            input=final_conversation,
        )

        response = ai.output_text # Getting AI response

        pyperclip.copy(response) # Copy to clipboard
        pyautogui.click(539, 730) # Click on text box to write
        sleep(5) # Wait for 5 seconds to give human vibe
        pyautogui.hotkey('ctrl', 'v') # Paste the text
        pyautogui.hotkey('enter') # Enter(send)

    sleep(5) # Wait for every 5 seconds before rechecking