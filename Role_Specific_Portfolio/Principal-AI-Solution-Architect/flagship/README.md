# Intelligent Enterprise Assistant

**Maturity:** local Python reference implementation; tests supplied but not executed in this publication. No vendor integration claimed.

## Business problem
Provide repeatable grounded retrieval for a fictional enterprise.

## Architecture
```mermaid
flowchart LR
 A[Synthetic input] --> B[Validation and business rules] --> C[Decision output]
 B --> D[Automated tests]
 C --> E[Executive review]
```

## Run the walkthrough
1. Download this folder and open it in VS Code.
2. Select Terminal > New Terminal and change to this folder.
3. Run `python app.py` to execute the embedded synthetic example.
4. Install pytest in an isolated environment and run `python -m pytest -q`.
5. Inspect the JSON output and compare against the test assertions.
6. Modify the sample input in app.py and rerun to inspect exception behavior.

[Source](app.py) | [Tests](test_app.py) | [Illustrative CSV](sample.csv)

CSV is an illustrative schema; the current program uses embedded input, not CSV ingestion.

## Executive deliverable
Use the grounded retrieval output as decision support, not as a production approval. Assign a business owner, document assumptions, review exceptions and require sign-off before operational use.

## Limitations
No production authentication, vendor deployment, persistent storage or verified vendor screenshots. Expanded input validation and edge-case tests are included; production hardening remains necessary.

## Review evidence
Expanded regression cases cover invalid inputs and boundary behavior. See repository Actions for actual test results. This remains a local reference implementation, not a vendor integration.

## Functional browser prototype
[Download demo.html](demo.html) and open in a browser. Edit the Search query fields, select Run analysis and inspect the decision. Try an invalid or empty input to inspect validation. The browser implementation is separate from Python and has not yet undergone browser or parity testing.
