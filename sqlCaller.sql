--# Display Sorted
-- SELECT *
-- FROM [dbo].[Transactions]
-- WHERE Amount = -65.70
-- ORDER BY DateTracked;

--# Display Month of Records
-- EXEC SelectRecordsByMonth @year = 2024, @month = 1;

--# Display Account Totals
SELECT * FROM AccountTotals;
-- WHERE Account = '';

--# Update Fields
-- UPDATE [dbo].[Transactions]
-- SET DateTracked = ActualDate
-- WHERE DateTracked is NULL;

--# Display Category Totals
-- SELECT * FROM Categories;

--# Display From Tag
-- SELECT * FROM [dbo].[Transactions] WHERE Tags LIKE '%Rent%';