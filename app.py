import pandas as pd
import streamlit as st

# Streamlit setup
st.set_page_config(page_title="SmartTech Enhanced Sales Report", layout="wide")

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
st.markdown('<div class="header">SmartTech Enhanced Sales Report</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Upload your transaction files to generate a detailed report</div>', unsafe_allow_html=True)

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
    cantaloupe_df["Source"] = cantaloupe_df.get("Location", "Unknown")
    cantaloupe_df["Transaction Type"] = cantaloupe_df.get("Trans Type", "Unknown")  # Include Trans Type
    cantaloupe_df.dropna(subset=["Day", "Amount ($)", "Source"], inplace=True)

    # Preprocess Kiosoft Card Data
    # Dynamically identify the amount column
    amount_column_card = [col for col in kiosoft_card_df.columns if "Amount" in col][0]
    kiosoft_card_df["Date Time"] = pd.to_datetime(kiosoft_card_df["Date Time"], errors="coerce").dt.date
    kiosoft_card_df["Amount ($)"] = pd.to_numeric(kiosoft_card_df[amount_column_card], errors="coerce")
    kiosoft_card_df["Source"] = kiosoft_card_df["Machine ID"].apply(lambda x: f"Machine ID {x}" if pd.notnull(x) else "Unknown Machine")
    kiosoft_card_df["Response Code"] = kiosoft_card_df.get("Response Code", "Unknown")
    kiosoft_card_df["Transaction Type"] = kiosoft_card_df.get("Transaction Type", "Unknown")
    if "Bank Card Number" in kiosoft_card_df.columns:
        kiosoft_card_df["Card Type"] = kiosoft_card_df["Bank Card Number"].str.extract(r"([A-Za-z]+)$", expand=False).fillna("Unknown")
    else:
        kiosoft_card_df["Card Type"] = "Unknown"
    kiosoft_card_df.dropna(subset=["Date Time", "Amount ($)", "Source"], inplace=True)

    # Preprocess Kiosoft Coin Data
    # Dynamically identify the amount column
    amount_column_coin = [col for col in kiosoft_coin_df.columns if "Amount" in col][0]
    kiosoft_coin_df["Date/Time"] = pd.to_datetime(kiosoft_coin_df["Date/Time"], errors="coerce").dt.date
    kiosoft_coin_df["Amount ($)"] = pd.to_numeric(kiosoft_coin_df[amount_column_coin].replace("[$,]", "", regex=True), errors="coerce")
    kiosoft_coin_df["Source"] = kiosoft_coin_df["Machine ID"].apply(lambda x: f"Machine ID {x}" if pd.notnull(x) else "Unknown Machine")
    kiosoft_coin_df["Response Code"] = "N/A"  # Coin transactions won't have response codes
    kiosoft_coin_df["Transaction Type"] = "Coin"
    kiosoft_coin_df.dropna(subset=["Date/Time", "Amount ($)", "Source"], inplace=True)

    # Combine Data
    kiosoft_combined = pd.concat([
        kiosoft_card_df[["Date Time", "Amount ($)", "Source", "Response Code", "Transaction Type", "Card Type"]].rename(
            columns={"Date Time": "Day"}),
        kiosoft_coin_df[["Date/Time", "Amount ($)", "Source", "Response Code", "Transaction Type"]].rename(
            columns={"Date/Time": "Day"})
    ])
    combined_sales = pd.concat([
        cantaloupe_df[["Day", "Amount ($)", "Source", "Transaction Type"]],
        kiosoft_combined[["Day", "Amount ($)", "Source", "Response Code", "Transaction Type", "Card Type"]]
    ])
    combined_sales.dropna(subset=["Day", "Amount ($)", "Source"], inplace=True)

    # Flatten data for pivot table
    flat_data_csv = combined_sales.copy()
    flat_csv_data = flat_data_csv.to_csv(index=False)

    # Render Flat Data Download
    st.download_button(
        label="Download Enhanced Detailed Flat Data for Pivot Table",
        data=flat_csv_data,
        file_name="enhanced_sales_data.csv",
        mime="text/csv"
    )
