# Methods

An item directory contains canonical metadata and may carry transcripts, captions, translations, or curated assets. Diarized transcript segments keep machine speaker labels and timestamps. Human name mappings live in the part metadata; the reader-facing transcript is a derived text view. Original captions and translated subtitles have separate directory roles [@schema]. Media audio has a separate branch policy.

The ingestion pathway links the data repository and Journal-Utilities. Record generation and metadata enrichment feed the index and integrity checks rather than treating the human README files as primary data [@pipeline]. The identity schema defines stable item and part records for consumers [@identity].
