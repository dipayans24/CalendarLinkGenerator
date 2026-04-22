import streamlit as st
from datetime import timedelta
from calendar_link import CalendarEvent, CalendarGenerator

header = st.header("Calendar Link Generator")
title = st.text_input("Title:")
zoom_link = st.text_input("Zoom Link:")
meetingID = st.text_input("Meeting ID:")

description = st.text_area("Enter additional details", placeholder="Optional")

col1, col2 = st.columns(2)
with col1:
    start_date = st.datetime_input(label="Start Time", format="YYYY-MM-DD")
    start_time = start_date - timedelta(hours=5, minutes=30)
with col2:
    end_date = st.datetime_input(label="End Time", format="YYYY-MM-DD")
    end_time = end_date - timedelta(hours=5, minutes=30)

calenderLinkType = "google"
#calenderLinkType = st.selectbox(label = "Select the calendar Link Type", options=["google", "apple", "yahoo", "aol", "office365"],)

def generateLink(title, start_time, end_time, description, calenderLinkType,zoom_link, meetingID ):
    total_seconds = (end_time - start_time).seconds
    hours = round(total_seconds // 3600, 0)
    minutes = round((total_seconds % 3600) // 60, 0)
    Duration = f"{hours}h {minutes}m"

    event = CalendarEvent(
        title=title,
        start_time=start_time,
        end_time=end_time,
        description=f"""📌 {description}\n🔗Zoom Link: {zoom_link}\n🆔 Webinar ID: {meetingID}\n⏰ Duration: {Duration}""" 
    )

    generator = CalendarGenerator()
    google_link = generator.generate_link(event, calenderLinkType)

    st.code(google_link, wrap_lines=True)

@st.dialog("Error Alert")
def checkButton(text):   
    st.error(text)


GenerateButton = st.button("Generate Calendar Link", type="primary")
if GenerateButton:
    if title == "":
        checkButton("Title cannot be empty")
    elif zoom_link == "":
        checkButton("Zoom Link cannot be empty")
    elif meetingID =="":
        checkButton("Meeting ID cannot be empty")
    else:
        if start_time >= end_time:
            checkButton("Start time must be before end time.")
        else:
            description = "Details" if description == "" else description
            generateLink(title, start_time, end_time,description, calenderLinkType, zoom_link, meetingID)

