# FF-Predator (BETA TESTE!)

Este script é um IP sniffer para o jogo Free Fire. Ele usa a biblioteca Scapy para capturar pacotes de rede e filtrar pacotes do jogo. Ele começa capturando pacotes TCP que passam pela porta 5222, que é a porta usada para jogos Free Fire.

Em seguida, ele usa a função packet_callback() para imprimir o endereço IP de origem dos pacotes capturados que tem como origem ou destino a porta 5222. A função verifica se o endereço IP de origem não é o mesmo do dispositivo que está executando o script, para evitar capturar o seu próprio endereço IP.

O script também adiciona uma estrutura de dicionário para armazenar os nomes de usuário correspondentes aos endereços IP capturados. Ele verifica se o endereço IP de origem já está presente no dicionário, se sim, ele imprime o nome de usuário correspondente, se não, ele solicita que o usuário insira o nome de usuário correspondente ao endereço IP e armazena-o no dicionário.
