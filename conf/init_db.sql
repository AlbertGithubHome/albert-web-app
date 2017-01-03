-- init_db.sql

drop database if exists web_app;

create database web_app;

use web_app;

grant select, insert, update, delete on web_app.* to 'albertwebapp'@'localhost' identified by '123456';

create table users (
    `id` varchar(64) not null,
    `email` varchar(64) not null,
    `password` varchar(64) not null,
    `admin` bool not null,
    `name` varchar(64) not null,
    `image` varchar(640) not null,
    `created_at` real not null,
    unique key `idx_email` (`email`),
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table blogs (
    `id` varchar(64) not null,
    `user_id` varchar(64) not null,
    `user_name` varchar(64) not null,
    `user_image` varchar(640) not null,
    `name` varchar(64) not null,
    `summary` varchar(256) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table comments (
    `id` varchar(64) not null,
    `blog_id` varchar(64) not null,
    `user_id` varchar(64) not null,
    `user_name` varchar(64) not null,
    `user_image` varchar(640) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;
