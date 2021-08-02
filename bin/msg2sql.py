from enum import Enum, auto
from pathlib import Path
from typing import List

from polib import pofile, POFile, POEntry
from typer import Typer

from msg.database import engine, session, Base
from msg.models import MSG


manage = Typer()
db = session()


class MSGType(Enum):
    en_US = auto()
    bo_CN = auto()
    zh_CN = auto()
    invalid = auto()


def db_import_msg(msg_id: str = "", msg_str_bo_cn: str = "", msg_str_zh_cn: str = ""):
    msg = MSG(
        msg_id=msg_id,
        msg_str_bo_CN=msg_str_bo_cn,
        msg_str_zh_CN=msg_str_zh_cn,
    )
    db.add(msg)


def db_import_entry(entry: POEntry, entry_type: MSGType):
    if entry.msgid_plural:
        if entry_type is MSGType.zh_CN:
            db_import_msg(msg_id=entry.msgid, msg_str_zh_cn=entry.msgstr_plural[0])
        elif entry_type is MSGType.bo_CN:
            db_import_msg(msg_id=entry.msgid, msg_str_bo_cn=entry.msgstr_plural[0])
    else:
        if entry_type is MSGType.zh_CN:
            db_import_msg(msg_id=entry.msgid, msg_str_zh_cn=entry.msgstr)
        elif entry_type is MSGType.bo_CN:
            db_import_msg(msg_id=entry.msgid, msg_str_bo_cn=entry.msgstr)


@manage.command()
def import_po(files: List[Path]):
    for file in files:
        if file.exists() and file.suffix == ".po":
            po = pofile(str(file))
            if po.metadata['Language'] == 'zh_CN':
                po_type = MSGType.zh_CN
            elif po.metadata['Language'] == 'bo_CN':
                po_type = MSGType.zh_CN
            else:
                po_type = MSGType.invalid
            for entry in po:
                db_import_entry(entry, po_type)
            db.commit()
        else:
            pass


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    manage()
