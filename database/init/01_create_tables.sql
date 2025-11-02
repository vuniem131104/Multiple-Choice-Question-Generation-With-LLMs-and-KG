CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    teaching_courses TEXT[],
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (user_name, email, password, full_name, teaching_courses)
VALUES 
('tavietcuong', 'cuongtv@vnu.edu.vn', '$2b$12$cM1kkAoyHDCrUgVoK9q9oeBz./X8aPCG9KU.Td2iQQMqn7GVUO6ym', 'Ta Viet Cuong', ARRAY['int3405', 'dsa2025', 'rl2025']);