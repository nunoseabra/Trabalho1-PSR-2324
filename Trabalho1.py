#!/usr/bin/env python3
# ----------------------------------------------
# Typing test program - PSR - Trabalho 1
# Miguel Bento Simoes - 118200
# Nuno Seabra - 102889
# Luís Fernades - 103085
# ----------------------------------------------

#Imports

import argparse
import random
import string
from pprint import pprint
from time import time, ctime
from readchar import readkey, readchar
from nltk.corpus import words
from collections import namedtuple
from colorama import Fore, Back, Style


# Define o namedtuple Input

Input = namedtuple('Input', ['requested', 'received', 'duration'])

##############################    Functions    ############################## 


def obtain_input_answer(x,random_word, bem_sucedido,input_records):  #Esta funçao compara a random word com as respostas do jogador e regista na lista de inputs

    start_time = time() #Inicio do jogo

    if x == 1: #se for palavra
    
    
        keys= ''  #vetor de caracteres 

        tti = time() #Inicio da tentativa
        
        print(Back.WHITE + Fore.BLACK + f'Digite: {random_word} ' + Style.RESET_ALL) # Print com fundo branco e letras a preto  da palavra a ser escrita . No fim reset 


        while len(keys) < len(random_word): #compara o tamanho da palavra de jogo e a palavra escrita pelo jogador

            key = readchar() #leitura do carater escrito

            if ord(key) == 32: #caso seja premido a tecla ESPAÇO o jogo é interrompido
                break
        
            keys += key #adiciona o carater escrito 

            print(key, end = "",flush=True)   #Printa na mesma linha os varios caracteres à medida que sao escritos
            
        
         

        if keys == random_word: #comparaçao da palavra dada com a escrita pelo jogador
            print('\n'+ Fore.GREEN+ f"Correto! " + Style.RESET_ALL + "Voce inseriu " + Fore.GREEN + f"{keys}" + Style.RESET_ALL)
            bem_sucedido += 1 #tentativa bem sucedida

        elif ord(key) == 32:
            print('\n' + Fore.YELLOW + f"Teste cancelado" + Style.RESET_ALL) #carregou espaço para cancelar o jogo

           
        else:
            print('\n' + Fore.RED + f"Incorreto! "+ Style.RESET_ALL + "Voce inseriu " + Fore.RED + f"{keys}" + Style.RESET_ALL) #tentativa falhada

        ttf = time() #Final da tentativa 

        tempo_tentativa = round(ttf-tti,2)  #tempo da tentativa arredondado para 2 casas decimais

        input_record = Input(requested=random_word, received=keys, duration=tempo_tentativa) #Registo dos dados da tentativa no namedtuple

        input_records.append(input_record)  # Adiciona o registo à lista das tentativas       
        
        
  

    else: #se for caracter

        tti = time() #Inicio da tentativa
        

        print(Back.WHITE + Fore.BLACK+ f'Digite: {random_word} '+ Style.RESET_ALL)    

        key = readkey() #leitura da tecla premida

        if key == random_word:
            print(Fore.GREEN + f"Correto! " + Style.RESET_ALL + "Voce inseriu " + Fore.GREEN + f"{key}" + Style.RESET_ALL) # Correto e key escrita a verde
            bem_sucedido += 1 

        elif ord(key) == 32:
            print(Fore.YELLOW + f"Teste cancelado" + Style.RESET_ALL) #Escrito a amarelo
           
        else:
            print(Fore.RED + f"Incorreto! " + Style.RESET_ALL + "Voce inseriu " +Fore.RED + f"{key}" + Style.RESET_ALL)

        ttf = time() #Final da tentativa 

        tempo_tentativa = round(ttf-tti,2)    #tempo da tentativa arredondado para 2 casas decimais
  
        input_record = Input(requested=random_word, received=key, duration=tempo_tentativa) #Registo dos dados da tentativa no namedtuple

        input_records.append(input_record)  # Adicione o registro à lista

    return bem_sucedido, key, input_records    #devolve as tentativas bem sucedidas, letra premida e os namedtuples  

def temp_mx( bem_sucedido, tempo_decorrido):  #gerar palavras ou letras com o modo tempo limitado

    args = arg_init() #Chamada da função arg_init()

    input_records = [] #lista para os inputs

    x=0  #para definir por default modo letra na funçao obtain_input_answer

    number_of_types=0 #variavel das tentativas

    bem_sucedido=0 #variavel das tentativas bem sucedidas
    
    start_time= time() #Inicio do teste

    while True: 

        tempo_inicio=time() #Inicio da tentativa
        
        if args.use_words:

            x=1 #para definir modo palavra na funçao obtain_input_answer

            random_word = generate_random_word() #gera a nossa palavra aleatoria 
        else:
            random_word = random.choice(string.ascii_lowercase) #gera o nosso carater aleatorio
        
        bem_sucedido, key, input_records = obtain_input_answer(x,random_word, bem_sucedido,input_records) #resultados da tentativa: tentativas certas, tecla premida, namedtuples das tentativas feitas

        input_ascii = ord(key) #conversao para ascii

        tempo_fim=time() #Fim da tentativa

        tempo_tentativa=  round(tempo_fim- tempo_inicio ,2) #tempo da tentativa arredondado para 2 casas decimais

        if input_ascii == 32: #se a tecla premida foi ESPAÇO para o teste
            break

        number_of_types +=1 #incrementa uma tentativa
 
        
        end_time=time() #Final do teste

        tempo_decorrido= round(end_time - start_time, 2) #tempo do teste arredondado para 2 casas decimais

        if tempo_decorrido >= args.max_value: #quando o tempo do teste for superior ao tempo selecionado no argumento incial
            break    
        

    print(f"De {number_of_types} tentativas voce acertou  " + Fore.GREEN + f"{bem_sucedido}" +Style.RESET_ALL+ f" em {tempo_decorrido} segundos.")   
    return number_of_types, bem_sucedido, tempo_decorrido, input_records  


def input_mx( bem_sucedido, tempo_decorrido): #gerar palavras ou letras com o modo tentativas limitadas

    args = arg_init() #Chamada da função arg_init()

    input_records = [] #lista para os inputs

    x=0 #para definir por default modo letra na funçao obtain_input_answer

    number_of_types=0 #variavel das tentativas

    bem_sucedido=0 #variavel das tentativas bem sucedidas

    start_time=time() #Inicio do teste

    while True:

        tempo_inicio=time() #Inicio da tentativa

        if args.use_words:

            x=1 #para definir modo palavra na funçao obtain_input_answer

            random_word = generate_random_word() # gera a nossa palavra aleatoria
        else:
            random_word = random.choice(string.ascii_lowercase) #gera o nosso carater aleatorio
        
        bem_sucedido, key, input_records = obtain_input_answer(x,random_word, bem_sucedido,input_records) #resultados da tentativa: tentativas certas, tecla premida, namedtuples das tentativas feitas

        input_ascii = ord(key) #conversao para ascii

        tempo_fim=time() #Inicio da tentativa

        tempo_decorrido=  round(tempo_fim- tempo_inicio ,2) 

        if input_ascii == 32: #se a tecla premida foi ESPAÇO para o teste

            break

        number_of_types +=1 #incrementa uma tentativa


        if number_of_types >= args.max_value:  #quando o numero de tentativas do teste for superior ao numero selecionado no argumento incial
            break    

    end_time=time() #Final do teste

    tempo_decorrido= round(end_time - start_time, 2)    #tempo do teste arredondado para 2 casas decimais
   

    print(f"De {number_of_types} tentativas voce acertou " + Fore.GREEN + f"{bem_sucedido}" + Style.RESET_ALL + f" em {tempo_decorrido} segundos.")  

    return number_of_types, bem_sucedido, tempo_decorrido, input_records   


def generate_random_word(): #gera a palavra aleatoriamente em funçao do numero de caracters pretendidos para o teste
    
    args = arg_init() 

    if args.test_level == 1:
        length = random.randint(3, 4)        #Nivel 1 - Facil - palavras com 3 a 4 caracters
    elif args.test_level == 2:
        length = random.randint(5, 6)        #Nivel 2 - Medio - palavras com 5 a 6 caracters
    elif args.test_level == 3:
        length = random.randint(7, 8)        #Nivel 3 - Dificil -palavras com 7 a 8 caracters
    else:
        length = random.randint(3, 6)        #default - caso nao seja selecionado o nivel do teste no modo palavras. As palavras terão entre 3 a 6 caracters
     
    word_list = words.words() #acesso às palavras de uma biblioteca existente

    words_with_length = [word for word in word_list if len(word) == length] #seleçao de todas as palavras que cumprem o requisito de caracters

    a=random.choice(words_with_length) #escolha da palavra para a tentativa

    return a.lower() #devolve a palavra selecionada escrita em minusculas

def arg_init():  # Esta funçao configura o parser de argumentos de entrada

    parser = argparse.ArgumentParser(description="Definição do modo de teste")

    parser.add_argument("-utm", "--use_time_mode", action="store_true",
                        help="Tempo máximo em segundos para o modo de tempo ou número máximo de entradas para o modo de número de entradas.") # argumento modo tempo limitado , nao obrigatorio
    
    parser.add_argument("-mv", "--max_value", type=int,
                        help="Tempo máximo em segundos para o modo de tempo ou número máximo de entradas para o modo de número de entradas.") # argumento para tempo maximo ou tentativas limite em inteiro, obrigatorio
    
    parser.add_argument("-uw", "--use_words", action="store_true",
                        help="Usar o modo de digitação de palavras em vez de digitação de caracteres individuais.") # argumento modo palavras , nao obrigatorio
    
    parser.add_argument("-tl","--test_level",type=int, required=False, default=0 ,help="Para o modo de palavras selecione o nivel de dificuldade de 1 a 3") # argumento nivel do teste em inteiro, por default é zero , nao obrigatorio

    return parser.parse_args()     

def aguardar_tecla(): #Esta funçao da inicio ao teste com o premir que qualquer tecla

    print("Pressione uma tecla para começar ...")

    digitado = readkey() #leitura da tecla premida para começar o teste

#############################    MAIN    #############################

def main():

    # Variaveis
    
    test_start = ctime() #Data de inicio do teste
    
    bem_sucedido = 0 #Tentativas acertadas

    tempo_decorrido =0 #Tempo do teste
    
    args = arg_init()   #Chamada da função arg_init()

    aguardar_tecla()  #começar o teste

    if args.use_time_mode: #se for modo tempo limitado

        number_of_types, bem_sucedido, tempo_decorrido, input_records = temp_mx( bem_sucedido, tempo_decorrido)

    else: #se for modo tentativas limitadas

        number_of_types, bem_sucedido, tempo_decorrido, input_records = input_mx(bem_sucedido,tempo_decorrido) 



    ############################# Statistic #############################

    accuracy = str(round((bem_sucedido / number_of_types)* 100)) + '%' if number_of_types > 0 else str(0) + '%' # taxa de acerto com arredondamento para zero casas decimais

    type_average_duration = round(sum(input_record.duration for input_record in input_records) / number_of_types, 2) if number_of_types > 0 else 0 # tempo medio de tentativa arredondado com 2 casas decimais

    type_hit_average_duration = round(sum(input_record.duration for input_record in input_records if input_record.requested == input_record.received and bem_sucedido > 0) / bem_sucedido , 2) if bem_sucedido > 0 else 0 # tempo medio de tentativa acertada

    type_miss_average_duration = round(sum(input_record.duration for input_record in input_records if input_record.requested != input_record.received and number_of_types - bem_sucedido > 0) / (number_of_types - bem_sucedido), 2) if number_of_types - bem_sucedido > 0 else 0 # tempo medio de tentativa acertada


    test_end = ctime() #Data do final do teste

    result_dict = {                                    #dicionario dos resultados
        'accuracy': accuracy,
        'inputs': input_records,
        'number_of_hits': bem_sucedido,
        'test_duration': tempo_decorrido,
        'test_start': test_start,
        'test_end': test_end,
        'test_level': args.test_level,
        'number_of_types': number_of_types,
        'type_average_duration': type_average_duration,
        'type_hit_average_duration': type_hit_average_duration,
        'type_miss_average_duration': type_miss_average_duration
        }      

    pprint(result_dict) #print do dicionario

    
if __name__ == "__main__":
    main() 
