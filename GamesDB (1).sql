-- Configurações iniciais (opcional, mas boas práticas)
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

-- ======================
-- SEQUENCES
-- ======================
CREATE SEQUENCE public.categoria_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE public.editora_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE public.jogo_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE public.usuario_id_seq START WITH 1 INCREMENT BY 1;

-- ======================
-- TABELAS
-- ======================

-- Categoria
CREATE TABLE public.categoria (
    id integer NOT NULL DEFAULT nextval('categoria_id_seq'),
    nome character varying(100) NOT NULL,
    PRIMARY KEY (id)
);

-- Editora
CREATE TABLE public.editora (
    id integer NOT NULL DEFAULT nextval('editora_id_seq'),
    nome character varying(100) NOT NULL,
    PRIMARY KEY (id)
);

-- Usuario
CREATE TABLE public.usuario (
    id integer NOT NULL DEFAULT nextval('usuario_id_seq'),
    senha character varying(100) NOT NULL,
    nome character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    PRIMARY KEY (id)
);

-- Jogo
CREATE TABLE public.jogo (
    id integer NOT NULL DEFAULT nextval('jogo_id_seq'),
    id_editora integer NOT NULL,
    id_categoria integer NOT NULL,
    descricao text,
    nome character varying(100) NOT NULL,
    idioma character varying(50),
    duracao integer,
    tipo character varying(50),
    min_jogadores integer,
    max_jogadores integer,
    PRIMARY KEY (id),
    FOREIGN KEY (id_editora) REFERENCES public.editora(id),
    FOREIGN KEY (id_categoria) REFERENCES public.categoria(id)
);

-- Jogo_Usuario
CREATE TABLE public.jogo_usuario (
    usuario_id integer NOT NULL,
    jogo_id integer NOT NULL,
    lugar text,
    status character varying(50),
    data_aquisicao date,
    PRIMARY KEY (usuario_id, jogo_id),
    FOREIGN KEY (usuario_id) REFERENCES public.usuario(id),
    FOREIGN KEY (jogo_id) REFERENCES public.jogo(id)
);
