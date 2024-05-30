BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "music" (
	"Id"	INTEGER,
	"file_id"	TEXT,
	"right_answer"	TEXT,
	"wrong_answers"	TEXT,
	PRIMARY KEY("Id")
);
INSERT INTO "music" ("Id","file_id","right_answer","wrong_answers")
VALUES (1,'AwACAgQAAxkDAAM6ZliRTpmucrKiAAHgCwEGGq5WFTTiAAL7EgACOivIUiF2LmFuTLu5NQQ','Imagine Dragons','Nogu Svelo'),
 (2,'AwACAgQAAxkDAAM4ZliRSw085I3X5IMTXmTCQeKuOAMAAvoSAAI6K8hSw-16GfdPyoc1BA','Artic Monkeys','Lana Del Grey'),
 (3,'AwACAgQAAxkDAAM0ZliRRPJtlBD-9TKQDhLuufsGRnIAAvgSAAI6K8hSp4Sk1pHEbtM1BA','The Pixies','The Toxic Avenger'),
 (4,'AwACAgQAAxkDAAMyZliRQRq3vnKIC00EE_s552DcLA8AAvcSAAI6K8hSqeF8xJqjkc41BA','The Black Eyed','Travis Scott'),
 (5,'105','AwACAgQAAxkDAAM2ZliRR-LPl20c1S6qyc3ZHB1rO9sAAvkSAAI6K8hS0A07m0nacxQ1BA','Frank Dunwalle');
COMMIT;
