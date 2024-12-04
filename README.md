# Career Ladder Assessment Splitter

A command-line tool that splits career ladder assessment data into separate CSV files for each job level, making it easier to review and manage competency behaviors across different career levels.

## Description

This tool takes a career ladder assessment matrix (in Excel or CSV format) and splits it into separate files by job level. It expects input data where:
- The first column contains competency areas
- Subsequent columns represent different job levels
- Cells contain behavior descriptions, which may be separated by newlines or periods

## Installation

1. Ensure you have Python 3.x installed
2. Install required dependencies:

```bash
pipenv install
pipenv shell
```

## Usage

Run the script from the command line:

```bash
python career-ladder-assessment.py INPUT_FILE OUTPUT_FOLDER
```

### Arguments:
- `input_file`: Path to your Excel (.xlsx) or CSV (.csv) file containing the career ladder matrix
- `output_folder`: Directory where the split files should be saved

### Example:

```bash
python career-ladder-assessment.py career_ladder.xlsx output/
```

## Input File Format

Your input file should be structured as follows:

| Levels          | Level 1 | Level 2 | Level 3 |
|-----------------|---------|---------|---------|
| Competency Area | Behavior descriptions | Behavior descriptions | Behavior descriptions |

Each behavior description cell can contain multiple behaviors separated by periods or newlines.

## Output

The script will generate separate CSV files for each job level, named according to the level (e.g., `Level_1_Behaviors.csv`). Each output file will contain two columns:
- Competency Area
- Competency at Level

## Error Handling

The script includes error handling for:
- Invalid input file formats
- Missing input files
- File processing errors

## License

[MIT License](LICENSE)