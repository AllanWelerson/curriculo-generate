
def dadosCurriculo(dados):
    curriculo = {
        "nome" : dados.form["nome"],
        "idade" : dados.form["idade"],
        "email" : dados.form["email"],
        "nacionalidade" : dados.form["nacionalidade"],
        "endereco" : dados.form["endereco"],
        "bairro" : dados.form["bairro"],
        "cidade" : dados.form["cidade"],
        "estado" : dados.form["estado"],
        "cep" : dados.form["cep"],
        "telefone1" : dados.form["telefone1"],
        "telefone2" : dados.form["telefone2"],
        "telefone3" : dados.form["telefone3"],
        "objetivo" : dados.form["objetivo"],
        "grau" : dados.form["grau"],
        "curso1_desc" : dados.form["curso1_desc"],
        "curso1_instituicao" : dados.form["curso1_instituicao"],
        "curso1_periodo" : dados.form["curso1_periodo"],
        "curso1_nivel" : dados.form["curso1_nivel"],
        "curso1_situacao" : dados.form["curso1_situacao"],
        "curso1_horario": dados.form["curso1_horario"],
        "curso2_desc" : dados.form["curso2_desc"],
        "curso2_instituicao" : dados.form["curso2_instituicao"],
        "curso2_periodo" : dados.form["curso2_periodo"],
        "curso2_nivel" : dados.form["curso2_nivel"],
        "curso2_situacao" : dados.form["curso2_situacao"],
        "curso2_horario": dados.form["curso2_horario"],
        "exp1_funcao" : dados.form["exp1_funcao"],
        "exp1_empresa" : dados.form["exp1_empresa"],
        "exp2_funcao" : dados.form["exp2_funcao"],
        "exp2_empresa" : dados.form["exp2_empresa"],
        "exp3_funcao" : dados.form["exp3_funcao"],
        "exp3_empresa" : dados.form["exp3_empresa"],
    }


    return curriculo

