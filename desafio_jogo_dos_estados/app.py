# Crie um "Jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada estado do Brasil. O jogo deve perguntar ao 
# usuário "Qual a capital do estado x?" e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuario
# decidir parar ou quando todas as perguntas forem respondidas,
# o código mostra o numero bruto e porcentagem de acertos

import random

estados_brasil = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

pontuacao = 0
jogos_feitos = 0

print('Vamos começar o jogo! \n')

while estados_brasil:
    estado = random.choice(list(estados_brasil.keys()))

    resposta = input(f'Qual a capital de {estado}?   ')

    if resposta.lower() == estados_brasil[estado].lower():
        print('Resposta correta!\n')
        pontuacao += 1
    else:
        print(f'Resposta errada! O correto seria {estados_brasil[estado]}\n')
    estados_brasil.pop(estado)
    jogos_feitos += 1

    opcao = input('Aperte Q para finalizar ou ENTER para continuar \n')

    if opcao == 'q':
        break

porcentagem = (pontuacao*100)/jogos_feitos
print('Jogo finalizado! \n')
print(f'Você jogou {jogos_feitos} rodadas e acertou {pontuacao} respostas ({porcentagem:.2f}% de acerto)')