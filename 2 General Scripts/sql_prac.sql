-- Create the function
CREATE FUNCTION SumRideHrsDateRange (@StartDateParm DATETIME, @EndDateParm DATETIME)
-- Specify return data type
RETURNS NUMERIC
AS
BEGIN
RETURN
-- Sum the difference between StartDate and EndDate
(SELECT SUM(DATEDIFF(second, StartDate, EndDate))/3600
FROM CapitalBikeShare
-- Include only the relevant transactions
WHERE StartDate > @StartDateParm and StartDate < @EndDateParm)
END