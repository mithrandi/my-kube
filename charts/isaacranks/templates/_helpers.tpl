{{/* vim: set filetype=mustache: */}}
{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
*/}}
{{- define "isaacranks.fullname" -}}
{{- printf "%s-%s" .Release.Name "isaacranks" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "isaacranks.web" -}}
{{- printf "%s-%s" .Release.Name "web" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "isaacranks.rebuild" -}}
{{- printf "%s-%s" .Release.Name "rebuild" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Environment variables shared between the app and the ranks rebuilder.
*/}}
{{- define "isaacranks.env" -}}
- name: PGHOST
  value: {{ required "Must provide DB hostname" .Values.db.hostname | quote }}
- name: PGPORT
  value: {{ .Values.db.port | quote }}
- name: PGUSER
  valueFrom:
    secretKeyRef:
      name: {{ .Values.db.secretName | quote }}
      key: username
- name: PGPASS
  valueFrom:
     secretKeyRef:
       name: {{ .Values.db.secretName | quote }}
       key: password
- name: PGDATABASE
  value: {{ .Values.db.database | quote }}
- name: BALLOT_MASKING_KEY
  valueFrom:
    secretKeyRef:
      name: {{ template "isaacranks.fullname" . }}
      key: ballot-key
{{- end -}}
