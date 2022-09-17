from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)   # because frozen true it behaves as namedtuple
class DataIngestionConfig:
    root_dir: Path          # these are class variables
    source_URL: str
    local_data_file: Path
    unzip_dir: Path