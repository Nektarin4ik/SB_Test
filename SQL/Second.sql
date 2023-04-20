SELECT e.id, e.name, 
       COUNT(s.id) AS sales_c, 
       RANK() OVER (ORDER BY COUNT(s.id) DESC) AS sales_rank_c, 
       SUM(s.price) AS sales_s, 
       RANK() OVER (ORDER BY SUM(s.price) DESC) AS sales_rank_s
FROM employee e
LEFT JOIN sales s ON e.id = s.employee_id
GROUP BY e.id, e.name
ORDER BY sales_rank_s, sales_rank_c