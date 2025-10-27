SELECT 22

--1
SELECT *
FROM Aluno
--2
SELECT nome, nota1
FROM Aluno
--3
SELECT nome, nota2
FROM Aluno
WHERE nota2 > 8
--4
SELECT nome, data_nascimento
FROM Aluno
WHERE data_nascimento > '2000-01-01';
--5
SELECT nome, mensalidade
FROM Curso
WHERE mensalidade > 600;
--6
SELECT nome, ano
FROM Turma
ORDER BY ano ASC;
--7
SELECT ano, COUNT (*) AS quantidade_turmas
FROM Turma
GROUP BY ano;
--8
SELECT id_turma, AVG (nota1) AS Media
FROM Aluno
GROUP BY id_turma;
--9
SELECT ano, COUNT (*) as quantidade_turmas_alunos_mais2tur
FROM Turma
GROUP BY ano
HAVING COUNT (*) > 2;
--10
SELECT nome, mensalidade
FROM Curso
ORDER BY mensalidade DESC;