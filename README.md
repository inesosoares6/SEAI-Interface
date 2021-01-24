# SEAI-Interface

Este repositório é um dos módulos do sistema de gestão de carregamento de veículos elétricos. Este sistema foi dividido em Controlo, Gestão e Monitorização e Interface com o Utilizador.

Uma das partes essenciais deste grande sistema é a interacção com o utilizador de forma a que se consiga apresentar-lhe a informação necessária e permitir que este possa tomar decisões simples associadas ao carregamento. Numa abordagem mínima e essencial a interface será feita localmente no carregador e adicionalmente será feita através de uma aplicação para smartphones.

![Design-Interface](https://user-images.githubusercontent.com/47570179/105633549-24576000-5e51-11eb-9b72-f466386e5cfd.jpg)

A Interface com o utilizador é um elemento que se baseia na comunicação entre o utilizador e o software, mais especificamente, a componente de Controlo e base de dados. Assim, é possível dividi-la em dois diferentes ramos: Comunicação e Interação com o Utilizador.

**Comunicação**

Para que as configurações feitas pelo utilizador sejam passadas ao sistema, terá de ser estabelecer uma via de comunicação entre a Interface a o módulo do Controlo. A comunicação com o módulo de Controlo será feita através de *Transmission Control Protocol* (TCP). Além disso, será também preciso estabelecer uma ligação com a base de dados para consulta de dados necessários para apresentar ao utilizador (preços, disponibilidade, etc.). Para que esta comunicação fosse possível, desenvolveu-se uma API que executa tal tarefa. Desta forma, a interface web apenas necessitava de fazer pedidos à API de acordo com os dados que necessita. Uma vez que foi também desenvolvida uma aplicação para dispositivos móveis, a comunicação foi feita também pela API, fazendo com que a aplicação não tivesse de abrir sockets de comunicação TCP que poderiam comprometer o seu desempenho.

**Interação com o utilizador**

A interação com o utilizador foi feita, inicialmente, através da interface existente no carregador local (requisito mínimo). Onde será possível o utilizador consultar preços, escolher o modo de carregamento (rápido, normal ou verde) e iniciar ou interromper o carregamento. Após a concretização desta plataforma, para uma melhor interação com o utilizador, foi desenvolvida uma aplicação para dispositivos móveis (requisito adicional). Nesta aplicação, inicialmente, implementaram-se apenas as mesmas funcionalidades que a plataforma local e, posteriormente, foram desenvolvidas funcionalidades adicionais.

## Authors
* André Martins up201605016@fe.up.pt
* Ines Soares up201606615@fe.up.pt
