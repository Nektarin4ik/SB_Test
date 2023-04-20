WITH RECURSIVE random_dates(random_date, flag) AS (
  SELECT current_date::timestamp, 1
  UNION ALL
  SELECT random_date + (random() * 5 + 2) * interval '1 day', flag + 1
  FROM random_dates
  WHERE flag < 100
)
SELECT random_date::date FROM random_dates;