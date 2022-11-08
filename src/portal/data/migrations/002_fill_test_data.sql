INSERT INTO project (title, description, technology, image)
VALUES
    ('My Project #1', 'This is my first project', 'python', 'project_1.png'),
    ('My Project #2', 'This is my second project', 'c#', 'project_2.png'),
    ('My Project #3', 'This is my third project', 'python', 'project_3.png');

INSERT INTO category (name)
VALUES
    ('python'),
    ('c#');

INSERT INTO post (title, body, created_on, last_modified)
VALUES
    ('First Django Project', 
    'This is my first Django project. It has special project structure different than vanilla Django apps structure', 
    '2022-10-10', '2022-10-10'),
    ('.NET Project Structure', 
    'This post is about project structure used in .NET ASP projects. It has three strictly differentiated layers: data, busyness and presentation', 
    '2022-10-11', '2022-10-11'),
    ('Django vs .NET', 
    'In this post I compare python Django web framework with very similar c# ASP.NET projects', 
    '2022-11-12', '2022-11-12');

INSERT INTO post_category (post_id, category_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 1),
    (3, 2);

INSERT INTO comment (post_id, author, body, created_on)
VALUES
    (1, 'aeinstein', 'Totally agree', '2022-10-10'),
    (1, 'niels_bohr', 'Totally disagree', '2022-10-10'),
    (1, 'Neu_maNN', 'interesting...', '2022-10-12'),
    (3, 'niels_bohr', 'really good', '2022-11-12'),
    (3, 'aeinstein', 'this sukks', '2022-12-03');
