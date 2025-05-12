###############################################################################
def SL(text, strip_prefix=None):
  '''
  SL: StripLines... strip space from beginning of lines to allow indented
  multi-line strings
  '''
  if text is None:
    return None

  lines = text.split('\n')

  if lines[0] == '':
    del lines[0]

  if len(lines) == 0:
    return ''

  if lines[-1].strip():
    raise ValueError('There must be only whitespace after last newline.')

  if strip_prefix is None:
    for line in lines:
      if line.strip():
        strip_prefix = line[:len(line) - len(line.lstrip())]
        break
    else:
      strip_prefix = ""


  # Only strip the beginning if it is an exact match for the strip_prefix
  return str.join('\n', (line.removeprefix(strip_prefix) for line in lines[:-1])) + '\n'
