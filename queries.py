
# ------------------------------------
# SQL queries for OLA Ride Analytics
# ------------------------------------

# 1️. Successful rides
SUCCESS_RIDES = """
SELECT *
FROM ola_ride
WHERE "Booking_Status" = 'Success';
"""

# 2️. Average ride distance by vehicle (successful rides)
AVG_DISTANCE_BY_VEHICLE = """
SELECT
    "Vehicle_Type",
    AVG("Ride_Distance") AS Avg_Distance
FROM ola_ride
WHERE "Booking_Status" = 'Success'
GROUP BY "Vehicle_Type"
ORDER BY Avg_Distance DESC;
"""

# 3️. Cancelled rides by customer (with total using ROLLUP)
CANCELLED_BY_CUSTOMERS = """
SELECT
    COALESCE("Vehicle_Type", 'Total') AS "Vehicle_Type",
    COUNT(*) AS Cancelled_Rides
FROM ola_ride
WHERE "Booking_Status" = 'Canceled by Customer'
GROUP BY ROLLUP ("Vehicle_Type")
ORDER BY
    CASE WHEN "Vehicle_Type" IS NULL THEN 1 ELSE 0 END,
    Cancelled_Rides DESC;
"""

# 4️. Top 5 customers by successful rides
TOP_5_CUSTOMERS = """
SELECT
    "Customer_ID",
    COUNT(*) AS Total_Rides_Booked
FROM ola_ride
WHERE "Booking_Status" = 'Success'
GROUP BY "Customer_ID"
ORDER BY Total_Rides_Booked DESC
LIMIT 5;
"""

# 5️. Driver cancellations due to personal/car issues
DRIVER_CANCEL_PERSONAL_ISSUE = """
SELECT
    COUNT(*) AS Canceled_Rides_by_Driver_Personal_Car_issue
FROM ola_ride
WHERE "Canceled_Rides_by_Driver" = 'Personal & Car related issue';
"""

# 6️. Highest & lowest driver rating for Prime Sedan
SEDAN_DRIVER_RATINGS = """
SELECT
    MAX("Driver_Ratings") AS Highest_Driver_Rating_Sedan,
    MIN("Driver_Ratings") AS Lowest_Driver_Rating_Sedan
FROM ola_ride
WHERE "Vehicle_Type" = 'Prime Sedan';
"""

# 7️. UPI payment rides
UPI_PAYMENTS = """
SELECT *
FROM ola_ride
WHERE "Payment_Method" = 'UPI';
"""

# 8️. Average customer rating by vehicle
AVG_CUSTOMER_RATING_BY_VEHICLE = """
SELECT
    "Vehicle_Type",
    ROUND(AVG("Customer_Rating"), 2) AS AVG_CUST_Rating
    FROM ola_ride
	GROUP BY "Vehicle_Type"
	ORDER BY AVG_CUST_Rating DESC;
"""

# 9️. Total booking value for successful rides
TOTAL_SUCCESS_BOOKING_VALUE = """
SELECT
    SUM("Booking_Value") AS Total_Booking_Value
FROM ola_ride
WHERE "Booking_Status" = 'Success';
"""

# 10. Incomplete rides by reason
INCOMPLETE_RIDES_BY_REASON = """
Select "Incomplete_Rides_Reason", COUNT(*) as Count
	FROM ola_ride
	WHERE "Incomplete_Rides" = 'Yes'
	GROUP BY "Incomplete_Rides_Reason"
	ORDER BY Count DESC;
"""
