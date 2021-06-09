import sublime
import sublime_plugin

import os.path

class MakeHeader(sublime_plugin.TextCommand):
   def run(self, edit):
      view = self.view

      file_name = os.path.basename(view.file_name())
      if len(file_name) != 0:
         result = '__'
         first_symbol = True
         for c in file_name:
            if c == '.':
               break
            if c.isupper():
               if not first_symbol:
                  result += '_'
               result += c
            else:
               result += c.upper()
            first_symbol = False

         result += '_H__'

         view.insert(edit, 0, f'#ifndef {result}\n#define {result}\n\n\n#endif // {result}')
