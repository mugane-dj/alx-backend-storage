-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE project_score DECIMAL(10, 2);

    SELECT AVG(score) INTO project_score
    FROM corrections
    WHERE user_id = user_id;

    UPDATE users
    SET average_score = project_score
    WHERE id = user_id;
END;
//
DELIMITER ;