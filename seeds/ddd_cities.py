from ..database import db
from ..models.ddd_cities import DDD, Cities


def create_ddd():
    db.session.add(DDD(code='011'))
    db.session.add(DDD(code='016'))
    db.session.add(DDD(code='017'))
    db.session.add(DDD(code='018'))

    db.session.commit()


def create_cities():
    ddd_011 = DDD.query.filter_by(code='011').first()
    ddd_016 = DDD.query.filter_by(code='016').first()
    ddd_017 = DDD.query.filter_by(code='017').first()
    ddd_018 = DDD.query.filter_by(code='018').first()

    db.session.add(Cities(name='São Paulo', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Arujá', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Atibaia', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Bom Jesus dos Perdões', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Barueri', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Biritiba-Mirim', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Bragança Paulista', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Cabreúva', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Caieiras', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Campo Limpo Paulista', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Carapicuíba', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Cotia', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Diadema', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Embu das Artes', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Embu-Guaçu', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Ferraz de Vasconcelos', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Franco da Rocha', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Francisco Morato', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Guararema', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Igaratá', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Itapecerica da Serra', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Itapevi', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Itaquaquecetuba', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Itatiba', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Itu', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Jandira', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Jarinu', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Joanópolis', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Jundiaí', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Juquitiba', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Mairinque', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Mairiporã', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Mauá', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Mogi das Cruzes', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Morungaba', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Nazaré Paulista', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Osasco', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Pinhalzinho', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Piracaia', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Pirapora do Bom Jesus', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Poá', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Ribeirão Pires', ddd_code=ddd_011.code))
    db.session.add(Cities(name='São Bernardo do Campo', ddd_code=ddd_011.code))
    db.session.add(Cities(name='São Caetano do Sul', ddd_code=ddd_011.code))
    db.session.add(Cities(name='São Lourenço da Serra', ddd_code=ddd_011.code))
    db.session.add(Cities(name='São Roque', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Salesópolis', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Salto', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Santana de Parnaíba', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Santa Isabel', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Santo André', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Suzano', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Taboão da Serra', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Várgem', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Várzea Paulista', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Pedra Bela', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Tuiuti', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Cajamar', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Itupeva', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Riacho Grande', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Guarulhos', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Araçariguama', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Taquaral', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Rio Grande da Serra', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Pindorama', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Vargem Grande Paulista', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Alumínio', ddd_code=ddd_011.code))
    db.session.add(Cities(name='Américo Brasiliense', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Araraquara', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Barrinha', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Boa Esperança do Sul', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Borborema', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Cândido Rodrigues', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Cravinhos', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Cristais Paulista', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Dobrada', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Dourado', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Dumont', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Fernando Prestes', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Franca', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Guariba', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Ibaté', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Ibitinga', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Igarapava', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Itápolis', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Itirapuã', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Jaboticabal', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Matão', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Monte Alto', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Nova Europa', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Patrocínio Paulista', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Pitangueiras', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Pontal', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Pradópolis', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Restinga', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Ribeirão Bonito', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Ribeirão Preto', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Rincão', ddd_code=ddd_016.code))
    db.session.add(Cities(name='São Carlos', ddd_code=ddd_016.code))
    db.session.add(Cities(name='São José da Bela Vista', ddd_code=ddd_016.code))
    db.session.add(Cities(name='São Simão', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Serra Azul', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Serrana', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Sertãozinho', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Santa Ernestina', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Santa Lúcia', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Santa Rosa de Viterbo', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Tabatinga', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Taiaçu', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Taiuva', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Taquaritinga', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Vista Alegre do Alto', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Gavião Peixoto', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Motuca', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Trabiju', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Santa Cruz da Esperança', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Jeriquara', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Guatapará', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Luís Antônio', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Altinópolis', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Aramina', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Batatais', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Brodowski', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Buritizal', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Cajuru', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Cássia dos Coqueiros', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Guará', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Ipua', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Ituverava', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Jardinópolis', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Miguelópolis', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Morro Agudo', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Nuporanga', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Orlândia', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Pedregulho', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Ribeirão Corrente', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Rifaina', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Sales Oliveira', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Santo Antônio da Alegria', ddd_code=ddd_016.code))
    db.session.add(Cities(name='São Joaquim da Barra', ddd_code=ddd_016.code))
    db.session.add(Cities(name='Adolfo', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Altair', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Álvares Florence', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Américo de Campos', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Aparecida D.Oeste', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Ariranha', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Auriflama', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Bady Bassitt', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Bálsamo', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Barretos', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Bebedouro', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Cajobi', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Cardoso', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Catanduva', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Catiguá', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Cedral', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Colina', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Cosmorama', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Dirce Reis', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Dolcinópolis', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Elisiário', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Estrela D.Oeste', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Fernandópolis', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Floreal', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Gastão Vidigal', ddd_code=ddd_017.code))
    db.session.add(Cities(name='General Salgado', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Guaíra', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Guapiaçú', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Guaraci', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Guarani D.Oeste', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Guzolândia', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Ibirá', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Icém', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Indiaporã', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Ipiguá', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Irapuã', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Itajobi', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Jaborandi', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Jaci', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Jales', ddd_code=ddd_017.code))
    db.session.add(Cities(name='José Bonifácio', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Macaubal', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Macedônia', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Magda', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Marinópolis', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Mendonça', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Meridiano', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Mira Estrela', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Mirassol', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Mirassolândia', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Monções', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Monte Aprazível', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Monte Azul Paulista', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Neves Paulista', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Nhandeara', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Nipoã', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Nova Aliança', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Nova Granada', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Nova Luzitânia', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Novo Horizonte', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Olímpia', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Onda Verde', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Orindiúva', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Ouroeste', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Palestina', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Palmares Paulista', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Palmeira D.Oeste', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Paraíso', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Paranapuã', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Paulo de Faria', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Pedranópolis', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Pirangi', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Poloni', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Pontalinda', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Pontes Gestal', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Populina', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Potirendaba', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Riolândia', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Rubinéia', ddd_code=ddd_017.code))
    db.session.add(Cities(name='São Francisco', ddd_code=ddd_017.code))
    db.session.add(Cities(name='São João das Duas Pontes', ddd_code=ddd_017.code))
    db.session.add(Cities(name='São José do Rio Preto', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Sales', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Santana da Ponte Pensa', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Sebastianópolis do Sul', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Severínia', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Santa Adélia', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Santa Albertina', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Santa Clara D.Oeste', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Santa Fé do Sul', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Santa Rita D.Oeste', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Tabapuã', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Tanabi', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Terra Roxa', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Três Fronteiras', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Turmalina', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Uchôa', ddd_code=ddd_017.code))
    db.session.add(Cities(name='União Paulista', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Urânia', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Urupes', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Valentim Gentil', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Viradouro', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Votuporanga', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Embaúba', ddd_code=ddd_017.code))
    db.session.add(Cities(name='São João de Iracema', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Marapoama', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Vitória Brasil', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Mesópolis', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Novais', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Nova Canaã Paulista', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Aspásia', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Santa Salete', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Parisi', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Ubarana', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Nova Castilho', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Colômbia', ddd_code=ddd_017.code))
    db.session.add(Cities(name='Adamantina', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Alfredo Marcondes', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Alto Alegre', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Álvares Machado', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Andradina', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Anhumas', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Araçatuba', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Assis', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Avanhandava', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Barbosa', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Bento de Abreu', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Bilac', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Birigüi', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Bora', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Brauna', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Buritama', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Caiabú', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Caiua', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Cândido Mota', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Castilho', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Clementina', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Coroados', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Cruzália', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Dracena', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Echaporã', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Estrela do Norte', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Euclides da Cunha Paulista', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Flora Rica', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Flórida Paulista', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Florínia', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Gabriel Monteiro', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Glicério', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Guaraçaí', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Guararapes', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Iepê', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Ilha Solteira', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Indiana', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Inúbia Paulista', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Irapuru', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Itapura', ddd_code=ddd_018.code))
    db.session.add(Cities(name='João Ramalho', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Junqueirópolis', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Lavínia', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Lucélia', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Luiziânia', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Lutécia', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Marabá Paulista', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Maracaí', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Mariápolis', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Martinópolis', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Mirandópolis', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Mirante do Paranapanema', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Monte Castelo', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Murutinga do Sul', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Narandiba', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Nova Guataporanga', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Nova Independência', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Osvaldo Cruz', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Ouro Verde', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Pacaembú', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Palmital', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Panorama', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Paraguaçu Paulista', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Parapuã', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Paulicéia', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Penápolis', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Pereira Barreto', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Piacatu', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Piquerobi', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Pirapozinho', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Planalto', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Platina', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Pracinha', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Presidente Bernardes', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Presidente Epitácio', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Presidente Prudente', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Presidente Venceslau', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Quatá', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Rancharia', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Regente Feijó', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Rinópolis', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Rosana', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Rubiacea', ddd_code=ddd_018.code))
    db.session.add(Cities(name='São João do Pau D.Alho', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Sagres', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Salmourão', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Sandovalina', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Santópolis do Aguapeí', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Santa Mercedes', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Santo Anastácio', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Santo Expedito', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Sud Mennucci', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Taciba', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Tarabaí', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Teodoro Sampaio', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Tupi Paulista', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Turiuba', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Valparaíso', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Zacarias', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Pedrinhas Paulista', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Suzanápolis', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Ribeirão dos Índios', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Lourdes', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Brejo Alegre', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Tarumã', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Santo Antônio do Aracangua', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Emilianópolis', ddd_code=ddd_018.code))
    db.session.add(Cities(name='Nantes', ddd_code=ddd_018.code))

    db.session.commit()


def delete_ddd():
    db.session.execute('DELETE FROM ddd;')
    db.session.commit()


def delete_cities():
    db.session.execute('DELETE FROM cities;')
    db.session.commit()
