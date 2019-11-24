[![Build Status](https://travis-ci.org/gbbocchini/ChallengeClinic.svg?branch=master)](https://travis-ci.org/gbbocchini/ChallengeClinic)


# Soluçao para o challenge proposto em https://github.com/iclinic/weather-mini-challenge


## Implementaçao:
Serverless (AWS Lambda, AWS S3, AWS API Gateway, AWS CloudWatch, AWS CloudFormation) utilizando Django e Zappa (https://www.zappa.io/).


## Estrutura do Projeto
- Nome Projeto: iclinic (na pasta `iclinic/iclinic` encontram-se todos os setting e configuraçoes Django);
- App Core (`iclinic/core`): app do projeto;
- `iclinic/core/repository`: contem classe `ApiHandler` (toda a interaçao com a API e feita somente por essa classe e seus metodos);
- `iclinic/data_processor`: contem classe `Processor` responsavel por todo o processamento/transformaçao dos dados obtidos via `ApiHandler`;
- `iclinic/views`: responsavel pela renderizaçao do template `templates/home.html` com as infos processadas via metodos de `Processor`

## Execuçao local
- Clone este repositorio (`git clone` ...);
- Crie um Virtual Env em Python (`python3 -m venv venv`) e ative-o (`source venv/bin/activate`);
- Instale os requisitos necessarios para o projeto (`pip install -r requirements.txt`);
- Necessario chave (gratuita) para API a ser consumida (https://openweathermap.org/api);
- Dentro do folder clonado: `python manage.py runserver`
- Pronto!


## Deploy
Um versão pode ser encontrada em: https://bm58oqe17c.execute-api.us-east-1.amazonaws.com/dev

## Testes
Os testes podem ser rodados com `python manage.py test` do folder clonado. Este repo esta integrado com TravisCI.