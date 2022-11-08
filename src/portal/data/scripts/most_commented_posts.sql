SELECT p.id, count(*) AS cnt
FROM post AS p JOIN comment AS c ON p.id = c.post_id
GROUP BY p.id
ORDER BY cnt DESC
LIMIT {max_cnt}