#DB選択
USE TEACHERSDB;

DROP TABLE S100_SHITSMN_ID;
CREATE TABLE S100_SHITSMN_ID (
	SAIBNDATE char(8) NOT NULL,
	SEQ int(9) NOT NULL,
	CRTDATE DATETIME(6) NOT NULL,
	PRIMARY KEY(SAIBNDATE,SEQ)
);