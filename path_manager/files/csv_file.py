from path_manager.files.output_file import OutputFile


class CsvFile(OutputFile):
    def __init__(self):
        super().__init__('csv')
