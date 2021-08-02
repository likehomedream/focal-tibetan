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

## Translation Data

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

We simply import the translation data(gettext PO format) to PostgreSQL database with `bin/msg2sql.py`.

```shell
# Import Chinese data
 DATABASE_URI='postgresql+pg8000://focal-tibetan:focal-tibetan@127.0.0.1:5432/focal-tibetan' python bin/msg2sql.py locale-langpack/zh_CN/LC_MESSAGES/*
# Import Tibetan(China) data
 DATABASE_URI='postgresql+pg8000://focal-tibetan:focal-tibetan@127.0.0.1:5432/focal-tibetan' python bin/msg2sql.py xenial-tibetan/locale-langpack/bo_CN/LC_MESSAGES/*
```

And another script named `bin/ts2sql.py` is used to import the translation data(Qt Translation Format) to PostgreSQL database.

```shell
DATABASE_URI='postgresql+pg8000://focal-tibetan:focal-tibetan@127.0.0.1:5432/focal-tibetan' python bin/ts2sql.py $(find ./ -type f -name "*zh_CN.ts")
```

## File Operations

This project current support some operations of the PO and TS files.

### PO/POT

It is a script `bin/msgfile.py` to support compile, decompile and generate template(POT) from a PO file.

```shell
# compile .po to .mo (in-place)
python bin/msgfile.py compress locale-langpack/zh_CN/LC_MESSAGES/*.po
# decompile .mo to .po (in-place)
python bin/msgfile.py compress locale-langpack/zh_CN/LC_MESSAGES/*.mo
# create .pot from .po to specified directory
python bin/msgfile.py generate-template locale-langpack/zh_CN/LC_MESSAGES/*.po locale-langpack/pot/
```

And another script named `bin/tsfile.py` provides support of compile, decompile TS or QM file.  And support generate an empty bo_CN TS file too.  These operations are all in-place.

```shell
# compile .ts to .qm
python bin/tsfile.py compress kylin-calculator/translations/kylin-calculator_zh_CN.ts # to kylin-calculator/translations/kylin-calculator_zh_CN.qm
# decompile .qm to .ts
python bin/tsfile.py compress kylin-calculator/translations/kylin-calculator_zh_CN.qm # to kylin-calculator/translations/kylin-calculator_zh_CN.ts
# generate an empty bo_CN translation file.
python bin/tsfile.py generate-bo-cn-empty-template kylin-calculator/translations/kylin-calculator_zh_CN.ts # to kylin-calculator/translations/kylin-calculator_bo_CN.ts
```
