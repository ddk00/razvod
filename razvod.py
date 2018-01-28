
#! /usr/bin/python
# -*- coding: utf-8 -*-

#
#MIT License
#
#Copyright (c) 2018 Danil Karandin
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    
    emails = []
    with open(filename, mode='r') as contacts_file:
        for a_contact in contacts_file:

            emails.append(a_contact.split()[0])
    return emails


print ' Razvod 1.0 '
print '[*] Which SMTP? 1 - gmail, 2 - yahoo, 3 - hotmail'
smtpProvider = raw_input("[?] SMTP Provider       ")
if smtpProvider == "1" or smtpProvider == "gmail":
  s = smtplib.SMTP(host='smtp.gmail.com', port=587)

elif smtpProvider == "2" or smtpProvider == "yahoo":
  s = smtplib.SMTP(host='smtp.mail.yahoo.com', port=587)

elif smtpProvider == "3" or smtpProvider == "hotmail":
  s = smtplib.SMTP(host='smtp.live.com', port=587)

else:
  print 'Enter your own SMTP provider and port'
  smtpHost = raw_input("[?] SMTP host?        ")
  smtpPort = raw_input("[?] SMTP port?        ")

login = raw_input("[?] Login to attacker's email        ")
password = raw_input("[?] Password to attacker's email        ")
print '[!] Type all victim emails in contacts.txt'

#============================= templates =================================================

templateSelect = raw_input("[?] Choose a template: 1 - Russian store, 2 - Friendly link         ")

#==============================Russian Store template===============================

if templateSelect == "1":
  text = ""
  msg = MIMEMultipart('alternative')
  msg['Subject'] = raw_input("[?] Subject:       ")
  fromName = raw_input("[?] From who?:       ")
  city = raw_input("[?] What city? city,state:        ")
  
  pic1 = raw_input("[?] Change the first picture? Yes/No:        ")
  if pic1 == "Yes":
    pic1link = raw_input("[?] Insert the link:        ")
  else: 
    pic1link = "https://s3-media1.fl.yelpcdn.com/bphoto/_lpULh18qc9tUeJ4GQrLNw/o.jpg"
  
  pic2 = raw_input("[?] Change the second picture? Yes/No:        ")
  if pic2 == "Yes":
    pic2link = raw_input("[?] Insert the link:        ")
  else: 
    pic2link = "https://s3-media3.fl.yelpcdn.com/bphoto/fBasjWZ7pUs8ZPv1buaF3g/o.jpg"
    
  maliLink = raw_input("[?] Change the malicious link? Yes/No:        ")
  if maliLink == "Yes":
    maliLink = raw_input("[?] Insert the link:        ")
  else: 
    maliLink = "https://www.google.com/search?ei=BxZuWoHhI8mzzwKt4K24DQ&q=you+have+been+redirected&oq=you+have+been+redirected&gs_l=psy-ab.3..0l2j0i22i30k1l8.2101.8048.0.8428.24.24.0.0.0.0.134.2130.18j6.24.0....0...1c.1.64.psy-ab..0.24.2128...0i131k1j0i131i67k1j0i67k1j0i131i10i67k1j0i10k1.0.HqK-v7cdmkA"
    
  facebookLink = raw_input("[?] Change the Facebook link? Yes/No:        ")
  if facebookLink == "Yes":
    facebookLink = raw_input("[?] Insert the link:        ")
  else: 
    facebookLink = "https://facebook.com"

  instagramLink = raw_input("[?] Change the Instagram link? Yes/No:        ")
  if instagramLink == "Yes":
    instagramLink = raw_input("[?] Insert the link:        ")
  else: 
    instagramLink = "https://instagram.com"

  template_Russian_Store = """\
<html>
<head></head>
<body><div id=":110" class="a3s aXjCH m1613825284e093a5"><div class="adM">

</div><div><div style="display:none;display:none!important;color:transparent;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;height:0;width:0;font-size:0px">Огромные скидки в честь открытия нового русского магазина в """+city+"""</div>
<div><img src="https://ci3.googleusercontent.com/proxy/x_32LwXxz6wygiNhMgZuhrcmR7mzYP0zt9-TIFZ0l1gB6dTDd94EYtjZzowU8aOcI1yBQeQ1nNIQoDACmfnyNf-tGTBrWIkAG4cKnzGS79AN-iq3pWH6AX7hGKv4oGkxncCE8T-tmjDwqChZ6LTZU4_9VWvhBRtE3AsMe34Lz8YjfO4Vd3fUjD2iKRZSY1HyuYydDW7t6gAkyBHPrVSFY_NVKivSHCYsfT5XvYNAfAMbn5006X3dXjIfNfrLgie02F3hLR1YeTVv9zW0L_3oKDLSpXi239AJZfWvAeYSzr21uJvlNdd2wIOPybu_p7CAnHgjeGon-UlDwKWPZn2j4Go=s0-d-e1-ft#http://r20.rs6.net/on.jsp?a=1118715500493&amp;r=3&amp;c=0fe25350-4e6d-11e4-87fc-d4ae528eaf6c&amp;d=1129908401082&amp;ch=106d2e30-4e6d-11e4-88ff-d4ae528eaf6c&amp;ca=2b64d27a-56c7-4a21-a19b-9c45e3ad2a3f&amp;>
<div align="center">
<table style="background-color:#ffffff" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" width="100%" border="0">
<tbody><tr>
    <td rowspan="1" colspan="1" align="center"><table style="width:600px" cellspacing="0" cellpadding="1" width="600" border="0">
    <tbody><tr>
        <td style="padding:0px" rowspan="1" colspan="1" width="100%"><table style="background-color:#ffffff" id="m_3668120050698307362content_LETTER.BLOCK1" cellspacing="0" cellpadding="5" bgcolor="#FFFFFF" width="100%" border="0"><tbody><tr><td style="color:#000000" rowspan="1" colspan="1" align="center">
<div style="color:#f7f700;font-size:28pt">
<div style="font-size:28pt;font-family:Tahoma,Arial,sans-serif">
<div style="color:#000000;font-size:26pt;font-family:&quot;Times New Roman&quot;,Times,serif">
<div style="color:#000000">
<div>
<div>
<div style="font-size:20pt;font-family:'Times New Roman',Times,serif"><strong>Огромные скидки в честь открытия нового русского магазина в """+city+"""</strong></div>
<table style="color:#f7f700;font-size:24pt;font-family:Tahoma,Arial,sans-serif" cellspacing="0" cellpadding="0" width="601"><tbody><tr><td style="padding-top:5px;padding-left:0px;padding-bottom:5px;padding-right:0px" rowspan="1" colspan="1" width="100%">
<div align="center"><img name="sweets" src=" """+pic1link+""" " tabindex="0" hspace="0" width="601" border="0" vspace="0"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 1074px; top: 495px;"><div role="button" tabindex="0" aria-label="Ð¡ÐºÐ°Ñ‡Ð°Ñ‚ÑŒ Ñ„Ð°Ð¹Ð» " data-tooltip-class="a1V" data-tooltip="Ð¡ÐºÐ°Ñ‡Ð°Ñ‚ÑŒ"><div class="aSK J-J5-Ji aYr"></div></div></div></div>
</td></tr></tbody></table>



</div>
</div>
</div>
</div>
</div>
<div style="font-size:24pt;font-family:Tahoma,Arial,sans-serif"><span style="font-size:8pt;font-family:Arial Narrow,Arial MT Condensed Light,sans-serif">
<div><b><br></b></div>
</span></div>
<div style="color:#000000;font-size:36pt;font-family:Arial Black,Avant Garde"><span style="text-decoration:underline"><strong>Самые</strong></span></div>
<div style="color:#000000;font-size:36pt;font-family:Arial Black,Avant Garde">
<div><span style="text-decoration:underline"><strong>Низкие Цены</strong></span></div>
<div><span style="text-decoration:underline"><strong>Гарантированы</strong></span></div>
<div style="font-size:16pt;font-family:Arial Narrow,Arial MT Condensed Light,sans-serif"><span style="text-decoration:underline"><b>Зайдите на наш сайт чтобы получить купоны и скидки на Вашу первую покупку!</b></span></div>
</div>

<table border="0" cellspacing="0" cellpadding="0">
    <tbody><tr>
    <td align="center" bgcolor="#fff200">
    <a href=" """+maliLink+""" " style="font-size:28px;font-family:Arial,sans-serif;font-weight:bold;color:#003b64;text-decoration:none;padding:10px 15px 10px 15px;border:1px solid #fbe27e;display:block" target="_blank">
    Получить Скидки
    </a>
    </td>
    </tr>
    </tbody></table>

</div>
</td></tr></tbody></table><table cellspacing="0" cellpadding="0" width="100%" border="0"><tbody><tr><td style="color:#000000" rowspan="1" colspan="1"><img name="m_3668120050698307362_ACCOUNT.IMAGE.92" src=" """+pic2link+""" " class="CToWUd a6T" tabindex="0" hspace="0" width="609" border="0" vspace="5"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 1077px; top: 952.8px;"><div id=":18e" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" title="Ð¡ÐºÐ°Ñ‡Ð°Ñ‚ÑŒ" role="button" tabindex="0" aria-label="Ð¡ÐºÐ°Ñ‡Ð°Ñ‚ÑŒ Ñ„Ð°Ð¹Ð» " data-tooltip-class="a1V"><div class="aSK J-J5-Ji aYr"></div></div></div></td></tr></tbody></table></td>
    </tr>
    <tr>
        <td style="background-color:#ffff00;padding:1px" rowspan="1" colspan="1" bgcolor="#FFFF00"><table style="background-color:#ffffff" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" width="100%" border="0">
        <tbody><tr>
            <td style="padding:0px" rowspan="1" colspan="1" align="center" width="100%">
            
            </td>
        </tr>
        <tr>
            <td   style="background-color:#959282;padding:0px" rowspan="1" colspan="1" bgcolor="#959282" width="100%">
            </td>
        </tr>
        </tbody></table></td>
    </tr>
    <tr>
        <td rowspan="1" colspan="1" height="10" width="100%">

         <table style="display:table"  cellspacing="0" cellpadding="5" width="100%" border="0"><tbody><tr><td yle="color:#fff5c2;font-size:10pt;font-family:Trebuchet MS,Verdana,Helvetica,sans-serif" rowspan="1" colspan="1" align="center">
            <a href=" """+facebookLink+""" " shape="rect" target="_blank"><img alt="Like us on Facebook" title="Like us on Facebook" src="https://www.usflagsupply.com/images/companies/1/Like-US-Flag-Supply-on-facebook.png?1478777645028" align="null" height="35" width="160" border="0"></a>
            <a href=" """+instagramLink+""" " shape="rect" target="_blank"><img alt="View on Instagram" title="View on Instagram" src="http://www.synergydancemn.com/i/instagram-button.png" align="null" height="35" width="160" border="0"></a><br></td></tr></tbody></table></td>
    </tr>
    </tbody></table></td>
</tr>
</tbody></table>
</div>
<div style="background-color:#ffffff" align="center">
<table style="background-color:#ffffff"  cellspacing="0" cellpadding="0" width="100%" border="0">
<tbody><tr>
<td rowspan="1" colspan="1" align="center">

<table style="background-color:#ffffff" cellspacing="0" cellpadding="0" width="100%" border="0"><tbody><tr><td bile" rowspan="1" colspan="1">
    <img src="" 
    class="CToWUd" hspace="0" height="5" width="1" border="0" vspace="0"></td><td style="background-color:#ffffff" rowspan="1" colspan="1" align="center" width="610" valign="top">
        <div style="margin-left:auto;max-width:610px;margin-right:auto" align="center"><table style="margin-left:auto;margin-right:auto" cellspacing="0" cellpadding="0" width="100%" border="0">
            <tbody><tr><td style="padding:15px 10px 15px 10px" rowspan="1" colspan="1" align="center" width="100%" valign="top"><table style="margin-left:auto;margin-right:auto" cellspacing="0" 
                cellpadding="0" width="100%" border="0"><tbody><tr><td style="padding-bottom:15px" rowspan="1" colspan="1" align="center" width="100%" valign="top">
                    <div style="color:#5d5d5d;font-size:13px;font-family:Verdana,Geneva,sans-serif">
                        <span lumn">Магазин Калинка</span>
                            </div></td></tr><tr><td rowspan="1" colspan="1" align="center" width="100%" valign="top"><table cellspacing="0" cellpadding="0" width="100%" border="0">
                                <tbody><tr><td style="padding-bottom:5px" rowspan="1" colspan="1" align="center" width="100%" valign="top">
                                    <div xt" style="color:#5d5d5d;font-size:12px;font-family:Verdana,Geneva,sans-serif;line-height:1.4">
                                        <a lyFwd" style="color:#5d5d5d" shape="rect" href=" """+maliLink+""" " 
                                        target="_blank"><span>Отписаться</span></a>
                                    </div></td></tr></tbody></table><table cellspacing="0" cellpadding="0" width="100%" border="0"><tbody><tr><td rowspan="1" colspan="1" align="center" width="100%" valign="top"><div xt" 
                                        style="color:#5d5d5d;font-size:12px;font-family:Verdana,Geneva,sans-serif;line-height:1.4"><span lumn"><a style="color:#5d5d5d" shape="rect" 

                                            target="_blank" ></a></span></div></td></tr></tbody></table><table cellspacing="0" cellpadding="0" width="100%" border="0"><tbody><tr><td style="padding-top:5px" rowspan="1" colspan="1" align="center" width="100%" valign="top">
                                                <div xt" style="color:#5d5d5d;font-size:12px;font-family:Verdana,Geneva,sans-serif">Sent by 
                                                <a style="color:#5d5d5d" shape="rect" href=" """+login+""" " target="_blank"> """+fromName+""" </a></div></td></tr></tbody></table></td></tr><tr>
                                                    <td style="padding-top:20px;padding-bottom:20px" rowspan="1" colspan="1" align="center" width="100%" valign="top"><table cellspacing="0" cellpadding="0" width="100%" border="0"><tbody><tr><td style="padding-bottom:5px" rowspan="1" colspan="1" align="center" width="100%" valign="top">
                                                        <div><a shape="rect" href="" target="_blank" ><img style="display:block;height:auto!important;max-width:100%!important"</a></div></td></tr><tr><td rowspan="1" colspan="1" align="center" width="100%" valign="top"><table cellspacing="0" cellpadding="0" width="128" border="0"><tbody><tr><td rowspan="1" colspan="1" align="left" width="100%" valign="top"><div style="color:#184f8e;font-size:11px;font-family:Verdana,Geneva,sans-serif"><a style="color:#184f8e;text-decoration:none;font-size:11px;font-family:Verdana,Geneva,sans-serif" shape="rect" target="_blank"></a></a></div></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></div></td><td bile" rowspan="1" colspan="1"><img src="" hspace="0" height="5" width="1" border="0" vspace="0"></td></tr></tbody></table>
</td>
</tr>
</tbody></table><div></div><div class="adL">
</div></div></div></div><div class="adL">
</div></div></body></html>
"""
  template = template_Russian_Store
  

#==============================Friendly Link template===============================
if templateSelect == "2":
  msg = MIMEMultipart('alternative')
  msg['Subject'] = raw_input("[?] Subject:       ")
  fromName = raw_input("[?] From who?:       ")
  maliLink = raw_input("[?] Change the malicious link? Yes/No:        ")
  if maliLink == "Yes":
    maliLink = raw_input("[?] Insert the link:        ")
  else: 
    maliLink = "https://www.google.com/search?ei=BxZuWoHhI8mzzwKt4K24DQ&q=you+have+been+redirected&oq=you+have+been+redirected&gs_l=psy-ab.3..0l2j0i22i30k1l8.2101.8048.0.8428.24.24.0.0.0.0.134.2130.18j6.24.0....0...1c.1.64.psy-ab..0.24.2128...0i131k1j0i131i67k1j0i67k1j0i131i10i67k1j0i10k1.0.HqK-v7cdmkA"
  
  text = "Привет!\nКак дела?\nЗдесь ссылка которую ты просил:\nhttp://www.google.com"
  template_Friendly_Link = """\
<html>
  <head></head>
  <body>
    <p>Привет!<br>
       Как дела?<br>
       Здесь <a href=" """+maliLink+""" ">ссылка</a> которую ты просил.
    </p>
  </body>
</html>
"""
  template = template_Friendly_Link
#==============================End of Templates===============================


emails = get_contacts('contacts.txt')

s.starttls()
s.login(login, password)
for email in emails:
  
  msg['To']=email
  msg['From']= fromName
  part1 = MIMEText(text, 'plain')
  part2 = MIMEText(template, 'html')
  msg.attach(part1)
  msg.attach(part2)
  
  s.sendmail(login, email, msg.as_string())
   
  print ("[!] "+ email + " Message has been sent")
s.quit()

