#!/usr/bin/env bash
set -euo pipefail

PROJECT="${PROJECT:-delta-entry-496910-e7}"
REGION="${REGION:-asia-east1}"
SERVICE="${SERVICE:-glm-proxy}"
GLM_BASE_URL="${GLM_BASE_URL:-https://www.tokenrouter.tech/v1}"
GLM_MODEL="${GLM_MODEL:-glm-5.2}"
GLM_ALLOWED_MODELS="${GLM_ALLOWED_MODELS:-${GLM_MODEL}}"
MAX_OUTPUT_TOKENS="${MAX_OUTPUT_TOKENS:-16384}"
ALLOW_ORIGIN="${ALLOW_ORIGIN:-*}"
GLM_API_KEY="${GLM_API_KEY:-${TOKENROUTER_API_KEY:-}}"

if [[ -z "$GLM_API_KEY" ]]; then
  echo "GLM_API_KEY or TOKENROUTER_API_KEY is required." >&2
  exit 1
fi

ENV_VARS="GLM_BASE_URL=${GLM_BASE_URL},GLM_MODEL=${GLM_MODEL},GLM_ALLOWED_MODELS=${GLM_ALLOWED_MODELS},MAX_OUTPUT_TOKENS=${MAX_OUTPUT_TOKENS},ALLOW_ORIGIN=${ALLOW_ORIGIN},GLM_API_KEY=${GLM_API_KEY}"
echo "Project: $PROJECT  Region: $REGION  Service: $SERVICE  Model: $GLM_MODEL"

gcloud run deploy "$SERVICE" \
  --source . \
  --project "$PROJECT" \
  --region "$REGION" \
  --allow-unauthenticated \
  --set-env-vars "$ENV_VARS"

echo
echo "GLM proxy URL:"
gcloud run services describe "$SERVICE" --project "$PROJECT" --region "$REGION" --format='value(status.url)'
