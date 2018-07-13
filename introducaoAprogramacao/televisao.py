class Televisao:
    def __init__(self, cmin, cmax):
	'Televisao'
        self.ligada = False
        self.canal = 2
        self.cmin = cmin
        self.cmax = cmax

    def muda_canal_para_cima(self):
        if (self.canal+1 <= self.cmax):
            self.canal+=1
        else:
            pass #canal = cmin
            
    def muda_canal_para_baixo(self):
        if (self.canal-1 >= self.cmin):
            self.canal-=1
        else:
            pass #canal = cmax

    def __str__(self):
        return 'ligada:{0} ; canal:{1}'.format(self.ligada,self.canal)
    
