from pathlib import Path
from shlex import split
from subprocess import run
from typing import List
from lxml.etree import parse

from typer import Typer


ts = Typer()


def execute(command: str):
    args = split(command)
    run(args)


@ts.command()
def compress(files: List[Path]):
    for file in files:
        if file.exists() and file.suffix == ".ts":
            execute("lconvert " + str(file) + " -o " + str(file.with_suffix(".qm")))
        else:
            pass


@ts.command()
def decompress(files: List[Path]):
    for file in files:
        if file.exists() and file.suffix == ".qm":
            execute("lconvert " + str(file) + " -o " + str(file.with_suffix(".ts")))
        else:
            pass


@ts.command()
def generate_bo_cn_empty_template(files: List[Path]):
    for file in files:
        if file.exists() and file.suffix == ".ts":
            tree = parse(str(file))
            root = tree.getroot()
            for context in root:
                for message in context:
                    if message.find('translation') is not None:
                        translation = message.find('translation')
                        translation.text = ""
                        translation.set('type', 'unfinished')
            root.set('language', 'bo_CN')
            new_ts = Path(str(file).replace("zh_CN", "bo_CN"))
            tree.write(str(new_ts), encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    ts()
