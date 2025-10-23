'''
Aula Banco de dados em pratica
instalar sqllite alexcv


show tables
.tables

ctrl + shift + Q


.schema   mostra o esquema de criação da tabela (codigo para criar a tabela)

SELECT indicando a coluna (atributos) COUNT () AS e coluna conta registros

FROM vai para a tabela

WHERE DEPOIS DO FROM  faz busca (filtro) exata pelo nome ou dados que solicite

GROUP BY agrupar as colunas 

HAVING filtragem só depois do agrupamento group by

ORDER BY  ordenar

SELECT nom MAX((calculo)/2) AS media
FROM Aluno


funções
COUNT ()
MAX((CALCULO))
MIN ((calculo))
SUM  soma   - SELECT SUM (coluna) 
AVG media   - SELECT AVG (coluna)


SELECT nome
FROM Aluno

WHERE
WHERE nome IN
WHERE nome LIKE "%nome%"
_ underline quantidade caracteres
"%li__"


Antonio
ter., 21 de out., 20:33 (há 2 dias)
para Antonio, mim

join sql

junção
união de tabelas  chave primaria e um chave estrangeira

left join  prioriza a esquerda agrupa o que vem a direita
right join  inverso
inner join interseção comum aos dois
full join união tudo


INSERT INTO  Aluno (dados da tabela, colunas atributos)
VALUES ( dados inserção)

SELECT *
FROM Aluno
JOIN Turma
ON 


Atividade Banco de Dados


'''