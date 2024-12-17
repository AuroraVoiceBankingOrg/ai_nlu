import os
import shutil

repo_name = "ai_nlu"

# If repo exists, remove it for a fresh start
if os.path.exists(repo_name):
    shutil.rmtree(repo_name)

os.makedirs(repo_name)
print(f"Created repository directory: {repo_name}")

# Main Python files from name_patterns (as indicated by the user)
# These represent core functionalities (e.g., intent detection, entity extraction, LLM prompts)
name_patterns = [
    "nlu_intent_banking",
    "nlu_intent_credit_card",
    "nlu_entity_extraction",
    "nlu_llm_prompt_uz",
    "nlu_llm_prompt_ru",
    "nlu_llm_prompt_en",
    "nlu_sentiment_analysis",
    "nlu_topic_classification",
    "nlu_cloud_nlu_api",
    "nlu_local_nlp_engine",
    "nlu_multilang_integration",
    "nlu_banking_scenario_tests",
    "nlu_credit_card_entities",
    "nlu_confidence_scores",
    "nlu_resource_stats"
]

# Top-level support files
top_level_files = {
    "README.md": [
        "# ai_nlu",
        "",
        "This repository focuses on Natural Language Understanding (NLU) and Large Language Model (LLM) integration. It handles:",
        "- Intent detection for banking and credit card operations.",
        "- Entity extraction (e.g., account numbers, transaction details).",
        "- Multilingual prompts (Uzbek, Russian, English) for LLM-based reasoning.",
        "- Sentiment analysis, topic classification, confidence scoring.",
        "- Integration with cloud NLU APIs or local NLP engines.",
        "",
        "## Integration with Other Repos:",
        "- **config_manager**: Provides global configs for languages, endpoints, etc.",
        "- **asr_core**: Supplies the text output from speech, which ai_nlu interprets.",
        "- **tts_core**: After NLU determines the response, a final answer is passed to TTS.",
        "- **conversation_flow**: Orchestrates the NLU calls, using ai_nlu to determine user intent and entities.",
        "- **external_integrations**: Banking or credit card APIs may inform NLU domain adaptation.",
        "- **frontend_integrations**: NLU results flow back to frontends (mobile/desktop/web).",
        "",
        "## What Happens Here:",
        "1. Text input (from ASR) is processed by these NLU scripts.",
        "2. Intent classification: identify if user wants 'check balance', 'credit card limit', etc.",
        "3. Entity extraction: find specific details (like card number, amount).",
        "4. LLM prompts (e.g., nlu_llm_prompt_uz.py) refine complex queries using advanced language models.",
        "5. Sentiment and topic classification add more context.",
        "6. Output: a structured representation (intent, entities, confidence) returned to conversation_flow.",
        "",
        "## Directory Structure Overview:",
        "Explore `docs/` for architecture diagrams, `tests/` for test coverage, `language_support/` for multilingual configs, `models/` for NLU model data, `integration/` for hooking up to external services, `configs/` for config files, `scripts/` for utility tools, and `notebooks/` for experimentation.",
        "",
        "Refer to `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `LICENSE`, and `CHANGELOG.md` for project norms, license info, and changes."
    ],
    "LICENSE": [
        "MIT License",
        "Permission is hereby granted ... (license text)"
    ],
    "CONTRIBUTING.md": [
        "# Contributing",
        "Guidelines on how to contribute to this ai_nlu project."
    ],
    "CHANGELOG.md": [
        "# Changelog",
        "## [Unreleased]",
        "- Initial NLU structure, multilingual prompts, banking integrations."
    ],
    "CODE_OF_CONDUCT.md": [
        "# Code of Conduct",
        "Rules and guidelines for participant behavior."
    ],
    "CITATION.cff": [
        "cff-version: 1.2.0",
        "message: If you use this software, please cite it.",
        "authors:",
        "  - family-names: Doe",
        "    given-names: Jane"
    ],
    "requirements.txt": [
        "numpy",
        "scipy",
        "transformers",
        "spacy",
        "requests",
        "torch"
    ],
    "pyproject.toml": [
        "[build-system]",
        "requires = [\"setuptools\", \"wheel\"]",
        "build-backend = \"setuptools.build_meta\"",
        "",
        "[project]",
        "name = \"ai_nlu\"",
        "version = \"0.1.0\"",
        "description = \"NLU core functionalities\"",
        "dependencies = [\"numpy\", \"spacy\", \"transformers\"]"
    ],
    "Makefile": [
        "# Makefile for building, testing, and linting ai_nlu",
        "install:",
        "\tpip install -r requirements.txt",
        "test:",
        "\tpytest tests",
        "lint:",
        "\tflake8 ."
    ]
}

subdirs = [
    "docs",
    "docs/architecture",
    "docs/api",
    "docs/user_guides",
    "docs/user_stories",
    "docs/security",
    "tests",
    "tests/unit",
    "tests/integration",
    "tests/performance",
    "tests/security",
    "tests/end_to_end",
    "language_support",
    "language_support/tests",
    "models",
    "models/en",
    "models/ru",
    "models/uz",
    "models/generic",
    "integration",
    "integration/banking",
    "integration/credit_card",
    "integration/cloud_nlu",
    "integration/local_nlp",
    "cache",
    "samples",
    "samples/multilingual",
    "samples/domain_adapt",
    "scripts",
    "configs",
    "configs/env",
    "configs/templates",
    "notebooks",
    "utils",
    "utils/logging",
    "utils/nlp_tools",
    "utils/prompts",
    "test_env",
    "test_env/simulated_inputs",
    "test_env/scenario_data"
]

dir_files = {
    "docs/architecture": [
        "nlu_system_overview.mmd",       # Mermaid diagram of NLU pipeline
        "architecture_notes.txt",        # Text notes on architecture decisions
        "diagram_instructions.md"        # How to update and interpret diagrams
    ],
    "docs/api": [
        "nlu_api_endpoints.yaml",         # Defines API endpoints if NLU offered as service
        "api_overview.md",               # Overview of NLU API usage
        "auth_guide.txt"                 # Authentication instructions for protected endpoints
    ],
    "docs/user_guides": [
        "getting_started_nlu.md",         # Basic steps to start using NLU
        "frontend_usage_guide.md",        # How frontends (mobile/desktop/web) integrate with NLU results
        "model_deployment_guide.md"       # Deploying/updating NLU models
    ],
    "docs/user_stories": [
        "banking_user_stories_nlu.md",    # User scenarios focusing on banking intents
        "credit_card_user_stories_nlu.md",# Stories focusing on credit card operations
        "multilingual_nlu_stories.md"     # Stories covering multiple languages usage
    ],
    "docs/security": [
        "nlu_security_threat_model.md",   # Security considerations for handling user text
        "data_privacy_nlu.yaml",          # Policies for data handling & privacy
        "vulnerability_report_template.txt" # Template for reporting security issues
    ],
    "tests/unit": [
        "test_intent_classification.py",  # Unit tests for intent detection logic
        "test_entity_extraction.py"       # Unit tests for entity extraction functions
    ],
    "tests/integration": [
        "test_frontend_integration.py",   # Ensure NLU results integrate well with UI frontends
        "test_banking_terms.py"           # Check recognition of banking-specific terms
    ],
    "tests/performance": [
        "test_latency_measure.py",        # Checks how fast NLU responds
        "test_scalability.py"             # Tests how system performs under load
    ],
    "tests/security": [
        "test_input_sanitization.py",     # Ensure user input is safely handled
        "test_access_controls.py"         # Verify only authorized requests processed
    ],
    "tests/end_to_end": [
        "test_full_nlu_pipeline.py",       # Runs a scenario from raw text to final structured intent & entities
        "test_complex_multilang_scenario.py" # Tests a scenario mixing languages
    ],
    "language_support": [
        "lang_mapping.yaml",              # Maps language codes (uz, ru, en) to model/processing steps
        "supported_languages.json"        # JSON listing which languages are enabled
    ],
    "language_support/tests": [
        "test_lang_mapping.py"            # Tests correctness of language mappings
    ],
    "models/en": [
        "english_nlu_model_info.txt",     # Info on English NLU model (version, accuracy)
        "en_feature_extractor.py"         # Code to extract features from English text (e.g., tokenization)
    ],
    "models/ru": [
        "russian_nlu_model_info.txt",     # Info on Russian NLU model
        "ru_feature_extractor.py"         # Feature extraction tailored for Russian
    ],
    "models/uz": [
        "uzbek_nlu_model_info.txt",       # Info on Uzbek NLU model
        "uz_feature_extractor.py"         # Uzbek-specific text processing
    ],
    "models/generic": [
        "generic_nlu_resources.txt",      # Notes on generic resources (stopwords, synonyms)
        "generic_feature_extractor.py"    # A general-purpose feature extraction script
    ],
    "integration/banking": [
        "banking_terms.yaml",             # YAML listing banking domain terms
        "test_banking_adaptation.py"      # Tests adaptation of NLU to banking domain terms
    ],
    "integration/credit_card": [
        "credit_card_domain.yaml",        # Terms, phrases related to credit cards
        "test_credit_card_entities.py"    # Tests extracting credit card-related entities
    ],
    "integration/cloud_nlu": [
        "cloud_nlu_config.yaml",          # Config for connecting to a cloud NLU API
        "cloud_nlu_integration_tests.py"  # Tests integration with external cloud NLU services
    ],
    "integration/local_nlp": [
        "local_nlp_config.yaml",          # Config for running local NLP engine
        "local_nlp_engine_setup.py"       # Setup or initialization code for local NLP engine
    ],
    "cache": [
        "cache_config.yaml",              # Configuration for caching NLU results
        "cache_manager.py"                # Python script to manage cached NLU responses
    ],
    "samples/multilingual": [
        "multi_lang_samples.json",         # Sample inputs in multiple languages
        "sample_analysis.ipynb"            # Notebook analyzing performance on these samples
    ],
    "samples/domain_adapt": [
        "banking_adapt_samples.txt",       # Sample utterances focusing on banking domain
        "credit_card_adapt_samples.txt"    # Sample utterances focusing on credit card domain
    ],
    "scripts": [
        "run_nlu_pipeline.sh",             # Shell script to run a full NLU pipeline test
        "evaluate_nlu_quality.py",         # Python script evaluating NLU quality (WER, accuracy)
        "convert_lexicon.py"               # Converts domain-specific lexicon into model-friendly format
    ],
    "configs/env": [
        "dev_env.yaml",                    # Dev environment config (less strict, verbose logs)
        "prod_env.yaml",                   # Production environment config (optimized, secure)
        "env_notes.txt"                    # Notes on environment differences
    ],
    "configs/templates": [
        "template_config.yaml",            # A template for generating NLU configs
        "template_vars.json"               # Variables used in template expansion
    ],
    "notebooks": [
        "nlu_research.ipynb",              # Experiment with new NLU techniques or LLM prompts
        "data_insight_analysis.ipynb"      # Analyze dataset distributions, entity frequency
    ],
    "utils": [
        "readme_utils.md",                 # Explains utilities available in utils/
        "utils_init.py"                    # Might initialize utils as a Python package
    ],
    "utils/logging": [
        "log_config.yaml",                 # Logging configuration (levels, format)
        "log_formatter.py"                 # Code to format logs for easier reading
    ],
    "utils/nlp_tools": [
        "tokenizer.py",                    # Custom tokenizer script
        "lemmatizer.py",                   # Lemmatization for different languages
        "stopword_filter.py",              # Removes stopwords from text
        "synonym_expander.py"              # Expand synonyms for domain adaptation
    ],
    "utils/prompts": [
        "prompt_template_en.yaml",         # English prompt template for LLM queries
        "prompt_template_ru.yaml",         # Russian prompt template
        "prompt_template_uz.yaml",         # Uzbek prompt template
        "prompt_merger.py"                 # Merge base prompts with domain-specific terms
    ],
    "test_env/simulated_inputs": [
        "mock_user_queries.txt",           # Sample user queries (text) simulating real conditions
        "simulate_input_stream.sh"         # Script simulating a stream of user queries
    ],
    "test_env/scenario_data": [
        "complex_scenarios.json",          # Complex scenario sets mixing banking and multilingual aspects
        "scenario_runner.py"               # Runs scenarios against NLU pipeline
    ]
}

def write_file(path, lines):
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")

def generate_content_for_file(filename):
    ext = os.path.splitext(filename)[1]
    if ext == ".py":
        return [f"# {filename}", "# Python code for NLU logic or tools related to its name."]
    elif ext in [".yaml", ".yml"]:
        return [f"# {filename}", "# YAML configuration or domain data."]
    elif ext == ".json":
        return ["{", f'  "description": "Placeholder for {filename}"', "}"]
    elif ext == ".txt":
        return [f"# {filename}", "# Text file for notes, documentation."]
    elif ext == ".sh":
        return [f"#!/usr/bin/env bash", f"# {filename}", "# Shell script placeholder.", "echo 'Running script...'"]
    elif ext == ".ipynb":
        return ['{"cells":[],"metadata":{},"nbformat":4,"nbformat_minor":5}']
    elif ext == ".md":
        return [f"# {filename}", "# Markdown documentation or guides."]
    elif ext == ".mmd":
        return ["%% Mermaid diagram", "graph TD;", "A-->B;"]
    else:
        return [f"# {filename}", "# Generic placeholder file."]

# Create directories and files
for fname, content in top_level_files.items():
    file_path = os.path.join(repo_name, fname)
    write_file(file_path, content)
    print(f"Created top-level file: {file_path}")

for d in subdirs:
    dir_path = os.path.join(repo_name, d)
    os.makedirs(dir_path, exist_ok=True)
    gitkeep_path = os.path.join(dir_path, ".gitkeep")
    write_file(gitkeep_path, [f"# .gitkeep to keep {d} directory in version control"])
    print(f"Created directory: {dir_path} and .gitkeep")

for directory, files in dir_files.items():
    for f in files:
        file_path = os.path.join(repo_name, directory, f)
        lines = generate_content_for_file(f)
        write_file(file_path, lines)
        print(f"Created file: {file_path}")

# Create main python files from name_patterns
for pattern in name_patterns:
    fname = pattern + ".py"
    file_path = os.path.join(repo_name, fname)
    lines = generate_content_for_file(fname)
    write_file(file_path, lines)
    print(f"Created core NLU file: {file_path}")

print("File tree creation for ai_nlu completed with a comprehensive set of directories and files!")
