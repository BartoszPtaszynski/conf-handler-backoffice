import pandas as pd
import streamlit as st

from utils.restController import get_sessions, get_events
from utils.utils import load_css

css = load_css("style/styles.css")

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
logout_button = st.sidebar.button("Wyloguj")

st.markdown("Conf-handler backoffices")

conference_id = 1

sessions, events = st.tabs(["Sessions", "Lectures / Events"])
session_list = pd.DataFrame(get_sessions())
with sessions:
    selected_columns = session_list.iloc[:, 1:]
    st.write(selected_columns)

with events:
    df = pd.DataFrame(get_events())

    # df["eventDate"] = pd.to_datetime(df["eventDate"], format="%Y-%m-%d")
    # df["timeStart"] = pd.to_datetime(df["timeStart"], format="%H:%M:%S").dt.time
    # df["timeEnd"] = pd.to_datetime(df["timeEnd"], format="%H:%M:%S").dt.time

    df = df.sort_values(by=["eventDate", "timeStart"])

    for eventDate, day_events in df.groupby("eventDate"):
        st.header(f"📅 {eventDate}")

        displayed_sessions = set()

        for idx, row in day_events.iterrows():
            if pd.notnull(row["sessionId"]):  # Jeśli event należy do sesji
                session_id = row["sessionId"]

                if session_id not in displayed_sessions:
                    session_name = session_list.loc[session_list["id"] == session_id, "name"].values

                    if len(session_name) > 0:
                        session_name_str = session_name[0]
                    else:
                        session_name_str = "Events without session"

                    with st.expander(f"📌{session_name_str}"):
                        session_events = day_events[day_events["sessionId"] == session_id]

                        edited_events = st.data_editor(session_events, num_rows="dynamic")

                    displayed_sessions.add(session_id)
            else:
                st.write(f"🕘 {row['timeStart']} - {row['timeEnd']} | {row['eventName']} at ")
                if pd.notna(row["abstract"]):
                    st.markdown(f"[🔗 Abstract]({row['abstract']})")
