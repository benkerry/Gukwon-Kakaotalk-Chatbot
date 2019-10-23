CREATE DATABASE  chatbot_manager_web;
USE chatbot_manager_web;

CREATE TABLE auth_code(
    auth_code TEXT NOT NULL
);

CREATE TABLE authed_user(
    user_val TEXT NOT NULL,
    signed_suggestion TEXT
);

CREATE TABLE sign_info(
    id VARCHAR(30) PRIMARY KEY NOT NULL,
    pwd TEXT NOT NULL,
    root INT NOT NULL
);

CREATE TABLE suggestion(
    idx INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    user_val TEXT NOT NULL,
    description TEXT NOT NULL,
    status INT NOT NULL,
    num_signs INT NOT NULL,
    open_datetime TEXT NOT NULL
);

CREATE TABLE suggestion_comment(
    idx INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    sug_idx INT NOT NULL,
    description TEXT NOT NULL,
    commit_datetime TEXT NOT NULL
);