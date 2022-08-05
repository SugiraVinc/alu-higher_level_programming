-- List number of records with the same values
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
