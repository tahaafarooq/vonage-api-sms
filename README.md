# vonage-api-sms
A simple wrapper for the vonage SMS API

## Installation

```shell
~$ git clone https://github.com/tahaafarooq/vonage-sms-api
~$ cd vonage-sms-api
vonage-sms-api/~$ pip3 install -r requirements.txt
vonage-sms-api/~# python3 setup.py install
```

## Configuration

create a `.env` file in the path where you shall run your project, the file should contain the following:

```dotenv
API_KEY=xxxxxxxx
API_SECRET=xxxxxxxxxxxx
```

## Sending Single SMS

```python
from vonage_sms_api.vonager import VonageSMSApi

# sending single SMS

receiver = input("Enter Phone Number : ")
message = input("Enter Message : ")

vonage_object = VonageSMSApi()
send = vonage_object.send_sms(receiver, message)

print(send)
```

```shell
Enter Phone Number : XXXXXXXXX
Enter Message : hello
[{'to': 'XXXXXXXXX', 'message-id': 'XXXXXX', 'status': '0', 'remaining-balance': '1.04000000', 'message-price': '0.12000000', 'network': 'XXXXX'}]
Message Sent Successfully
```

## Sending Bulk SMS

```python
from vonage_sms_api.vonager import VonageSMSApi

# sending bulk SMS

numbers = input("Enter Phone Numbers Seperated by Comma : ")
msisdns = numbers.split(',')
msisdns = [msisdn.strip() for msisdn in msisdns]

message = input("Enter message to send")

print(msisdns)

vonage_object = VonageSMSApi()
send = vonage_object.send_bulk_sms(msisdns, message)

print(send)
```
