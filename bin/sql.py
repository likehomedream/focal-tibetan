import os
import sys

sys.path.append(os.path.join(sys.path[0], os.pardir))

from typer import Typer

from msg.database import engine, session, Base
from msg.models import MSG


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
