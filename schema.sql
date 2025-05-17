CREATE TABLE IF NOT EXISTS prefix (
    user_id BIGINT PRIMARY KEY,
    prefixes TEXT
);

CREATE TABLE IF NOT EXISTS general_data (
    create_epoch DATE,
    ping INT,
    users INT,
    guilds INT,
    channels INT,
    disnake_version INT
);

CREATE TABLE IF NOT EXISTS overall_score (
    score INT
);

CREATE TABLE IF NOT EXISTS lang_guild (
    id INTEGER PRIMARY KEY,
    guildid TEXT,
    language TEXT
);

CREATE TABLE IF NOT EXISTS level (
        id INTEGER PRIMARY KEY,
        guildid TEXT,
        username TEXT,
        userid TEXT,
        level INTEGER,
        exp INTEGER
);