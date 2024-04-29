from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = 21879714
API_HASH = 'e0b60d05a896beaa3f69dc70e26b0a5d'
SESSION_STRING = "1ApWapzMBuxCSzFSC9prU5R5PdgdXExbvaur2VLTpiUmWheGZs8Jr0DHl-c083Xo15eVA0aTrp-pfgj2F09FPZ5MU2iKQ7jZUcd0Ebz8BlrsSXCpnrm-BCZSJ2Bo5U3jJ12BmHlRPPL2JatmttFPa5az99cK4P78ObEDmqbuZEzkRqnDZsYUER9m2ljsb5J6rFNFkqol3f7IFlApNHguLcgQ4jPwxhUmls-5ve9tX0hbPywsWk2j6MDV3xBqae5qd6hZIrkMu7CuhbTBMiNCmUG6WmRHDslsRepTwojG_obSeQREXBAASlm28lqOl95DqQyOZRgcS708oPPMld5bRjpJFCJhHP_Y="

# Create Telethon client
client = TelegramClient(
    StringSession(SESSION_STRING),  # Passing the session as a StringSession object
    API_ID,
    API_HASH,
)

# Define the user's username
username = "@S_J_O_D"

# Message to be sent
message = "تاج راسك سجاد اني جلسة"

# Define the async function to send message
async def send_message():
    await client.send_message(username, message)

# Run the client and send the message
with client:
    client.loop.run_until_complete(send_message())
