from translate import Translator

if __name__ == '__main__':
    import sys
    import os
    sys.path.insert(0, os.path.join(
        os.path.abspath(os.path.dirname(__file__)), '../..'))

from fcg.helpers.constants import ISO_ALPHA2_COUNTRY_CODES, COUNTRY_CODE_TO_LANG, ORIGIN_TEXT, LANGUAGES

def country_code_to_langs(country_code):
    langs = COUNTRY_CODE_TO_LANG.get(country_code, [])
    if langs:
        langs = [lang.strip() for lang in langs.strip().split(',')]

    return langs


def is_supported_lang(lang):
    return lang in LANGUAGES


def get_lang_name(lang):
    return LANGUAGES.get(lang, None)


def get_translated(lang):
    translator = Translator(to_lang=lang)
    results = [translator.translate(text) for text in ORIGIN_TEXT]

    return results

def check_supported_country_code_and_lang():
    for country_code in ISO_ALPHA2_COUNTRY_CODES:
        print('='*3)
        langs = country_code_to_langs(country_code)
        if langs:
            for lang in langs.strip().split(','):
                if is_supported_lang(lang):
                    print('   {} => {}'.format(
                        ISO_ALPHA2_COUNTRY_CODES[country_code], get_lang_name(lang)))
                    break
                else:
                    print('   Xlang: {}-{}-{}'.format(country_code,
                                                      ISO_ALPHA2_COUNTRY_CODES[country_code], lang))
                    pass
        else:
            print('   Xcountry_code {}-{}'.format(
                country_code, ISO_ALPHA2_COUNTRY_CODES[country_code]))


def main():
    langs = country_code_to_langs('CN')
    for lang in langs:
        if is_supported_lang(lang):
            translations = get_translated(lang)
            print('{} - {}'.format(lang, get_lang_name(lang)))
            print(translations)
            break


if __name__ == '__main__':
    main()
