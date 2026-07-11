#!/usr/bin/env bash
# Deploy the Gemini proxy to Cloud Run. Run from this folder: bash deploy.sh
set -euo pipefail

PROJECT="${PROJECT:-delta-entry-496910-e7}"
REGION="${REGION:-asia-east1}"
SERVICE="${SERVICE:-gemini-proxy}"
MODEL="${MODEL:-gemini-2.5-flash}"
# Vertex location for the model. "global" matches the existing summarization script.
VERTEX_LOCATION="${VERTEX_LOCATION:-global}"
# Lock this down to your own origin if you serve the page from a known URL.
# For a local file:// page the browser sends Origin: null, so "*" is simplest.
ALLOW_ORIGIN="${ALLOW_ORIGIN:-*}"
# Max length of each AI answer (tokens). Raise if responses get cut off.
MAX_OUTPUT_TOKENS="${MAX_OUTPUT_TOKENS:-16384}"

echo "Project: $PROJECT  Region: $REGION  Service: $SERVICE  Model: $MODEL  MaxTokens: $MAX_OUTPUT_TOKENS"

# The runtime service account needs Vertex AI access.
RUNTIME_SA="$(gcloud projects describe "$PROJECT" --format='value(projectNumber)')-compute@developer.gserviceaccount.com"
gcloud projects add-iam-policy-binding "$PROJECT" \
  --member="serviceAccount:${RUNTIME_SA}" \
  --role="roles/aiplatform.user" --condition=None >/dev/null || true

gcloud run deploy "$SERVICE" \
  --source . \
  --project "$PROJECT" \
  --region "$REGION" \
  --allow-unauthenticated \
  --set-env-vars "GCP_PROJECT=${PROJECT},GEMINI_MODEL=${MODEL},VERTEX_LOCATION=${VERTEX_LOCATION},ALLOW_ORIGIN=${ALLOW_ORIGIN},MAX_OUTPUT_TOKENS=${MAX_OUTPUT_TOKENS}"

echo
echo "Done. Service URL:"
gcloud run services describe "$SERVICE" --project "$PROJECT" --region "$REGION" --format='value(status.url)'
echo "Paste that URL (it ends without a slash) into the timeline panel's Gemini settings."
