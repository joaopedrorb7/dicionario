dicionário =[]
while True:
    op=int(input("\n1.adicionar palavra\n2.bucar palavra\n3.filtrar inicial\n4.filtrar por tipo\n5.sair \ndigite oque deseja fazer :"))
    if op ==1:
        palavra=str(input("digite a palavra (em inglês ):")).lower()
        tradução=str(input("digite a tradução (em português ):")).lower()
        tipo_num=str(input("digite o tipo da palavra:\n1.verbo\n2.adjetivo\n3.substantivo\n"))
        
        if  tipo_num=="1":
                      tipo="verbo"
        elif tipo_num=="2":
                      tipo="adjetivo"
        elif tipo_num=="3":
                       tipo="substantivo"
        else:
                       print("opção inválida")  
                       continue
                       
        inicial=palavra[0]
        conjunto={"palavra":palavra,"tradução": tradução,"tipo":tipo,"inicial":inicial}
        dicionário.append(conjunto)
    elif op==2:
        filtro=str(input("digite a palavra que busca (em inglês ):")). lower ()
        for ingles in dicionário:  
            if ingles["palavra"]==filtro:
                print()
                print(f"palavra encontrada : {ingles}")
    elif op ==3:
        filtro=str(input("digite a incial que busca :")). lower ()
        for ingles in dicionário:  
            if ingles["inicial"]==filtro:
                print ()
                print(f"palavras encontradas : ")
                print (f"{ingles}")
    elif op==4:
        filtro=int(input("digite o tipo da palavra:\n1.Verbo\n2.Adjetivo\n3.Substantivo\n"))
        if filtro==1:
            for ingles in dicionário:  
               if ingles["tipo"]=="verbo":
                    print ()
                    print(f"palavra encontrada : {ingles}")
        elif filtro ==2:
            for ingles in dicionário:  
               if ingles["tipo"]=="adjetivo":
                    print ()
                    print(f"palavra encontrada : {ingles}")
        elif filtro ==3:
            for ingles in dicionário:  
               if ingles["tipo"]=="substantivo":
                    print ()
                    print(f"palavra encontrada : {ingles}")   
        else:
            print("opção inválida ")
    elif op ==5:
        print ("você saiu")
        break
    else:
        print("comando inválido")
        break
                
    
