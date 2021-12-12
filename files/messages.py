geral_faceis = [ # 60 palavras de 6 letras cada
    'teste', 'apice', 'animo', 'comum', 'graca', 'graxa', 'terra', 'corda', 'carro', 'visor', 'tampa', 'vidro', 
    'barra', 'ganso', 'manso', 'senso', 'algoz', 'nobre', 'exito', 'sagaz', 'inato', 'ideia', 'honra', 'poder',
    'sutil', 'mutua', 'afeto', 'mexer', 'aquem', 'ardil', 'corja', 'prole', 'digno', 'crivo', 'culto', 'mundo',
    'brado', 'gleba', 'tenaz', 'regra', 'saude', 'viril', 'usura', 'clava', 'pifio', 'feliz', 'heroi', 'coisa',
    'plato', 'alibi', 'fluxo', 'senil', 'lugar', 'ligar', 'crise', 'grato', 'vital', 'valor', 'olhar', 'fator',
] 

geral_medianas = [ # 63 palavras de 8 letras cada
    'inerente', 'peculiar', 'denegrir', 'respeito', 'genocida', 'anuencia', 'deferido', 'prudente', 'equidade',
    'pandemia', 'iminente', 'invasivo', 'essencia', 'desgraca', 'alienado', 'misogino', 'eminente', 'extensao',
    'abstrato', 'empirico', 'premissa', 'conceito', 'ardiloso', 'reiterar', 'ascensao', 'passivel', 'prodigio',
    'devaneio', 'talarico', 'lascivia', 'conserto', 'modestia', 'apologia', 'analogia', 'insercao', 'ativista',
    'inospito', 'monotono', 'respaldo', 'remissao', 'sinonimo', 'mediocre', 'concerne', 'rapariga', 'despeito',
    'gratidao', 'alicerce', 'retorica', 'destarte', 'rechacar', 'fomentar', 'proceder', 'demagogo', 'primazia',
    'metodico', 'consiste', 'distinto', 'abnegado', 'criterio', 'desfecho', 'sucumbir', 'historia', 'elegivel',
]

# geral_dificeis = [
#     'paralelepipedo', 'empoderamento', 'delineamento', 'caleidoscopio', 'polinesio', 'polifonico',
# ]

categoria_geral = [geral_faceis, geral_medianas, geral_faceis]


tech_faceis = ['byte', 'bit', 'git', 'put', 'add']

tech_medianas = ['append', 'enumerate', 'while', 'atribuicao', 'repeticao', 'condicional', 'flutuante']

tech_dificeis = ['engenharia_de_dados', 'data_wharehouse', 'business_intelligence', 'data_mining', 'data_science', 'artificial_intelligence',
'machine_learning','deep_learning']

categoria_tech = [tech_faceis, tech_medianas, tech_dificeis]

tech_dicionario = {
'engenharia de dados':' DICA: É a disciplina focada nos apectos como a identificação das fontes de dados, coletânea e,'
'\nno armazenamento dos dados.',
'data wharehouse' :' DICA: É um repositório central de informações que pode ser usado para analisar e tomar decisões mais informadas.',
'business intelligence' :'DICA: É a disciplina de analisar e transformar dados para extrair valiosos insights de negócios para permitir'
'\na tomada de decisões. Hoje, o BI é normalmente usado para se referir a análises descritivas e relatórios.',
'data mining' : 'DICA: É um processo de extração e descoberta de padrões em grandes conjuntos de dados envolvendo métodos na interseção'
'\nde aprendizado de máquina, estatísticas e sistemas de banco de dados.',
'data science' : 'DICA: É a disciplina de aplicação de técnicas analíticas avançadas para extrair informações valiosas de dados para a'
'\ntomada de decisões de negócios e planejamento estratégico.',
'artificial intelligence' : 'DICA: Refere-se à capacidade de uma máquina de imitar as capacidades da mente humana, como aprender com'
'\nexemplos e experiências, reconhecer objetos, compreender e responder à linguagem, tomar decisões e resolver problemas.',
'machine learning': 'DICA: É um subconjunto da disciplina de inteligência artificial (IA) que fornece aos sistemas a capacidade'
'\nde aprender e melhorar automaticamente com a experiência, sem ser explicitamente programado.',
'deep learning' : 'DICA: É uma técnica que se enquadra na disciplina de aprendizado de máquina. É baseado em redes neurais artificiais'
'\ninspiradas na estrutura do cérebro humano.',
}















































































































































geral_dificeis = [ # 56 palavras de 14 letras cada
    'imprescindivel', 'condescendente', 'caracteristica','idiossincrasia', 'extraordinario', 'concupiscencia', 'demasiadamente',
    'consubstanciar', 'intercorrencia', 'irrepreensivel', 'incomensuravel', 'preponderancia', 'arbitrariedade', 'especificidade',
    'discricionario', 'posteriormente', 'imprescritivel', 'empreendimento', 'intransponivel', 'revolucionario', 'contextualizar',
    'atenciosamente', 'superveniencia', 'entretenimento', 'periodicamente', 'infraestrutura', 'paulatinamente', 'transcendental', 
    'democratizaçao', 'ancestralidade', 'diligentemente', 'espontaneidade', 'insignificante', 'reconhecimento', 'arrependimento',
    'intransigencia', 'relacionamento', 'inconsistencia', 'aplicabilidade', 'imparcialidade', 'despretensioso', 'desprendimento',
    'impessoalidade', 'personificaçao', 'procrastinador', 'prestatividade', 'socioambiental', 'congratulaçoes', 'licenciosidade', 
    'exequibilidade', 'inconveniencia', 'pusilanimidade', 'transcendencia', 'excentricidade', 'insubstituivel', 'credenciamento'
]



geral_dificeis_dicionario = {
'imprescindivel': 'DICA: Que não se pode dispensar nem renunciar; que é extremamente necessário ou essencial para; indispensável, essencial.', 
'condescendente': 'DICA: Qualidade da pessoa que é incapaz de se impor, que aceita os sentimentos ou os desejos de alguém; permissivo. ', 
'caracteristica': 'DICA:O que difere uma pessoa de outra; qualidade: ',
'idiossincrasia': 'DICA: Ato ou comportamento próprio de um indivíduo ou de um grupo de pessoas.', 
'extraordinario': 'DICA:Que não se adequa ao costume geral ou ordinário; excepcional. ', 
'concupiscencia': 'DICA:Ambição ou desejo desmedido por bens materiais ou sensuais.', 
'demasiadamente': 'DICA:De maneira excessiva; em grande quantidade, excessivo, exagerado. ',
'consubstanciar': 'DICA: Efetuar a consolidação ou o fortalecimento de; consolidar. ', 
'intercorrencia': 'DICA:Ocorrer ao mesmo tempo que outra coisa. Que expressa ou denota irregularidade; mudança. ', 
'irrepreensivel': 'DICA:Que não merece censura; que não merece ser repreendido', 
'incomensuravel': 'DICA:Que não se pode nem se consegue medir; cuja medida não pode ser comparada ', 
'preponderancia': 'DICA:Circunstância, particularidade ou comportamento do que prevalece. ', 
'arbitrariedade': 'DICA: Ação em que há uso abusivo de autoridade; violência ou despotismo.', 
'especificidade': 'DICA:Característica particular de uma espécie; categorização de uma espécie',
'discricionario': 'DICA: Que dependente da decisão de uma autoridade competente.', 
'posteriormente': 'DICA: De modo que vem depois. Que está situado ou acontece depois. ', 
'imprescritivel': 'DICA:Que não fica sem efeito; que não pode caducar. ', 'empreendimento': 'DICA:Ação de quem toma para si uma responsabilidade. ', 
'intransponivel': 'DICA:Que não se pode transpor, ir além de; intransitável. ', 
'revolucionario': 'DICA:Definido pela criatividade, originalidade, ousadia; capaz de ocasionar mudanças em normas preestabelecidas; inovador. ', 
'contextualizar': 'DICA:Mostrar as circunstâncias que estão ao redor de um fato, acontecimento, situação. ',
'atenciosamente': 'DICA: Delicadamente; em que há atenção ou gentileza', 
'superveniencia': 'DICA: Ação de sobrevir, de ocorrer após um outro evento', 
'entretenimento': 'DICA:Aquilo que é feito como diversão, distração; divertimento. ', 
'periodicamente': 'DICA: Que ocorre de períodos em períodos; com regularidade nos espaços de tempo ', 
'infraestrutura': 'DICA:Base; que assegura o desenvolvimento ou a criação de certo grupo, organização, sociedade, teoria, ideologia. ', 
'paulatinamente': 'DICA: De modo lento; em que há lentidão ', 
'transcendental': 'DICA:Que pertence à razão pura, a priori, anteriormente a qualquer experiência, e que constitui uma condição prévia dessa experiência. ', 
'democratizaçao': 'DICA: Ato de tornar acessível a todas as pessoas e classes; popularização', 
'ancestralidade': 'DICA:O que se recebeu das gerações anteriores; hereditariedade. ', 
'diligentemente': 'DICA:Que age prontamente; que expressa rapidez, prontidão ', 
'espontaneidade': 'DICA: Característica ou particularidade do que é desprovido de afetação; em que há simplicidade e originalidade; naturalidade. ', 
'insignificante': 'DICA:Que não possui valor; sem importância; desprezível. ', 
'reconhecimento': 'DICA: Admitir como verdadeiro, lembrança de um benefício, gratidão por ele.', 
'arrependimento': 'DICA: emorso ou mágoa por se ter cometido um mal; contrição ',
'intransigencia': 'DICA: Que expressa rigidez ou intolerância; severidade ou rigor. ', 
'relacionamento': 'DICA: Ato de estabelecer uma ligação, uma conexão com algo ou alguém.', 
'inconsistencia': 'DICA: Falta de lógica, de firmeza.', 
'aplicabilidade': 'DICA: Qualidade do que ocasiona um efeito; característica do que se consegue aplicar, empregar, colocar em prática.', 
'imparcialidade': 'DICA: Equidade; qualidade da pessoa que julga com neutralidade e justiça; característica de quem não toma partido numa situação.', 
'despretensioso': 'DICA: Modesto ou simples; sem afetação.', 
'desprendimento': 'DICA: Comportamento ou característica de abnegado; qualidade da pessoa que não tem interesse por dinheiro; altruísmo ou desapego ',
'impessoalidade': 'DICA: Qualidade do que é geral, do que não diz repeito a alguém em específico', 
'personificaçao': 'DICA: Pessoa que interpreta ou representa de modo perfeito uma ideia ou alguma coisa de teor abstrato. ', 
'procrastinador': 'DICA: Aquele que vive adiando, deixando seus afazeres para um outro momento ou para depois.', 
'prestatividade': 'DICA: Solicitude; característica da pessoa solícita; qualidade de quem se oferece para ajudar ou presta auxílio ', 
'socioambiental': 'DICA: Refere-se aos problemas e processos sociais, tendo em conta sua relação com o meio ambiente.', 
'congratulaçoes': 'DICA: Dirigir cumprimentos, através de palavras, a alguém pela conquista de alguma coisa.', 
'licenciosidade': 'DICA: Característica de quem age indisciplinada e desregradamente.', 
'exequibilidade': 'DICA: Característica do que é exequível, possível, realizável ou executável.', 
'inconveniencia': 'DICA: Comportamento de quem é indelicado, incivil, indiscreto e grosseiro.', 
'pusilanimidade': 'DICA: Qualidade, particularidade ou condição do que é pusilânime; qualidade da pessoa covarde; covardia ou frouxidão.', 
'transcendencia': 'DICA: Qualidade do que ultrapassa os limites do considerado normal ou aceitável.', 
'excentricidade': 'DICA: Comportamento que se difere do considerado normal; originalidade, anormalidade, extravagância, irregularidade.', 
'insubstituivel': 'DICA: Qualidade de quem é excepcional, incomparável ou superior.', 
'credenciamento': 'DICA: Concessão de procuração para representar algo ou alguém em procedimentos burocráticos. '
}
