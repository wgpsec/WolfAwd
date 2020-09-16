from .Filer import UseFiler


class FileManager:
    def __init__(self):
        self.usage()
        while True:
            function_choice = input(">>>")
            if function_choice == "0" or function_choice == "help":
                self.usage()
            elif function_choice == "1" or function_choice == "down":
                UseFiler(method="download")
            elif function_choice == "2" or function_choice == "upload":
                UseFiler(method="upload")

    @staticmethod
    def usage():
        """
        帮助信息
        """
        print("+----------------------------------------------------+")
        print("|Num|Command |    Describe                           |")
        print("+----------------------------------------------------+")
        print("|0. | help   |    Get Usage                          |")
        print("|1. | down   |    Download files from server         |")
        print("|2. | upload |    Upload files from Server           |")
        print("+----------------------------------------------------+")
