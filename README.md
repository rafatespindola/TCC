# Transferência de dados por ondas sonoras com FSK

> Projeto de TCC de Engenharia de Telecomunicações - IFSC Campus São José
> 

## Getting Started - Loopback

> Permite testar com apenas um computador. A parte Tx gera uma informação, transmite pelo ar e outra parte Rx monitora o som e decodifica o sinal recebido:
> 
1. Executar Rx
    
    ```bash
    cd Rx
    python3 main.py
    ```
    
    Pronto. Você já está processando o áudio
    
2. Executar Tx
    
    ```bash
    cd Tx
    python3 main.py
    ```
    
    Pronto. Você já está preparado para transmitir algo e receber pelo Rx. Digite algo agora!
    

---

## Getting Started - Transferir dados entre dispositivos

> Permite dois computadores distintos se comunicarem entre si. Para isso basta ajustar qual canal físico cada um vai utilizar para Rx e Tx. Um canal é um conjunto de 18 frequências. Há o canal 1 e o canal 2.
> 

Configure assim:

|  | PC1 | PC2 |
| --- | --- | --- |
| TX | 1 | 2 |
| RX | 2 | 1 |

![Canais](canais.png)

### PC1

- Configuração do Rx1, linha 6, arquivo `main.py`:
    
    ```bash
    channel = 1 # canal para comunicação
    ```
    
    Configuração Tx1, linha 12, `Physic.py`:
    
    ```bash
    self.channel = 2 # Canal para comunicação
    ```
    

### PC2

- Configuração do Rx1, linha 6, arquivo `main.py`:
    
    ```bash
    channel = 2 # canal para comunicação
    ```
    
    Configuração Tx1, linha 12, `Physic.py`:
    
    ```bash
    self.channel = 1 # Canal para comunicação
    ```
    

Após os canais configurados, execute os mesmos passos do Lookback em cada PC:

1. Executar Rx
    
    ```bash
    cd Rx
    python3 main.py
    ```
    
2. Executar Tx
    
    ```bash
    cd Tx
    python3 main.py
    ```
    
    Agora você pode enviar e receber dados pelo som!