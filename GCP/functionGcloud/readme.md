https://dev.to/googlecloud/using-secrets-in-google-cloud-functions-5aem


Criar o secret 

echo -n "The chickens are in the hayloft." | \
    gcloud secrets create my-secret \
      --data-file=- \
      --replication-policy automatic



Ver o secret
gcloud secrets versions access 1 --secret="my-secret"




Aplicando permissoes
gcloud secrets add-iam-policy-binding my-secret \
    --role roles/secretmanager.secretAccessor \
    --member serviceAccount:PROJECT_ID@appspot.gserviceaccount.com


Essa ainda não testei
gcloud secrets add-iam-policy-binding my-secret \
    --role roles/secretmanager.admin \
    --member serviceAccount:PROJECT_ID@appspot.gserviceaccount.com




deploy function

 gcloud functions deploy secret_hello \
    --entry-point=secret_hello \
    --source=. \
    --runtime python38 \
    --allow-unauthenticated \
    --trigger-http


    chamando a função

gcloud functions call secret_hello




usando pub/sub como trigger

gcloud functions deploy YOUR_FUNCTION_NAME \
--trigger-event=providers/cloud.pubsub/eventTypes/topic.publish \
--trigger-resource=YOUR_PUBSUB_TOPIC \
...

########################################################


Rodar function de um repositório
https://cloud.google.com/functions/docs/create-deploy-gcloud#functions-clone-sample-repository-python








gcloud auth application-default login