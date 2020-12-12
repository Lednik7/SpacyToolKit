try:
    from googletrans import Translator
    def get_translate(text):
        """
        get_translate(text)
        For this function to work, you must install the module - googletrans.
        This function takes one argument - string and returns - string.
        Any other argument will result in an error.
        """
        assert type(text) == str, "The data must be a string"
        return Translator().translate(text).text
except Exception as e:
    print(e)
    print("\033[31mPlease use 'pip install googletrans'\033[0m")