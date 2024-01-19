-- Find weighted average
-- Using a procedure to comute the value

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Change Delimiter
DELIMITER $$

-- Create Procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
DECLARE score_weight FLOAT;
DECLARE user_id_rep INT;
DECLARE b INT;

-- Define a cursor to traverse the user table to update it
DECLARE user_curs CURSOR FOR SELECT id FROM users;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET b = 1;
OPEN user_curs;

-- query for the scores in corrections and weight of each course in projects
user_loop: LOOP
FETCH user_curs INTO user_id_rep;
IF b = 1 THEN
LEAVE user_loop;
END IF;

SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight) INTO score_weight
FROM corrections
JOIN projects ON projects.id = corrections.project_id
WHERE corrections.user_id = user_id_rep;

-- Update the user table for the given ID
UPDATE users
SET average_score = score_weight
WHERE id = user_id_rep;

-- end loop on user table, close cursor and the compound statement
END LOOP;
CLOSE user_curs;
END $$

DELIMITER ;
