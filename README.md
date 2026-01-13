# OLA-Insights
An end-to-end data analytics project built with PostgreSQL, SQL, Python, Streamlit, and Power BI to analyze ride performance, cancellations, revenue, and customer behavior through interactive dashboards.

---

## 📌 Project Overview

The **OLA Ride Analytics Platform** is designed to:
- Analyze ride performance, revenue, cancellations, and ratings
- Identify operational issues such as incomplete rides and driver-related problems
- Present insights in two formats:
  - **Streamlit App** → Query-level, technical analysis
  - **Power BI Dashboard** → High-level business storytelling

---

## 🧠 Key Analytics Covered

The project answers **10 real-world business questions** using SQL:

1. ✅ Successful rides analysis  
2. 📏 Average distance by vehicle type  
3. ❌ Customer cancellations  
4. 🧑‍🤝‍🧑 Top customers by rides booked  
5. 🚗 Driver issues & vehicle breakdowns  
6. ⭐ Sedan driver ratings (highest & lowest)  
7. 💳 UPI-based rides analysis  
8. 😊 Average customer rating by vehicle type  
9. 💰 Total revenue from completed rides  
10. ⚠️ Incomplete rides with root-cause analysis  

---

## 🖥️ Streamlit SQL Analytics App

The Streamlit application executes SQL queries on a PostgreSQL database and displays results in a **dark-themed, interactive UI**.

### 🔹 Key Features
- KPI cards for revenue, successful rides, and top vehicle type  
- Query-wise navigation (1–10)  
- Clean tabular results with business context  
- Focus on operational insights and decision-making  

### 📸 Screenshots – Streamlit App

#### Dashboard & KPIs
<img width="1837" height="454" alt="image" src="https://github.com/user-attachments/assets/024454d7-eefe-4a59-be2a-8972f721d182" />


#### SQL Query Results 

- Success Ride Booking 
<img width="1732" height="677" alt="image" src="https://github.com/user-attachments/assets/127dd58d-fa36-4b77-9897-643a6999b74b" />

– Average Distance by Vehicle
<img width="1735" height="516" alt="image" src="https://github.com/user-attachments/assets/b4f581f4-e887-4556-b177-c6975b3a48d7" />

- Customer Cancellations
<img width="1735" height="516" alt="image" src="https://github.com/user-attachments/assets/e6a51f02-3812-4d8b-844b-d2a7197a505f" />

#### Customer Cancellations
<img width="1735" height="516" alt="image" src="https://github.com/user-attachments/assets/e6a51f02-3812-4d8b-844b-d2a7197a505f" />


#### Incomplete Rides Analysis
![Incomplete Rides](screenshots/incomplete_rides.png)

---

## 📊 Power BI Dashboard

The Power BI dashboard provides an **executive-level overview** of the same dataset used in Streamlit.

### 🔹 Dashboard Highlights
- Total successful rides, cancellations, distance, and booking value  
- Payment method distribution  
- Booking status breakdown  
- Driver vs customer cancellation comparison  
- Day-wise booking trends  
- Interactive slicers (date & vehicle type)  

###  Power BI Dashboard

- 📸 Screenshot 
<img width="1542" height="845" alt="image" src="https://github.com/user-attachments/assets/603b063d-1da0-431f-9f36-3cb462d98a77" />

- 🌐 Link – Power BI Dashboard
 https://app.powerbi.com/view?r=eyJrIjoiMjNjMzdjZjMtYmFhYy00ZjU5LThmNjUtOTFhODU0MDZiMjI0IiwidCI6IjMxMDYwNmQ3LWJiZGUtNDc4Zi05ZWM0LTRkYjBhM2Q0ZTJkMyJ9


---

## 📌 Key Business Insights

- 🚦 Over **70% of incomplete rides** are caused by **customer demand issues and vehicle breakdowns**
- 🚲 **eBike and Prime vehicles** show higher average ride distances
- ⭐ Customer ratings remain consistently high across most vehicle types
- 🔁 Cancellations are almost evenly split between drivers and customers, requiring balanced interventions

---

## 🛠 Tech Stack

- **Database:** PostgreSQL  
- **Query Language:** SQL  
- **Backend & Analysis:** Python, Pandas  
- **Web App:** Streamlit  
- **BI & Visualization:** Power BI  

---

## 🚀 How This Project Adds Value

This project demonstrates:
- Strong **SQL and data analysis skills**
- Ability to convert **data → insights → business decisions**
- Experience working with **multiple analytics tools on the same dataset**
- Clear separation between **technical analysis** and **stakeholder reporting**

---

## 📬 Contact

- 💼 LinkedIn: *https://www.linkedin.com/in/sayanj1999/*  
- 🌐 Portfolio: *https://sayanj-portfolio.netlify.app/*  

---

⭐ **If you find this project useful, consider giving it a star!**
