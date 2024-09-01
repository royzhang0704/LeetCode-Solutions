DELETE p1
FROM Person p1
INNER JOIN (
    SELECT MIN(Id) as Id, Email
    FROM Person
    GROUP BY Email
) as p2 
ON p1.Id > p2.Id AND p1.Email = p2.Email;
