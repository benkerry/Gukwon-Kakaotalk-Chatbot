CREATE DATABASE  chatbot_manager_web;
USE chatbot_manage;

CREATE TABLE auth_code(
    TEXT auth_code
);

CREATE TABLE user(
    TEXT id NOT NULL,
    TEXT pwd NOT NULL
);

CREATE TABLE bamboo(
    TEXT code NOT NULL,
    TEXT bamboo_description NOT NULL
);

CREATE TABLE suggestion(
    TEXT code NOT NULL,
    TEXT suggestion_description NOT NULL    
);