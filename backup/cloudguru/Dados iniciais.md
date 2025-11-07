* Dados iniciais
JWT API's
passwords (DB ou outros)
Json Accounts od service


* Polita de replicação.
A politica de replicação de um secret não pode ser mudada depois de sua criação
Definição: devem ser deixado por padrão, automaticas sem gerenciamento.



* Criptografia
Definição deve ser deixada por padrão, automática sem gerenciamento.



* Rotação.
90 dias a ser implementado de forma gradual.
rotação
Serão definidos horários de folga como horário de rotação chave, para que no caso de afetar algum sistema com o rotação, não cause indisponibilidade de serviços.

* expiração.
Definição deve ser deixado por padrão, não deve expirar


* TAG
Definição nomenclatura, ID do projeto + nome do aplicativo.



* Versionamento
estados de um segredo.
Toda parte de versionamento exige uma solução robusta e bem pensada.
Como manter apenas as últimas duas versões de um segredo.
Ao criar uma nova versão é possivel marcar um check box desabilitando as versões anteriores.


* Notificações

Selecione os tópicos do Pub/Sub que receberão notificações de eventos quando o segredo ou uma de suas versões for modificado
Esses eventos podem ser iniciados pelo usuário ou eventos programados

Como trigar um Pub/Sub através da alteração de um secret ?

Ao criar um secret é possivel notificar um Pub/Sub sobre alterações no secret.
Select Pub/Sub topic(s) that will receive event notifications whenever the secret or one of its versions is changed. These events can be user initiated changes or scheduled 


* Permissões
*Service account*
Deve ser usada uma conta de serviço exclusiva associada ao projeto, que será atribuída ao segredo correspondente, a conta deve ter a seguinte permissão secretmanager.secretAccessor


* segredos temporários
podem ser definidos temporariamente indicando no no momento de sua criação a seção de expiração, esse tipo de segredo pode ser usado para projetos temporários ou testes não produtivos.











