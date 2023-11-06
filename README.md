Genera Classi
======
### Architettura
![Architettura](https://github.com/lucadigangi/generateClass/assets/57185672/c2317183-f790-49c8-8fd8-90407bdb91eb)
L'architettura è organizzata come segue:
<ul>
<li>Lambda Function: Le Lambda functions possono rimanere pressoché invariate, ma puoi configurare l'API Gateway in modo che richieda un token di accesso valido generato da Cognito nelle richieste. In questo modo, solo gli utenti autenticati possono invocare le Lambda functions.</li> 

<li>S3 Bucket e Sito Web: Puoi configurare l'autenticazione anche per l'accesso ai file nell'S3 bucket che ospita il sito web. Amazon Cognito può essere configurato per fornire temporanei URL di accesso ai file S3 solo agli utenti autenticati.</li> 
</ul>

<li>Amazon CloudWatch
  
</li>

<li>Amazon DynamoDB
  
</li>

### Utilizzo
Una volta caricato il file in formato csv e si attiva il trigger con l'apposito button e 
si otterranno in output le classi suddivise
