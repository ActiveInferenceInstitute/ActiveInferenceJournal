# Security

ActiveInferenceJournal is a public data repository: transcripts, metadata,
captions, translations, and curated materials. There is no application code here,
but the repository has a hard rule about credentials — see the security note in
[`docs/PIPELINE.md`](docs/PIPELINE.md).

## Rules

- **Never commit credentials.** Cookies, tokens, API keys, or session data of any
  kind must never appear in this repository. The download pipeline runs
  cookie-free by design; a historical `cookies.txt` leak in Journal-Utilities was
  purged and is a permanent cautionary note in the pipeline docs.
- **No audio on `main`.** Audio files (`*.m4a`, `*.mp3`, `*.wav`) live on the
  `audio` branch only.
- **No machine-internal paths.** Content must not embed absolute local filesystem
  paths from contributors' machines.

## Reporting

This repository is generated and validated by the
[Journal-Utilities](https://github.com/ActiveInferenceInstitute/Journal-Utilities)
pipeline. If you discover a credential, a leaked internal path, or any other
security issue:

1. Do **not** open a public issue with the material in it.
2. Report it privately via GitHub's private vulnerability reporting for this
   repository (or directly to the Active Inference Institute maintainers), and
   include the file path(s) affected.
