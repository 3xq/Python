import colorsys,time
hue=0
def colored(r,g,b,text):
  return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r,g,b,text)
while True:
  time.sleep(0.1)
  (r,g,b)=colorsys.hsv_to_rgb(hue,1.0,1.0)
  R,G,B=int(255*r),int(255*g),int(255*b)
  print(colored(R,G,B,'Hello, World'))
  hue=hue+0.01
