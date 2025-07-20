# helpers/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pydantic import Field, field_validator # Import Field and field_validator

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPEN_AI_KEY: str

    # Give it a default value as a Python list
    FILE_ALLOWED_TYPES: List[str] 
    FILE_MAX_SIZE: int

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='forbid',
        env_nested_delimiter='__',
        case_sensitive=True
    )

    @field_validator('FILE_ALLOWED_TYPES', mode='before')
    @classmethod
    def parse_allowed_types(cls, v): # Remove the type hint for 'v' temporarily
        print(f"DEBUG: Type of 'v' received by validator: {type(v)}")
        print(f"DEBUG: Value of 'v' received by validator (repr): {repr(v)}") # Use repr() to show hidden chars
        if isinstance(v, str):
            # Split by comma and strip whitespace from each item
            return [item.strip() for item in v.split(',')]
        return v


def get_settings():
    settings = Settings()
    # For Pydantic v2, use .model_dump()
    print(f"DEBUG: Final Loaded Settings: {settings.model_dump()}")
    return settings