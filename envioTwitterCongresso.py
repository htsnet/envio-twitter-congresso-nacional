# MUDE AQUI AS VARIÁVEIS DE ACORDO COM SUAS INFORMAÇÕES
idTwitter = "<SEU ID NO TWITTER>"
senhaTwitter = "<SUA SENHA DA CONTA NO TWITTER>"
localDriver = "<CAMINHO COMPLETO>/chromedriver.exe"


## NÃO ALTERAR DESTA LINHA PARA BAIXO

#importa as bibliotecas
from selenium import webdriver
from time import sleep
import pickle #https://www.semicolonworld.com/question/43757/how-to-save-and-load-cookies-using-python-selenium-webdriver
import readchar
import random

procura = False

def escolheDestino():
    quem = input("Para quem enviar? D (deputados) ou S (senadores): ").upper()
    if quem == "D":
        print("Envio para Deputados")
    elif quem == "S":
        print("Envio para Senadores")
    else:
        escolheDestino()
    return quem


def enviaTwittes(elemento):
    global procura
    conta = 0
    for i in elemento:
        conta += 1
        print(conta, sep=" ")
        print(i.get_attribute('href'))
        link = i.get_attribute('href')
        partes = link.split("/")
        destino = partes[3]
        if procura == False:
            try:
                driverT.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div').click()
                sleep(0.4)
                driverT.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/span').send_keys("@" + destino + " " + texto)
                driverT.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]').click()
            except: 
                print("Não conseguiu enviar para ", destino)
            
            sleep(1)
            try:
                #se achou o campo de fechar, então não foi enviada
                driverT.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div').click
                print("Não conseguiu enviar para ", destino)
            except:
                #aguarda 3 segundos
                sleep(3)    
                
            
        else:
            if retomada == destino:
                procura = False

paraQuem = escolheDestino()        

texto = input("Digite o texto a enviar com até 220 caracteres: ")

print('\n\nO texto a ser enviado é: ', texto)
print('\n\nO texto tem {} caracteres'.format(len(texto)))

if len(texto) > 235:
    print("\n\nAtenção: pode haver trucamento no final do texto!")
    

retomada = input("Se for uma retomada, indique último envio com sucesso: ")
    
confirmacao = input("Confirma o envio? S/n: ")

if confirmacao == "s" or confirmacao == "S" or confirmacao == "":
    
    if len(retomada) > 0:
        procura = True
    else:
        procura = False
        
    
    urlLogin = "https://twitter.com/login"
    
    #tenta acessar usando os cookies para não precisar logar novamente        
    try:
        driverT.get(urlLogin)    
        
        cookies = pickle.load(open("twitter.pkl", "rb"))
        for cookie in cookies:
            driverT.add_cookie(cookie)
            
        driverT.get("https://twitter.com/")           
        
    except:
        driverT = webdriver.Chrome(localDriver)

        
        driverT.get(urlLogin)    
        sleep(3)
        #abre e se loga no Twitter
        driverT.find_element_by_name("session[username_or_email]").send_keys(idTwitter)
        driverT.find_element_by_name("session[password]").send_keys(senhaTwitter)
        driverT.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div').click()
        sleep(1)
        #guarda a sessão
        #mantém as sessões do browser
        pickle.dump(driverT.get_cookies() , open("twitter.pkl","wb"))
    
    
    driver = webdriver.Chrome(localDriver)
    
    #define URL para acesso da págin com os endereços do twitter
    if paraQuem == "S":
        url = "https://www.vemprarua.net/senado/br/"
        driver.get(url)
        elemento = driver.find_elements_by_class_name("twitter-share")
        enviaTwittes(elemento)
    else:
        #faz embaralhamento para enviar em ordem aleatória
        estados = ['ac', 'al', 'ap', 'am', 'ba', 'ce', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to', 'df'] 
        random.suffle(estados)
        for estado in estados:
            url = "https://www.vemprarua.net/camara/" + estado + "/"
            print("\nEstado ", estado.upper())
            driver.get(url)
            elemento = driver.find_elements_by_class_name("twitter-share")
            enviaTwittes(elemento)
            #aguarda 10 segundos antes do próximo estado se está enviando
            if procura == False:
                sleep(10)
    
    driver.close()
    driverT.close()

else:
    print("Processamento encerrado.")

