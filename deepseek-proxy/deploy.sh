#!/usr/bin/env bash
set -euo pipefail

PROJECT="${PROJECT:-delta-entry-496910-e7}"
REGION="${REGION:-asia-east1}"
SERVICE="${SERVICE:-deepseek-proxy}"
MODEL="${DEEPSEEK_MODEL:-deepseek-v3.2-maas}"
VERTEX_LOCATION="${VERTEX_LOCATION:-global}"
MAX_OUTPUT_TOKENS="${MAX_OUTPUT_TOKENS:-8192}"
REQUEST_TIMEOUT_SECONDS="${REQUEST_TIMEOUT_SECONDS:-600}"
MAX_INSTANCES="${MAX_INSTANCES:-1}"
ALLOW_ORIGIN="${ALLOW_ORIGIN:-*}"

echo "Project: $PROJECT  Region: $REGION  Service: $SERVICE  Model: $MODEL"
RUNTIME_SA="$(gcloud projects describe "$PROJECT" --format='value(projectNumber)')-compute@developer.gserviceaccount.com"
gcloud projects add-iam-policy-binding "$PROJECT" \
  --member="serviceAccount:${RUNTIME_SA}" \
  --role="roles/aiplatform.user" --condition=None >/dev/null || true

gcloud run deploy "$SERVICE" \
  --source . \
  --project "$PROJECT" \
  --region "$REGION" \
  --allow-unauthenticated \
  --timeout=900 \
  --concurrency=1 \
  --max-instances="$MAX_INSTANCES" \
  --set-env-vars "GCP_PROJECT=${PROJECT},DEEPSEEK_MODEL=${MODEL},VERTEX_LOCATION=${VERTEX_LOCATION},MAX_OUTPUT_TOKENS=${MAX_OUTPUT_TOKENS},REQUEST_TIMEOUT_SECONDS=${REQUEST_TIMEOUT_SECONDS},ALLOW_ORIGIN=${ALLOW_ORIGIN}"

echo
echo "DeepSeek proxy URL:"
gcloud run services describe "$SERVICE" --project "$PROJECT" --region "$REGION" --format='value(status.url)'
