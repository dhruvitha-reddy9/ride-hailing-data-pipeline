CREATE TABLE ride_dw.dim_driver AS
SELECT DISTINCT
    userId AS driver_id
FROM ride_dw.fact_trips;