def exists_word(word, instance):
    result = []

    for i in instance.data:
        ocorrencias = []

        for index, line in enumerate(i["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                ocorrencias.append({"linha": index})
    if ocorrencias:
        result.append({
            "palavra": word,
            "arquivo": i["nome_do_arquivo"],
            "ocorrencias": ocorrencias
        })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
