# Automated regression matrix — v1.2.1

Run UTC: 2026-10-21T09:41:33.454218+00:00

Evidence: [verbose unittest output](TEST_RUN.txt), [machine-readable results](TEST_RESULTS.json).
PASS means assertions in the named automated test passed; P15/P16 are static checks, not model runs.

| ID | Preconditions | Input | Expected | Actual | Status |
|---|---|---|---|---|---|
| I01 | audited upstream and imports | compare SHA-256 | protected files and skill functionality unchanged | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| I02 | approved current contract | compare eight documents | same artifact limits and no repeat approval | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| I03 | current task template | restore absolute no-change sentence | conflict detected | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| I04 | integrated manifests and licenses | inspect versions and legal scope | repo 1.1.0 candidate skill 1.2.1 Apache copies match | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| I05 | source publish tree | heuristic path/secret/history scan | no flags in reviewed source | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| I06 | synthetic marker only | introduce fake credential and home path | detect without printing contents | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| I07 | fixed canonical source | build twice in fresh external directories | both ZIP hashes reproducible | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| I08 | integrated docs and archives | validate local Markdown references | zero required broken links | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| I09 | local workflow candidate | inspect permission and OS policy | two OS no external actions secrets write or release | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| I10 | static current contract | check unauthorized artifacts and product protections | limits and lifecycle retained | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| I11 | protected snapshot fixture | alter v1.0.0 bytes | preservation failure | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| I12 | mocked permission failure | enumerate source tree | error propagates rather than false PASS | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| O01 | three synthetic entries | search ghidra mcp | active specific candidate ranks first; license and evidence status retained | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| O02 | synthetic index | unmatched query | exit 0 and empty JSON list | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| O03 | synthetic index | limit 0 | exit 2 and BLOCKED | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| O04 | mixed categories/languages | parser, formats, Rust | only PSD reader returned | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| O05 | synthetic repository URL | example/ghidra-bridge | matching entry returned | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| O06 | three entries | categories | RE Tooling count is 2 | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| O07 | invalid JSON file | search ghidra | exit 2 and BLOCKED | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| O08 | object instead of JSON list | search ghidra | exit 2 and BLOCKED | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| O09 | missing fixture file | search ghidra | exit 2 and unavailable error | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| O10 | metadata containing shell text/control bytes | search ghidra | no marker execution; control characters removed | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| O11 | entry without license | inspect example/old | license NOT_VERIFIED | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P01 | pristine bundle | validator | PASS before Git initialization | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P02 | temp bundle and installed Git | git init then validator | PASS with same source hashes | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P03 | synthetic worktree .git file | validator | metadata ignored without reading target | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P04 | .git with invalid Markdown bytes | validator | never traverses Git metadata | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P05 | pristine bundle | add unexpected.txt | FAIL with new-file evidence | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P06 | .gitignore ignores .env | add synthetic .env | manifest still rejects file | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P07 | tracked README | append one byte | FAIL with changed hash evidence | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P08 | tracked README | move outside bundle | FAIL with missing-file evidence | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P09 | root canonical templates | compare all ten copies | exact bytes and no missing dependency | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P10 | standalone template copy | append one byte | validator reports divergence | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P11 | full bundle and nested skill | inspect all local Markdown references | zero broken links | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P12 | required reference | add absent Markdown target | precise link failure | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P13 | existing external fixture | link outside package | reject without importing external content | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P14 | copy only skill into isolated location | validate resources and run CLI | independent success | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P15 | core/task/integrations/adaptive/A01-A44 | static consistency check | consistent contract and all models NOT_RUN | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P16 | valid Gemma adapter | reintroduce old command prohibition | static check rejects conflict | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P17 | edited canonical fixture | --prepare | byte-identical copy and refreshed valid manifests | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P18 | validated bundle | build two archives outside root | CRC, matching skill and zero local link errors | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P19 | modified unprepared source | build archives | nonzero and no ZIP produced | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P20 | existing artifact | same output name | BLOCKED without overwrite | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P21 | unlisted .venv fixture | validator | still rejects non-Git metadata files | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| P22 | hashed text and LF checkout rules | prepare manifests | every packaged text uses LF | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U01 | Unicode index | Straße/STRASSE/strasse | same original entry | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U02 | NFD name | NFC/NFD query | match and preserve original codepoints | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U03 | emoji in description | search 🔒 | exact Unicode description retained | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U04 | one populated weighted field | STRASSE | each field searchable | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U05 | Unicode filters | decomposed category/language | one match | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U06 | redirected cp1252 strict stdout | all CLI modes | parseable escaped JSON | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U07 | redirected UTF-8 strict stdout | Unicode metadata | literal bytes and valid JSON | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U08 | StringIO stdout | print Unicode object | valid JSON without encoding attribute | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U09 | valid index | lengths 160/161 | exit 0 then controlled exit 2 | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U10 | valid index | limits 1/50/51/-1 | accept only inclusive valid range | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U11 | mixed JSON array | object plus scalar | controlled BLOCKED exit 2 | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U12 | mocked OS denial | open index | controlled BLOCKED with no file mutation | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U13 | bounded fixture thresholds | oversize bytes/entry count | reject both limits | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U14 | original ranking weights | repeated ASCII search | active specific candidate first | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
| U15 | nonexistent Unicode path, cp1252 stderr | search | controlled exit 2, no traceback | All assertions completed successfully; asserted outputs are defined in the named test. | PASS |
