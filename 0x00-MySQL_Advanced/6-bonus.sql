-- A procedure AddBonus thats adds a new correction for a student.
-- Correction is added based on input values user_id, project_name, score

DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN

DECLARE projectId INT;

SELECT id INTO projectId FROM projects
WHERE name = project_name;

IF projectId IS NULL THEN
INSERT INTO projects (name) VALUES (project_name);
SELECT id INTO projectId FROM projects
WHERE name = project_name;
END IF;

INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, projectId, score); 
END $$

DELIMITER ;
