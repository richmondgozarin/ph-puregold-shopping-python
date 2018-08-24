DROP TABLE shoppinglists;
DROP TABLE items;

CREATE TABLE shoppinglists (
 shopping_id integer PRIMARY KEY,
 store_name text NOT NULL,
 date_created text NOT NULL,
 date_modified text NOT NULL
);

CREATE TABLE items (
 item_id integer PRIMARY KEY,
 quantity integer NOT NULL,
 item_name text NOT NULL,
 date_created text NOT NULL,
 date_modified text NOT NULL,
 shopping_id integer,
 FOREIGN KEY (shopping_id) REFERENCES shoppinglists(shopping_id)
);