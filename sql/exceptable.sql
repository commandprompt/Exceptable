

SET search_path TO 'exceptable';

INSERT INTO exceptions VALUES ('Exception', 'Base exception');
INSERT INTO exceptions VALUES ('NotFoundException', 'Could not find specified record', 'Exception');
INSERT INTO exceptions VALUES ('NotAuthorizedException', 'Connecting user Not Authorized for access to this record.', 'Exception');


CREATE OR REPLACE FUNCTION exceptable.raise (
    in_name TEXT,
    in_reason TEXT
) RETURNS VOID AS $body$

    DECLARE
        v_formatted text;

    BEGIN

        PERFORM name
           FROM exceptable.exceptions
          WHERE name = in_name;

        IF FOUND THEN

            RAISE EXCEPTION '%::%', in_name, in_reason;
        ELSE
            -- You stupid git, don't do that.
            PERFORM exceptable.not_found('Unknown exception.');
        END IF;
    END;

$body$ LANGUAGE PLPGSQL;


CREATE OR REPLACE FUNCTION exceptable.not_found (
    in_reason TEXT
) RETURNS VOID as $body$

    SELECT exceptable.raise('NotFoundException', $1);

$body$ LANGUAGE SQL;

CREATE OR REPLACE FUNCTION exceptable.not_authorized (
    in_reason TEXT
) RETURNS VOID as $body$

    SELECT exceptable.raise('NotAuthorizedException', $1)

$body$ LANGUAGE SQL;

-- CREATE OR REPLACE FUNCTION exceptable.map (
--     in_string text,
--     in_terms variadic text[]
-- ) RETURNS text AS $body$
--
--     DECLARE
--         v_pos TEXT;
--     BEGIN
--
--         FOR v_pos IN unnest(in_terms) LOOP
--
--         END LOOP;
--     END;
--
-- $body$ language plpgsql;


CREATE OR REPLACE FUNCTION exceptable.register (
    in_type text,
    in_description text
) RETURNS boolean AS $body$

    INSERT INTO exceptable.exceptions (name, description) VALUES ($1, $2) RETURNING TRUE;

$body$ language SQL;


CREATE OR REPLACE FUNCTION exceptable.register (
    in_type text,
    in_description text,
    in_parent text
) RETURNS boolean AS $body$
    INSERT INTO exceptable.exceptions (name, description, parent) VALUES ($1, $2, $3) RETURNING TRUE;
$body$ language SQL;

SET search_path TO 'public';

