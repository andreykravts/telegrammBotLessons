BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "music" (
	"Id"	INTEGER,
	"file_id"	TEXT,
	"right_answer"	TEXT,
	"wrong_answers"	TEXT,
	PRIMARY KEY("Id")
);
INSERT INTO "music" ("Id","file_id","right_answer","wrong_answers") VALUES (1,'101','Imagine Dragons','Nogu Svelo'),
 (2,'102','Artic Monkeys','Lana Del Grey'),
 (3,'103','The Pixies','The Toxic Avenger'),
 (4,'104','The Black Eyed','Travis Scott'),
 (5,'105','Arabeqsque','Frank Dunwalle');
COMMIT;
