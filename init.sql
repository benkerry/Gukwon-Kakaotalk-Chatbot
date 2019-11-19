CREATE DATABASE chatbot DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE chatbot;

CREATE TABLE auth_code(
    auth_code TEXT NOT NULL,
    staged INT NOT NULL
);

CREATE TABLE manager_auth_code(
    auth_code TEXT NOT NULL,
    root INT NOT NULL,
    staged INT NOT NULL
);

CREATE TABLE authed_user(
    user_val TEXT NOT NULL,
    signed_suggestion TEXT
);

CREATE TABLE user_info(
    user_val TEXT NOT NULL,
    _class VARCHAR(5) NOT NULL,
    _name TEXT NOT NULL
);

CREATE TABLE sign_info(
    id VARCHAR(30) PRIMARY KEY NOT NULL,
    pwd TEXT NOT NULL,
    root INT NOT NULL,
    nickname TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE suggestion(
    idx INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    user_val TEXT NOT NULL,
    description TEXT NOT NULL,
    status INT NOT NULL,
    num_signs INT NOT NULL,
    open_datetime TEXT NOT NULL,
    handler_nickname TEXT,
    deleted_datetime TEXT
);

CREATE TABLE suggestion_comment(
    idx INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    sug_idx INT NOT NULL,
    description TEXT NOT NULL,
    nickname TEXT NOT NULL,
    commit_datetime TEXT NOT NULL
);