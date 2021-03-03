import sys

# Implements a simple stack-based VM

class VM:
  print_ins=False;
  def __init__(self, rom):
    self.rom = rom
    self.accumulator1 = 0
    self.accumulator2 = 0
    self.instruction_pointer = 1
    self.stack = []

  def step(self):
    cur_ins = self.rom[self.instruction_pointer]
    self.instruction_pointer += 1
    #input('Proceed?')
    fn = VM.OPERATIONS.get(cur_ins, None)

    if cur_ins[0] == '🖋':
      return
    if fn is None:
      raise RuntimeError("Unknown instruction '{}' at {}".format(
          repr(cur_ins), self.instruction_pointer - 1))
    else:
      fn(self)

  def add(self):
  	a=self.stack.pop()
  	b=self.stack.pop()
  	if VM.print_ins:
  	  print(a,"+",b)
  	self.stack.append(a + b)

  def sub(self):
    a = self.stack.pop()
    b = self.stack.pop()
    if VM.print_ins:
  	  print(b,"-",a)
    self.stack.append(b - a)

  def if_zero(self):
    if VM.print_ins:
      print("ifzero");
	
    if self.stack[-1] == 0:
      while self.rom[self.instruction_pointer] != '😐':
        if self.rom[self.instruction_pointer] in ['🏀', '⛰']:
          break
        self.step()
    else:
      self.find_first_endif()
      self.instruction_pointer += 1

  def if_not_zero(self):
    if VM.print_ins:
      print("ifnotzero");	
    if self.stack[-1] != 0:
      while self.rom[self.instruction_pointer] != '😐':
        if self.rom[self.instruction_pointer] in ['🏀', '⛰']:
          break
        self.step()
    else:
      self.find_first_endif()
      self.instruction_pointer += 1

  def find_first_endif(self):
    while self.rom[self.instruction_pointer] != '😐':
      self.instruction_pointer += 1

  def jump_to(self):
    marker = self.rom[self.instruction_pointer]
    if marker[0] != '💰':
      print('Incorrect symbol : ' + marker[0])
      raise SystemExit()
      print("Jumping to ",marker);
    marker = '🖋' + marker[1:]
    self.instruction_pointer = self.rom.index(marker) + 1

  def jump_top(self):
    self.instruction_pointer = self.stack.pop()
    if VM.print_ins:
  	  print("Jumping to top");

  def exit(self):
    print('\nDone.')
    raise SystemExit()

  def print_top(self):
    c=input("Proceed?");
    if(c=='s'):
      print('-'*25)
      for x in self.stack[::-1]:
        print(x)
      print('-'*25+'\n')
    elif(c=='p'):
      VM.print_ins=not VM.print_ins;
      
    sys.stdout.write(chr(self.stack.pop()))
    sys.stdout.flush()
    print("\n var1:",self.accumulator1," var2:",self.accumulator2);
	
  def push(self):
    #if VM.print_ins:
      #print("push from ","var1" if self.rom[self.instruction_pointer] == '🥇' else "var2");	
    if self.rom[self.instruction_pointer] == '🥇':
      self.stack.append(self.accumulator1)
    elif self.rom[self.instruction_pointer] == '🥈':
      self.stack.append(self.accumulator2)
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          self.rom[self.instruction_pointer], str(self.instruction_pointer)))
    self.instruction_pointer += 1

  def pop(self):
    #if VM.print_ins:
      #print("pop to ","var1" if self.rom[self.instruction_pointer] == '🥇' else "var2");	
    if self.rom[self.instruction_pointer] == '🥇':
      self.accumulator1 = self.stack.pop()
    elif self.rom[self.instruction_pointer] == '🥈':
      self.accumulator2 = self.stack.pop()
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          self.rom[self.instruction_pointer], str(self.instruction_pointer)))
    self.instruction_pointer += 1

  def pop_out(self):
    self.stack.pop()

  def load(self):
    num = 0
    if self.rom[self.instruction_pointer] == '🥇':
      acc = 1
    elif self.rom[self.instruction_pointer] == '🥈':
      acc = 2
    else:
      raise RuntimeError('Unknown instruction {} at position {}'.format(
          self.rom[self.instruction_pointer], str(self.instruction_pointer)))
    self.instruction_pointer += 1

    while self.rom[self.instruction_pointer] != '✋':
      num = num * 10 + (ord(self.rom[self.instruction_pointer][0]) - ord('0'))
      self.instruction_pointer += 1
    #print("Load ",num," into var"+str(acc));

    if acc == 1:
      self.accumulator1 = num
    else:
      self.accumulator2 = num

    #print("var1: ",self.accumulator1,"var2: ",self.accumulator2);
    self.instruction_pointer += 1

  def clone(self):
    self.stack.append(self.stack[-1])

  def multiply(self):
    a = self.stack.pop()
    b = self.stack.pop()
    if VM.print_ins:
  	  print(b,"*",a);
    self.stack.append(b * a)

  def divide(self):
    a = self.stack.pop()
    b = self.stack.pop()
    if VM.print_ins:
      print(b,"/",a);
    self.stack.append(b // a)

  def modulo(self):
    a = self.stack.pop()
    b = self.stack.pop()
    if VM.print_ins:
      print(b,"%",a);
    self.stack.append(b % a)

  def xor(self):
    a = self.stack.pop()
    b = self.stack.pop()
    if VM.print_ins:
      print(b,"^",a);
    self.stack.append(b ^ a)

  OPERATIONS = {
      '🍡': add,
      '🤡': clone,
      '📐': divide,
      '😲': if_zero,
      '😄': if_not_zero,
      '🏀': jump_to,
      '🚛': load,
      '📬': modulo,
      '⭐': multiply,
      '🍿': pop,
      '📤': pop_out,
      '🎤': print_top,
      '📥': push,
      '🔪': sub,
      '🌓': xor,
      '⛰': jump_top,
      '⌛': exit
  }


if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Missing program')
    raise SystemExit()

  with open(sys.argv[1], 'r') as f:
    print('Running ....')
    all_ins = ['']
    all_ins.extend(f.read().split())
    vm = VM(all_ins)

    while 1:
      vm.step()
			
			
			
			
			
			
			
			
			
			
			
			
