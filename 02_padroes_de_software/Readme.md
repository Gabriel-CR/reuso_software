# Factory ou Fábrica

## Padrões de projeto

### O que são padrões de projetos?

Padrões de projeto são soluções comprovadas e reutilizáveis para problemas comuns no desenvolvimento de software. Eles funcionam como modelos pré-definidos que podem ser adaptados conforme necessário para resolver questões recorrentes em seu código.

### Como um padrão é definido?

A maioria dos padrões de projeto é descrita formalmente para que possam ser aplicados em diferentes contextos. Uma descrição típica de um padrão inclui as seguintes seções:

- **O Propósito do padrão**: Descreve brevemente o problema que o padrão resolve e a solução que ele oferece.
- **A Motivação**: Explica detalhadamente o problema e como a solução proposta pelo padrão ajuda a resolvê-lo.
- **As Estruturas de classes**: Mostram as partes do padrão e como elas se relacionam entre si.
- **Exemplos de código**: Apresentam implementações em linguagens de programação populares, facilitando a compreensão da ideia por trás do padrão.


## Problemas resolvidos

### Desacoplamento entre criação e uso de objetos:
**Problema:** Quando você cria objetos diretamente no código, o cliente precisa saber os detalhes sobre como os objetos são instanciados, o que pode levar a um acoplamento forte entre o código que cria os objetos e o código que os utiliza.

**Consequência / Solução:** O padrão Factory resolve isso ao abstrair a lógica de criação dos objetos. O cliente não precisa saber como a notificação é criada (se é por SMS, e-mail, WhatsApp, etc.), apenas solicita uma instância de Notification e a fábrica se encarrega de providenciar o objeto correto.

### Facilidade para adicionar novos tipos de notificações:
**Problema:** Se você adicionar novos tipos de notificação (por exemplo, notificação via push, Telegram, etc.), você precisaria modificar o código cliente, o que é um risco para a manutenção e aumenta o acoplamento.

**Consequência / Solução:** O padrão Factory permite que você adicione novos tipos de notificações sem alterar o código do cliente. Você só precisa criar uma nova classe NotificationFactory para o novo tipo de notificação e o cliente continuará funcionando corretamente sem mudanças.