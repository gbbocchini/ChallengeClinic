
# Soluçao para o challenge proposto em https://github.com/iclinic/weather-mini-challenge


## Implementaçao:
Serverless (AWS Lambda, AWS S3, AWS API Gateway, AWS CloudWatch, AWS CloudFormation) utilizando Zappa (https://www.zappa.io/) e Django.


## Execuçao local
- Clone este repositorio (`git clone` ...);
- Crie um Virtual Env em Python (`python3 -m venv venv`) e ative-o (`source venv/bin/activate`);
- Instale os requisitos necessarios para o projeto (`pip install -r requirements.txt`);
- Necessario chave (gratuita) para API a ser consumida (https://openweathermap.org/api);
- Dentro do folder clonado: `python manage.py runserver`
- Pronto!


##Deploy
Um versão pode ser encontrada em: https://bm58oqe17c.execute-api.us-east-1.amazonaws.com/dev

##Testes
Os testes podem ser rodados com `python manage.py test` do folder clonado. Este repo esta integrado com TravisCI.