#DB選択
USE TEACHERSDB;

DROP TABLE T102_KAIGIKBUJKN;
CREATE TABLE T102_KAIGIKBUJKN (
	SHITSMN_ID char(18) NOT NULL,
	SEQ  tinyint NOT NULL,
	KAISHNCHJ DATETIME(0) ,
	SHURYNCHJ DATETIME(0) ,
	KAIGIJIKN smallint ,
	CRTSRV char(5) NOT NULL,
	CRTUSR varchar(30) NOT NULL,
	CRTDATE DATETIME(6) NOT NULL,
	UPDSRV char(5) NOT NULL,
	UPDUSR varchar(30) NOT NULL,
	UPDDATE DATETIME(6) NOT NULL,
	DELFLG char(1) NOT NULL,
	PRIMARY KEY(SHITSMN_ID, SEQ)
);
