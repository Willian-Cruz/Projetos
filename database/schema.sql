CREATE TABLE IF NOT EXISTS vagas (

    id INT PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    empresa TEXT,
    localizacao TEXT,
    salario REAL,
    nivel TEXT,
);