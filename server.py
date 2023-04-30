import rpyc
import sys
import time

class MyService(rpyc.Service):

    #----------------------------QUESTION 1 -----------------------------
    def on_connect(self, conn):
    # código que é executado quando uma conexão é iniciada, caso seja necessário
        pass

    def on_disconnect(self, conn):
    # código que é executado quando uma conexão é finalizada, caso seja necessário
        pass

    def exposed_get_answer(self): # este é um método exposto
        return 42
    
    exposed_the_real_answer_though = 43 # este é um atributo exposto

    def get_question(self): # este método não é exposto
        return "Qual é a cor do cavalo branco de Napoleão?"
    #----------------------------QUESTION 1 -----------------------------

    #----------------------------QUESTION 4 and 5 -----------------------------
    def exposed_array_sum(self, array):
        start = time.time()
        sum = 0
        for i in range(len(array)):
            sum += array[i]
        end = time.time()
        print(end - start)
        return sum
    #----------------------------QUESTION 4 and 5 -----------------------------

#Para iniciar o servidor
if __name__ == "__main__":
    print("Server Started")
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()
    print("Server Stopped")