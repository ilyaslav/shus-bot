from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
import datetime

class Base(DeclarativeBase):
    pass

class UserBase(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True)
    rename_event: Mapped[bool] = mapped_column(default=1)
    score: Mapped[int] = mapped_column(default=3)
    feed: Mapped[int] = mapped_column(default=0)
    play: Mapped[int] = mapped_column(default=0)
    speak: Mapped[int] = mapped_column(default=0)
    sleep: Mapped[int] = mapped_column(default=0)
    level: Mapped[int] = mapped_column(default=1)
    upgrades: Mapped[int] = mapped_column(default=0)


class TaskBase(Base):
    __tablename__ = "tasks"

    key_word: Mapped[str] = mapped_column(primary_key=True)
    reward: Mapped[int] = mapped_column(default=0)
    text: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    button_name: Mapped[str] = mapped_column(nullable=False)
    attachments: Mapped[str] = mapped_column(nullable=True)
    attachment_type: Mapped[str] = mapped_column(nullable=True)
    date: Mapped[datetime.date] = mapped_column(nullable=True)


class UserTaskBase(Base):
    __tablename__ = "user_tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    key_word: Mapped[str] = mapped_column(ForeignKey("tasks.key_word"))
    reward: Mapped[int] = mapped_column(default=0)
