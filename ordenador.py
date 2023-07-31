class Sorter:
    def __init__(self):
        pass

    def ordene_selection(self, valores):  
        for i in range(0,len(valores)):  
            menor=i

            for j in range (i+1, len(valores)):
                if valores[j] < valores[menor]:
                    menor = j
            valores[i], valores[menor] = valores[menor], valores[i]
        return valores
    
            
    def ordene_insertion(self, valores):
        for i in range(0,len(valores)):
            while i > 0:
                if valores[i-1] > valores[i]:
                    valores[i],valores[i-1] = valores[i-1],valores[i]
                i-=1
        return valores
