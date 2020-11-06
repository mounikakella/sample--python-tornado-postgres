{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "todo-list-api.name" }}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this
(by the DNS naming spec).
*/}}
{{- define "todo-list-api.fullname" }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Calculate api certificate
*/}}
{{- define "todo-list-api.api-certificate" }}
{{- if (not (empty .Values.ingress.api.certificate)) }}
{{- printf .Values.ingress.api.certificate }}
{{- else }}
{{- printf "%s-api-letsencrypt" (include "todo-list-api.fullname" .) }}
{{- end }}
{{- end }}

{{/*
Calculate api hostname
*/}}
{{- define "todo-list-api.api-hostname" }}
{{- if (and .Values.config.api.hostname (not (empty .Values.config.api.hostname))) }}
{{- printf .Values.config.api.hostname }}
{{- else }}
{{- if .Values.ingress.api.enabled }}
{{- printf .Values.ingress.api.hostname }}
{{- else }}
{{- printf "%s-api" (include "todo-list-api.fullname" .) }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Calculate api base url
*/}}
{{- define "todo-list-api.api-base-url" }}
{{- if (and .Values.config.api.baseUrl (not (empty .Values.config.api.baseUrl))) }}
{{- printf .Values.config.api.baseUrl }}
{{- else }}
{{- if .Values.ingress.api.enabled }}
{{- $hostname := ((empty (include "todo-list-api.api-hostname" .)) | ternary .Values.ingress.api.hostname (include "todo-list-api.api-hostname" .)) }}
{{- $protocol := (.Values.ingress.api.tls | ternary "https" "http") }}
{{- printf "%s://%s" $protocol $hostname }}
{{- else }}
{{- printf "http://%s" (include "todo-list-api.api-hostname" .) }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Calculate postgres url
*/}}
{{- define "todo-list-api.postgres-url" }}
{{- $postgres := .Values.config.postgres }}
{{- if $postgres.url }}
{{- printf $postgres.url }}
{{- else }}
{{- $credentials := ((or (empty $postgres.username) (empty $postgres.password)) | ternary "" (printf "%s:%s@" $postgres.username $postgres.password)) }}
{{- printf "postgresql://%s%s:%s/%s" $credentials $postgres.host $postgres.port $postgres.database }}
{{- end }}
{{- end }}
