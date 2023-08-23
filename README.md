Genera Classi
======
### Architettura
![immagine](https://github.com/lucadigangi/generateClass/assets/57185672/e3d42917-1240-45e6-b62a-2480b625109f)
L'architettura è organizzata come segue:
<ul>
<li>Amazon Cognito: Configura Amazon Cognito per gestire l'autenticazione degli utenti. Cognito ti consente di creare pool di utenti, autenticare utenti tramite diverse opzioni (ad esempio, username/password, social login, ecc.) e assegnare ruoli e autorizzazioni ai tuoi utenti.</li>

<li>API Gateway: Puoi integrare l'API Gateway con Amazon Cognito per verificare le richieste provenienti dal frontend del tuo sito. Questo può assicurare che solo gli utenti autenticati e autorizzati possano accedere all'endpoint dell'API Gateway.</li> 

<li>Lambda Functions: Le Lambda functions possono rimanere pressoché invariate, ma puoi configurare l'API Gateway in modo che richieda un token di accesso valido generato da Cognito nelle richieste. In questo modo, solo gli utenti autenticati possono invocare le Lambda functions.</li> 

<li>S3 Bucket e Sito Web: Puoi configurare l'autenticazione anche per l'accesso ai file nell'S3 bucket che ospita il sito web. Amazon Cognito può essere configurato per fornire temporanei URL di accesso ai file S3 solo agli utenti autenticati.</li> 
</ul>

### Utilizzo
Per accedere all'applicativo è necessario essere in possesso delle credenziali
Una volta effettuato l'accesso si carica il file in formato csv e si attiva il trigger con l'apposito button
si otterranno in output le classi suddivise
