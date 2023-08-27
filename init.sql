--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.4 (Debian 15.4-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: bot_user; Type: TABLE; Schema: public; Owner: pyrogram_bot_user
--

CREATE TABLE public.bot_user (
    user_id integer NOT NULL,
    login_date date
);


ALTER TABLE public.bot_user OWNER TO pyrogram_bot_user;

--
-- Name: bot_user bot_user_pkey; Type: CONSTRAINT; Schema: public; Owner: pyrogram_bot_user
--

ALTER TABLE ONLY public.bot_user
    ADD CONSTRAINT bot_user_pkey PRIMARY KEY (user_id);


--
-- PostgreSQL database dump complete
--

