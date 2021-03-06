#DB選択
USE TEACHERSDB;

DROP TABLE T110_HASHTAG;
CREATE TABLE T110_HASHTAG (
	#HASHTAG_ID char(18) NOT NULL,
	#HASHTAG_NAIYO varchar(150) ,
	HASHTAG varchar(150) NOT NULL,
    COUNTER integer default 1,
    CRTSRV char(5) NOT NULL,
	CRTUSR char(18) NOT NULL,
	CRTDATE DATETIME(6) NOT NULL,
	UPDSRV char(5) NOT NULL,
	UPDUSR char(18) NOT NULL,
	UPDDATE DATETIME(6) NOT NULL,
	DELFLG char(1) NOT NULL,
	PRIMARY KEY(HASHTAG)
);
