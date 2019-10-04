CREATE DATABASE  chatbot_manager_web;
USE chatbot_manager_web;

CREATE TABLE auth_code(
    auth_code TEXT NOT NULL
);

CREATE TABLE authed_user(
    user_num INT NOT NULL
);

CREATE TABLE sign_info(
    id TEXT NOT NULL,
    pwd TEXT NOT NULL
);

CREATE TABLE suggestion(
    user_num INT NOT NULL,
    description TEXT NOT NULL,
    authed INT NOT NULL    
);