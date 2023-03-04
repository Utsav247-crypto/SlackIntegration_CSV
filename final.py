from slack_sdk import WebClient

client = WebClient(token='xoxb-4891217860754-4882528625543-lFT8ePlEa7rHssjeNwxZepaK')
client.chat_postMessage(channel="random",text="My File")

client.files_upload(
        channels="random",
        file='data.xlsx',
        title='XLSX DATA',
        filetype='xlsx'
    )

