celc = float(input('Digite a temperatura em °C: '))
fahr = celc * 1.8 + 32
kelv = celc + 273

print('A temperatura {:.2f} em °F é {:.2f}, e {:.2f} em °K'.format
      (celc, fahr, kelv))