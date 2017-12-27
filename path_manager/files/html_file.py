from path_manager.files.output_file import OutputFile


class HtmlFile(OutputFile):
    def __init__(self):
        super().__init__('html')
