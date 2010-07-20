\i base.sql

ALTER TABLE except.exceptions ADD COLUMN type text not null;

INSERT INTO except.exceptions (name, description, type) VALUES (
    'NotNullException',
    'Value is not permitted to be NULL.', 
    'null_value_not_allowed');
    

CREATE OR REPLACE FUNCTION raise (
    in_name TEXT,
    in_reason TEXT
) RETURNS VOID AS $body$
    
    DECLARE
        v_type TEXT
    
    BEGIN
         SELECT type
           INTO v_type
           FROM except.exceptions
          WHERE name = in_name;
        IF FOUND THEN
            
            RAISE EXCEPTION '%::%', in_name, in_reason;
        ELSE
            -- You stupid git, don't do that.
            except.not_found('Unknown exception.');
        END IF;
    END;

$body$ LANGUAGE PLPGSQL ;