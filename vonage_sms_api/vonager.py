from dotenv import load_dotenv
import vonage
import os

load_dotenv()


class VonageSMSApi(object):
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.api_secret = os.getenv('API_SECRET')

    def send_sms(self, msisdn: str, message: str):
        client = vonage.Client(self.api_key, self.api_secret)
        sms = vonage.Sms(client)

        data = {
            "from": "Vonage APIs",
            "to": f"{msisdn}",
            "text": f"{message}"
        }

        output = sms.send_message(data)

        if output["messages"][0]["status"] == "0":
            print(output["messages"])
            return "Message Sent Successfully"
        else:
            return f"Message failed with error: {output['messages'][0]['error-text']}"

    def send_bulk_sms(self, msisdns: list, message: str):
        sent_messages = []
        failed_messages = []
        client = vonage.Client(self.api_key, self.api_secret)
        sms = vonage.Sms(client)

        for msisdn in msisdns:
            data = {
                "from": "TEST",
                "to": f"{msisdn}",
                "text": f"{message}"
            }

            output = sms.send_message(data)

            if output["messages"][0]["status"] == "0":
                sent_messages.append(msisdn)
            else:
                failed_messages.append(failed_messages)
        print(output["messages"])
        return f"Messages Sent to : {sent_messages}"
