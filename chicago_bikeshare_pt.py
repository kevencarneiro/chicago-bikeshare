# coding: utf-8

# Começando com os imports
import csv
import math
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")

# TAREFA 1
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")


def print_line(enumerator, has_headers=False):
    """
    Imprime uma linha formatada com os cabeçalhos.
    Argumentos:
      enumerator: O Enumerador que deverá ser impresso.
      has_headers: Indica se a primeira linha do enumerador possui cabeçalhos ou não.
    Retorna:
      Um generator de strings formatadas para exibição em tela.
    """
    count = 1 if has_headers else 0
    while count < len(enumerator):
        if has_headers:
            columns = ('{}: {}'.format(header, item) for header, item in zip(enumerator[0], enumerator[count]))
            yield '{}: {}'.format(count, '\t\t'.join(columns))
        else:
            yield '{}: {}'.format(count+1, str(enumerator[count]))
        count += 1


print('\n'.join(print_line(data_list[:21], has_headers=True)))

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")


# TAREFA 2
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
print('\n'.join((x[6] for x in data_list[:20])))

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")


# TAREFA 3


def column_to_list(data, index):
    """
    Converte uma colunha de uma lista para uma lista de valores.
    Argumentos:
      data: A lista original.
      index: O índice onde estão os dados a serem retornados.
    Retorna:
      Uma lista de valores da coluna especificada.
    """
    return [x[index] for x in data]


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
gender_list = column_to_list(data_list, -2)
gender_dict = dict([(i, gender_list.count(i)) for i in set(gender_list)])
male = gender_dict.get('Male')
female = gender_dict.get('Female')


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)


def count_gender(data_list):
    """
    Contador de gênero.
    Argumentos:
      data_list: A lista que contém os dados de gênero.
    Retorna:
      Uma lista de quantos elementos existem para a lista, na ordem [male, female].
    """
    gender_list = column_to_list(data_list, -2)
    gender_dict = dict([(i, gender_list.count(i)) for i in set(gender_list)])
    male = gender_dict.get('Male')
    female = gender_dict.get('Female')
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# Esperamos ver "Male", "Female", ou "Equal" como resposta.


def most_popular_gender(data_list):
    """
    Retorna o gênero mais popular.
    Argumentos:
        data_list: A lista que contém os dados de gênero.
    Retorna:
        Uma string com o valor do gênero mais popular.
    """
    male_count, female_count = count_gender(data_list)
    if male_count == female_count:
        answer = "Equal"
    elif male_count < female_count:
        answer = "Female"
    else:
        answer = "Male"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7


def plot_single_column_bar(data_list, x_label, column_index, y_label="Quantidade", limit=None):
    """
    Exibe um gráfico na tela de acordo com a coluna especificada
    Argumentos:
      data_list: A lista que contém os dados.
      x_label: O nome da coluna que será exibida.
      column_index: O índice na lista que contém os dados que devem ser exibidos
      y_label: O nome da legenda
      limit: Limite de chaves (por maiores valores)
    """
    column_list = column_to_list(data_list, column_index)
    count_items = dict([(x, column_list.count(x)) for x in set(column_list)])
    if limit:
        count_items = sorted(count_items.items(), key=lambda x: x[1], reverse=True)[:limit]
        count_items = dict(count_items)
    y_pos = list(range(len(count_items)))
    plt.bar(y_pos, count_items.values())
    plt.xticks(y_pos, count_items.keys(), rotation=90)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title('{} por {}'.format(y_label, x_label))
    plt.show(block=True)


print("\nTAREFA 7: Verifique o gráfico!")
plot_single_column_bar(data_list, 'Tipo de Usuário', -3)

input("Aperte Enter para continuar...")

# Exploração de dados adicionais
print("\nDados sobre as estações de destino")
plot_single_column_bar(data_list, "Destino", 4, "Quantidade de passageiros", 5)
input("Aperte Enter para continuar...")

# TAREFA 8
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque existem dados sem a informação de gênero preenchida"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = None
max_trip = None
mean_trip = None
median_trip = 0.
sum_trip = 0.

for duration in trip_duration_list:
    duration = float(duration)
    if not min_trip:
        min_trip = duration
    elif duration < min_trip:
        min_trip = duration

    if not max_trip:
        max_trip = duration
    elif duration > max_trip:
        max_trip = duration

    sum_trip += duration

mean_trip = sum_trip/len(trip_duration_list)

sorted_trip_duration_list = sorted([float(x) for x in trip_duration_list])

if len(trip_duration_list) % 2 == 0:
    median_index = int(len(trip_duration_list) / 2)
    median_trip = sorted_trip_duration_list[median_index]
else:
    division_result = len(trip_duration_list) / 2
    index1, index2 = math.ceil(division_result), math.floor(division_result)
    median_trip = (sorted_trip_duration_list[index1] + sorted_trip_duration_list[index2])/2

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#       """
#       Função de exemplo com anotações.
#       Argumentos:
#           param1: O primeiro parâmetro.
#           param2: O segundo parâmetro.
#       Retorna:
#           Uma lista de valores x.
#
#       """

input("Aperte Enter para continuar...")


# TAREFA 12 - Desafio! (Opcional)
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


def count_items(column_list):
    count_dict = dict(((x, column_list.count(x)) for x in set(column_list)))
    item_types = count_dict.keys()
    count_items = count_dict.values()
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
