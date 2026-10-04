# Configuration Documentation - Validação de variáveis ambiente

## Version
É a versão do projeto, e não a do openTelemetry. Estamos dizendo: `Este arquivo segue a versão 1 do padrão de configuração que eu estou escolhendo`

## Variables
É simplesmente o começo da lista de variáveis. Tudo abaixo disso representa uma variável que você quer padronizar, É como dizeer: `As configurações do meu padrão estão aqui.`

## Otel Service Name
Essa variável identifica qual é o serviço /aplicação que está enviando a telemetria.

## Otel Service Version
Representa a versão da aplicação. Isso é util para observar uma aplicação durante mudanças de versão, podemos relacionar problemas de obersavilidade com uma versão específica.

## Otel Traces Exporter
Define para onde/como os tracesserão exportados. 

## Otel Logs Exporter
Variável define o exporter utilizado para os logs.

## Otel Exporter OTLP Endpoint
Essa é uma das mais importantes! Ela diz: `Para onde eu devo enviar minha telemetria VIA OTLP?` Por exemplo: 
```
OTEL_EXPORTER_OTLP_ENDPOINT=http:///otel-collector:4317
``` 
Ou dependendo da arquitetura:
```
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

E uma coisa importante: `No é necessáriamente é o endereço do tempo!` Se possuirmos:
```
Aplicação
    |
   OTLP
    |
Alloy / OpenTelemetry
    |
  Tempo
```
Então o endpoint da aplicação é o `Alloy / OpenTelemetry Collector`

## Otel Exporter OTLP Protocol
Define o protocolo usado para enviar OTLP. Isso significa que o padrão que estamos estabelecendo é `OTLP via gRPC`. Também existe OTLP via HTTP, dependendo do cenário, então podemos ter:
```
OTEL_EXPORTER_OTLP_PROTOCOL=grpc
```
Ou
```
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
```