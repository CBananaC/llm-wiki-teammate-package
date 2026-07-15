#!/usr/bin/env bash
# Deploy the standalone TokenRouter ChatGPT proxy to Cloud Run.
set -euo pipefail

PROJECT="${PROJECT:-delta-entry-496910-e7}"
REGION="${REGION:-asia-east1}"
SERVICE="${SERVICE:-chatgpt-proxy}"
BASE_URL="${TOKENROUTER_BASE_URL:-https://www.tokenrouter.tech/v1}"
MODEL="${TOKENROUTER_DEFAULT_MODEL:-gpt-5.4}"
ALLOWED_MODELS="${TOKENROUTER_ALLOWED_MODELS:-gpt-5.4}"
MAX_OUTPUT_TOKENS="${MAX_OUTPUT_TOKENS:-16384}"
ALLOW_ORIGIN="${ALLOW_ORIGIN:-*}"
REQUEST_TIMEOUT_SECONDS="${REQUEST_TIMEOUT_SECONDS:-290}"

if [[ -z "${TOKENROUTER_API_KEY:-}" ]]; then
  echo "TOKENROUTER_API_KEY is required. Export it before deployment." >&2
  exit 1
fi

echo "Project: $PROJECT  Region: $REGION  Service: $SERVICE  Model: $MODEL"

# The key is supplied from the caller's environment and is not stored in this
# repository. For production, prefer replacing this env var with a Secret
# Manager binding on the deployed service.
ENV_VARS="TOKENROUTER_BASE_URL=${BASE_URL},TOKENROUTER_DEFAULT_MODEL=${MODEL},TOKENROUTER_ALLOWED_MODELS=${ALLOWED_MODELS},MAX_OUTPUT_TOKENS=${MAX_OUTPUT_TOKENS},ALLOW_ORIGIN=${ALLOW_ORIGIN},REQUEST_TIMEOUT_SECONDS=${REQUEST_TIMEOUT_SECONDS},TOKENROUTER_API_KEY=${TOKENROUTER_API_KEY}"

gcloud run deploy "$SERVICE" \
  --source . \
  --project "$PROJECT" \
  --region "$REGION" \
  --allow-unauthenticated \
  --timeout 300 \
  --min-instances 1 \
  --set-env-vars "$ENV_VARS"

echo
echo "Done. Service URL:"
gcloud run services describe "$SERVICE" \
  --project "$PROJECT" \
  --region "$REGION" \
  --format='value(status.url)'
