import win32clipboard as clippy
from pygments import highlight
from pygments.lexers.c_cpp import CppLexer
from pygments.formatters import RtfFormatter
from pygments.style import Style
from pygments.styles import STYLE_MAP

# Stylizer settings
styles = list(STYLE_MAP.keys()) # Available styles
style = styles[6]
font = "Monaco"
fontsize = 24


# Stylize
input = """#include <vector>

int main()
{
  using std::cout;
  using std::begin;   using std::end;

  // Do stuff
  int x = 4;

  return 0;
}
"""

output = highlight(input, CppLexer(), RtfFormatter(style=style, fontface=font, fontsize=fontsize))


# Copy to clipboard
CF_RTF = clippy.RegisterClipboardFormat("Rich Text Format")

output = bytearray(output, "utf8")

clippy.OpenClipboard(0)
clippy.EmptyClipboard()
clippy.SetClipboardData(CF_RTF, output)
clippy.CloseClipboard()
