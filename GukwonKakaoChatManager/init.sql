CREATE DATABASE  chatbot_manager_web;
USE chatbot_manage;

CREATE TABLE auth_code(
    auth_code TEXT NOT NULL
);

CREATE TABLE authed_users(
    user_num INT NOT NULL
);

CREATE TABLE sign_info(
    id TEXT NOT NULL,
    pwd TEXT NOT NULL
);

CREATE TABLE bamboo(
    user_num INT NOT NULL,
    bamboo_description TEXT NOT NULL
);

CREATE TABLE suggestion(
    user_num INT NOT NULL,
    suggestion_description TEXT NOT NULL    
);