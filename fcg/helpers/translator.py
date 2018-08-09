from googletrans import Translator

__ORIGIN_TEXT = ['hello', 'thanks', 'the love', 'peace']
translator = Translator()


def get_translated_for(lang):
    return translator.translate(__ORIGIN_TEXT, lang, src='en')


def main():
    translations = get_translated_for('en')
    for translation in translations:
        print(translation.origin, ' -> ', translation.text)


if __name__ == '__main__':
    main()
