import pyautogui as p
import datetime, time, pyperclip

date = datetime.datetime.now()
AMPM = date.strftime("%p")
if AMPM == "AM":
    AMPM = "Manhã"
else:
    AMPM = "Tarde"
data = date.strftime(f"%d/%m/%Y - {AMPM}")
prioridades = []

msgInicio = f"""Boa tarde a todos🌞🌻

⏰{data} 

Nosso atendimento de hoje 🙏🏼😍❤️
"""

msgFinal = """
🪴Atendimento: Verificação do sistema SGP duas vezes ao dia.🪴


📢Vamos nos falando pelo nosso grupo. Qualquer dúvida nos contactem


🚨Informaremos qualquer imprevisto e seguiremos com foco total🚨
"""

numPrioridades = int(p.prompt(text='Quantas prioridades tem no dia de hoje?', title='Digite aqui o numero de prioridades e clique em OK!' , default=''))

for i in range(numPrioridades):
    a = p.prompt(text='Adicione uma prioridade!', title='Digite a prioridade e adicione e clique em OK!' , default='')
    prioridades.append(a)
    
print(prioridades)

p.hotkey("win", "r")
p.hotkey("ctrl", "a")
p.write("notepad")
p.hotkey("enter")
time.sleep(5)

pyperclip.copy(msgInicio)
p.hotkey("ctrl","v")
for i in range(numPrioridades):
    msg = f"\n- Prioridade {i+1} - {prioridades[i]}\n\n"
    p.write(msg, interval=0.05)
pyperclip.copy(msgFinal)
p.hotkey("ctrl","v")
