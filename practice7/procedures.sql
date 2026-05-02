CREATE OR REPLACE PROCEDURE upsert_contact(p_username VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO contacts(username, phone)
    VALUES (TRIM(p_username), TRIM(p_phone))
    ON CONFLICT (username) DO UPDATE SET phone = EXCLUDED.phone;
END;
$$;

CREATE OR REPLACE PROCEDURE update_contact_name(p_old_username VARCHAR, p_new_username VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    UPDATE contacts
    SET username = TRIM(p_new_username)
    WHERE username = p_old_username;
END;
$$;

CREATE OR REPLACE PROCEDURE update_contact_phone(p_username VARCHAR, p_new_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    UPDATE contacts
    SET phone = TRIM(p_new_phone)
    WHERE username = p_username;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE username = p_value OR phone = p_value;
END;
$$;

CREATE OR REPLACE FUNCTION search_contacts(p_username TEXT DEFAULT '', p_phone_prefix TEXT DEFAULT '')
RETURNS TABLE(id INTEGER, username VARCHAR, phone VARCHAR, created_at TIMESTAMP) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.username, c.phone, c.created_at
    FROM contacts c
    WHERE (COALESCE(p_username, '') = '' OR c.username ILIKE '%' || p_username || '%')
      AND (COALESCE(p_phone_prefix, '') = '' OR c.phone LIKE p_phone_prefix || '%')
    ORDER BY c.username;
END;
$$ LANGUAGE plpgsql;
