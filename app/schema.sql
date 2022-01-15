create table account(username varchar(15) 
primary key, name varchar(20), email text);

create table tweet(id serial primary key, username varchar(15), time_posted timestamp,
description text, FOREIGN KEY(username) references account(username));

create table comment(id serial primary key, tweet_id int, content text, parent_commend_id int,
FOREIGN KEY(tweet_id) references tweet(id), FOREIGN KEY(parent_commend_id) references comment(id));
