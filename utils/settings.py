from pydantic import BaseSettings


class ParseSettings(BaseSettings):

    # Path to raw bp db
    RAW_DB: str = './raw.sqlite'

    # Path to normalized bp db
    NORMALIZED_DB_NAME: str = 'bp.sqlite'
    NORMALIZED_DB: str = f'./{NORMALIZED_DB_NAME}'

    # Normalization script
    NORMALIZATION_SCRIPT: str = './bp_normalization.sql'

    # Excel columns re.patterns
    PARTNO_PATTERN: str = r'^[0-9A-Z]{10}$'
    TITLE_UA_PATTERN: str = r'^[0-9A-Za-zА-Яа-яЇїІіЄєҐґЁё\s/&+=,.()\'\"\[\]\-\\]+$'
    TITLE_EN_PATTERN: str = r'^[0-9A-Za-z\s/&+=,.()\[\]\-\\]+$'
    SECTION_PATTERN: str = r'^\d+.\s[0-9A-Za-z\s/&+=,.()\[\]\-\\\/]+$'
    SUBSECTION_PATTERN: str = r'^\d+.\d+\s[0-9A-Za-z\s/&+=,.()\[\]\-\\]+$'
    GROUP_PATTERN: str = r'^\d+.\d+.\d+\s[0-9A-Za-z\s/&+=,.()\[\]\-\\\/]+$'
    DECIMAL_PATTERN: str = r'^\d+[.,]?\d*$'
