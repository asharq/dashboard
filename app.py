import pandas as pd
import streamlit as st

# Streamlit setup
st.set_page_config(page_title="SmartTech Combined Sales Report", layout="wide")

# Custom CSS for theming
st.markdown(
    """
    <style>
    .header {font-size: 36px; font-weight: bold; color: #2c3e50; text-align: center; margin-bottom: 10px;}
    .sub-header {font-size: 18px; color: #7f8c8d; text-align: center; margin-bottom: 20px;}
    .divider {border-top: 2px solid #eaeaea; margin: 20px 0;}
    .upload-section {padding: 10px; border: 1px solid #ddd; border-radius: 8px; background-color: #f9f9f9;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Header
st.markdown('<div class="header">SmartTech Combined Sales Report</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Upload your transaction files to generate a consolidated report</div>', unsafe_allow_html=True)

# File Upload Section
st.markdown('<div class="upload-section"><b>Upload Files</b></div>', unsafe_allow_html=True)
uploaded_cantaloupe = st.file_uploader("Cantaloupe Transactions", type=["csv"])
uploaded_kiosoft_card = st.file_uploader("Kiosoft Card Transactions", type=["csv"])
uploaded_kiosoft_coin = st.file_uploader("Kiosoft Coin Transactions", type=["csv"])

if uploaded_cantaloupe and uploaded_kiosoft_card and uploaded_kiosoft_coin:
    # Load data
    cantaloupe_df = pd.read_csv(uploaded_cantaloupe)
    kiosoft_card_df = pd.read_csv(uploaded_kiosoft_card)
    kiosoft_coin_df = pd.read_csv(uploaded_kiosoft_coin)

    # Preprocess Cantaloupe Data
    cantaloupe_df.rename(columns={"Unnamed: 7": "Amount ($)"}, inplace=True)
    cantaloupe_df["Amount ($)"] = pd.to_numeric(cantaloupe_df["Amount ($)"].replace("[$,]", "", regex=True), errors="coerce")
    cantaloupe_df["Day"] = pd.to_datetime(cantaloupe_df["Day"], errors="coerce").dt.date
    cantaloupe_df["Source"] = cantaloupe_df["Location"]
    cantaloupe_df.dropna(subset=["Day", "Amount ($)", "Source"], inplace=True)

    # Preprocess Kiosoft Card Data
    # Flexible column lookup for date-time
    date_time_column = "Date Time" if "Date Time" in kiosoft_card_df.columns else kiosoft_card_df.columns[0]
    kiosoft_card_df[date_time_column] = pd.to_datetime(kiosoft_card_df[date_time_column].str.strip(), errors="coerce").dt.date
    kiosoft_card_df["Total Amount ($)"] = pd.to_numeric(kiosoft_card_df["Total Amount ($)"], errors="coerce")
    kiosoft_card_df["Source"] = kiosoft_card_df["Machine ID"].apply(lambda x: f"Machine ID {x}" if pd.notnull(x) else "Unknown Machine")
    kiosoft_card_df.dropna(subset=[date_time_column, "Total Amount ($)", "Source"], inplace=True)

    # Preprocess Kiosoft Coin Data
    # Flexible column lookup for date-time
    date_time_column_coin = "Date/Time" if "Date/Time" in kiosoft_coin_df.columns else kiosoft_coin_df.columns[0]
    kiosoft_coin_df[date_time_column_coin] = pd.to_datetime(kiosoft_coin_df[date_time_column_coin].str.strip(), errors="coerce").dt.date
    kiosoft_coin_df["Amount ($)"] = pd.to_numeric(kiosoft_coin_df["Amount ($)"].replace("[$,]", "", regex=True), errors="coerce")
    kiosoft_coin_df["Source"] = kiosoft_coin_df["Machine ID"].apply(lambda x: f"Machine ID {x}" if pd.notnull(x) else "Unknown Machine")
    kiosoft_coin_df.dropna(subset=[date_time_column_coin, "Amount ($)", "Source"], inplace=True)

    # Combine Data
    kiosoft_combined = pd.concat([
        kiosoft_card_df[[date_time_column, "Total Amount ($)", "Source"]].rename(columns={date_time_column: "Day", "Total Amount ($)": "Amount ($)"}),
        kiosoft_coin_df[[date_time_column_coin, "Amount ($)", "Source"]].rename(columns={date_time_column_coin: "Day"})
    ])
    combined_sales = pd.concat([
        cantaloupe_df[["Day", "Amount ($)", "Source"]],
        kiosoft_combined[["Day", "Amount ($)", "Source"]]
    ])
    combined_sales.dropna(subset=["Day", "Amount ($)", "Source"], inplace=True)

    # Flatten data for pivot table
    flat_data_csv = combined_sales.copy()
    flat_data_csv["Day"] = pd.to_datetime(flat_data_csv["Day"])
    flat_csv_data = flat_data_csv.to_csv(index=False)

    # Render Flat Data Download
    st.download_button(
        label="Download Flat Data for Pivot Table as CSV",
        data=flat_csv_data,
        file_name="flat_sales_data.csv",
        mime="text/csv"
    )
