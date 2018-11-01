# UDP Client Program

from socket import socket, AF_INET, SOCK_DGRAM # מייבא מספריית הסוקט את הפונק הדרושות לפתיחת סוקט

s = socket(AF_INET, SOCK_DGRAM) # יוצר סוקט UDP, בפרוטוקול ipv4
dest_ip = '172.18.36.119' # כתובת האייפי של שרת היעד
dest_port = 12345 # הפורט שעליו שרת היעד מאזין
msg = raw_input("Message to send: ") # קולט את ההודעה שהמשתמש רוצה לשלוח
while not msg == 'quit': # כל עוד המשתמש לא שלח הודעה יציאה, ממשיך בתהליך שליחת הודעות
    s.sendto(msg,(dest_ip,dest_port)) # 
    data, sender_info = s.recvfrom(2048)
    print "Server sent: ", data
    msg = raw_input("Message to send: ")
s.close()
