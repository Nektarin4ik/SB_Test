WITH RECURSIVE balances AS (
  SELECT acc_from AS acc, tdate AS dt, -amount AS balance
  FROM transfers
  UNION ALL
  SELECT acc_to AS acc, tdate AS dt, amount AS balance
  FROM transfers
), acc_balances AS (
  SELECT acc, dt, SUM(balance) OVER (PARTITION BY acc ORDER BY dt) AS balance
  FROM balances
), acc_periods AS (
  SELECT acc, dt AS dt_from, LEAD(dt) OVER (PARTITION BY acc ORDER BY dt) AS dt_to, balance
  FROM acc_balances
)
SELECT acc, dt_from, COALESCE(dt_to, '3000-01-01'::date) as dt_to, balance
FROM acc_periods
ORDER BY dt_from