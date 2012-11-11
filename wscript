srcdir = '.'
blddir = 'build'
VERSION = '0.0.1'

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')
  conf.env['CXX']       = 'g++-4.6'
  conf.env['CXXFLAGS']  = '-std=c++0x'
  conf.env['LINKFLAGS'] = ['/home/hecomi/Program/cpp/node/openjtalk/openjtalk/open_jtalk-1.05/text2mecab/libtext2mecab.a',
                           '/home/hecomi/Program/cpp/node/openjtalk/openjtalk/open_jtalk-1.05/mecab/src/libmecab.a',
                           '/home/hecomi/Program/cpp/node/openjtalk/openjtalk/open_jtalk-1.05/mecab2njd/libmecab2njd.a',
                           '/home/hecomi/Program/cpp/node/openjtalk/openjtalk/open_jtalk-1.05/njd/libnjd.a',
                           '/home/hecomi/Program/cpp/node/openjtalk/openjtalk/open_jtalk-1.05/njd_set_pronunciation/libnjd_set_pronunciation.a',
                           '/home/hecomi/Program/cpp/node/openjtalk/openjtalk/open_jtalk-1.05/njd_set_digit/libnjd_set_digit.a',
                           '/home/hecomi/Program/cpp/node/openjtalk/openjtalk/open_jtalk-1.05/njd_set_accent_phrase/libnjd_set_accent_phrase.a',
                           '/home/hecomi/Program/cpp/node/openjtalk/openjtalk/open_jtalk-1.05/njd_set_accent_type/libnjd_set_accent_type.a',
                           '/home/hecomi/Program/cpp/node/openjtalk/openjtalk/open_jtalk-1.05/njd_set_unvoiced_vowel/libnjd_set_unvoiced_vowel.a',
                           '/home/hecomi/Program/cpp/node/openjtalk/openjtalk/open_jtalk-1.05/njd_set_long_vowel/libnjd_set_long_vowel.a',
                           '/home/hecomi/Program/cpp/node/openjtalk/openjtalk/open_jtalk-1.05/njd2jpcommon/libnjd2jpcommon.a',
                           '/home/hecomi/Program/cpp/node/openjtalk/openjtalk/open_jtalk-1.05/jpcommon/libjpcommon.a',
                           '/home/hecomi/Program/cpp/node/openjtalk/openjtalk/hts_engine_API-1.06/lib/libHTSEngine.a']

def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
  obj.target = 'openjtalk'
  obj.source = 'openjtalk.cc text_to_speech.cpp'
  obj.lib      = ['alut', 'openal']
  obj.includes = 'openjtalk/open_jtalk-1.05/ \
                  openjtalk/open_jtalk-1.05/mecab \
                  openjtalk/open_jtalk-1.05/text2mecab \
                  openjtalk/open_jtalk-1.05/mecab/src \
                  openjtalk/open_jtalk-1.05/mecab2njd \
                  openjtalk/open_jtalk-1.05/njd \
                  openjtalk/open_jtalk-1.05/njd_set_pronunciation \
                  openjtalk/open_jtalk-1.05/njd_set_digit \
                  openjtalk/open_jtalk-1.05/njd_set_accent_phrase \
                  openjtalk/open_jtalk-1.05/njd_set_accent_type \
                  openjtalk/open_jtalk-1.05/njd_set_unvoiced_vowel \
                  openjtalk/open_jtalk-1.05/njd_set_long_vowel \
                  openjtalk/open_jtalk-1.05/njd2jpcommon \
                  openjtalk/open_jtalk-1.05/jpcommon \
                  hts_engine_API-1.06/include'

