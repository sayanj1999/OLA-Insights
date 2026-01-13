import streamlit as st
import pandas as pd
from db import get_engine
import queries

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="OLA Ride Analytics",
    layout="wide"
)

st.title("🚖 OLA Ride Analytics Platform")

# -------------------------------------------------
# Database Load Function
# -------------------------------------------------
@st.cache_data
def load_data(query):
    engine = get_engine()
    return pd.read_sql(query, engine)

# -------------------------------------------------
# KPI SECTION (from queries)
# -------------------------------------------------
st.subheader("📊 Key Metrics")

revenue_df = load_data(queries.TOTAL_SUCCESS_BOOKING_VALUE)
total_revenue = revenue_df.iloc[0, 0]

success_df = load_data(queries.SUCCESS_RIDES)
total_success_rides = success_df.shape[0]

avg_distance_df = load_data(queries.AVG_DISTANCE_BY_VEHICLE)
top_vehicle = avg_distance_df.iloc[0, 0]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Revenue (Successful Rides)", f"₹ {total_revenue:,.0f}")

with col2:
    st.metric("Total Successful Rides", total_success_rides)

with col3:
    st.metric("Top Avg Distance Vehicle", top_vehicle)

st.divider()

# -------------------------------------------------
# SQL QUERY RESULTS (ALL 10)
# -------------------------------------------------
st.subheader("🧠 SQL Query Results")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
    "1️. Success Rides",
    "2️. Avg Distance by Vehicle",
    "3️. Customer Cancellations",
    "4️. Top Customers",
    "5️. Driver Issues",
    "6️. Sedan Ratings",
    "7️. UPI Rides",
    "8️. Avg Cust Rating",
    "9️. Total Revenue",
    "1️0. Incomplete Rides"
])

with tab1:
    st.dataframe(
        load_data(queries.SUCCESS_RIDES),
        use_container_width=True
    )

with tab2:
    st.dataframe(
        load_data(queries.AVG_DISTANCE_BY_VEHICLE),
        use_container_width=True
    )

with tab3:
    st.dataframe(
        load_data(queries.CANCELLED_BY_CUSTOMERS),
        use_container_width=True
    )

with tab4:
    st.dataframe(
        load_data(queries.TOP_5_CUSTOMERS),
        use_container_width=True
    )

with tab5:
    st.dataframe(
        load_data(queries.DRIVER_CANCEL_PERSONAL_ISSUE),
        use_container_width=True
    )

with tab6:
    st.dataframe(
        load_data(queries.SEDAN_DRIVER_RATINGS),
        use_container_width=True
    )

with tab7:
    st.dataframe(
        load_data(queries.UPI_PAYMENTS),
        use_container_width=True
    )       

with tab8:
    st.dataframe(
        load_data(queries.AVG_CUSTOMER_RATING_BY_VEHICLE),
        use_container_width=True
    )
with tab9:
    st.dataframe(
        load_data(queries.TOTAL_SUCCESS_BOOKING_VALUE),
        use_container_width=True
    )

with tab10:
    st.dataframe(
        load_data(queries.INCOMPLETE_RIDES_BY_REASON),
        use_container_width=True
    )   

st.divider()

# -------------------------------------------------
# POWER BI DASHBOARD
# -------------------------------------------------
st.subheader("📊 Power BI Dashboard")

powerbi_url = (
    "https://app.powerbi.com/view?r=eyJrIjoiMjNjMzdjZjMtYmFhYy00ZjU5LThmNjUtOTFhODU0MDZiMjI0IiwidCI6IjMxMDYwNmQ3LWJiZGUtNDc4Zi05ZWM0LTRkYjBhM2Q0ZTJkMyJ9"
)

st.components.v1.iframe(
    src=powerbi_url,
    width=1200,
    height=650,
    scrolling=True
)
