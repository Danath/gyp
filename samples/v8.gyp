{
  'variables': {
    'depth': '..',
    'base_sources': [
      'src/third_party/dtoa/dtoa.c',
      'src/third_party/jscre/ASCIICType.h',
      'src/third_party/jscre/config.h',
      'src/third_party/jscre/pcre.h',
      'src/third_party/jscre/pcre_chartables.c',
      'src/third_party/jscre/pcre_compile.cpp',
      'src/third_party/jscre/pcre_exec.cpp',
      'src/third_party/jscre/pcre_internal.h',
      'src/third_party/jscre/pcre_tables.cpp',
      'src/third_party/jscre/pcre_ucp_searchfuncs.cpp',
      'src/third_party/jscre/pcre_xclass.cpp',
      'src/third_party/jscre/ucpinternal.h',
      'src/third_party/jscre/ucptable.cpp',
      'src/accessors.cc',
      'src/accessors.h',
      'src/allocation.cc',
      'src/allocation.h',
      'src/api.cc',
      'src/api.h',
      'src/apiutils.h',
      'src/arguments.h',
      'src/assembler-arm-inl.h',
      'src/assembler-arm.cc',
      'src/assembler-arm.h',
      'src/assembler-ia32-inl.h',
      'src/assembler-ia32.cc',
      'src/assembler-ia32.h',
      'src/assembler.cc',
      'src/assembler.h',
      'src/ast.cc',
      'src/ast.h',
      'src/bootstrapper.cc',
      'src/bootstrapper.h',
      'src/builtins-arm.cc',
      'src/builtins-ia32.cc',
      'src/builtins.cc',
      'src/builtins.h',
      'src/bytecodes-irregexp.h',
      'src/char-predicates-inl.h',
      'src/char-predicates.h',
      'src/checks.cc',
      'src/checks.h',
      'src/code-stubs.cc',
      'src/code-stubs.h',
      'src/code.h',
      'src/codegen-arm.cc',
      'src/codegen-arm.h',
      'src/codegen-ia32.cc',
      'src/codegen-ia32.h',
      'src/codegen-inl.h',
      'src/codegen.cc',
      'src/codegen.h',
      'src/compilation-cache.cc',
      'src/compilation-cache.h',
      'src/compiler.cc',
      'src/compiler.h',
      'src/constants-arm.h',
      'src/contexts.cc',
      'src/contexts.h',
      'src/conversions-inl.h',
      'src/conversions.cc',
      'src/conversions.h',
      'src/counters.cc',
      'src/counters.h',
      'src/cpu-arm.cc',
      'src/cpu-ia32.cc',
      'src/cpu.h',
      'src/dateparser.cc',
      'src/dateparser.h',
      'src/debug-arm.cc',
      'src/debug-ia32.cc',
      'src/debug.cc',
      'src/debug.h',
      'src/disasm-arm.cc',
      'src/disasm-ia32.cc',
      'src/disasm.h',
      'src/disassembler.cc',
      'src/disassembler.h',
      'src/dtoa-config.c',
      'src/execution.cc',
      'src/execution.h',
      'src/factory.cc',
      'src/factory.h',
      'src/flag-definitions.h',
      'src/flags.cc',
      'src/flags.h',
      'src/frames-arm.cc',
      'src/frames-arm.h',
      'src/frames-ia32.cc',
      'src/frames-ia32.h',
      'src/frames-inl.h',
      'src/frames.cc',
      'src/frames.h',
      'src/global-handles.cc',
      'src/global-handles.h',
      'src/globals.h',
      'src/handles-inl.h',
      'src/handles.cc',
      'src/handles.h',
      'src/hashmap.cc',
      'src/hashmap.h',
      'src/heap-inl.h',
      'src/heap.cc',
      'src/heap.h',
      'src/ic-arm.cc',
      'src/ic-ia32.cc',
      'src/ic-inl.h',
      'src/ic.cc',
      'src/ic.h',
      'src/interpreter-irregexp.cc',
      'src/interpreter-irregexp.h',
      'src/jsregexp-inl.h',
      'src/jsregexp.cc',
      'src/jsregexp.h',
      'src/list-inl.h',
      'src/list.h',
      'src/log.cc',
      'src/log.h',
      'src/macro-assembler-arm.cc',
      'src/macro-assembler-arm.h',
      'src/macro-assembler-ia32.cc',
      'src/macro-assembler-ia32.h',
      'src/macro-assembler.h',
      'src/mark-compact.cc',
      'src/mark-compact.h',
      'src/memory.h',
      'src/messages.cc',
      'src/messages.h',
      'src/natives.h',
      'src/objects-debug.cc',
      'src/objects-inl.h',
      'src/objects.cc',
      'src/objects.h',
      'src/parser.cc',
      'src/parser.h',
      'src/platform-freebsd.cc',
      'src/platform-linux.cc',
      'src/platform-macos.cc',
      'src/platform-nullos.cc',
      'src/platform-win32.cc',
      'src/platform.h',
      'src/prettyprinter.cc',
      'src/prettyprinter.h',
      'src/property.cc',
      'src/property.h',
      'src/regexp-macro-assembler-arm.cc',
      'src/regexp-macro-assembler-arm.h',
      'src/regexp-macro-assembler-ia32.cc',
      'src/regexp-macro-assembler-ia32.h',
      'src/regexp-macro-assembler-irregexp-inl.h',
      'src/regexp-macro-assembler-irregexp.cc',
      'src/regexp-macro-assembler-irregexp.h',
      'src/regexp-macro-assembler-tracer.cc',
      'src/regexp-macro-assembler-tracer.h',
      'src/regexp-macro-assembler.cc',
      'src/regexp-macro-assembler.h',
      'src/regexp-stack.cc',
      'src/regexp-stack.h',
      'src/rewriter.cc',
      'src/rewriter.h',
      'src/runtime.cc',
      'src/runtime.h',
      'src/scanner.cc',
      'src/scanner.h',
      'src/scopeinfo.cc',
      'src/scopeinfo.h',
      'src/scopes.cc',
      'src/scopes.h',
      'src/serialize.cc',
      'src/serialize.h',
      'src/shell.h',
      'src/simulator-arm.cc',
      'src/smart-pointer.h',
      'src/snapshot-common.cc',
      'src/snapshot.h',
      'src/spaces-inl.h',
      'src/spaces.cc',
      'src/spaces.h',
      'src/string-stream.cc',
      'src/string-stream.h',
      'src/stub-cache-arm.cc',
      'src/stub-cache-ia32.cc',
      'src/stub-cache.cc',
      'src/stub-cache.h',
      'src/token.cc',
      'src/token.h',
      'src/top.cc',
      'src/top.h',
      'src/unicode-inl.h',
      'src/unicode.cc',
      'src/unicode.h',
      'src/usage-analyzer.cc',
      'src/usage-analyzer.h',
      'src/utils.cc',
      'src/utils.h',
      'src/v8-counters.cc',
      'src/v8-counters.h',
      'src/v8.cc',
      'src/v8.h',
      'src/v8threads.cc',
      'src/v8threads.h',
      'src/variables.cc',
      'src/variables.h',
      'src/zone-inl.h',
      'src/zone.cc',
      'src/zone.h',
    ],
    'base_sources!': [
      # These files are #included by others and are not meant to be compiled
      # directly.
      'src/third_party/dtoa/dtoa.c',
      'src/third_party/jscre/pcre_chartables.c',
      'src/third_party/jscre/ucptable.cpp',
    ],
    'core_library_files': [
      'src/runtime.js',
      'src/v8natives.js',
      'src/array.js',
      'src/string.js',
      'src/uri.js',
      'src/math.js',
      'src/messages.js',
      'src/apinatives.js',
      'src/debug-delay.js',
      'src/mirror-delay.js',
      'src/date-delay.js',
      'src/regexp-delay.js',
      'src/macros.py',
    ],
  },
  'includes': [
    '../build/common.gypi',
  ],
  'target_defaults': {
    'configurations': {
      'Debug': {
        'defines': [
          'DEBUG',
          'ENABLE_DISASSEMBLER',
          'ENABLE_LOGGING_AND_PROFILING',
        ],
      },
    },
    'xcode_settings': {
      'GCC_ENABLE_CPP_EXCEPTIONS': 'NO',
      'GCC_ENABLE_CPP_RTTI': 'NO',
    },
  },
  'targets': [
    {
      'target_name': 'v8_base',
      'type': 'static_library',
      'sources': [
        '<@(base_sources)',
      ],
      'sources!': [
        '<@(base_sources!)',
      ],
      'sources/': [
        ['exclude', '-arm\\.cc$'],
        ['exclude', '^src/platform-.*\\.cc$' ],
      ],
      'conditions': [
        # TODO(mark): These only need to be 'sources/', the extra '+' is
        # for prepend, which is only temporary until the rules scanner is
        # rewritten to not pull things out of the list until all includes and
        # excludes are processed.
        ['OS=="linux"', {'sources/+': [['include', '^src/platform-linux\\.cc$']]}],
        ['OS=="mac"', {'sources/+': [['include', '^src/platform-macos\\.cc$']]}],
        ['OS=="win"', {
          'sources/+': [['include', '^src/platform-win32\\.cc$']],
          # 4355, 4800 came from common.vsprops
          # 4018, 4244 were a per file config on dtoa-config.c
          # TODO: It's probably possible and desirable to stop disabling the
          # dtoa-specific warnings by modifying dtoa as was done in Chromium
          # r9255.  Refer to that revision for details.
          'msvs_disabled_warnings': [4355, 4800, 4018, 4244],
        }],
      ],
      'include_dirs': [
        'src',
      ],
    },
    {
      'target_name': 'v8_nosnapshot',
      'type': 'static_library',
      'sources': [
        '<(INTERMEDIATE_DIR)/libraries.cc',
        'src/snapshot-empty.cc',
      ],
      'include_dirs': [
        'src',
      ],
      'dependencies': [
        'v8_base',
      ],
      'actions': [
        {
          # This action is duplicated in the v8 target.  The duplication is
          # is ugly, but it's necessary to guarantee that libraries.cc is
          # is generated, since INTERMEDIATE_DIR might not be the same for
          # this target as that one.
          'action_name': 'js2c',
          'inputs': [
            'tools/js2c.py',
            '<@(core_library_files)',
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/libraries.cc',
            '<(INTERMEDIATE_DIR)/libraries-empty.cc',
          ],
          'action': 'python tools/js2c.py <(_outputs) CORE <(core_library_files)'
        },
      ],
    },
    {
      'target_name': 'mksnapshot',
      'type': 'executable',
      'sources': [
        'src/mksnapshot.cc',
      ],
      'dependencies': [
        'v8_nosnapshot',
      ],
    },
    {
      'target_name': 'v8',
      'type': 'static_library',
      'sources': [
        '<(INTERMEDIATE_DIR)/libraries-empty.cc',
        '<(INTERMEDIATE_DIR)/snapshot.cc',
      ],
      'include_dirs': [
        'src',
      ],
      'dependencies': [
        'v8_base',
        'mksnapshot',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'include',
        ],
      },
      'actions': [
        {
          # This action is duplicated in the v8_nosnapshot target.  The
          # duplication is ugly, but it's necessary to guarantee that
          # libraries-empty.cc is generated, since INTERMEDIATE_DIR might not
          # be the same for this target as that one.
          'action_name': 'js2c',
          'inputs': [
            'tools/js2c.py',
            '<@(core_library_files)',
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/libraries.cc',
            '<(INTERMEDIATE_DIR)/libraries-empty.cc',
          ],
          'action': 'python tools/js2c.py <(_outputs) CORE <(core_library_files)'
        },
        {
          'action_name': 'mksnapshot',
          'inputs': [
            '<(PRODUCT_DIR)/<(EXECUTABLE_PREFIX)mksnapshot<(EXECUTABLE_SUFFIX)',
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/snapshot.cc',
          ],
          'action': '<(_inputs) <(_outputs)',
        },
      ],
    },
    {
      'target_name': 'v8_shell',
      'type': 'executable',
      'sources': [
        'samples/shell.cc',
      ],
      'dependencies': [
        'v8',
      ],
      'conditions': [
        [ 'OS=="win"', {
          # This could be gotten from external_code, if we decide it's ok.
          'defines': ['_CRT_SECURE_NO_WARNINGS'],
        }],
      ],
    },
    {
      'target_name': 'd8',
      'type': 'executable',
      'sources': [
        '<(INTERMEDIATE_DIR)/d8-js.cc',
        'src/d8-debug.cc',
        'src/d8-readline.cc',
        'src/d8.cc',
      ],
      'conditions': [
        [ 'OS=="linux"', {
          'link_settings': { 'libraries': [ '-lreadline' ] },
        }],
        [ 'OS=="mac"', {
          'link_settings': { 'libraries': [
            '$(SDKROOT)/usr/lib/libreadline.dylib'
          ]},
        }],
        [ 'OS=="win"', {
          'sources!': [ 'src/d8-readline.cc' ],
        }],
      ],
      'include_dirs': [
        'src',
      ],
      'dependencies': [
        'v8',
      ],
      'actions': [
        {
          'variables': {
            'd8_library_files': [
              'src/d8.js',
              'src/macros.py',
            ],
          },
          'action_name': 'js2c',
          'inputs': [
            'tools/js2c.py',
            '<@(d8_library_files)',
          ],
          'extra_inputs': [
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/d8-js.cc',
            '<(INTERMEDIATE_DIR)/d8-js-empty.cc',
          ],
          'action': 'python tools/js2c.py <(_outputs) D8 <(d8_library_files)'
        },
      ],
    },

    # ARM targets, to test ARM code generation.  These use an ARM simulator
    # (src/simulator-arm.cc).  The ARM targets are not snapshot-enabled.
    {
      'target_name': 'v8_arm',
      'type': 'static_library',
      'sources': [
        '<@(base_sources)',
        '<(INTERMEDIATE_DIR)/libraries.cc',
        'src/snapshot-empty.cc',
      ],
      'sources!': [
        '<@(base_sources!)',
      ],
      'sources/': [
        ['exclude', '-ia32\\.cc$'],
        ['exclude', '^src/platform-.*\\.cc$' ],
      ],
      'conditions': [
        # TODO(mark): These only need to be 'sources/', the extra '+' is
        # for prepend, which is only temporary until the rules scanner is
        # rewritten to not pull things out of the list until all includes and
        # excludes are processed.
        ['OS=="linux"', {'sources/+': [['include', '^src/platform-linux\\.cc$']]}],
        ['OS=="mac"', {'sources/+': [['include', '^src/platform-macos\\.cc$']]}],
        ['OS=="win"', {
          'sources/+': [['include', '^src/platform-win32\\.cc$']],
          # 4355, 4800 came from common.vsprops
          # 4018, 4244 were a per file config on dtoa-config.c
          # TODO: It's probably possible and desirable to stop disabling the
          # dtoa-specific warnings by modifying dtoa as was done in Chromium
          # r9255.  Refer to that revision for details.
          'msvs_disabled_warnings': [4355, 4800, 4018, 4244],
        }],
      ],
      'include_dirs': [
        'src',
      ],
      'defines': [
        'ARM',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'include',
        ],
      },
      'actions': [
        {
          'action_name': 'js2c',
          'inputs': [
            'tools/js2c.py',
            '<@(core_library_files)',
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/libraries.cc',
            '<(INTERMEDIATE_DIR)/libraries-empty.cc',
          ],
          'action': 'python tools/js2c.py <(_outputs) CORE <(core_library_files)'
        },
      ],
    },
    {
      'target_name': 'v8_shell_arm',
      'type': 'executable',
      'sources': [
        'samples/shell.cc',
      ],
      'dependencies': [
        'v8_arm',
      ],
      'conditions': [
        [ 'OS=="win"', {
          # This could be gotten from external_code, if we decide it's ok.
          'defines': ['_CRT_SECURE_NO_WARNINGS'],
        }],
      ],
      'defines': [
        'ARM',
      ],
    },
    {
      'target_name': 'd8_arm',
      'type': 'executable',
      'sources': [
        '<(INTERMEDIATE_DIR)/d8-js.cc',
        'src/d8-debug.cc',
        'src/d8-readline.cc',
        'src/d8.cc',
      ],
      'conditions': [
        [ 'OS=="linux"', {
          'link_settings': { 'libraries': [ '-lreadline' ] },
        }],
        [ 'OS=="mac"', {
          'link_settings': { 'libraries': [
            '$(SDKROOT)/usr/lib/libreadline.dylib'
          ]},
        }],
        [ 'OS=="win"', {
          'sources!': [ 'src/d8-readline.cc' ],
        }],
      ],
      'include_dirs': [
        'src',
      ],
      'defines': [
        'ARM',
      ],
      'dependencies': [
        'v8_arm',
      ],
      'actions': [
        {
          'variables': {
            'd8_library_files': [
              'src/d8.js',
              'src/macros.py',
            ],
          },
          'action_name': 'js2c',
          'inputs': [
            'tools/js2c.py',
            '<@(d8_library_files)',
          ],
          'extra_inputs': [
          ],
          'outputs': [
            '<(INTERMEDIATE_DIR)/d8-js.cc',
            '<(INTERMEDIATE_DIR)/d8-js-empty.cc',
          ],
          'action': 'python tools/js2c.py <(_outputs) D8 <(d8_library_files)'
        },
      ],
    },
  ],
}