-- A procedure ComputeAverageScoreForUser
-- The proedure computes and stores the average score for a student

-- change Delimiter
DELIMITER $$

-- Create the procedure DDL
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
DECLARE total_score INT;
DECLARE total_course INT;
DECLARE ave_score FLOAT DEFAULT 0;

-- Querry the corrections table for all the scores of the student
SELECT SUM(score), COUNT(score) INTO total_score, total_course FROM corrections
WHERE corrections.user_id = user_id;

-- Find the average of the score
SET ave_score = (total_score / total_course);

-- Update the user table with the average score
UPDATE users SET average_score=ave_score WHERE id = user_id;

-- End the compound statment
END $$

-- restore delimiter
DELIMITER ;
