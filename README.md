# Tibetan(China) I18N of Ubuntu Focal Fossa

[WIP] This project inherits the [Tibetan(China) I18N Translation Data of Ubuntu Xenial Xerus] and strives to create a Tibetan(China) language pack for Ubuntu Focal Fossa.

[Tibetan(China) I18N Translation Data of Ubuntu Xenial Xerus]: https://github.com/ubuntuylin-weblate/xenial-tibetan.git

## Getting Started

Checkout this repository and update the submodules.

```shell
git clone https://github.com/ubuntukylin-weblate/focal-tibetan.git
git submodule init
git submodule update
```

## Data

We use PostgreSQL to manage translation data that from the scratch, and though Weblate to promote the translation  work.

### Create the Initial Database

We use `docker` to quickly create an environment includes PostgreSQL.

```shell
docker-compose -f docker-compose.yml up -d
```

### Import Chinese and Tibetan(China) Translations

We have defined a global table to store all translations.

|    Column     |       Type        | Collation | Nullable |             Default             | Storage  | Stats target | Description |
|---------------|-------------------|-----------|----------|---------------------------------|----------|--------------|-------------|
| id            | integer           |           | not null | nextval('msg_id_seq'::regclass) | plain    |              |             |
| msg_id        | character varying |           |          |                                 | extended |              |             |
| msg_str_bo_CN | character varying |           |          |                                 | extended |              |             |
| msg_str_zh_CN | character varying |           |          |                                 | extended |              |             |

`msg_id` and `msg_str_bo_CN` is a Tibetan tuple of msg constructed by `msgid` and `msgstr`(or `ms gstr_plural[0]`).

Similarly, another Chinese tuple is constructed by `msg_id` and `msg_str_zh_CN`.

We simply import the translation data to PostgreSQL database with `bin/msg2sql.py`.

```shell
# Import Chinese data
 DATABASE_URI='postgresql+pg8000://focal-tibetan:focal-tibetan@127.0.0.1:5432/focal-tibetan' python bin/msg2sql.py locale-langpack/zh_CN/LC_MESSAGES/*
# Import Tibetan(China) data
 DATABASE_URI='postgresql+pg8000://focal-tibetan:focal-tibetan@127.0.0.1:5432/focal-tibetan' python bin/msg2sql.py xenial-tibetan/locale-langpack/bo_CN/LC_MESSAGES/*
```
