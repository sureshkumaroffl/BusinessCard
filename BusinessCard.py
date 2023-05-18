#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip install easyocr
# !pip install qrcode


# In[18]:


from PIL import Image, ImageDraw, ImageFont
import random
import os
import io
from datetime import datetime
import qrcode
import pandas as pd
import easyocr
import sqlite3
import streamlit as st



con = sqlite3.connect("Bcard3.db")
cur = con.cursor()
# cur.execute("CREATE TABLE cardDetails(company_name,card_holder_name,designation, mobile_number, email_address, website_URL,area, city, state,pincode)")



company_name=""
card_holder_name=""
designation=""
mobile_number=""
email_address=""
website_URL=""
area=""
city=""
state=""
pincode=""
comp_desc="Take this opportunity to craft your own business"
ImgOpt=""



fun_Mode=st.sidebar.selectbox('Select Mode', ['Select Mode','MyDetails', 'ocrFetch'])
if fun_Mode=="ocrFetch":
    getImage=st.file_uploader('Upload a CSV')
    if getImage:
        st.image(getImage)
    reader = easyocr.Reader(['en'])
    resultPic = reader.readtext(getImage,detail = 0)

if fun_Mode=="ocrFetch":
    if len(resultPic)!=0:
        if len(resultPic)==10:
            company_name,card_holder_name,designation, mobile_number, email_address, website_URL,area, city, state,pincode=resultPic
        elif len(resultPic)==9:
            company_name,card_holder_name,designation, mobile_number, email_address, website_URL,area, city,state=resultPic
        elif len(resultPic)==8:
            company_name,card_holder_name,designation, mobile_number, email_address, website_URL,area,city=resultPic
        else:
            if len(resultPic)==7:
                company_name,card_holder_name,designation, mobile_number, email_address, website_URL,area=resultPic

    cur.execute("insert into cardDetails values(?,?,?,?,?,?,?,?,?,?)",(company_name,card_holder_name,designation, mobile_number, email_address,website_URL,area, city, state,pincode))
    mysqlite_df=pd.read_sql("SELECT * FROM cardDetails", con, index_col=None,chunksize=None)
    #  ORDER BY company_name DESC LIMIT 1


if fun_Mode=="ocrFetch":

    if getImage:
        company_name=mysqlite_df.iloc[-1]["company_name"]
        card_holder_name=mysqlite_df.iloc[-1]["card_holder_name"]
        designation=mysqlite_df.iloc[-1]["designation"]
        mobile_number=mysqlite_df.iloc[-1]["mobile_number"]
        email_address=mysqlite_df.iloc[-1]["email_address"]
        website_URL=mysqlite_df.iloc[-1]["website_URL"]
        area=mysqlite_df.iloc[-1]["area"]
        city=mysqlite_df.iloc[-1]["city"]
        state=mysqlite_df.iloc[-1]["state"]
        pincode=mysqlite_df.iloc[-1]["pincode"]
        GetButton=st.button('Get Image')
    ImgOpt=st.selectbox('Select Image', ['Select Mode','Image-1', 'Image-2','Image-3'])

if fun_Mode=="MyDetails":
    ImgOpt=st.selectbox('Select Image', ['Select Mode','Image-1', 'Image-2','Image-3'])
    company_name=st.text_input("Enter Company Name")
    card_holder_name=st.text_input("Enter Card Holder Name")
    designation=st.text_input("Enter Designation")
    mobile_number=st.text_input("Enter Mobile Number")
    email_address=st.text_input("Enter Email ID")
    website_URL=st.text_input("Enter Website URL")
    area=st.text_input("Enter Area Name")
    city=st.text_input("Enter City")
    state=st.text_input("Enter State")
    pincode=st.text_input("Enter Pincode")
    
GetButton=st.button('Get Image')    
if GetButton:    
    if ImgOpt=="Image-1":
        im =Image.open(r"bluewhite.png")
        image_bytes=io.BytesIO()
        im.save(image_bytes,format="PNG")
        bcard=Image.open(io.BytesIO(image_bytes.getvalue()))
        draw=ImageDraw.Draw(bcard)

        (x,y)=(700,150)
        color='rgb(70,130,180)'
        font=ImageFont.truetype('arial.ttf',size=90)
        draw.text((x,y),company_name,fill=color,font=font)

        (holderName_x,holderName_y)=(1550,50)
        color='rgb(70,130,180)'
        font=ImageFont.truetype('arial.ttf',size=30)
        draw.text((holderName_x,holderName_y),"Mr."+card_holder_name,fill=color,font=font)

        (designation_x,designation_y)=(1550,90)
        color='rgb(70,130,180)'
        font=ImageFont.truetype('arial.ttf',size=30)
        draw.text((designation_x,designation_y),designation,fill=color,font=font)

        (desc_x,desc_y)=(500,275)
        color='rgb(70,125,170)'
        font=ImageFont.truetype('arial.ttf',size=50)
        draw.text((desc_x,desc_y),comp_desc,fill=color,font=font)

        Create_color='rgb(255,255,255)'
        font=ImageFont.truetype('arial.ttf',size=30)
        draw.text((1300,1050),"Created by: sureshkumaroffl",fill=Create_color,font=font)

        (details_x,details_y)=(400,480)
        ftext=f"""
        Contact Details:
        ----------------------
        ► {website_URL}
        ► {mobile_number}
        ► {email_address}
        ► {area},{city}
        ► {state}-{pincode}

            """
        color='rgb(70,130,180)'
        font=ImageFont.truetype('arial.ttf',size=45)
        draw.text((details_x,details_y),ftext,fill=color,font=font)

        qrc=qrcode.make(website_URL)
        bcard.paste(qrc,(1550,400))

        bcard.show()

if GetButton:
    if ImgOpt=="Image-2":
        im =Image.open(r"greenwhitered.png")
        image_bytes=io.BytesIO()
        im.save(image_bytes,format="PNG")
        bcard=Image.open(io.BytesIO(image_bytes.getvalue()))
        draw=ImageDraw.Draw(bcard)


        (x,y)=(1100,150)
        color='rgb(70,130,180)'
        font=ImageFont.truetype('arial.ttf',size=90)
        draw.text((x,y),company_name,fill=color,font=font)


        (holderName_x,holderName_y)=(50,70)
        color='rgb(70,130,180)'
        font=ImageFont.truetype('arial.ttf',size=30)
        draw.text((holderName_x,holderName_y),"Mr."+card_holder_name,fill=color,font=font)

        (designation_x,designation_y)=(50,110)
        color='rgb(70,130,180)'
        font=ImageFont.truetype('arial.ttf',size=30)
        draw.text((designation_x,designation_y),designation,fill=color,font=font)


        (desc_x,desc_y)=(850,275)
        color='rgb(70,125,170)'
        font=ImageFont.truetype('arial.ttf',size=50)
        draw.text((desc_x,desc_y),comp_desc,fill=color,font=font)


        Create_color='rgb(255,255,255)'
        font=ImageFont.truetype('arial.ttf',size=30)
        draw.text((200,1050),"Created by: sureshkumaroffl",fill=Create_color,font=font)


        (details_x,details_y)=(1250,430)
        ftext=f"""
        Contact Details:
        ----------------------
        ► {website_URL}
        ► {mobile_number}
        ► {email_address}
        ► {area},{city}
        ► {state}-{pincode}


            """
        color='rgb(70,130,180)'
        font=ImageFont.truetype('arial.ttf',size=45)
        draw.text((details_x,details_y),ftext,fill=color,font=font)
        qrc=qrcode.make(website_URL)
        bcard.paste(qrc,(50,200))
        bcard.show()

if GetButton:
    if ImgOpt=="Image-3":
        im =Image.open(r"BlueImg.png")
        image_bytes=io.BytesIO()
        im.save(image_bytes,format="PNG")
        bcard=Image.open(io.BytesIO(image_bytes.getvalue()))
        draw=ImageDraw.Draw(bcard)

#                     comp_name="Mayava Title text"
#                     holderName="Mayava Title text"
#                     designation="CEO"
#                     comp_desc="Mayava text description details for this company"
#                     website="Mayava Title text"
#                     phone="9876543210"
#                     Email="mymail@gmail.com"
#                     address="adsd hgjhgjhg jkhkjhkjh"

        (x,y)=(950,300)
        color='rgb(70,130,180)'
        font=ImageFont.truetype('arial.ttf',size=90)
        draw.text((x,y),company_name,fill=color,font=font)

        (holderName_x,holderName_y)=(1700,170)
        color='rgb(70,130,180)'
        font=ImageFont.truetype('arial.ttf',size=40)
        draw.text((holderName_x,holderName_y),"Mr."+card_holder_name,fill=color,font=font)

        (designation_x,designation_y)=(1700,210)
        color='rgb(70,130,180)'
        font=ImageFont.truetype('arial.ttf',size=40)
        draw.text((designation_x,designation_y),designation,fill=color,font=font)

        (desc_x,desc_y)=(750,425)
        color='rgb(70,125,170)'
        font=ImageFont.truetype('arial.ttf',size=50)
        draw.text((desc_x,desc_y),comp_desc,fill=color,font=font)

        Create_color='rgb(90,130,180)'
        font=ImageFont.truetype('arial.ttf',size=30)
        draw.text((1700,950),"Created by: sureshkumaroffl",fill=Create_color,font=font)

        (details_x,details_y)=(630,630)
        ftext=f"""
        Contact Details:
        ----------------------
        ► {website_URL}
        ► {mobile_number}
        ► {email_address}
        ► {area},{city}
        ► {state}-{pincode}

            """
        color='rgb(70,130,180)'
        font=ImageFont.truetype('arial.ttf',size=45)
        draw.text((details_x,details_y),ftext,fill=color,font=font)

        qrc=qrcode.make(website_URL)
        bcard.paste(qrc,(1750,650))
        bcard.show()





