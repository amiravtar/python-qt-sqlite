import logging

from sqlalchemy import (
    String,
    create_engine,
    delete,
    select,
    update,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

from setting import DB_PATH, DEBUG

logger = logging.getLogger(__name__)
# logging.getLogger("sqlalchemy").addHandler(logger.handlers[0])


engine = create_engine(f"sqlite:///{DB_PATH}", echo=DEBUG)


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String())

    # def __init__(self, name: str, last_name: str, email: str, **kw: Any):
    #     super().__init__(**kw)

    def __reper__(self):
        return "".join([str(self.id), self.name + " " + self.last_name, self.email])


def add_user(user: Users):
    with Session(engine) as session:
        session.add(user)
        session.commit()


def get_all_users() -> list[Users]:
    with Session(engine) as session:
        data = session.query(Users).all()
        return data


def delete_user(id: int):
    with Session(engine) as session:
        session.execute(delete(Users).where(Users.id == id))
        session.commit()


def update_user(user: Users):
    with Session(engine) as session:
        session.execute(
            update(Users),
            [
                {
                    "id": user.id,
                    "name": user.name,
                    "last_name": user.last_name,
                    "email": user.email,
                }
            ],
        )
        session.commit()


def select_users(name: str = "", last: str = "", email: str = "", id: int = -1):
    with Session(engine) as session:
        if id > -1:
            return session.execute(select(Users).where(Users.id == id)).all()
        else:
            args = []
            if name:
                args.append(Users.name.like(f"%{name}%"))
            if email:
                args.append(Users.email.like(f"%{email}%"))
            if last:
                args.append(Users.last_name.like(f"%{last}%"))
            return session.execute(select(Users).where(*args)).all()


Base.metadata.create_all(bind=engine)
