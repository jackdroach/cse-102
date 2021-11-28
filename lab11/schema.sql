-- Jack Roach, CSE 102 D, Lab 11, November 17, 2020

CREATE TABLE students (
  uniqueID int,
  name varchar(30),
  gpa double,
  university_name varchar(30), 
  university_state varchar(30),
  university_city varchar(30)
);

INSERT INTO students
(uniqueID,name,gpa,university_name,university_state,university_city)
VALUES
(123,'steve',4,'miami','ohio','oxford'),
(367,'amy',3.9,'osu','ohio','columbus'),
(124,'bob',3.7,'miami','ohio','oxford'),
(652,'charlie',2.7,'uc','ohio','cincinnati'),
(842,'dave',4,'osu','ohio','columbus'),
(358,'erin',2.9,'uk','kentucky','lexington'),
(302,'frank',3.8,'uc','ohio','cincinnati'),
(123,'george',3.4,'miami','ohio','oxford'),
(805,'hank',2.2,'uk','kentucky','lexington'),
(407,'ivan',2.8,'uc','ohio','cincinnati');