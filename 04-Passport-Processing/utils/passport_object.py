from dataclasses import dataclass
from typing import Optional


@dataclass
class Passport:
    byr: int  # Birth year
    iyr: int  # Issue year
    eyr: int  # Expiration Year
    hgt: str  # Height
    hcl: str  # Hair Color
    ecl: str  # Eye Color
    pid: str  # Passport ID
    cid: Optional[str] = None  # Country ID

    validation: Optional[bool] = False  # Run validation on creation

    _EYE_COLOURS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    _HEIGHT_LIMITS = limits = {
        "cm": (150, 193),
        "in": (59, 76),
    }

    def __post_init__(self):
        self.byr = int(self.byr)
        self.iyr = int(self.iyr)
        self.eyr = int(self.eyr)

        if self.validation:
            self.run_validation()

    def run_validation(self):
        """
        Runs all validation steps
        """
        try:
            self.validate_byr()
            self.validate_iyr()
            self.validate_eyr()
            self.validate_hgt()
            self.validate_hcl()
            self.validate_ecl()
            self.validate_pid()
        except Exception:
            raise TypeError

    def validate_byr(self):
        assert len(str(self.byr)) == 4
        assert 1920 <= self.byr <= 2002

    def validate_iyr(self):
        assert len(str(self.iyr)) == 4
        assert 2010 <= self.iyr <= 2020

    def validate_eyr(self):
        assert len(str(self.eyr)) == 4
        assert 2020 <= self.eyr <= 2030

    def validate_hgt(self):
        unit = self.hgt[-2:]
        assert unit in self._HEIGHT_LIMITS.keys()
        assert int(self.hgt[:-2])
        assert (
            self._HEIGHT_LIMITS[unit][0]
            <= int(self.hgt[:-2])
            <= self._HEIGHT_LIMITS[unit][1]
        )

    def validate_hcl(self):
        assert self.hcl[0] == "#"
        assert len(self.hcl[1:]) == 6
        assert self.hcl[1:].isalnum()

    def validate_ecl(self):
        assert self.ecl in self._EYE_COLOURS

    def validate_pid(self):
        assert len(self.pid) == 9
        assert self.pid.isnumeric()
