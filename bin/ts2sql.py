import os
import sys
from enum import Enum, auto
from pathlib import Path
from typing import List, NamedTuple
from lxml.etree import parse

from typer import run

sys.path.append(os.path.join(sys.path[0], os.pardir))

from msg.database import session
from msg.models import MSG


db = session()


class TSLangType(Enum):
    bo_CN = auto()
    en_US = auto()
    zh_CN = auto()
    invalid = auto()


class TSMessage(NamedTuple):
    id: str
    str: str


def db_import_msg(msg_id: str = "", msg_str_bo_cn: str = "", msg_str_zh_cn: str = ""):
    result = db.query(MSG).filter(MSG.msg_id == msg_id).first()
    if result:
        if msg_str_zh_cn != "" and bool(result.msg_str_zh_CN) is False:
            result.msg_str_zh_CN = msg_str_zh_cn
        if msg_str_bo_cn != "" and bool(result.msg_str_bo_CN) is False:
            result.msg_str_bo_CN = msg_str_bo_cn
    else:
        msg = MSG(
            msg_id=msg_id,
            msg_str_bo_CN=msg_str_bo_cn,
            msg_str_zh_CN=msg_str_zh_cn,
        )
        db.add(msg)


def db_import_message(message: TSMessage, lang_type: TSLangType):
    if lang_type is TSLangType.zh_CN:
        db_import_msg(msg_id=message.id, msg_str_zh_cn=message.str)
    elif lang_type is TSLangType.bo_CN:
        db_import_msg(msg_id=message.id, msg_str_bo_cn=message.str)


def import_ts(files: List[Path]):
    for file in files:
        if file.exists() and file.suffix == ".ts":
            if "zh_CN" in str(file):
                lang_type = TSLangType.zh_CN
            elif "bo_CN" in str(file):
                lang_type = TSLangType.bo_CN
            else:
                lang_type = TSLangType.invalid
            tree = parse(str(file))
            root = tree.getroot()
            for context in root:
                for message in context:
                    if message.find('source') is not None and message.find('translation') is not None:
                        m = TSMessage(id=message.find('source').text, str=str(message.find('translation').text or ''))
                        db_import_message(m, lang_type)
            db.commit()
        else:
            pass


if __name__ == '__main__':
    run(import_ts)
