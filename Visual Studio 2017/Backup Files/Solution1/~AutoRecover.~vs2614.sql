USE HospitalDB;

CREATE TABLE Table_USA (
    customer_name NVARCHAR(255) NOT NULL,
    customer_id NVARCHAR(18) NOT NULL PRIMARY KEY,
    open_date DATE,
    last_consulted_date DATE,
    vaccination_type CHAR(5),
    doctor_name NVARCHAR(255),
    state CHAR(5),
    country CHAR(5),
    post_code INT,
    dob DATE,
    is_active CHAR(1),
    age AS (DATEDIFF(YEAR, dob, GETDATE())),
    days_since_last_consulted AS (DATEDIFF(DAY, last_consulted_date, GETDATE()))
);
