-- Find weighted average
-- Using a procedure to comute the value

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Change Delimiter
DELIMITER $$

-- Create Procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
DECLARE score_weight FLOAT;

-- query for the scores in corrections and weight of each course in projects
SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight) INTO score_weight
FROM corrections
JOIN projects ON projects.id = corrections.project_id
WHERE corrections.user_id = user_id;

-- Update the user table for the given ID
UPDATE users
SET average_score = score_weight
WHERE id = user_id;

-- end the compound statement
END $$

DELIMITER ;
