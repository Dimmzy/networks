# UDP Server Program

from socket import socket, AF_INET, SOCK_DGRAM # מייבא מספריית הסוקט את הפונק הדרושות לפתיחת סוקט

s = socket(AF_INET, SOCK_DGRAM) # יוצר סוקט UDP, בפרוטוקול ipv4
source_ip = '0.0.0.0' # מאזין על כתובת אייפי מסוימת, במקרה שלנו על כל הכתובות הלוקליות
source_port = 12345 # הפורט שהשרת מאזין עליו
s.bind((source_ip, source_port)) # קשור את האייפי והפורט לסוקט שיצרנו
while True: # הרצת לולאה אינסופית עד שסוגרים את התוכנה בכח
    data, sender_info = s.recvfrom(2048) # מקבל מידע מהסוקט שומר אותו בדאטא, ואת פרטי השולח בסנדר אינפו
    print "Message: ", data, " from: ", sender_info # מדפיס חזרה את ההודעה ופרטי השולח
    s.sendto(data.upper(), sender_info) # שולח חזרה את הדאטא באותיות גדולות ואת מידע השולח (echo)
