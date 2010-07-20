/* Exceptable
   A library for handling exceptions in PL/PGSQL, and transmitting useful
   exception data to upstream consumers.
*/

CREATE SCHEMA exceptable;

SET search_path TO 'exceptable';

CREATE TABLE exceptions (
    name text primary key,
    description text not null,
    parent text references exceptions(name)
);