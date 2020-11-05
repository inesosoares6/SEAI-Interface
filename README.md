# SEAI-Interface

Este repositório é um dos módulos do sistema de gestão de carregamento de veículos elétricos. Este sistema foi dividido em Controlo, Gestão e Monitorização e Interface com o utilizador.

Uma das partes essenciais deste grande sistema é a interacção com o utilizador de forma a que se consiga apresentar-lhe a informação necessária e permitir que este possa tomar decisões simples associadas ao carregamento. Numa abordagem mínima e essencial a interface será feita localmente no carregador e adicionalmente será feita através de uma Aplicação para smartphones.

<p align="center">
  <img src="https://github.com/up201606615/SEAI-Interface/blob/devel/Design/Interface.jpg">
</p>

A Interface com o utilizador é um elemento que se baseia na comunicação entre o utilizador eo software, mais especificamente, a componente de Controlo. Assim, é possível dividi-la em trêsdiferentes ramos: Comunicação, Interação com o utilizador e Microcontrolador.A comunicação com o módulo de Controlo será feita através deUser Datagram Protocol(UDP).Foi escolhido este protocolo de comunicação por ser simples e não ser necessária a confirmação dachegada da mensagem.

## Authors
* André Martins up201605016@fe.up.pt
* Daniel Luiz up201703713@fe.up.pt
* Ines Soares up201606615@fe.up.pt
