# coding: utf-8
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class RegistrationCompany(Base):
    __tablename__ = 'registration_company'

    id_registration = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    code = Column(Integer, nullable=False)
    cnpj = Column(Integer, nullable=False)
    location = Column(String(45), nullable=False)
    certificate = Column(String(45), nullable=False)


if __name__ == "__main__":

    connection = create_engine("mysql://root:All_1234@localhost/registration")
    metadata.drop_all(bind=connection)
    metadata.create_all(bind=connection)

