#DB選択
USE TEACHERSDB;

#T010
DROP TABLE T100_SHITSMN;
CREATE TABLE T100_SHITSMN (
	SHITSMN_ID char(18) NOT NULL PRIMARY KEY,
	SHITSMN_TITLE varchar(256)NOT NULL,
	SHITSMN_NAIYO varchar(2048),
	SHITSMN_USERID varchar(30) NOT NULL,
	KAIGIID char(18),
	CRTSRV char(5) NOT NULL,
	CRTUSR varchar(30) NOT NULL,
	CRTDATE DATETIME NOT NULL,
	UPDSRV char(5) NOT NULL,
	UPDUSR varchar(30) NOT NULL,
	UPDDATE DATETIME NOT NULL,
	DELFLG char(1) NOT NULL
);
