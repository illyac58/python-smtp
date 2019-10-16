#!/usr/bin/env python
import smtplib
global smtp_server
global port
global fromaddr
global toaddrs
global line
smtp_server = "ip.add.re.ss"
port = 25
fromaddr = "from@email.com"
toaddrs = "to@email.com"

def alarm(subj,line):
  msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n %s"
       % (fromaddr, toaddrs, subj, line))
  try:
       server = smtplib.SMTP(smtp_server,port)
#    server.set_debuglevel(1)
       server.sendmail(fromaddr, toaddrs, msg)
  except Exception as e:
       print(e)
  finally:
       server.quit()
alarm('e-mail alarm','test body alarm')
