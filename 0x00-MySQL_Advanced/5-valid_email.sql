-- Create a trigger for resetting the valid email atribute of
-- the table users, when the email is updated

DELIMITER $$ ;
CREATE TRIGGER user_trigger BEFORE UPDATE ON users FOR EACH ROW
BEGIN
-- IF OLD.email <> NEW.email AND OLD.valid_email = 0 THEN
-- SET NEW.valid_email = 1;
-- ELSEIF OLD.email <> NEW.email AND OLD.valid_email = 1 THEN
-- SET NEW.valid_email = 0;
IF OLD.email <> NEW.email THEN
SET NEW.valid_email = 0;
END IF;
END $$

DELIMITER ;
