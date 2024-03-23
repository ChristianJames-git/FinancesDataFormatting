--# Display Sorted
-- SELECT *
-- FROM [dbo].[Transactions]
-- ORDER BY DateTracked;

--# Display Month of Records
-- EXEC SelectRecordsByMonth @year = 2024, @month = 1;

--# Display Account Totals
-- SELECT * FROM AccountTotals;
-- WHERE Account = '';