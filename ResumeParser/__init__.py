"""
ResumeParser

The main purpose of this Package is to parse 
unstructured data (resume file) to structured data (JSON).
"""

__version__ = "0.0.1"


class ResumeParser(object):
    """This class will be use to parse resume file and return JSON data."""

    def __init__(self, resume_file_name):
        """
        Initiation for ResumeParser class.

        :param resume_file_name: 
            name of resume file in DOC, DOCX or PDF extension.
        :type resume_file_name: str
        """
        self.resume_file = open(resume_file_name, 'r')

    def parse_data(self):
        """Parse and get data from file and store as JSON format."""
        # your code
        return json_data

    def get_json_data(self):
        """Get the processed data in JSON format."""
        return self.parse_data()
