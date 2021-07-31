# Introdução ao Machine Learning com Python

## Introdução

Machine Learning é sobre extrair conhecimento dos dados. É um campo de pesquisa na intersecção de estatística, inteligência artificial e ciência da computação e também é conhecido como **análise preditiva** ou **statistical learning**. A aplicação de métodos de machine learning nos últimos anos tornou-se onipresente na vida cotidiana. De recomendações automáticas de filmes, sobre quais comidas pedir ou quais produtos comprar, da personalização de rádios online ao reconhecimento de seus amigos em suas fotos; muitos websites e dispositivos modernos possuem algoritmos de machine learning em seu núcleo. Quando olhamos para um site complexo como o Facebook, Amazon ou Netflix, é muito possível que cada parte do site contém múltiplos modelos de machine learning. Fora de aplicações comerciais, Machine Learning teve uma tremenda influência na forma como a pesquisa conduzida por dados é feita hoje.

## Por que Machine Learning?

Nos primeiros dias de aplicações "inteligentes", muitos sistemas usavam regras de 'if' e 'else' escritas a mão como forma de tomar decisões para processar dados ou ajustar ao input do usuário. Pense em um filtro de spam no qual o trabalho é mover mensagens de e-mail recebidas apropriadas para uma pasta de spam. Poderíamos fazer uma lista negra de palavras que resultariam em um email sendo marcado como spam. Este seria um exemplo do uso de um sistema de regras projetado por especialistas para o projeto de uma aplicação "inteligente". A elaboração manual de regras de decisão é viável para algumas aplicações, particularmente aquelas em que os seres humanos têm uma boa compreensão do processo de modelagem. No entanto, usar regras codificadas manualmente para tomar decisões tem duas grandes desvantagens:

- A lógica necessária para tomar uma decisão é específica a um único domínio e tarefa. Alterando qualquer pequeno aspecto da tarefa pode exigir a reescrita de todo o sistema.
- Desenvolver regras requer um profundo entendimento de como a decisão deve ser feita por um expert humano.

Um exemplo onde essa abordagem de codificação manual irá falhar é no reconhecimento facial em imagens. Hoje, todo smartphone pode detectar uma face em uma imagem. Entretanto, detecção facial era um problema não-resolvido até recentemente em 2001. O principal problema é que a maneira no qual [pixels](https://pt.wikipedia.org/wiki/Pixel) são "percebidos" pelo computador é muito diferente de como humanos percebem faces. Essa diferença em representação torna basicamente impossível para um humano desenvolver um bom conjunto de regras para descrever o que constitui uma face em uma imagem digital.

Utilizando machine learning, entrentanto, simplesmente apresentando um programa com grandes coleções de imagens de faces é o suficiente para um algoritmo determinar quais características são necessárias para identificar a face.

## Problemas que Machine Learning pode Resolver

Os mais bem-sucedidos tipos de algoritmos de machine learning são aqueles que automatizam os processos de tomada de decisão ao generalizarem através de exemplos conhecidos. Nesse *setting*, no qual é conhecido por **supervised learning**, o usuário fornece ao algoritmo pares de **inputs** e **outputs** desejados e o algoritmo busca uma maneira de produzir o output desejado dado um input. Em particular, o algoritmo está apto a criar um output para um input que até então ele nunca viu, sem nenhuma ajuda humana. Retornando ao exemplo de classificação de spam, utilizando machine learning, o usuário fornece ao algoritmo um grande número de emails (no qual são o **input**), juntamente com a informação dos emails serem ou não um spam (no qual é o **output** desejado). Dado um novo email, o algoritmo irá então produzir uma previsão se o novo email é ou não um spam.

Algoritmos de machine learning que aprendem através de pares de input/output são chamados de algoritmos de **supervised learning** porque um "professor" fornece supervisão ao algoritmos na forma de outputs desejados para cada exemplo que eles aprendem. Enquanto que criar um conjunto de dados de inputs e outputs é normalmente um processo manual trabalhoso, algoritmos de **supervised learning** são bem compreendidos e sua performance é fácil de medir. Se sua aplicação pode ser formulada como um problema **supervised learning** e você está apto a criar um conjunto de dados que inclui o resultado desejado, machine learning provavelmente será capaz de resolver seu problema.

Exemplos de tarefas **supervised** de machine learning incluem:

Identificar o código postal de um envelópe com dígitos escritos a mão:

Aqui o input é um scan da caligrafia, e o output desejado são os dígitos do código postal. Para criar um conjunto de dados para construir um modelo de machine learning é necessário coletar muitos envelopes. Então você poderá ler os códigos postais você mesmo e guardar os dígitos como seus resultados desejados.

Determinar se um túmor é benígno baseado em imagens médicas:

Aqui o input é a imagem e o output será se o tumor é benígno ou não. Para criar um conjunto de dados para construir um modelo, você precisa de um banco de dados de imagens médicas. Você também precisará de uma opinião de um expert, sendo assim, um médico precisa olhar todas as imagens e decidir quais tumores são benígnos e quais não são. Possivelmente será necessário fazer diagnósticos adicionais além do conteúdo da imagem para determinar se o túmor na imagem é maligno ou não.

Detectar atividade fraudulenta em transações de cartão de crédito:

Aqui o input é o registro da transação de cartão de crédito, e o output é a possibilidade de ser fraudulento ou não. Assumindo que você é a entitade distribuindo os cartões de crédito, coletar um conjunto de dados significa guardar todas as transações e registros se um usuário reporta qualquer transação como fraudulenta.

Um ponto interessante para ressaltar sobre esses exemplos é que embora o input e output pareçam simples, o processo de coleta de dados para essas três tarefas é muito diferente. Enquanto que ler envelopes é um processo trabalhoso, é fácil e simples. Obter imagens médicas e diagnóstico, por outro lado, requer não apenas maquinário caro, mas também raro e custoso conhecimento expert, sem mencionar aspectos éticos e de privacidade. No exemplo de detecção de fraudes em cartão de crédito, a coleta de dados é muito mais simples. Seus clientes vão prover a você o output desejado, uma vez que eles vão denunciar as fraudes. Tudo que você precisa fazer é obter os pares de input/output de atividades fraudulentas e não-fraudulentas.

**Unsupervised Learning** é o outro tipo de algoritmo que vamos abordar. Nesta tarefa, apenas os dados de input são conhecidos, e nenhum dado de output conhecido é fornecido ao algoritmo. Enquanto que existem muitas aplicações de sucesso desses métodos, eles são normalmente difíceis de compreender e avaliar.

Exemplos de **unsupervised learning** incluem:

Identificar tópicos em um conjunto de blog posts:

Se você tem uma grande coleção de dados textuais, possivelmente você gostaria de sumarizar ele para buscar temas prevalentes nele. Você talvez não saiba de antemão quais são esses tópicos e quantos existem, sendo assim, não existem outputs conhecidos.

Segmentação de clientes em grupos com preferências similares:

Dado um conjunto de registros de clientes, você talvez queira identificar quais clientes são similares, e se há grupos de clientes com preferências similares. Para um site de compras, esses talvez sejam família, gamers, leitores. Porque você não sabe de antemão quais são esses grupos, ou até mesmo quantos eles são, você não tem um outputs conhecidos.

Detectar acesso anormal a um website:

Para identificar abusos ou bugs, é de muita ajuda encontrar padrões de acesso que sejam diferentes da norma. Cada padrão anormal pode ser muito diferente e você provavelmente não tem nenhuma instância de registro de comportamento anormal. Uma vez que nesse exemplo você apenas observa tráfego e você não sabe o que constitui comportamento anormal e normal, esse é um problema **unsupervised**.

Para ambas as tarefas de aprendizado **supervised** e **unsupervised**, é importante ter uma representação de seus dados de input de forma que o computador possa entender. É de grande ajuda pensar em seus dados como um **tabela**. Cada ponto de dados que você deseja racionalizar sobre (cada email, cliente, transação) é uma **linha** e cada propriedade que descreve esse ponto de dados (digamos, a idade do cliente, a quantidade ou localização de uma transação) é uma **coluna**. Você pode descrever usuários por suas idades, seus gêneros, quando eles criaram uma conta e com qual frequência eles compram de sua loja online. Você pode descrever a imagem de um túmor pelos valores de escala de cinza de cada pixel, ou talvez usando seu tamanho, forma e cor do túmor.

Cada entitade ou linha aqui é conhecimento como uma **amostra** (ou ponto de dados) em machine learning, enquanto que as colunas, as propriedades que descrevem essas entidades, são chamadas de características (**features**).

## Sabendo sua Tarefa e Conhecendo seus Dados

Possivelmente a parte mais importante do processo de machine learning é entender os dados que você está trabalhando e como ele se relaciona com a tarefa que você deseja resolver. Não será efetivo pegar um algoritmo aleatoriamente e colocar seus dados nele. É necessário entender o que está acontecendo em seu conjunto de dados antes que você comece a construir um modelo. Cada algoritmo é diferente em termos de quais tipos de dados e quais configurações de problema funcionam melhor. Enquanto você está construindo uma solução de machine learning, você deve responder, ou ao menos manter em mente as seguintes perguntas:

- Quais perguntas eu estou tentando responder? Será que os dados coletados podem responder essa pergunta?
- Qual a melhor maneira de elaborar minha pergunta como um problema de machine learning?
- Será que eu coletei dados o suficiente para representar o problema que quero resolver?
- Quais características dos dados eu extrai, e estas serão capazes de possibilitar as previsões corretas?
- Como eu irei medir o sucesso de minha aplicação?
- Como minha solução em machine learning irá interagir com outras partes de minha pesquisa ou produto empresarial?

Em um contexto maior, os algoritmos e métodos em machine learning são apenas uma parte de um grande processo para resolver um problema particular, e é importante termos a visão abrangente em mente o tempo todo. 

## Por que Python?

Python se tornou a linguagem franca para muitas aplicações de data science. Ela combina o poder de linguagens de programação de propósito geral com a facilidade de uso de linguagens de scripting de domínio específico como MATLAB ou R. Python possui bibliotecas para carregar dados, visualização, estatística, processamento de linguagem natural, processamento de imagem e muito mais. Essa caixa de ferramentas vasta provê cientistas de dados com uma grande gama de funcionalidades gerais e específicas. Uma das principais vantagens em utilizar Python é a habilidade de interagir diretamente com código, utilizando um terminal ou outras ferramentas como **Jupyter-Notebook**. Machine Learning e Análise de Dados são processos fundamentalmente iterativos, no qual os dados dirigem a análise. É essencial para esses processos ter ferramentas que permitem interação rápida e fácil. Como uma linguagem de programção de propósito geral, Python permite a criação de *Graphical User Interfaces* (GUI's), aplicações e serviços web e também possibilita integração com sistemas existentes, tornando ela muito poderosa e versátil.