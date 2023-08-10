-- creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER //
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_name_exists INT;

    SELECT COUNT(*) INTO project_name_exists
    FROM projects
    WHERE name = project_name;

    IF project_name_exists = 0 THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    UPDATE corrections
    SET score = score
    WHERE user_id = user_id AND project_name = project_name;
END
//
DELIMITER ;