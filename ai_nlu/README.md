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


Below is an example of a very detailed `README.md` that you could place at the root of the `ai_nlu` repository. It includes high-level visual flows, step-by-step descriptions, file-by-file explanations, and a clear running order, all written for someone seeing the code for the first time.

```markdown
# AI_NLU

## Overview

This repository focuses on **Natural Language Understanding (NLU)** and **Large Language Model (LLM) integration within a larger voice assistant ecosystem. The NLU logic here takes text as input (often transcribed from user speech by `asr_core`) and interprets the user’s intent, extracts relevant entities (like account numbers or transaction amounts), and adds contextual understanding, potentially with help from advanced language models (LLMs).

The final output from `ai_nlu` is a structured representation of the user’s request (intent + entities + confidence scores), which is then passed on to other parts of the system (like `conversation_flow`), and ultimately might lead to calling `external_integrations` (banking APIs, credit card operations) or formatting a response for `tts_core` to speak back to the user.

## High-Level Integration with Other Systems

**Visual Flow of the Entire Ecosystem (High Level)**:

```
          ┌─────────────────────────────────┐
          │            User Input            │
          │  (User speaks into microphone)   │
          └───────────▲─────────────────────┘
                      │
                      │ Voice
                      │
            (asr_core transcribes voice to text)
                      │
                      ▼
              ┌───────────────────────┐
              │        ai_nlu         │
              │  (This Repository)    │
              │  Interprets text:     │
              │  - Detect intent      │
              │  - Extract entities   │
              │  - Possibly query LLM │
              │  for complex reasoning│
              │  - Return structured  │
              │    representation     │
              └─────────▲────────────┘
                        │
                 Text intent/entities
                        │
                        ▼
           ┌───────────────────────────┐
           │      conversation_flow     │
           │  Orchestrates logic:       │
           │  - Checks Q&A cache        │
           │  - If needed, calls        │
           │    external_integrations   │
           │  - Assembles final answer  │
           └───────────▲──────────────┘
                       │
                 Answer text/data
                       │
                       ▼
                (tts_core generates speech)
                       │
                       ▼
           ┌───────────────────────────┐
           │        Frontend (UI)       │
           │ (mobile/desktop/web)       │
           │ receives final speech/text │
           └───────────────────────────┘
```

From this flow, you can see `ai_nlu` in the center, converting raw transcribed text into meaningful structured data.

## Detailed Flow Within the `ai_nlu` Repository

**Step-by-Step Flow Inside `ai_nlu`:**

1. **Input Text Arrival**: `ai_nlu` receives a text input (usually from `asr_core`), e.g., "What is my current account balance?".
   
2. **Preprocessing**: 
   - The system might run `utils/nlp_tools` scripts (like `tokenizer.py`, `lemmatizer.py`, `stopword_filter.py`) to clean and normalize the input text.
   - Language mappings from `language_support/lang_mapping.yaml` are checked if the request contains multiple languages (e.g., some users mixing Uzbek and English).

3. **Intent Detection**:
   - Scripts like `nlu_intent_banking.py` or `nlu_intent_credit_card.py` might classify the utterance into a domain-specific intent (e.g., "check_balance", "view_credit_card_limit").
   - If needed, `nlu_multilang_integration.py` might handle multilingual aspects, and `nlu_local_nlp_engine.py` or `nlu_cloud_nlu_api.py` might call local or cloud-based NLP services.

4. **Entity Extraction**:
   - `nlu_entity_extraction.py` identifies key entities like "account number=1234", "amount=100 USD".
   - Domain adaptation files in `integration/banking/banking_apis.yaml` help detect banking-related terms.
   - Similarly, `integration/credit_card/credit_card_scenarios.yaml` aids identifying credit card terms.

5. **LLM Prompts (If Needed)**:
   - If the request is complex, `nlu_llm_prompt_en.py` or `nlu_llm_prompt_uz.py` might generate a prompt to send to an LLM, refining the interpretation.
   - `nlu_confidence_scores.py` might help combine LLM responses with local NLP results to produce a confidence measure.

6. **Additional Analysis**:
   - `nlu_sentiment_analysis.py` or `nlu_topic_classification.py` add extra context. Sentiment could be helpful if the user is upset, and topic classification ensures correct domain handling.

7. **Output Structure**:
   - After processing, the system outputs a structured dict:
     ```json
     {
       "intent": "check_balance",
       "entities": {
         "account_number": "1234"
       },
       "confidence": 0.95,
       "language_detected": "en"
     }
     ```
   - This is returned to `conversation_flow`, which decides the next step (like calling `external_integrations` for bank info).

## Running Order and What Each File Does

**Running Order at a High Level:**
1. **Language configs load**: `language_support/lang_mapping.yaml`, `supported_languages.json` guide how text is processed.
2. **NLP tools invoke**: `utils/nlp_tools/*.py` scripts clean/prepare the text.
3. **Intent detection files run**: e.g., `nlu_intent_banking.py` tries to identify banking intents.
4. **Entity extraction**: `nlu_entity_extraction.py` extracts structured entities.
5. **LLM prompts**: If complexity is detected, files like `nlu_llm_prompt_en.py` run to refine results.
6. **Sentiment/Topic**: `nlu_sentiment_analysis.py`, `nlu_topic_classification.py` run if configured.
7. **Integration with domain-specific data**: `integration/banking/test_banking_adaptation.py` or `integration/credit_card/test_credit_card_entities.py` may run checks or load domain data.
8. **Final output assembled**: The main Python files (like `nlu_intent_banking.py`) will eventually produce the final structured output.

**Key Files and Their Roles:**

- **Top-Level Python Files (name_patterns):**  
  Each `nlu_*.py` file corresponds to a particular aspect:
  - `nlu_intent_banking.py`: Classifies intents related to banking.
  - `nlu_intent_credit_card.py`: Handles credit card-related intents.
  - `nlu_entity_extraction.py`: Extracts entities (amounts, card numbers).
  - `nlu_llm_prompt_en.py`, `nlu_llm_prompt_ru.py`, `nlu_llm_prompt_uz.py`: Specialized prompts for LLM reasoning in English/Russian/Uzbek.
  - `nlu_sentiment_analysis.py`: Determines user sentiment (positive/negative).
  - `nlu_topic_classification.py`: Classifies topic domain.
  - `nlu_cloud_nlu_api.py`, `nlu_local_nlp_engine.py`: Integrate with external NLP engines (cloud/local).
  - `nlu_multilang_integration.py`: Handle multiple languages in single utterances.
  - `nlu_banking_scenario_tests.py`, `nlu_credit_card_entities.py`: Domain-specific tests or extraction logic for banking/credit cards.
  - `nlu_confidence_scores.py`: Calculate confidence scores combining multiple sources.
  - `nlu_resource_stats.py`: Evaluate resource usage of NLU processes (e.g., memory/CPU).

- **Language Support:**
  - `language_support/lang_mapping.yaml`: Maps language codes to model/config.
  - `language_support/supported_languages.json`: Lists which languages are currently enabled.
  - `language_support/tests/test_lang_mapping.py`: Tests that language mapping is correct.

- **Models Directory (models/*):**
  - `models/en/english_nlu_model_info.txt`: Documents English NLU model (type, version).
  - `en_feature_extractor.py`: Extract features from English text.
  - Similarly for `models/ru/` and `models/uz/` for Russian and Uzbek models.
  - `models/generic/` holds generic resources (generic_model_notes.txt, generic_feature_extractor.py).

- **Integration Directories:**
  - `integration/banking/banking_apis.yaml`: Domain terms and API endpoints for banking.
  - `test_banking_adaptation.py`: Tests how well NLU adapts to banking domain.
  - `integration/credit_card/credit_card_scenarios.yaml`: Terms related to credit cards.
  - `test_credit_card_entities.py`: Tests extracting credit card details.
  - `integration/cloud_nlu/cloud_nlu_integration_tests.py`: Tests integration with external cloud NLU.
  - `integration/local_nlp/local_nlp_engine_setup.py`: Setup for local NLP engine.

- **Cache:**
  - `cache/cache_config.yaml`: Config for caching results.
  - `cache/cache_manager.py`: Manages cached NLU responses (faster repeated queries).

- **Samples and Domain Adaptation:**
  - `samples/multilingual/multi_lang_samples.json`: Multilingual sample inputs.
  - `samples/domain_adapt/banking_adapt_samples.txt`: Banking-specific text samples.
  - `samples/domain_adapt/credit_card_adapt_samples.txt`: Credit card-specific samples.

- **Scripts:**
  - `scripts/run_nlu_pipeline.sh`: Runs a full pipeline test (from input text to final NLU output).
  - `scripts/evaluate_nlu_quality.py`: Evaluate quality (accuracy, WER-like metrics).
  - `scripts/convert_lexicon.py`: Convert domain lexicons into model-friendly formats.

- **Configs:**
  - `configs/tts_config.yaml`: Might store general NLP/LLM config keys, or be adapted for NLU.
  - `configs/default_settings.json`: Generic default settings.
  - `configs/env/dev_env.yaml`, `configs/env/prod_env.yaml`: Different environment setups.
  - `configs/templates/template_config.yaml`: A template for generating final configs.
  - `template_vars.json`: Variables for template expansion.

- **Notebooks:**
  - `notebooks/nlu_research.ipynb`: Experiment with new NLU techniques or prompts.
  - `notebooks/data_insight_analysis.ipynb`: Analyze dataset distributions, performance on various domains.

- **Utils:**
  - `utils/readme_utils.md`: Documentation about utils folder.
  - `utils_init.py`: Might initialize utils as a package.
  - `utils/logging/log_config.yaml`, `log_formatter.py`: Logging config and formatters.
  - `utils/nlp_tools/tokenizer.py`, `lemmatizer.py`, `stopword_filter.py`, `synonym_expander.py`: NLP preprocessing tools.
  - `utils/prompts/prompt_template_en.yaml`, `prompt_merger.py`: Manage prompt templates for LLM queries.

- **Test Env:**
  - `test_env/simulated_inputs/mock_user_queries.txt`: Mock queries simulating real user input.
  - `test_env/simulated_inputs/simulate_input_stream.sh`: Simulate continuous input stream.
  - `test_env/scenario_data/complex_scenarios.json`: Complex scenario sets.
  - `test_env/scenario_data/scenario_runner.py`: Run scenarios to ensure pipeline robustness.

## Running the System

1. **Installation**:  
   ```bash
   cd ai_nlu
   pip install -r requirements.txt
   ```

2. **Basic Test**:  
   ```bash
   make test
   ```  
   Runs tests in `tests/` to ensure everything is working.

3. **Run Pipeline Manually**:  
   - Use `scripts/run_nlu_pipeline.sh` to simulate running an input through NLU pipeline.
   - Adjust configs in `configs/` if needed (e.g., `dev_env.yaml` vs `prod_env.yaml`).

4. **Integration in Full System**:
   - Normally, `ai_nlu` is invoked by `conversation_flow`. When `conversation_flow` receives text from `asr_core`, it calls these NLU files (e.g., `nlu_intent_banking.py`) to interpret user requests.
   - If needed, `nlu_llm_prompt_en.py` interacts with an LLM (if configured) to refine interpretations.
   - The final structured result is returned upstream.

## Conclusion

This `ai_nlu` repository provides all necessary building blocks to understand user queries, extract detailed information, handle multiple languages, integrate domain knowledge, and interact with advanced language models.