from pathlib import Path
from typing import List

from polib import mofile, pofile
from typer import Typer


msg = Typer()


@msg.command()
def compress(files: List[Path]):
    for file in files:
        if file.exists() and file.suffix == ".po":
            mo_file = file.with_suffix(".mo")
            po = pofile(str(file))
            po.save_as_mofile(str(mo_file))
        else:
            print(str(file) + "is not exists or invalid type.")


@msg.command()
def decompress(files: List[Path]):
    for file in files:
        if file.exists() and file.suffix == ".mo":
            po_file = file.with_suffix(".po")
            mo = mofile(str(file))
            mo.save_as_pofile(str(po_file))
        else:
            print(str(file) + "is not exists or invalid type.")


if __name__ == '__main__':
    msg()
