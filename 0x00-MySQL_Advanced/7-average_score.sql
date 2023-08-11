-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE project_score DECIMAL(10, 2);
    DECLARE project_count INT;

    SET project_score = 0;
    SET project_count = 0;

    SELECT SUM(score), COUNT(*) INTO project_score, project_count
    FROM corrections
    WHERE user_id = user_id;

    IF project_count > 0 THEN
        UPDATE users
        SET average_score = project_score / project_count
        WHERE id = user_id;
    END IF;
END;
//
DELIMITER ;