import pyautogui
import time
import pyperclip
from openai import OpenAI


client = OpenAI(
  api_key="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",
)

def is_last_message_from_sender(chat_log, sender_name="Maa"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False

    # Step 1: Click on the chrome icon at coordinates (1639, 1412)
pyautogui.click(606, 741)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(2)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(480,239)
    pyautogui.dragTo(1317, 648, duration=1.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(1317, 648)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Nitesh who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (747, 699)
        pyautogui.click(747, 699)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')