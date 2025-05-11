# Звіт
## Кроки виконання завдання
* на основі заданого regex_pattern = "a*4.+hi" автоматично створюється скінченний автомат. він відобраається у терміналі:
```RegexFSM States and Transitions:
  StartState -> ['StarState(AsciiState(a))', 'AsciiState(4)']
  StarState(AsciiState(a)) -> ['StarState(AsciiState(a))', 'AsciiState(4)']
  AsciiState(4) -> ['DotState']
  DotState -> ['PlusState(DotState)']
  PlusState(DotState) -> ['PlusState(DotState)', 'AsciiState(h)']
  AsciiState(h) -> ['AsciiState(i)']
  AsciiState(i) -> ['TerminationState']
  TerminationState -> [] 
```
* перевірка тестових послідовностей відбувається по створеному скінченному автомату. результат відображається у терміналі.
```
print(regex_compiled.check_string("aaaaaa4uuhi"))  # True
```
```
Processing character: 'a'
  Current state: StartState
  Next states: ['StarState(AsciiState(a))']
Processing character: 'a'
  Current state: StarState(AsciiState(a))
  Next states: ['StarState(AsciiState(a))']
Processing character: 'a'
  Current state: StarState(AsciiState(a))
  Next states: ['StarState(AsciiState(a))']
Processing character: 'a'
  Current state: StarState(AsciiState(a))
  Next states: ['StarState(AsciiState(a))']
Processing character: 'a'
  Current state: StarState(AsciiState(a))
  Next states: ['StarState(AsciiState(a))']
Processing character: 'a'
  Current state: StarState(AsciiState(a))
  Next states: ['StarState(AsciiState(a))']
Processing character: '4'
  Current state: StarState(AsciiState(a))
  Next states: ['AsciiState(4)']
Processing character: 'u'
  Current state: AsciiState(4)
  Next states: ['DotState']
Processing character: 'u'
  Current state: DotState
  Next states: ['PlusState(DotState)']
Processing character: 'h'
  Current state: PlusState(DotState)
  Next states: ['PlusState(DotState)', 'AsciiState(h)']
Processing character: 'i'
  Current state: PlusState(DotState)
  Current state: AsciiState(h)
  Next states: ['PlusState(DotState)', 'AsciiState(i)']
String accepted.
True
```
* перевірка наступного рядка:
```
 print(regex_compiled.check_string("4uuhi"))  # True
```
```
Processing character: '4'
  Current state: StartState
  Next states: ['AsciiState(4)']
Processing character: 'u'
  Current state: AsciiState(4)
  Next states: ['DotState']
Processing character: 'u'
  Current state: DotState
  Next states: ['PlusState(DotState)']
Processing character: 'h'
  Current state: PlusState(DotState)
  Next states: ['PlusState(DotState)', 'AsciiState(h)']
Processing character: '4'
  Current state: StartState
  Next states: ['AsciiState(4)']
Processing character: 'u'
  Current state: AsciiState(4)
  Next states: ['DotState']
Processing character: 'u'
  Current state: DotState
  Next states: ['PlusState(DotState)']
Processing character: 'h'
  Current state: PlusState(DotState)
  Next states: ['PlusState(DotState)', 'AsciiState(h)']
  Next states: ['AsciiState(4)']
Processing character: 'u'
  Current state: AsciiState(4)
  Next states: ['DotState']
Processing character: 'u'
  Current state: DotState
  Next states: ['PlusState(DotState)']
Processing character: 'h'
  Current state: PlusState(DotState)
  Next states: ['PlusState(DotState)', 'AsciiState(h)']
  Current state: AsciiState(4)
  Next states: ['DotState']
Processing character: 'u'
  Current state: DotState
  Next states: ['PlusState(DotState)']
Processing character: 'h'
  Current state: PlusState(DotState)
  Next states: ['PlusState(DotState)', 'AsciiState(h)']
Processing character: 'u'
  Current state: DotState
  Next states: ['PlusState(DotState)']
Processing character: 'h'
  Current state: PlusState(DotState)
  Next states: ['PlusState(DotState)', 'AsciiState(h)']
  Next states: ['PlusState(DotState)']
Processing character: 'h'
  Current state: PlusState(DotState)
  Next states: ['PlusState(DotState)', 'AsciiState(h)']
Processing character: 'i'
Processing character: 'h'
  Current state: PlusState(DotState)
  Next states: ['PlusState(DotState)', 'AsciiState(h)']
Processing character: 'i'
  Current state: PlusState(DotState)
  Current state: AsciiState(h)
Processing character: 'i'
  Current state: PlusState(DotState)
  Current state: AsciiState(h)
  Current state: PlusState(DotState)
  Current state: AsciiState(h)
  Current state: AsciiState(h)
  Next states: ['PlusState(DotState)', 'AsciiState(i)']
String accepted.
True
```
* перевірка останньої послідовності:
```
print(regex_compiled.check_string("meow"))  # False
```
```
Processing character: 'm'
  Current state: StartState
  No valid transitions found. String rejected.
False
```
## Висновок:
Скінченні автомати дозволяють ефективно вирішувати складні лінгвістичні моделі.
