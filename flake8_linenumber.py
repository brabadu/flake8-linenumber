import sys
from enum import Enum
from flake8.formatting.default import Default

if sys.version_info < (3, 8):  # pragma: no cover (<PY38)
    import importlib_metadata
else:  # pragma: no cover (PY38+)
    import importlib.metadata as importlib_metadata


class LineNumberErrors(Enum):
    L001 = 'L001 File is too long (limit: {limit}, total lines: {total_lines})'


def config_parser(linenumber_config):
    size_pairs = map(lambda s: s.split('='), linenumber_config)
    return {filename: int(size) for filename, size in size_pairs}


class LineNumberPlugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree, total_lines, filename):
        self.total_lines = total_lines
        self.filename = filename

    @classmethod
    def add_options(cls, options_manager):
        options_manager.add_option(
            '--linenumbers',
            type='str',
            comma_separated_list=True,
            default=[],
            parse_from_config=True,
            help='List of modules and their max line nums'
        )

    @classmethod
    def parse_options(cls, options):
        cls.filesizes = config_parser(options.linenumbers)

    def run(self):
        filesize_limit = self.filesizes.get(self.filename)

        if filesize_limit and self.total_lines > filesize_limit:
            message = LineNumberErrors.L001.value.format(
                limit=filesize_limit,
                total_lines=self.total_lines
            )
            for i in range(self.total_lines):
                yield (i + 1, 0, message, 1)


class LineNumberFromat(Default):
    def after_init(self):
        self.filenames_already_printed = set()
        self.filesizes = config_parser(self.options.linenumbers)

    def format(self, error):
        if error.code != LineNumberErrors.L001.name:
            return super(LineNumberFromat, self).format(error)

        if error.filename not in self.filenames_already_printed:
            self.filenames_already_printed.add(error.filename)
            return super(LineNumberFromat, self).format(error)
