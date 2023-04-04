create extension if not exists "uuid-ossp";

create table if not exists topic(
    id uuid primary key not null default uuid_generate_v4(),
    name text
);
insert into topic(name) values ('test');