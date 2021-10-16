#DB選択
USE TEACHERSDB;

DROP TABLE T110_HASHTAG;
CREATE TABLE T110_HASHTAG (
	#HASHTAG_ID char(18) NOT NULL,
	#HASHTAG_NAIYO varchar(150) ,
	HASHTAG varchar(150) NOT NULL,
    CRTSRV char(5) NOT NULL,
	CRTUSR varchar(30) NOT NULL,
	CRTDATE DATETIME(6) NOT NULL,
	UPDSRV char(5) NOT NULL,
	UPDUSR varchar(30) NOT NULL,
	UPDDATE DATETIME(6) NOT NULL,
	DELFLG char(1) NOT NULL,
	PRIMARY KEY(HASHTAG)
);
