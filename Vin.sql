PGDMP     3    !                z            Vin    14.1    14.1     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    40511    Vin    DATABASE     i   CREATE DATABASE "Vin" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1258';
    DROP DATABASE "Vin";
                postgres    false            ?            1259    40520    calls    TABLE     ?   CREATE TABLE public.calls (
    user_name character varying NOT NULL,
    call_duration integer NOT NULL,
    call_count integer NOT NULL,
    block_count integer NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL
);
    DROP TABLE public.calls;
       public         heap    postgres    false            ?          0    40520    calls 
   TABLE DATA           ^   COPY public.calls (user_name, call_duration, call_count, block_count, created_at) FROM stdin;
    public          postgres    false    209   ?       ]           2606    40527    calls calls_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.calls
    ADD CONSTRAINT calls_pkey PRIMARY KEY (user_name);
 :   ALTER TABLE ONLY public.calls DROP CONSTRAINT calls_pkey;
       public            postgres    false    209            ?   K   x??K??4?@##]3]C##c+SC+#s=sCcK3ms.?̼N0DRhhiebfeh?gbhanjR???? ?w:     