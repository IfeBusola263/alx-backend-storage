-- Creating a view 'need_meeting' that lists students with students
-- Under 80 and no 'last_meeting' or more than 1 month

DROP VIEW IF EXISTS need_meeting;

-- Create view
CREATE VIEW need_meeting
AS SELECT name
FROM students

-- Specify the Where clause for scores below 8 and last_meeting
-- greater than 30 days
WHERE score < 80 AND (last_meeting IS NULL OR DATEDIFF(CURDATE(),last_meeting) > 31);
