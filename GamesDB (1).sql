--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

-- Started on 2025-07-01 21:21:39

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- TOC entry 220 (class 1259 OID 16396)
-- Name: categoria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categoria (
    id integer NOT NULL,
    nome character varying(100) NOT NULL
);


ALTER TABLE public.categoria OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16395)
-- Name: categoria_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categoria_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.categoria_id_seq OWNER TO postgres;

--
-- TOC entry 4891 (class 0 OID 0)
-- Dependencies: 219
-- Name: categoria_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categoria_id_seq OWNED BY public.categoria.id;


--
-- TOC entry 218 (class 1259 OID 16389)
-- Name: editora; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.editora (
    id integer NOT NULL,
    nome character varying(100) NOT NULL
);


ALTER TABLE public.editora OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16388)
-- Name: editora_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.editora_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.editora_id_seq OWNER TO postgres;

--
-- TOC entry 4892 (class 0 OID 0)
-- Dependencies: 217
-- Name: editora_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.editora_id_seq OWNED BY public.editora.id;


--
-- TOC entry 224 (class 1259 OID 16410)
-- Name: jogo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jogo (
    id integer NOT NULL,
    id_editora integer NOT NULL,
    id_categoria integer NOT NULL,
    descricao text,
    nome character varying(100) NOT NULL,
    idioma character varying(50),
    duracao integer,
    tipo character varying(50),
    min_jogadores integer,
    max_jogadores integer
);


ALTER TABLE public.jogo OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16409)
-- Name: jogo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.jogo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.jogo_id_seq OWNER TO postgres;

--
-- TOC entry 4893 (class 0 OID 0)
-- Dependencies: 223
-- Name: jogo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.jogo_id_seq OWNED BY public.jogo.id;


--
-- TOC entry 225 (class 1259 OID 16428)
-- Name: jogo_usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jogo_usuario (
    usuario_id integer NOT NULL,
    jogo_id integer NOT NULL,
    lugar text,
    status character varying(50),
    data_aquisicao date
);


ALTER TABLE public.jogo_usuario OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16403)
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario (
    id integer NOT NULL,
    senha character varying(100) NOT NULL,
    nome character varying(100) NOT NULL,
    email character varying(100) NOT NULL
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16402)
-- Name: usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.usuario_id_seq OWNER TO postgres;

--
-- TOC entry 4894 (class 0 OID 0)
-- Dependencies: 221
-- Name: usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuario_id_seq OWNED BY public.usuario.id;


--
-- TOC entry 4715 (class 2604 OID 16399)
-- Name: categoria id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria ALTER COLUMN id SET DEFAULT nextval('public.categoria_id_seq'::regclass);


--
-- TOC entry 4714 (class 2604 OID 16392)
-- Name: editora id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.editora ALTER COLUMN id SET DEFAULT nextval('public.editora_id_seq'::regclass);


--
-- TOC entry 4717 (class 2604 OID 16413)
-- Name: jogo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogo ALTER COLUMN id SET DEFAULT nextval('public.jogo_id_seq'::regclass);


--
-- TOC entry 4716 (class 2604 OID 16406)
-- Name: usuario id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario ALTER COLUMN id SET DEFAULT nextval('public.usuario_id_seq'::regclass);


--
-- TOC entry 4880 (class 0 OID 16396)
-- Dependencies: 220
-- Data for Name: categoria; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categoria (id, nome) FROM stdin;
\.


--
-- TOC entry 4878 (class 0 OID 16389)
-- Dependencies: 218
-- Data for Name: editora; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.editora (id, nome) FROM stdin;
\.


--
-- TOC entry 4884 (class 0 OID 16410)
-- Dependencies: 224
-- Data for Name: jogo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jogo (id, id_editora, id_categoria, descricao, nome, idioma, duracao, tipo, min_jogadores, max_jogadores) FROM stdin;
\.


--
-- TOC entry 4885 (class 0 OID 16428)
-- Dependencies: 225
-- Data for Name: jogo_usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jogo_usuario (usuario_id, jogo_id, lugar, status, data_aquisicao) FROM stdin;
\.


--
-- TOC entry 4882 (class 0 OID 16403)
-- Dependencies: 222
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuario (id, senha, nome, email) FROM stdin;
\.


--
-- TOC entry 4895 (class 0 OID 0)
-- Dependencies: 219
-- Name: categoria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categoria_id_seq', 1, false);


--
-- TOC entry 4896 (class 0 OID 0)
-- Dependencies: 217
-- Name: editora_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.editora_id_seq', 1, false);


--
-- TOC entry 4897 (class 0 OID 0)
-- Dependencies: 223
-- Name: jogo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.jogo_id_seq', 1, false);


--
-- TOC entry 4898 (class 0 OID 0)
-- Dependencies: 221
-- Name: usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuario_id_seq', 1, false);


--
-- TOC entry 4721 (class 2606 OID 16401)
-- Name: categoria categoria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria
    ADD CONSTRAINT categoria_pkey PRIMARY KEY (id);


--
-- TOC entry 4719 (class 2606 OID 16394)
-- Name: editora editora_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.editora
    ADD CONSTRAINT editora_pkey PRIMARY KEY (id);


--
-- TOC entry 4725 (class 2606 OID 16417)
-- Name: jogo jogo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogo
    ADD CONSTRAINT jogo_pkey PRIMARY KEY (id);


--
-- TOC entry 4727 (class 2606 OID 16434)
-- Name: jogo_usuario jogo_usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogo_usuario
    ADD CONSTRAINT jogo_usuario_pkey PRIMARY KEY (usuario_id, jogo_id);


--
-- TOC entry 4723 (class 2606 OID 16408)
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);


--
-- TOC entry 4728 (class 2606 OID 16423)
-- Name: jogo jogo_id_categoria_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogo
    ADD CONSTRAINT jogo_id_categoria_fkey FOREIGN KEY (id_categoria) REFERENCES public.categoria(id);


--
-- TOC entry 4729 (class 2606 OID 16418)
-- Name: jogo jogo_id_editora_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogo
    ADD CONSTRAINT jogo_id_editora_fkey FOREIGN KEY (id_editora) REFERENCES public.editora(id);


--
-- TOC entry 4730 (class 2606 OID 16440)
-- Name: jogo_usuario jogo_usuario_jogo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogo_usuario
    ADD CONSTRAINT jogo_usuario_jogo_id_fkey FOREIGN KEY (jogo_id) REFERENCES public.jogo(id);


--
-- TOC entry 4731 (class 2606 OID 16435)
-- Name: jogo_usuario jogo_usuario_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jogo_usuario
    ADD CONSTRAINT jogo_usuario_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuario(id);


-- Completed on 2025-07-01 21:21:40

--
-- PostgreSQL database dump complete
--

