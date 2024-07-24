import os
import pandas as pd

c = os.path.dirname(__file__)
arquivo = c + '/teste.xlsx'

# Lendo planilha
planilha = pd.read_excel(arquivo)

df = pd.DataFrame(planilha)
print(df)

# Inserindo dados na planilha
dados = {'verificador': [],
        }


# df2 = pd.DataFrame(dados)

# df_concat = pd.concat([df, df2], ignore_index=True)

# with pd.ExcelWriter(arquivo) as writer:
#     df_concat.to_excel(writer, sheet_name='Sheet1', index=False)

# c=0


# df_concat = pd.concat([df, df2], ignore_index=True)

# with pd.ExcelWriter(arquivo) as writer:
#     df_concat.to_excel(writer, sheet_name='Sheet1', index=False)


planilha_att = pd.read_excel(arquivo)
print("Planilha atualizada:")
print(planilha_att)