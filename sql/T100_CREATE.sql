#DB選択
USE TEACHERSDB;

#T100
DROP TABLE T100_SHITSMN;
CREATE TABLE T100_SHITSMN (
	SHITSMN_ID char(18) NOT NULL PRIMARY KEY,
	SHITSMN_TITLE varchar(256)NOT NULL,
	SHITSMN_NAIYO varchar(2048),
	SHITSMN_USERID char(18) NOT NULL,
	KAIGIID char(18),
	CRTSRV char(5) NOT NULL,
	CRTUSR char(18) NOT NULL,
	CRTDATE DATETIME NOT NULL,
	UPDSRV char(5) NOT NULL,
	UPDUSR char(18) NOT NULL,
	UPDDATE DATETIME NOT NULL,
	DELFLG char(1) NOT NULL
);
