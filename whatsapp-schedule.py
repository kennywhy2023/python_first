'''
sendmessage

'''

def send_msg():
    print("send to user!")

def send_msg_to_group():
    print("send to group!")

def main():
    msg_type = int(input("Enter 1 to send a message to user and 2 to a group:"))
    if msg_type == 1:
        phone = input("Enter phone number:")
        if phone[0] == "0":
            phone = phone[1::]
        while True:
            if len(phone) < 9:
                raise ValueError("Invalid phone number: ")
            else:
                break
        phone = f"+233{phone}"
    elif msg_type == 2:
        group = input("Enter group to send message: ")
    msg = str(input("Enter message: "))
    hour = int(input("Enter the time in hour: "))
    minute = int(input("Enter the time in minute: "))

    if msg_type == 1:
        send_msg()
    elif msg_type == 2:
        send_msg_to_group()

if __name__ == '__main__':
    main()