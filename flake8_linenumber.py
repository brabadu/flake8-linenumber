from enum import Enum
from pathlib import Path
from flake8.utils import parse_unified_diff

class LineNumberErrors(Enum):
    L001 = 'L001 File is too long (limit: {limit}, total lines: {total_lines})'


def config_parser(linenumber_config):
    size_pairs = map(lambda s: s.split('='), linenumber_config)
    return {Path(filename): int(size) for filename, size in size_pairs}


class LineNumberPlugin:
    name = __name__
    version = '0.1.8'

    def __init__(self, tree, total_lines, filename):
        self.total_lines = total_lines
        self.filename = Path(filename)
        self.last_changed_lines = {
            Path(f): max(changed_lines)
            for f, changed_lines in parse_unified_diff().items()
            if changed_lines
        }

    @classmethod
    def add_options(cls, options_manager):
        options_manager.add_option(
            '--max-linenumber',
            type='int',
            default=None,
            parse_from_config=True,
            help='Default max line limit for a python module'
        )
        options_manager.add_option(
            '--linenumber',
            type='str',
            comma_separated_list=True,
            default=[],
            parse_from_config=True,
            help='List of modules and their max line nums'
        )

    @classmethod
    def parse_options(cls, options):
        cls.filesizes = config_parser(options.linenumber)
        cls.diff = options.diff
        cls.default_limit = options.max_linenumber

    def run(self):
        filesize_limit = self.filesizes.get(self.filename, self.default_limit)

        if filesize_limit and self.total_lines > filesize_limit:
            message = LineNumberErrors.L001.value.format(
                limit=filesize_limit,
                total_lines=self.total_lines
            )

            # report error on last line of the file
            err_line = self.total_lines - 1

            # if flake is run on diff, then report on last changed line
            if self.diff and self.filename in self.last_changed_lines:
                err_line = self.last_changed_lines[self.filename]

            yield (err_line, 0, message, 1)
