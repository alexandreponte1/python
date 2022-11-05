export GOOGLE_APPLICATION_CREDENTIALS=/path/of/your/key/Downloads/key.json

https://cloud.google.com/secret-manager/docs/creating-and-accessing-secrets?hl=pt-br
https://cloud.google.com/secret-manager/docs/creating-and-accessing-secrets?hl=pt-br



https://cloud.google.com/secret-manager/docs/creating-and-accessing-secrets?hl=pt-br 

curl "https://secretmanager.googleapis.com/v1/projects/active-chimera-359118/secrets?secretId=criadoviaapi" \
    --request "POST" \
    --header "authorization: Bearer $(gcloud auth print-access-token)" \
    --header "content-type: application/json" \
    --data "{\"replication\": {\"automatic\": {}}}"




curl "https://secretmanager.googleapis.com/v1/projects/active-chimera-359118/secrets/criadoviaapi:addVersion" \
    --request "POST" \
    --header "authorization: Bearer $(gcloud auth print-access-token)" \
    --header "content-type: application/json" \
    --data "{\"payload\": {\"data\": \"criadoviaapicriadoviaapi\"}}"


curl "https://secretmanager.googleapis.com/v1/projects/active-chimera-359118/secrets/criadoviaapi:addVersion" \
    --request "POST" \
    --header "authorization: Bearer $(gcloud auth print-access-token)" \
    --header "content-type: application/json" \
    --data "{\"payload\": {\"data\": \"${SECRET_DATA}\"}}"
