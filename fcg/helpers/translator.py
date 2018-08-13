from googletrans import Translator
from googletrans.constants import LANGUAGES

from constants import ISO_ALPHA2_COUNTRY_CODES, COUNTRY_CODE_TO_LANG

__ORIGIN_TEXT = ['hello', 'thanks', 'the love', 'peace']
translator = Translator()


def country_code_to_langs(country_code):
    return COUNTRY_CODE_TO_LANG.get(country_code, None)


def get_translated_by_country_code(country_code):
    langs = country_code_to_langs(country_code)
    country_lang = 'en'
    if langs:
        for lang in langs.strip().split(','):
            if lang in LANGUAGES:
                country_lang = lang
                break

    return get_translated_by_lang(country_lang)


def get_translated_by_lang(lang):
    return translator.translate(__ORIGIN_TEXT, lang, src='en')


def check_supported_country_code_and_lang():
    for country_code in ISO_ALPHA2_COUNTRY_CODES:
        print('='*3)
        langs = country_code_to_langs(country_code)
        if langs:
            for lang in langs.strip().split(','):
                if lang in LANGUAGES:
                    print('   {} => {}'.format(
                        ISO_ALPHA2_COUNTRY_CODES[country_code], LANGUAGES[lang]))
                    break
                else:
                    print('   Xlang: {}-{}-{}'.format(country_code,
                                                      ISO_ALPHA2_COUNTRY_CODES[country_code], lang))
                    pass
        else:
            print('   Xcountry_code {}-{}'.format(
                country_code, ISO_ALPHA2_COUNTRY_CODES[country_code]))


def main():
    translations = get_translated_by_country_code('CN')
    for translation in translations:
        print(translation.origin, ' -> ', translation.text)


if __name__ == '__main__':
    main()
