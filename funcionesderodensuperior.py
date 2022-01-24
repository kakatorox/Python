def saludo(idioma):
    def saludo_es():
        print("hola")
    def saludo_en():
        print ("hi")
    idioma_func={"es:"saludo_es,"en:"saludo_en}
    return idioma_func[idioma]
saludar=saludo("en")
saludar()
