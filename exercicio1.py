senha = (input("digite sua senha com pelo menos 5 digitos contendo 1 caractere especial "))
email = (input("digite seu e-mail ex:nome@nome"))
cpf = (input("digite seu cpf"))
endereço = (input("digite seu endereço"))
celular = (input("digite seu numero de celular"))
nome = (input("digite seu nome contendo pelo menos 3 letras"))
sobrenome = (input("digite seu sobrenome contendo pelo menos 3 letras"))
saldo = 0
padraonome= ("aaa")
padraosobrenome= ("aaa")
padraosenha=("aaaa@")
padraoemail=("nome@nome")

len(nome)
len(padraonome)
len(sobrenome)
len(padraosobrenome)
len(senha)
len(padraosenha)
len(email)
len(padraoemail)

if len(nome) > len(padraonome)
   if len(sobrenome) > len(padraosobrenome)
      if len(senha) > len(padraosenha)
         if len(email) > len(padraoemail)
          menu = int(input("escolha uma das opçoes a seguir:1-Depositar 2-Sacar 3-Conferir Saldo 4-Transferir 5-Encerrar Conta")) 
            if(menu==1):
                depositar=(input("Deposite uma quantia:"))
                saldo=saldo+depositar
                print("Saldo:",saldo)
            else  :
               pass
              if(menu==1):
                depositar=(input("Deposite uma quantia:"))
                saldo=saldo+depositar
                print("Saldo:",saldo)
              else  :
                pass    
                 if(menu==2):
                   sacar=(input("saque uma quantia:"))
                   saldo=saldo-sacar
                    if sacar > saldo 
                    print("voce nao possui essa quantia pra sacar")
                    else:

                    print("Saldo:",saldo)
                 else  :
                   pass    
                      if(menu==3):
                        
                        print("Saldo:",saldo)
                      else  :
                        pass    
                          if(menu==4):
                            transferir=(input("tranfira uma quantia:"))
                            saldo=saldo-transferir
                             if transferir > saldo
                             print ("voce nao possui saldo para transferir")
                             else :
                             print("Saldo:",saldo)
                           else  :
                             pass 
                                 if(menu==5):
                                  print(" voce encerrou sua conta")
                                 else  :
                                  pass           

else :
print("digite seu nome novamente ele esta fora do padrão")
    else :
    print("digite seu sobrenome novamente ele esta fora do padrão")
      else :
    print("digite sua senha novamente ela esta fora do padrão")
         else :
    print("digite seu e-mail novamente ele esta fora do padrão")