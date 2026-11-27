SELECT COUNT(*) AS row_count, SUM(budget) AS budget, SUM(actual) AS actual, SUM(budget)-SUM(actual) AS variance FROM dbo.FactDelivery;
