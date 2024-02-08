# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 22:21:04 2024

@author: Sreejit
"""

import streamlit as st

# Page title
st.title("When we first met")

# Image and text side by side
col1, col2 = st.columns(2)

# Image on the left
image_path = "img1.jpeg"  # Replace with the actual path to your image
col1.image(image_path, use_column_width=True, caption="Our First Date")

# Text on the right
col2.write("""
We matched on 19th March, and we had to wait 41 days to go out on our first date! Those 41 days were nothing less than an emotional roller coaster.

Having an ACTUAL GIRLFRIEND for the very first time felt surreal. My head couldn't believe it... A girl LIKES ME??? This guy??? How?? But you did... you loved me, and so did I. I knew I was done when, on the very first day, you had me smiling by just looking at your texts—with all your inappropriate jokes and the cutest smile ever. Every day, I woke up, and the first thing I saw was a good morning wish from you. And that, to this day, makes me smile.

And Then one day you said, "I am already in love with you," and I swear to God, I jumped with a smile so big on my face... you're just so perfect and so mine.

Love,
Bhoduu
""")

st.header("[When we first hugged thik koree!](https://zq3xt4bru3ckvpabrq6q4p.streamlit.app/)")
