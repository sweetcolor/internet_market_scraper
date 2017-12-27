from path_manager.files.output_file import OutputFile


class JpegFile(OutputFile):
    def __init__(self):
        super().__init__('jpeg')
