	
CREATE TABLE shoppinglists (
 id integer PRIMARY KEY,
 store_name text NOT NULL,
 date_created text NOT NULL,
 date_modified text NOT NULL
);

CREATE TABLE items (
 id integer PRIMARY KEY,
 quantity integer NOT NULL,
 item_name text NOT NULL,
 date_created text NOT NULL,
 date_modified text NOT NULL
);