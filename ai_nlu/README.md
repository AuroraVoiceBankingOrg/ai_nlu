# ai_nlu

This repository focuses on Natural Language Understanding (NLU) and Large Language Model (LLM) integration. It handles:
- Intent detection for banking and credit card operations.
- Entity extraction (e.g., account numbers, transaction details).
- Multilingual prompts (Uzbek, Russian, English) for LLM-based reasoning.
- Sentiment analysis, topic classification, confidence scoring.
- Integration with cloud NLU APIs or local NLP engines.

## Integration with Other Repos:
- **config_manager**: Provides global configs for languages, endpoints, etc.
- **asr_core**: Supplies the text output from speech, which ai_nlu interprets.
- **tts_core**: After NLU determines the response, a final answer is passed to TTS.
- **conversation_flow**: Orchestrates the NLU calls, using ai_nlu to determine user intent and entities.
- **external_integrations**: Banking or credit card APIs may inform NLU domain adaptation.
- **frontend_integrations**: NLU results flow back to frontends (mobile/desktop/web).

## What Happens Here:
1. Text input (from ASR) is processed by these NLU scripts.
2. Intent classification: identify if user wants 'check balance', 'credit card limit', etc.
3. Entity extraction: find specific details (like card number, amount).
4. LLM prompts (e.g., nlu_llm_prompt_uz.py) refine complex queries using advanced language models.
5. Sentiment and topic classification add more context.
6. Output: a structured representation (intent, entities, confidence) returned to conversation_flow.

## Directory Structure Overview:
Explore `docs/` for architecture diagrams, `tests/` for test coverage, `language_support/` for multilingual configs, `models/` for NLU model data, `integration/` for hooking up to external services, `configs/` for config files, `scripts/` for utility tools, and `notebooks/` for experimentation.

Refer to `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `LICENSE`, and `CHANGELOG.md` for project norms, license info, and changes.
