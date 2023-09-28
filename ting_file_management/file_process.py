import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in list(instance.data):
        if i["nome_do_arquivo"] == path_file:
            return None
    fileTxt = txt_importer(path_file)

    dataObj = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(fileTxt),
        "linhas_do_arquivo": fileTxt
    }

    instance.enqueue(dataObj)
    sys.stdout.write(str(dataObj))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
