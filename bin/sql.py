import os
import sys

from typer import Typer

sys.path.append(os.path.join(sys.path[0], os.pardir))

from msg.database import engine, session, Base

manage = Typer()
db = session()


@manage.command()
def init():
    Base.metadata.create_all(bind=engine)


@manage.command()
def drop():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    manage()
