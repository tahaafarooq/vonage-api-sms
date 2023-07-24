from vonager import VonageSMSApi

# sending single SMS

receiver = input("Enter Phone Number : ")
message = input("Enter Message : ")

vonage_object = VonageSMSApi()
send = vonage_object.send_sms(receiver, message)

print(send)

# sending bulk SMS

numbers = input("Enter Phone Numbers Seperated by Comma : ")
msisdns = numbers.split(',')
msisdns = [msisdn.strip() for msisdn in msisdns]

message = input("Enter message to send")

print(msisdns)

vonage_object = VonageSMSApi()
send = vonage_object.send_bulk_sms(msisdns, message)

print(send)
