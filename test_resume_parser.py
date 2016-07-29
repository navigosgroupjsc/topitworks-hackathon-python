import pytest
from ResumeParser import ResumeParser


@pytest.fixture
def rp():
    """Fixture for pytest."""
    resume_file_name = '/path/to/resume.ext'
    rp = ResumeParser(resume_file_name)
    return rp


def test_rp(rp):
    """Test RP."""
    # your test code
