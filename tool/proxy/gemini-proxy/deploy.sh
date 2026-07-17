#!/usr/bin/env bash
# Deploy the multi-provider AI proxy to Cloud Run. Run from this folder: bash deploy.sh
set -euo pipefail

PROJECT="${PROJECT:-delta-entry-496910-e7}"
REGION="${REGION:-asia-east1}"
SERVICE="${SERVICE:-gemini-proxy}"
MODEL="${MODEL:-deepseek-v3.2-maas}"
# Vertex location for the model. "global" matches the existing summarization script.
VERTEX_LOCATION="${VERTEX_LOCATION:-global}"
# Lock this down to your own origin if you serve the page from a known URL.
# For a local file:// page the browser sends Origin: null, so "*" is simplest.
ALLOW_ORIGIN="${ALLOW_ORIGIN:-*}"
# Max length of each AI answer (tokens). Raise if responses get cut off.
MAX_OUTPUT_TOKENS="${MAX_OUTPUT_TOKENS:-16384}"
# TokenRouter is an OpenAI-compatible ChatGPT route. Keep its credential in the
# shell environment or Secret Manager; never put the key in this script.
TOKENROUTER_BASE_URL="${TOKENROUTER_BASE_URL:-https://www.tokenrouter.tech/v1}"
TOKENROUTER_DEFAULT_MODEL="${TOKENROUTER_DEFAULT_MODEL:-gpt-5.4}"
TOKENROUTER_ALLOWED_MODELS="${TOKENROUTER_ALLOWED_MODELS:-gpt-5.4}"
TOKENROUTER_TOKEN_FIELD="${TOKENROUTER_TOKEN_FIELD:-max_tokens}"
TOKENROUTER_JSON_MODE="${TOKENROUTER_JSON_MODE:-json_object}"

echo "Project: $PROJECT  Region: $REGION  Service: $SERVICE  Model: $MODEL  MaxTokens: $MAX_OUTPUT_TOKENS"
if [[ -n "${TOKENROUTER_API_KEY:-}" ]]; then
  echo "TokenRouter: configured ($TOKENROUTER_DEFAULT_MODEL via $TOKENROUTER_BASE_URL)"
else
  echo "TokenRouter: no key supplied; set TOKENROUTER_API_KEY before deployment or enter it in the browser session"
fi

# The runtime service account needs Vertex AI access.
RUNTIME_SA="$(gcloud projects describe "$PROJECT" --format='value(projectNumber)')-compute@developer.gserviceaccount.com"
gcloud projects add-iam-policy-binding "$PROJECT" \
  --member="serviceAccount:${RUNTIME_SA}" \
  --role="roles/aiplatform.user" --condition=None >/dev/null || true

ENV_VARS="GCP_PROJECT=${PROJECT},MODEL=${MODEL},VERTEX_LOCATION=${VERTEX_LOCATION},ALLOW_ORIGIN=${ALLOW_ORIGIN},MAX_OUTPUT_TOKENS=${MAX_OUTPUT_TOKENS},TOKENROUTER_BASE_URL=${TOKENROUTER_BASE_URL},TOKENROUTER_DEFAULT_MODEL=${TOKENROUTER_DEFAULT_MODEL},TOKENROUTER_ALLOWED_MODELS=${TOKENROUTER_ALLOWED_MODELS},TOKENROUTER_TOKEN_FIELD=${TOKENROUTER_TOKEN_FIELD},TOKENROUTER_JSON_MODE=${TOKENROUTER_JSON_MODE}"
if [[ -n "${TOKENROUTER_API_KEY:-}" ]]; then
  ENV_VARS="${ENV_VARS},TOKENROUTER_API_KEY=${TOKENROUTER_API_KEY}"
fi

gcloud run deploy "$SERVICE" \
  --source . \
  --project "$PROJECT" \
  --region "$REGION" \
  --allow-unauthenticated \
  --set-env-vars "$ENV_VARS"

echo
echo "Done. Service URL:"
gcloud run services describe "$SERVICE" --project "$PROJECT" --region "$REGION" --format='value(status.url)'
echo "Paste that URL (it ends without a slash) into the timeline panel's AI settings."
