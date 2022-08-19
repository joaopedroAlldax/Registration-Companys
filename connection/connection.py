from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schemas.schemas import RegistrationCompany
import random


connection = create_engine("mysql://root:All_1234@localhost/registration")

Session = sessionmaker(bind=connection)
session = Session()
# Primeira forma de fazer inserção
""" session.execute("INSERT INTO registration_company (name, code, cnpj, location, certificate) VALUES ('luscas', 123, 321, 'santa maria', 3)");
session.commit()
session.close()"""

# Segunda forma de fazer inserção
""" obj = RegistrationCompany(name = 'bruscas', code= 123, cnpj = '123', location='guara', certificate='1')

session.add(obj)
session.commit()
session.close() """

"""# Terceira forma de fazer inserção
lista_adicionar = []
for i in range(10):
    cnpj = random.randint(1111, 123432)
    dict_obj = {
        'name':'bruno gay',
        'code': i,
        'cnpj': f'{cnpj}',
        'location': 'celilandia',
        'certificate' : '2'
    }

    obj = RegistrationCompany(**dict_obj)
    lista_adicionar.append(obj)

session.add_all(lista_adicionar)
session.commit()
session.close() 
"""
"""
query = session.query(RegistrationCompany).all()

for i in query:
    print(f'{i.name} - {i.code} - {i.cnpj}')

# select para ver conteudo da tabela
query = session.execute('SELECT * FROM registration_company')
query = [dict(a) for a in query]

print(query)
# update na table, neste caso, update da coluna name, no registro 10
query = session.query(RegistrationCompany).where(RegistrationCompany.id_registratnameionamn == 10)
query.name = 'namasdasde'
session.commit()
session.refresh(query)

# como se fosse a função __repr__
query = session.query(RegistrationCompany).all()

for i in query:
    print(f'{i.name} - {i.code} - {i.cnpj}')

"""