import os
import pandas as pd

def listar_ficheiros(pasta):
    """Lista todos os ficheiros numa pasta."""
    return os.listdir(pasta)

def verificar_ficheiros_unicos(pasta1, pasta2):
    """Verifica quais ficheiros estão em pasta1 mas não estão em pasta2."""
    ficheiros_pasta1 = listar_ficheiros(pasta1)
    ficheiros_pasta2 = listar_ficheiros(pasta2)
    
    ficheiros_unicos = [f for f in ficheiros_pasta1 if f not in ficheiros_pasta2]
    
    ficheiros_repetidos = [f for f in ficheiros_unicos if ficheiros_unicos.count(f) > 1]
    ficheiros_unicos_set = set(ficheiros_unicos)
    
    return ficheiros_unicos_set, ficheiros_repetidos

def exportar_para_csv(ficheiros_unicos, ficheiros_repetidos, caminho_csv):
    """Exporta uma lista de ficheiros para um ficheiro CSV, indicando duplicados."""
    df = pd.DataFrame(list(ficheiros_unicos), columns=['Ficheiros Unicos'])
    df['Duplicado'] = df['Ficheiros Unicos'].apply(lambda x: 'Sim' if x in ficheiros_repetidos else 'Não')
    df.to_csv(caminho_csv, index=False)
    print(f"Ficheiros exportados para {caminho_csv}")

def main():
    pasta1 = '/home/andre/Público/BD_QuintelaPenalva_completo'
    pasta2 = '/home/andre/Público/BD_QuintelaPenalva_incompleto'
    caminho_csv = '/home/andre/Público/ficheiros_unicos.csv'
    
    ficheiros_unicos, ficheiros_repetidos = verificar_ficheiros_unicos(pasta1, pasta2)
    exportar_para_csv(ficheiros_unicos, ficheiros_repetidos, caminho_csv)

if __name__ == "__main__":
    main()

