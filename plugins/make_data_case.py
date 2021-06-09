import sublime
import sublime_plugin

class MakeDataCaseCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      view = self.view

      print('asd')

      selection = view.sel()
      for _s in selection :
         text = view.substr( _s )
         if len( text ):
            pre_converted = 'k_' + text.lower()
            symbols = []
            i = 0
            while i < len(pre_converted)-1:
               if pre_converted[i] == '_':
                  i = i+1
                  symbols.append(pre_converted[i].upper())
               else:
                  symbols.append(pre_converted[i])
               i = i+1
            symbols.append(pre_converted[i])

            converted = ''.join(symbols)

            view.replace( edit, _s, converted )
