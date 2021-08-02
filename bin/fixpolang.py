from pathlib import Path
from typing import List

from polib import pofile
from typer import run


def fix(files: List[Path]):
    for file in files:
        if file.exists() and file.suffix == ".po":
            po = pofile(str(file))
            if 'Language' not in po.metadata:
                po.metadata['Language'] = 'zh_CN'
            print(str(file))
            po.save()


if __name__ == '__main__':
    run(fix)
