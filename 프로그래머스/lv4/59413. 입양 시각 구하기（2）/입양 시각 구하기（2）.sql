# 코드를 입력하세요
WITH RECURSIVE sub1 AS (SELECT 0 as HOUR
                        UNION
                        SELECT HOUR + 1 FROM sub1
                        WHERE HOUR < 23),
sub2 AS (SELECT HOUR(DATETIME) as HOUR, COUNT(*) as count
            FROM ANIMAL_OUTS
            GROUP BY 1
            ORDER BY 1)

SELECT s1.HOUR, IFNULL(s2.count,0) as COUNT
FROM sub1 s1
LEFT JOIN sub2 s2
ON s1.HOUR = s2.HOUR