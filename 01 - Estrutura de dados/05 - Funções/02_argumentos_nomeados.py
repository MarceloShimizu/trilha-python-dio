def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# insert the values using arguments order.
salvar_carro("Fiat", "Palio", 1999, "ABC-1234") 

# insert the values identifying the arguments
salvar_carro(modelo="Palio", marca="Fiat", ano=1999, placa="ABC-1234")

# passa um dicionario que eh "convertido" mais ou menos nisso: (modelo="Palio", marca="Fiat", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
