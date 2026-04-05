
CREATE TABLE "anime"(
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(50) NOT NULL,
	"time_stop" TIME,
	"number_episode" INT
);

CREATE TABLE "users" (
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(50) NOT NULL UNIQUE,
	"email" VARCHAR(100) NOT NULL UNIQUE,
	"password" VARCHAR(255) NOT NULL,
	"avatar" VARCHAR(100), 
	"id_anime" INT,

	FOREIGN KEY ("id_anime") REFERENCES "anime" ("id")
);

CREATE TABLE "user_anime"(
	"user_id" INT,
	"anime_id" INT
);

