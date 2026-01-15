## ADDED Requirements
### Requirement: Text File Splitting
The system SHALL provide a node to read and split text files into a list of strings.

#### Scenario: Split by newline
- **WHEN** a text file is provided AND split method is "newline"
- **THEN** return a list of strings where each line is an item (stripping empty lines)

#### Scenario: Split by numbered list
- **WHEN** a text file with "1. Item", "2. Item" is provided AND split method is "numbered list"
- **THEN** return a list where each item corresponds to the numbered entry

#### Scenario: Encoding fallback
- **WHEN** a file is provided
- **THEN** allow selecting encoding (utf-8 default) to support Chinese characters

### Requirement: Loop Integration
The system SHALL provide outputs suitable for iteration.

#### Scenario: Output list and count
- **WHEN** text is split
- **THEN** output the list of strings AND the total count of items
